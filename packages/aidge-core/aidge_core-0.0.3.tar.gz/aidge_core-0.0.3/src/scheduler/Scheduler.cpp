/********************************************************************************
 * Copyright (c) 2023 CEA-List
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 ********************************************************************************/

#include "aidge/scheduler/Scheduler.hpp"

#include <algorithm> // std::find, std::find_if, std::max, std::min, std::replace, std::transform
#include <cassert>
#include <chrono>
#include <cstddef>   // std::size_t
#include <cstdio>    // std::fclose, std::fopen
#include <iterator>  // std::back_inserter, std::distance
#include <map>
#include <memory>
#include <set>
#include <string>
#include <vector>

#include <fmt/core.h>
#include <fmt/color.h>
#include <fmt/ranges.h>

#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/Memorize.hpp"
#include "aidge/operator/MetaOperator.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/Types.h"


Aidge::Scheduler::~Scheduler() noexcept = default;
Aidge::Scheduler::PriorProducersConsumers::PriorProducersConsumers() = default;
Aidge::Scheduler::PriorProducersConsumers::PriorProducersConsumers(const PriorProducersConsumers&) = default;
Aidge::Scheduler::PriorProducersConsumers::~PriorProducersConsumers() noexcept = default;

void Aidge::Scheduler::generateScheduling() {
    auto schedule = generateBaseScheduling();
    generateEarlyLateScheduling(schedule);
    mStaticSchedule.push_back(schedule);
}

std::vector<std::shared_ptr<Aidge::Scheduler::StaticSchedulingElement>> Aidge::Scheduler::generateBaseScheduling() const {

    // 0) setup useful variables
    // map associating each node with string "name (type#rank)"
    const std::map<std::shared_ptr<Node>, std::string> namePtrTable
        = mGraphView->getRankedNodesName("{0} ({1}#{3})");

    // consumers that were run by but can still consume data.
    // They must be run AFTER the remaining consumer to ensure a non-greedy
    // producers-consumers model!
    std::set<std::shared_ptr<Node>> stillConsumers;

    std::vector<std::shared_ptr<StaticSchedulingElement>> schedule;


    // 1) Initialize consumers list:
    // 1.1) List of the GraphView's input nodes
    std::set<std::shared_ptr<Node>> consumers = mGraphView->inputNodes();

    // 1.2) List of nodes inside the GraphView connected to an inner Producer
    std::set<std::shared_ptr<Node>> producers;
    for (const std::shared_ptr<Node>& nodePtr : mGraphView->getNodes()) {
        if (nodePtr->type() == Producer_Op::Type) {
            for (const auto& child : nodePtr->getChildren()) {
                // Do not schedule childs outside current graph!
                if (mGraphView->inView(child)) {
                    consumers.insert(child);
                }
            }
        }
    }

    do {
        // 2) From the current consumers list, check if any prior consumer node
        // is needed. A prior will generally be required for any node consuming
        // parameters (weights and bias) that is not an input node.
        // If for a given node, only parent producers (at any depth) are needed
        // to satisfy its required data, it becomes a prior.
        // If the prior node is a producer, it is added to the list of required
        // producers.
        // If the prior node is of another type, it replaces the initial consumer
        // in the new priorConsumers list. The initial consumer will become
        // again a consumer later, by construction.
        Log::debug("List of consumers with their priors:");
        std::set<std::shared_ptr<Node>> requiredProducers;  // Priors of type Producer
        std::set<std::shared_ptr<Node>> priorConsumers;  // Priors of other type
        mPriorCache.clear();

        for (const auto& consumer : consumers) {
            Log::debug("\t- consumer: {}", fmt::styled(namePtrTable.at(consumer), fg(fmt::color::orange)));

            const auto& prior = getPriorProducersConsumers(consumer);

            if (prior.isPrior) {
                std::vector<std::string> requiredProducersName;
                std::transform(prior.requiredProducers.begin(), prior.requiredProducers.end(),
                    std::back_inserter(requiredProducersName),
                    [&namePtrTable](auto val){ return namePtrTable.at(val); });
                Log::debug("\t\trequired producers: {}", requiredProducersName);

                std::vector<std::string> priorConsumersName;
                std::transform(prior.priorConsumers.begin(), prior.priorConsumers.end(),
                    std::back_inserter(priorConsumersName),
                    [&namePtrTable](auto val){ return namePtrTable.at(val); });
                Log::debug("\t\tprior consumers: {}", priorConsumersName);

                requiredProducers.insert(prior.requiredProducers.cbegin(), prior.requiredProducers.cend());
                priorConsumers.insert(prior.priorConsumers.cbegin(), prior.priorConsumers.cend());
            }
            else {
                priorConsumers.insert(consumer);
            }
        }

        // 3) Prior consumers replace the initial consumers list.
        // By construction, initial consumers will necessarily become consumers
        // again later.
        consumers.swap(priorConsumers);

        // 4) Make producers generate the required data.
        // Producers are special nodes that generate data on demand.
        for (const auto& requiredProducer : requiredProducers) {
            requiredProducer->getOperator()->updateConsummerProducer();
            schedule.push_back(std::make_shared<StaticSchedulingElement>(requiredProducer));
        }

        // 5) Find runnable consumers.
        // A consumer is runnable if the required data is available for all of
        // its inputs. At this point, not all consumers are necessarily
        // runnable because some may depend on the execution of others (when
        // there is multiple successive priors for example).
        std::set<std::shared_ptr<Node>> runnableConsumers;
        Log::debug("Updated list of consumers:");
        for (const auto& consumer : consumers) {
            summarizeConsumerState(consumer, namePtrTable.at(consumer));  // debug print

            bool isRunnable = true;
            for (IOIndex_t inputIdx = 0; inputIdx < consumer->nbInputs(); ++inputIdx) {
                AIDGE_LOG_CONTEXT("Consumer node {} input #{}", namePtrTable.at(consumer), inputIdx);

                if ((consumer->getOperator()->getNbConsumedData(inputIdx) + consumer->getOperator()->getNbRequiredData(inputIdx)) >
                            getNbAvailableData(consumer, inputIdx)) {
                    Log::debug("  not runnable: C{} + R{} > P{} for input #{}",
                        consumer->getOperator()->getNbConsumedData(inputIdx),
                        consumer->getOperator()->getNbRequiredData(inputIdx),
                        getNbAvailableData(consumer, inputIdx), inputIdx);

                    // not enough data to run
                    isRunnable = false;
                    break;
                }
            }

            if (isRunnable) {
                runnableConsumers.insert(consumer);
            }
        }

        // 5) If not consumer is runnable, it is a stop condition!
        if (runnableConsumers.empty()) {
            Log::debug("********************");
            // No consumer is runnable: some required data is missing for all of
            // them. There is two possibilities:
            // - At least one required data source is exhausted, which may be
            //   an expected stop condition.
            // - There is a deadlock between consumers, if some one is waiting
            //   for data from the other and reciprocally.
            break;
        }

        // 6) Push runnable consumers in the list of nodes to run and update the
        // consumer producer system.
        // At this point, simultaneously runnable consumers have no data
        // dependency and could be run in parallel!
        for (const auto& runnable : runnableConsumers) {
            Log::debug("Runnable: {}", namePtrTable.at(runnable));
            runnable->getOperator()->updateConsummerProducer();
            schedule.push_back(std::make_shared<StaticSchedulingElement>(runnable));
        }

        // 7) Update consumers list
        Log::debug("Updating producer and consumer lists...");
        for (const auto& consumer : runnableConsumers) {
            summarizeConsumerState(consumer, namePtrTable.at(consumer));  // debug print
            // 7.1) If the current consumer has still data to consume, it will
            // be put back in the consumers list once the remaining consumers
            // have been exhausted.
            bool isStillConsumer = false;
            for (IOIndex_t inputIdx = 0; inputIdx < consumer->nbInputs(); ++inputIdx) {
                AIDGE_LOG_CONTEXT("Consumer node {} input #{}", namePtrTable.at(consumer), inputIdx);

                if (consumer->getOperator()->getNbConsumedData(inputIdx) <
                            getNbAvailableData(consumer, inputIdx)) {
                    Log::debug("  still consumer: C{} < P{} for input #{}",
                        consumer->getOperator()->getNbConsumedData(inputIdx),
                        getNbAvailableData(consumer, inputIdx), inputIdx);

                    // there is still data to consume
                    isStillConsumer = true;
                    break;
                }
            }

            // 7.2) If the current consumer becomes a producer for other nodes,
            // its childs become consumers.
            bool isProducer = false;
            for (IOIndex_t outId = 0; outId < consumer->nbOutputs(); ++outId) {
                for (const auto& child : consumer->getChildren(outId)) {
                    if (child) {
                        IOIndex_t inputIdx = 0;
                        for (const auto& childParent : child->getParents()) {
                            if (childParent == consumer) {
                                AIDGE_LOG_CONTEXT("Consumer node {} input #{} / Producer node {} output #{}",
                                    namePtrTable.at(child), inputIdx, namePtrTable.at(consumer), outId);

                                if (child->getOperator()->getNbConsumedData(inputIdx) < consumer->getOperator()->getNbProducedData(outId)) {
                                    isProducer = true;
                                    break;
                                }
                            }
                            ++inputIdx;
                        }

                        if (isProducer) {
                            break;
                        }
                    }
                }
/*
                if (consumer->getOperator()->getNbProducedData(outId) > 0) {
                    Log::debug("  also producer");
                    // make sure consumer is also a producer
                    producers.insert(consumer);

                    const auto& newConsumers = getConsumers({consumer});
                    consumers.insert(newConsumers.cbegin(), newConsumers.cend());
                    break;
                }
*/
            }

            consumers.erase(consumer);

            if (isProducer) {
                Log::debug("  also producer");
                // make sure consumer is also a producer
                producers.insert(consumer);

                const auto& newConsumers = getConsumers({consumer});
                consumers.insert(newConsumers.cbegin(), newConsumers.cend());
            }

            if (isStillConsumer) {
                // If there is still data to consume, the consumer will be
                // run AFTER the other remaining consumers
                // (= non-greedy consumers)
                stillConsumers.insert(consumer);
            }
        }

        // 8) If there is no more consumers, swap with possible "still consumers"
        // This ensures that the "non-greedy" consumer behavior
        if (consumers.empty()) {
            consumers.swap(stillConsumers);
            stillConsumers.clear();
        }

        Log::debug("********************");
    } while (!consumers.empty());

    mPriorCache.clear();

    if (!consumers.empty()) {
        Log::warn("Remaining consumers: possible dead-lock");
    }

    return schedule;
}


void Aidge::Scheduler::summarizeConsumerState(const std::shared_ptr<Aidge::Node>& consumer, const std::string& nodeName) const {
    Log::debug("\t- consumer: {}", fmt::styled(nodeName, fg(fmt::color::orange)));
    std::string crLog = "\t\tC/R:\t";
    for (IOIndex_t inId = 0; inId < consumer->nbInputs() - 1; ++inId) {
        crLog += fmt::format("{}/{}\n\t\t\t", consumer->getOperator()->getNbConsumedData(inId),
                consumer->getOperator()->getNbRequiredData(inId));
    }
    crLog += fmt::format("{}/{}", consumer->getOperator()->getNbConsumedData(static_cast<IOIndex_t>(consumer->nbInputs()) - 1),
            consumer->getOperator()->getNbRequiredData(static_cast<IOIndex_t>(consumer->nbInputs()) - 1));
    Log::debug("{}", crLog);

    std::string pLog = "\t\tP:\t";
    for (IOIndex_t outId = 0; outId < consumer->nbOutputs() - 1; ++outId) {
        pLog += fmt::format("{}\n\t\t\t", consumer->getOperator()->getNbProducedData(outId));
    }
    pLog += fmt::format("{}", consumer->getOperator()->getNbProducedData(static_cast<IOIndex_t>(consumer->nbOutputs()) - 1));
    Log::debug("{}", pLog);
}


void Aidge::Scheduler::generateEarlyLateScheduling(std::vector<std::shared_ptr<StaticSchedulingElement>>& schedule) const {
    std::size_t latest = 0;
    // Calculate early (logical) start
    for (std::size_t elt = 0; elt < schedule.size(); ++elt) {
        const auto node = schedule[elt]->node;
        const auto itNode = std::find_if(schedule.rend() - elt, schedule.rend(),
            [node](const auto& v) { return (v->node == node); });

        // Node can be run the earliest just after its childs were run the last time!
        std::size_t early = 0;
        if (itNode != schedule.rend()) {
            for (const auto& child : node->getChildren()) {
                // Find child node next scheduled position
                const auto it = std::find_if(schedule.rend() - elt, itNode,
                    [child](const auto& v) { return (v->node == child); });
                AIDGE_INTERNAL_ASSERT(it != schedule.rend());

                const std::size_t step = std::distance(schedule.begin(), it.base()) - 1;
                early = std::max(early, schedule[step]->early + 1);
                schedule[step]->earlierThan.push_back(schedule[elt]);
            }
        }

        // Node can be run the earliest just after its latest parent was run
        for (const auto& parent : node->getParents()) {
            // Find parent node latest scheduled position
            const auto it = std::find_if(schedule.rend() - elt, schedule.rend(),
                [parent](const auto& v) { return (v->node == parent); });
            if (it != schedule.rend()) {
                const std::size_t step = std::distance(schedule.begin(), it.base()) - 1;
                early = std::max(early, schedule[step]->early + 1);
                schedule[step]->earlierThan.push_back(schedule[elt]);
            }
        }

        latest = std::max(latest, early);
        schedule[elt]->early = early;
    }

    // Calculate late (logical) start
    for (std::size_t elt = schedule.size(); elt-- != 0; ) {
        const auto node = schedule[elt]->node;
        const auto itNode = std::find_if(schedule.begin() + elt + 1, schedule.end(),
            [node](const auto& v) { return (v->node == node); });

        // Node can be run the latest just before its parents are run the next time!
        std::size_t late = latest;
        if (itNode != schedule.end()) {
            for (const auto& parent : node->getParents()) {
                // Find child node next scheduled position
                const auto it = std::find_if(schedule.begin() + elt + 1, itNode,
                    [parent](const auto& v) { return (v->node == parent); });
                AIDGE_INTERNAL_ASSERT(it != schedule.end());

                const std::size_t step = std::distance(schedule.begin(), it);
                late = std::min(late, schedule[step]->late - 1);
                schedule[step]->laterThan.push_back(schedule[elt]);
            }
        }

        // Node can be run the latest just before its earliest child is run
        for (const auto& child : node->getChildren()) {
            // Find child node earliest scheduled position
            const auto it = std::find_if(schedule.begin() + elt + 1, schedule.end(),
                [child](const auto& v) { return (v->node == child); });
            if (it != schedule.end()) {
                const std::size_t step = std::distance(schedule.begin(), it);
                late = std::min(late, schedule[step]->late - 1);
                schedule[step]->laterThan.push_back(schedule[elt]);
            }
        }

        schedule[elt]->late = late;
    }
}

void Aidge::Scheduler::resetScheduling() {
    for (auto node : mGraphView->getNodes()) {
        node->getOperator()->resetConsummerProducer();
    }

    mStaticSchedule.clear();
    mStaticScheduleStep = 0;
    mScheduling.clear();
}

/**
 * This version is a simplified version without special handling of concatenation.
*/
Aidge::MemoryManager Aidge::Scheduler::generateMemory(bool incProducers, bool wrapAroundBuffer) const {
    MemoryManager memManager;

    for (std::size_t step = 0; step < mStaticSchedule.size(); ++step) {
        for (const auto& node : getStaticScheduling(step)) {
            if (!incProducers && node->type() == Producer_Op::Type) {
                memManager.releaseDependencies(node);
                continue;
            }

            const auto childs = node->getChildren();
            AIDGE_ASSERT(node->getOperator()->operatorType() == OperatorType::Tensor,
                "Operator must be of Tensor type for node {} (of type {}).",
                node->name(), node->type());
            const auto op = std::static_pointer_cast<OperatorTensor>(node->getOperator());

            std::vector<const MemoryManager::MemoryPlane*> wrapAroundMemPlane;

            // Allocate a memory plane for each node's output
            for (IOIndex_t outputIdx = 0; outputIdx < node->nbOutputs(); ++outputIdx) {
                const auto requiredSize = op->getRequiredMemory(outputIdx, {});
                AIDGE_ASSERT(requiredSize.type == Elts_t::Data,
                    "Cannot generate memory with token-based producer-consumer model for node {} (of type {}).",
                    node->name(), node->type());

                // By default, specifies a fully monolithic memory block
                std::size_t size = requiredSize.data;
                std::size_t stride = 0;
                std::size_t length = 1;
                std::size_t count = 1;

                if (op->getOutput(outputIdx) && op->getOutput(outputIdx)->dims().size() > 3) {
                    // If it is possible, assume a NCHW layout
                    size = op->getOutput(outputIdx)->dims().end()[-3];
                    stride = size;
                    length = op->getOutput(outputIdx)->dims().end()[-1];
                    count = op->getOutput(outputIdx)->dims().end()[-2];
                }

                // Check if wrap around buffer is possible for this node
                // (re-using previous node outputs memory for this node outputs).
                // => only if this node is the only child of its parent(s)
                std::size_t wrapAroundSize = 0;
                std::size_t wrapAroundExtra = 0;
                wrapAroundMemPlane.push_back(nullptr);

                // Select the best parent among all allocable nodes for
                // reallocation, which is the one with most memory (in order
                // to minimize the reallocation size).
                IOIndex_t inputIdx = 0;
                for (const auto& parent : node->dataInputs()) {
                    if (parent.first && parent.first->getChildren(parent.second).size() == 1
                        // there might be no existing plane if the parent was
                        // not yet scheduled (because it may be a recurrent connection)
                        && memManager.getNbPlanes(parent.first) >= parent.first->nbOutputs()
                        // memSpace should not be already released
                        && memManager.getPlanes(parent.first).end()[-parent.first->nbOutputs()+parent.second].memSpace->released == -1)
                    {
                        const auto requiredData = op->getNbRequiredData(inputIdx);
                        const auto requiredProtected = op->getNbRequiredProtected(inputIdx);
                        AIDGE_ASSERT(requiredData.type == Elts_t::Data && requiredProtected.type == Elts_t::Data,
                            "Cannot generate memory with token-based producer-consumer model for node {} (of type {}).",
                            node->name(), node->type());

                        const bool isWrappable = (requiredProtected.data < requiredData.data);
                        const MemoryManager::MemoryPlane& memPlane = memManager.getPlanes(parent.first).end()[-parent.first->nbOutputs()+parent.second];

                        if (isWrappable || !memManager.isWrapAround(
                                    memPlane.memSpace,
                                    memPlane.getFinalOffset()
                                        - memPlane.memSpace->offset,
                                    requiredSize.data))
                        {
                            if (memPlane.getSize() > wrapAroundSize + requiredProtected.data
                                && std::find(wrapAroundMemPlane.begin(), wrapAroundMemPlane.end(), &memPlane) == wrapAroundMemPlane.end())
                            {
                                wrapAroundSize = memPlane.getSize() - requiredProtected.data;
                                if (requiredSize.data > wrapAroundSize) {
                                    wrapAroundExtra = requiredSize.data - wrapAroundSize;
                                }
                                wrapAroundMemPlane[outputIdx] = &memPlane;
                            }

                            if (wrapAroundExtra == 0) {
                                break;
                            }
                        }
                    }
                    ++inputIdx;
                }

                // MemoryPlane to (re)use
                const MemoryManager::MemoryPlane& memPlane
                    = (wrapAroundBuffer && wrapAroundSize > 0)
                        ? (*wrapAroundMemPlane[outputIdx]) :
                            memManager.allocate(requiredSize.data, childs, stride, length, count);

                if (wrapAroundBuffer && wrapAroundSize > 0) {
                    memManager.reallocate(memPlane,
                        node, 0,
                        requiredSize.data, true, wrapAroundExtra, childs, stride, length, count);
                }
                else {
                    memManager.reallocate(memPlane.memSpace,
                        node, memPlane.offset,
                        requiredSize.data, false, 0, childs, stride, length, count);
                }
            }

            memManager.releaseDependencies(node);
            memManager.tick();
        }
    }

    return memManager;
}

void Aidge::Scheduler::connectInputs(std::vector<std::shared_ptr<Aidge::Tensor>> data){
    // This version of connect inputs only connects tensor inputs in input data producers.
    auto inputNodes = mGraphView->getOrderedInputs();

    // Assert that the number of input data producers corresponds to the number of data input
    assert(data.size() == inputNodes.size()  && "Scheduler connectInput error - Inconsistent number of graph inputs and inputs passed to the graph");

    for (std::size_t i = 0; i < data.size(); ++i){
        // TODO : maybe shallow copy instead of deepcopy
        inputNodes[i].first->getOperator()->setInput(inputNodes[i].second, data[i]);
    }
}

void Aidge::Scheduler::saveSchedulingDiagram(const std::string& fileName) const {
    auto fp = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen((fileName + ".mmd").c_str(), "w"), &std::fclose);

    if (!fp) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create scheduling diagram log file: {}", fileName + ".mmd");
    }

    fmt::print(fp.get(), "gantt\ndateFormat x\naxisFormat %Q µs\n\n");

    if (!mScheduling.empty()) {
        const std::map<std::shared_ptr<Node>, std::string> namePtrTable
            = mGraphView->getRankedNodesName("{0} ({1}#{3})");
        const auto globalStart = mScheduling[0].start;

        for (const auto& element : mScheduling) {
            auto name = namePtrTable.at(element.node);
            // Mermaid does not allow : character in task title
            std::replace(name.begin(), name.end(), ':', '_');

            fmt::print(fp.get(), "{} :{}, {}\n",
                         name,
                         std::chrono::duration_cast<std::chrono::microseconds>(element.start - globalStart).count(),
                         std::chrono::duration_cast<std::chrono::microseconds>(element.end - globalStart).count());
        }
    }

    fmt::print(fp.get(), "\n");
}

void Aidge::Scheduler::saveStaticSchedulingDiagram(const std::string& fileName) const {
    auto fp = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen((fileName + ".mmd").c_str(), "w"), &std::fclose);

    if (!fp) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create scheduling diagram log file: {}", fileName + ".mmd");
    }

    fmt::print(fp.get(), "gantt\ndateFormat x\naxisFormat %Q\n\n");

    if (!mStaticSchedule.empty()) {
        const std::map<std::shared_ptr<Node>, std::string> namePtrTable
            = mGraphView->getRankedNodesName("{0} ({1}#{3})");

        for (const auto& schedule : mStaticSchedule) {
            for (const auto& element : schedule) {
                auto name = namePtrTable.at(element->node);
                // Mermaid does not allow : character in task title
                std::replace(name.begin(), name.end(), ':', '_');

                fmt::print(fp.get(), "{} :{}, {}\n",
                            name, element->early, element->late);
            }
        }
    }

    fmt::print(fp.get(), "\n");
}

std::vector<std::shared_ptr<Aidge::Node>> Aidge::Scheduler::getStaticScheduling(std::size_t step) const {
    const auto& staticSchedule = mStaticSchedule.at(step);
    std::vector<std::shared_ptr<Node>> schedule;
    std::transform(staticSchedule.begin(), staticSchedule.end(), std::back_inserter(schedule), [](const auto& v) { return v->node; });
    return schedule;
}

std::set<std::shared_ptr<Aidge::Node>> Aidge::Scheduler::getConsumers(
        const std::set<std::shared_ptr<Node>>& producers) const {
    std::set<std::shared_ptr<Node>> consumers;

    for (const auto& producer : producers) {
        const auto& childs = producer->getChildren();
        for (const auto& child : childs) {
            // Do not schedule childs outside current graph!
            if (mGraphView->inView(child)) {
                consumers.insert(child);
            }
        }
    }

    return consumers;
}

Aidge::Elts_t Aidge::Scheduler::getNbAvailableData(const std::shared_ptr<Node>& node, const IOIndex_t inputIdx) const {
    const auto parent = node->inputs()[inputIdx];

    if (parent.first) {
        // Parent is connected, everything if fine!
        return parent.first->getOperator()->getNbProducedData(parent.second);
    }
    else if (std::shared_ptr<Node> upperNode = mUpperNode.lock()) {
        // We are inside an upper operator (for instance a MetaOperator)
        // We need to connect the "local" producer-consumer model to the upper
        // one, by mapping local node inputs to the upper node inputs.
        IOIndex_t nodeInputIdx = 0;
        for (const auto& input : mGraphView->getOrderedInputs()) {
            if (input.first == node) {
                // Current node is an input
                const auto upperInput = upperNode->inputs()[nodeInputIdx];
                if (upperInput.first) {
                    return upperInput.first->getOperator()->getNbProducedData(upperInput.second);
                }
            }
            ++nodeInputIdx;
        }
    }

    // Otherwise, two cases:
    if (node->getOperator()->getRawInput(inputIdx)) {
        // Input is not connected but a valid tensor exists
        // => This means data was fed manually to the input, without a Producer
        // In this case, we assume a single-use data (unlike a Producer, which
        // keep producing the data each time it is needed).
        fmt::print("No producer node attached to input#{} for node {} ({})\n", inputIdx, node->name(), node->type());
        return Elts_t::DataElts(std::static_pointer_cast<Tensor>(node->getOperator()->getRawInput(inputIdx))->size());
    }
    else {
        // Input is not connected, this is an error
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Missing input#{} for node {} ({})\n", inputIdx, node->name(), node->type());
    }

    return Elts_t::NoneElts();
}

Aidge::Scheduler::PriorProducersConsumers Aidge::Scheduler::getPriorProducersConsumers(
    const std::shared_ptr<Node>& node) const
{
    const auto priorCache = mPriorCache.find(node);
    if (priorCache != mPriorCache.end()) {
        return priorCache->second;
    }

    PriorProducersConsumers prior;

    IOIndex_t inputIdx = 0;
    for (const auto& parent : node->inputs()) {
        if (parent.first) {
            AIDGE_LOG_CONTEXT("Producer node {} (of type {}) output #{}",
                parent.first->name(), parent.first->type(), parent.second);

            if ((node->getOperator()->getNbConsumedData(inputIdx) + node->getOperator()->getNbRequiredData(inputIdx)) >
                        parent.first->getOperator()->getNbProducedData(parent.second))
            {
                // the node needs more data than the current parent has provided yet
                if (!mGraphView->inView(parent.first)) {
                    // Do not schedule prior outside the current graph!
                    // return PriorProducersConsumers(); // not scheduled
                    prior.priorConsumers.insert(node);
                }

                else if (parent.first->type() == Producer_Op::Type) {
                    prior.requiredProducers.insert(parent.first);
                    prior.priorConsumers.insert(node);
                }
                else if (parent.first->type() == Memorize_Op::Type) {
                    // Break cycles
                    return PriorProducersConsumers(); // not scheduled
                }
                else {
                    const auto& parentPrior = getPriorProducersConsumers(parent.first);

                    if (!parentPrior.isPrior) {
                        return PriorProducersConsumers(); // not scheduled
                    }
                    else {
                        prior.requiredProducers.insert(parentPrior.requiredProducers.cbegin(), parentPrior.requiredProducers.cend());
                        prior.priorConsumers.insert(parentPrior.priorConsumers.cbegin(), parentPrior.priorConsumers.cend());
                    }
                }
            }
        }
        ++inputIdx;
    }

    prior.isPrior = true;
    if (prior.priorConsumers.empty()) {
        prior.priorConsumers.insert(node);
    }
    mPriorCache.insert(std::make_pair(node, prior));
    return prior;
}
