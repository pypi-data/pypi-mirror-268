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

#ifndef AIDGE_CORE_SCHEDULER_PARALLELSCHEDULER_H_
#define AIDGE_CORE_SCHEDULER_PARALLELSCHEDULER_H_

#include <chrono>
#include <memory>
#include <set>
#include <string>
#include <vector>
#include <map>

#include "aidge/scheduler/Scheduler.hpp"

namespace Aidge {
/**
 * Multi-threaded parallel scheduler with dynamic scheduling.
*/
class ParallelScheduler : public Scheduler {
public:
    ParallelScheduler(std::shared_ptr<GraphView> graphView, std::shared_ptr<Node> upperNode = nullptr)
        : Scheduler(graphView, upperNode)
    {
        // ctor
    };
    ~ParallelScheduler() = default;

    /**
     * @brief Run the provided Computational Graph with a batch of data
     */
    virtual void forward(bool forwardDims = true, std::vector<std::shared_ptr<Aidge::Tensor>> data = {});
};
} // namespace Aidge

#endif /* AIDGE_CORE_SCHEDULER_PARALLELSCHEDULER_H_ */
