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

#ifndef AIDGE_CORE_SCHEDULER_SCHEDULER_H_
#define AIDGE_CORE_SCHEDULER_SCHEDULER_H_

#include <cstddef>  // std::size_t
#include <chrono>
#include <map>
#include <memory>
#include <set>
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/scheduler/MemoryManager.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
class Node;
class GraphView;

class Scheduler {
protected:
    struct StaticSchedulingElement {
        StaticSchedulingElement(
            std::shared_ptr<Node> node_,
            std::size_t early_ = static_cast<std::size_t>(-1),
            std::size_t late_ = static_cast<std::size_t>(-1))
            : node(node_), early(early_), late(late_) {}

        std::shared_ptr<Node> node;
        std::size_t early;
        std::size_t late;
        std::vector<std::shared_ptr<StaticSchedulingElement>> earlierThan;
        std::vector<std::shared_ptr<StaticSchedulingElement>> laterThan;
    };

    /**
     * @brief Node with its start/end execution time stored for later display.
     */
    struct SchedulingElement {
        SchedulingElement(
            std::shared_ptr<Node> node_,
            std::chrono::time_point<std::chrono::high_resolution_clock> start_,
            std::chrono::time_point<std::chrono::high_resolution_clock> end_)
            : node(node_), start(start_), end(end_) {}
        ~SchedulingElement() noexcept = default;
        std::shared_ptr<Node> node;
        std::chrono::time_point<std::chrono::high_resolution_clock> start;
        std::chrono::time_point<std::chrono::high_resolution_clock> end;
    };
public:
    struct PriorProducersConsumers {
        PriorProducersConsumers();
        PriorProducersConsumers(const PriorProducersConsumers&);
        ~PriorProducersConsumers() noexcept;
        bool isPrior = false;
        std::set<std::shared_ptr<Aidge::Node>> requiredProducers;
        std::set<std::shared_ptr<Aidge::Node>> priorConsumers;
    };

public:
    Scheduler(std::shared_ptr<GraphView> graphView, std::shared_ptr<Node> upperNode = nullptr)
        : mGraphView(graphView),
          mUpperNode(upperNode)
    {
        // ctor
    };

    virtual ~Scheduler() noexcept;

public:
    /**
     * @brief Return a vector of Node ordered by the order they are called by the scheduler.
     * @return std::vector<std::shared_ptr<Node>>
     */
    std::vector<std::shared_ptr<Node>> getStaticScheduling(std::size_t step = 0) const;

    inline std::shared_ptr<GraphView> graphView() const noexcept {
        return mGraphView;
    }

    /**
     * @brief Generate full static scheduling of the GraphView.
     * For each node, an earliest and latest possible execution logical step
     * is specified. Nodes that may be scheduled at the same logical step have
     * no data dependency and can be run in parallel.
    */
    void generateScheduling();

    /**
     * Reset all scheduling and associated nodes producer consumer.
    */
    void resetScheduling();

    /**
     * Generate the memory layout for the current static scheduling.
     * @param incProducers If true, include the producers in the memory layout.
     * @param wrapAroundBuffer If true, allow wrapping in memory planes.
    */
    MemoryManager generateMemory(bool incProducers = false, bool wrapAroundBuffer = false) const;

    /**
     * @brief Place the data tensors inside in the data input tensor of the graphView. In case of multiple data input tensors, they are mapped to producers in the order given by the graph.
     *
     * @param data data input tensors
     */
    void connectInputs(std::vector<std::shared_ptr<Aidge::Tensor>> data);

    /**
     * @brief Save in a Markdown file the static scheduling with early and late relative order for the nodes.
     * @param fileName Name of the generated file.
     */
    void saveStaticSchedulingDiagram(const std::string& fileName) const;

    /**
     * @brief Save in a Markdown file the order of layers execution.
     * @param fileName Name of the generated file.
     */
    void saveSchedulingDiagram(const std::string& fileName) const;


protected:
    /**
     * @brief Getter for the set of children Nodes of the given input Nodes.
     * @param producers Set of Nodes for which we want to obtain the set of children Nodes.
     * @return std::set<std::shared_ptr<Node>> Children Nodes.
     */
    std::set<std::shared_ptr<Node>> getConsumers(const std::set<std::shared_ptr<Node>>& producers) const;

    Elts_t getNbAvailableData(const std::shared_ptr<Node>& node, const IOIndex_t inputIdx) const;

    PriorProducersConsumers getPriorProducersConsumers(const std::shared_ptr<Node>& node) const;

    /**
     * @brief Generate an initial base scheduling for the GraphView.
     * The scheduling is entirely sequential and garanteed to be valid w.r.t.
     * each node producer-consumer model.
    */
    std::vector<std::shared_ptr<StaticSchedulingElement>> generateBaseScheduling() const;

    /**
     * Fill-in early and late scheduling step from initial base scheduling.
     * For each node, specifies the earliest and latest possible execution
     * logical step.
    */
    void generateEarlyLateScheduling(std::vector<std::shared_ptr<StaticSchedulingElement>>& schedule) const;

private:
    void summarizeConsumerState(const std::shared_ptr<Node>& consumer, const std::string& nodeName) const;

protected:
    /** @brief Shared ptr to the scheduled graph view */
    std::shared_ptr<GraphView> mGraphView;
    /** @brief Shared ptr to the upper node containing the graph view */
    std::weak_ptr<Node> mUpperNode;
    /** @brief List of SchedulingElement (i.e: Nodes with their computation time) */
    std::vector<SchedulingElement> mScheduling;
    /** @brief List of nodes ordered by their */
    std::vector<std::vector<std::shared_ptr<StaticSchedulingElement>>> mStaticSchedule;
    std::size_t mStaticScheduleStep = 0;
    mutable std::map<std::shared_ptr<Node>, PriorProducersConsumers> mPriorCache;
};
} // namespace Aidge

#endif /* AIDGE_CORE_SCHEDULER_SCHEDULER_H_ */
