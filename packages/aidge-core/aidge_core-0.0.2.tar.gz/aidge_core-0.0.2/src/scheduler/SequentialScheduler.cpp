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

#include "aidge/scheduler/SequentialScheduler.hpp"

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
#include "aidge/recipes/GraphViewHelper.hpp"

void Aidge::SequentialScheduler::forward(bool forwardDims, std::vector<std::shared_ptr<Aidge::Tensor>> data) {
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

    // Sort static scheduling according to the policy
    std::vector<std::shared_ptr<StaticSchedulingElement>> staticSchedule(mStaticSchedule.at(mStaticScheduleStep).begin(), mStaticSchedule.at(mStaticScheduleStep).end());

    if (mSchedulingPolicy == SchedulingPolicy::AsSoonAsPossible) {
        std::stable_sort(staticSchedule.begin(), staticSchedule.end(),
            [](const auto& lhs, const auto& rhs) { return (lhs->early < rhs->early); });
    }
    else if (mSchedulingPolicy == SchedulingPolicy::AsLateAsPossible) {
        std::stable_sort(staticSchedule.begin(), staticSchedule.end(),
            [](const auto& lhs, const auto& rhs) { return (lhs->late < rhs->late); });
    }

    const auto namePtrTable = mGraphView->getRankedNodesName("{0} ({1}#{3})");

    for (const auto& runnable : staticSchedule) {
        Log::debug("run: {}", namePtrTable.at(runnable->node));

        const auto tStart = std::chrono::high_resolution_clock::now();
        runnable->node->forward();
        const auto tEnd = std::chrono::high_resolution_clock::now();
        mScheduling.push_back(SchedulingElement(runnable->node, tStart, tEnd));
    }

    ++mStaticScheduleStep;
    if (mStaticScheduleStep == mStaticSchedule.size()) {
        mStaticScheduleStep = 0;
    }
}

void Aidge::SequentialScheduler::backward(std::vector<std::shared_ptr<Aidge::Tensor>> data, bool instanciateGrad) {
    // create ad set Grad values
    if (instanciateGrad) { compile_gradient(mGraphView); }

    const auto& ordered_outputs = mGraphView->getOrderedOutputs();
    AIDGE_ASSERT(ordered_outputs.size() == data.size(), "You must provide the \
                   right number of data objects to run the backward function. \
                   {} outputs detected for the current GraphView when {} were \
                   provided.", ordered_outputs.size(), data.size());
    for (std::size_t i = 0; i < ordered_outputs.size(); ++i) {
        const std::shared_ptr<OperatorTensor> op_ = std::dynamic_pointer_cast<OperatorTensor>(ordered_outputs[i].first->getOperator());
        const std::shared_ptr<Tensor> t_grad = op_->getOutput(ordered_outputs[i].second)->grad();
        AIDGE_ASSERT(data[i]->dims() == t_grad->dims(), "Wrong gradient size.");
        *t_grad = data[i]->clone();
    }
    // Generate scheduling *only if empty*
    // If scheduling was already generated (in one or several steps, i.e. one or
    // several successive call to generateScheduling()), do not generate it twice
    if (mStaticSchedule.empty()) {
        this->generateScheduling();
    }

    // map of node <-> info to display with verbose
    const auto namePtrTable = mGraphView->getRankedNodesName("{0} ({1}#{3})");

    // run scheduled operators in reverse order
    const auto& runnableList = mStaticSchedule.at(mStaticScheduleStep);
    for (auto runnable = runnableList.crbegin(); runnable != runnableList.crend(); ++runnable) {
        Log::debug("run: {}", namePtrTable.at((*runnable)->node));

        const auto tStart = std::chrono::high_resolution_clock::now();
        (*runnable)->node->backward();
        const auto tEnd = std::chrono::high_resolution_clock::now();
        mScheduling.push_back(SchedulingElement((*runnable)->node, tStart, tEnd));
    }

    ++mStaticScheduleStep;
    if (mStaticScheduleStep == mStaticSchedule.size()) {
        mStaticScheduleStep = 0;
    }
}
