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

#include "aidge/scheduler/ParallelScheduler.hpp"
#include "aidge/scheduler/ThreadPool.hpp"

#include <chrono>
#include <memory>
#include <set>
#include <string>

#include <fmt/ranges.h>
#include <fmt/color.h>

#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/operator/Memorize.hpp"
#include "aidge/operator/MetaOperator.hpp"

void Aidge::ParallelScheduler::forward(bool forwardDims, std::vector<std::shared_ptr<Aidge::Tensor>> data) {
    // Collect all data input of the graph (that are producers)
    if (!data.empty()){
        connectInputs(data);
    }

    // Forward dims (if allowed)
    if (forwardDims) {mGraphView->forwardDims(); }

    // Generate scheduling *only if empty*
    // If scheduling was already generated (in one or several steps, i.e. one or
    // several successive call to generateScheduling()), do not generate it twice
    if (mStaticSchedule.empty()) {
        this->generateScheduling();
    }

    const auto namePtrTable = mGraphView->getRankedNodesName("{0} ({1}#{3})");

    // Sort static scheduling, the order will be the prefered threads scheduling
    // order for non critical nodes
    std::deque<std::shared_ptr<StaticSchedulingElement>> staticSchedule(mStaticSchedule.at(mStaticScheduleStep).begin(), mStaticSchedule.at(mStaticScheduleStep).end());
    std::stable_sort(staticSchedule.begin(), staticSchedule.end(),
        [](const auto& lhs, const auto& rhs) { return ((lhs->early < rhs->early) || (lhs->early == rhs->early && lhs->late < rhs->late)); });

    // The thread pool has N threads running to process nodes.
    // Thread pooling avoid the overhead of threads creation and deletion for
    // each node execution.
    ThreadPool pool;

    size_t latest = 0;
    std::mutex schedulingMutex;
    std::map<std::shared_ptr<StaticSchedulingElement>, std::atomic<bool>> finished;

    while (!staticSchedule.empty()) {
        Log::debug("Step {}", latest);

        std::vector<std::shared_ptr<StaticSchedulingElement>> mustFinish;

        // Run all nodes that must be run at this step: latest (critical nodes)
        for (size_t i = 0; i < staticSchedule.size(); ) {
            auto runnable = staticSchedule[i];

            if (runnable->late == latest) {
                // Wait for potential preceding non-critical nodes to finish
                while (true) {
                    bool ready = true;
                    for (auto elt : runnable->laterThan) {
                        ready = ready && finished.at(elt);
                    }
                    if (!ready) {
                        std::this_thread::yield();
                    }
                    else {
                        break;
                    }
                }

                // Add the critical node to the thread pool queue, to be run ASAP
                finished[runnable] = false;
                pool.queueJob([node = runnable->node, &finished = finished.at(runnable), &schedulingMutex, this]() {
                    const auto tStart = std::chrono::high_resolution_clock::now();
                    node->forward();
                    const auto tEnd = std::chrono::high_resolution_clock::now();
                    finished = true;
                    {
                        std::unique_lock<std::mutex> lock(schedulingMutex);
                        mScheduling.emplace_back(SchedulingElement(node, tStart, tEnd));
                    }
                });
                staticSchedule.erase(staticSchedule.begin() + i);
                mustFinish.push_back(runnable);

                Log::debug("  run critical {}", namePtrTable.at(runnable->node));

                // Ensure the following nodes cannot start earlier than next step
                for (auto elt : runnable->earlierThan) {
                    if (elt->early < latest + 1) {
                        Log::debug("    {}: {} -> {}", namePtrTable.at(elt->node), elt->early, latest + 1);
                        elt->early = latest + 1;
                        AIDGE_INTERNAL_ASSERT(elt->early <= elt->late);
                    }
                }
            }
            else if (runnable->early > latest + 1) {
                // There cannot be more node that must be run at latest + 1
                // latest + 1 and not latest because early may have been updated
                // for some elements to latest + 1 (above).
                break;
            }
            else {
                ++i;
            }
        }

        // If some threads are still available, run next early nodes
        // These nodes are non-critical, meaning they can still be run at least
        // in the next step
        for (size_t i = 0; i < staticSchedule.size(); ) {
            auto runnable = staticSchedule[i];
            if (!pool.busy() && runnable->early <= latest) {
                // Check that potential preceding non-critical nodes are finished
                bool ready = true;
                for (auto elt : runnable->laterThan) {
                    ready = ready && finished.at(elt);
                }

                if (ready) {
                    // All preceding nodes have finished, this node can be run.
                    // Add the node to the thread pool queue, to be run ASAP
                    finished[runnable] = false;
                    pool.queueJob([node = runnable->node, &finished = finished.at(runnable), &schedulingMutex, this]() {
                        const auto tStart = std::chrono::high_resolution_clock::now();
                        node->forward();
                        const auto tEnd = std::chrono::high_resolution_clock::now();
                        finished = true;
                        {
                            std::unique_lock<std::mutex> lock(schedulingMutex);
                            mScheduling.emplace_back(SchedulingElement(node, tStart, tEnd));
                        }
                    });
                    staticSchedule.erase(staticSchedule.begin() + i);

                    Log::debug("  run {}", namePtrTable.at(runnable->node));

                    // Ensure the following nodes cannot start earlier than next step
                    for (auto elt : runnable->earlierThan) {
                        if (elt->early < latest + 1) {
                            Log::debug("    {}: {} -> {}", namePtrTable.at(elt->node), elt->early, latest + 1);
                            elt->early = latest + 1;
                            AIDGE_INTERNAL_ASSERT(elt->early <= elt->late);
                        }
                    }
                }
                else {
                    // The node cannot be run yet, because preceding nodes are
                    // still running, move to the next one in schedule
                    ++i;
                }
            }
            else {
                // Thread pool is already full or no more node can be run at
                // this step (latest)
                break;
            }
        }

        // Wait for all nodes that must finish at latest to be finished
        // By scheduling construction, no other node can be started before all 
        // nodes at latest step are finished
        while (true) {
            bool ready = true;
            for (auto elt : mustFinish) {
                ready = ready && finished.at(elt);
            }
            if (!ready) {
                std::this_thread::yield();
            }
            else {
                break;
            }
        }

        ++latest;
    }

    ++mStaticScheduleStep;
    if (mStaticScheduleStep == mStaticSchedule.size()) {
        mStaticScheduleStep = 0;
    }
}
