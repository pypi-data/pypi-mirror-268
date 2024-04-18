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

#ifndef AIDGE_CORE_SCHEDULER_SEQUENTIALSCHEDULER_H_
#define AIDGE_CORE_SCHEDULER_SEQUENTIALSCHEDULER_H_

#include <memory>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/scheduler/Scheduler.hpp"

namespace Aidge {
/**
 * Multi-threaded parallel scheduler with dynamic scheduling.
*/
class SequentialScheduler : public Scheduler {
public:
    enum class SchedulingPolicy {
        Default,
        AsSoonAsPossible,
        AsLateAsPossible
    };

public:
    SequentialScheduler(std::shared_ptr<GraphView> graphView, std::shared_ptr<Node> upperNode = nullptr)
        : Scheduler(graphView, upperNode),
          mSchedulingPolicy(SchedulingPolicy::Default)
    {
        // ctor
    };

    ~SequentialScheduler() = default;

public:
    inline void setSchedulingPolicy(SchedulingPolicy policy) {
        mSchedulingPolicy = policy;
    }
    /**
     * @brief Run the provided Computational Graph with a batch of data
     */
    virtual void forward(bool forwardDims = true, std::vector<std::shared_ptr<Aidge::Tensor>> data = {});

    /**
     * @brief Run the provided Computational Graph with a batch of data
     */
    void backward(std::vector<std::shared_ptr<Aidge::Tensor>> data, bool instantiateGrad = true);

private:
    SchedulingPolicy mSchedulingPolicy;
};
} // namespace Aidge

#endif /* AIDGE_CORE_SCHEDULER_SEQUENTIALSCHEDULER_H_ */
