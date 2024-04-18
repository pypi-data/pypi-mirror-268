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

#include "aidge/operator/MetaOperator.hpp"

#include <cstddef>  // std::size_t
#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/utils/ErrorHandling.hpp"

Aidge::MetaOperator_Op::MetaOperator_Op(const std::string& type, const std::shared_ptr<GraphView>& graph)
    : OperatorTensor(type, graph->dataInputs().size(), (graph->getOrderedInputs().size() - graph->dataInputs().size()), graph->getOrderedOutputs().size()),
        mGraph(graph)
{
    mInputs = std::vector<std::shared_ptr<Tensor>>(mGraph->getOrderedInputs().size());
    for (std::size_t i = 0; i < mInputs.size(); ++i) {
        mInputs[i] = std::make_shared<Tensor>();
    }
    // Associate outputs to micro-graph outputs for custom implementation
    mOutputs = std::vector<std::shared_ptr<Tensor>>(mGraph->getOrderedOutputs().size());
    for (size_t outputIdx = 0; outputIdx < mOutputs.size(); ++outputIdx) {
        const auto& outputOp = mGraph->getOrderedOutputs()[outputIdx];
        if (outputOp.first) {
            mOutputs[outputIdx] = std::dynamic_pointer_cast<Tensor>(outputOp.first->getOperator()->getRawOutput(outputOp.second));
        }
    }
}

Aidge::Elts_t Aidge::MetaOperator_Op::getNbRequiredData(const IOIndex_t inputIdx) const {
    if (mImpl) {
        return mImpl->getNbRequiredData(inputIdx);
    }
    else {
        const auto& inputOp = mGraph->getOrderedInputs()[inputIdx];
        if (inputOp.first) {
            return inputOp.first->getOperator()->getNbRequiredData(inputOp.second);
        }
        else {
            return Elts_t::NoneElts();
        }
    }
}

Aidge::Elts_t Aidge::MetaOperator_Op::getNbRequiredProtected(const IOIndex_t inputIdx) const {
    if (mImpl) {
        return mImpl->getNbRequiredProtected(inputIdx);
    }
    else {
        const auto& inputOp = mGraph->getOrderedInputs()[inputIdx];
        if (inputOp.first) {
            return inputOp.first->getOperator()->getNbRequiredProtected(inputOp.second);
        }
        else {
            return Elts_t::NoneElts();
        }
    }
}

Aidge::Elts_t Aidge::MetaOperator_Op::getRequiredMemory(const IOIndex_t outputIdx, const std::vector<DimSize_t> &inputsSize) const {
    if (mImpl) {
        return mImpl->getRequiredMemory(outputIdx, inputsSize);
    }
    else {
        const auto& outputOp = mGraph->getOrderedOutputs()[outputIdx];
        if (outputOp.first) {
            return outputOp.first->getOperator()->getRequiredMemory(outputOp.second, inputsSize);
        }
        else {
            return Elts_t::NoneElts();
        }
    }
}

Aidge::Elts_t Aidge::MetaOperator_Op::getNbConsumedData(IOIndex_t inputIdx) const {
    if (mImpl) {
        return mImpl->getNbConsumedData(inputIdx);
    }
    else {
        const auto& inputOp = mGraph->getOrderedInputs()[inputIdx];
        if (inputOp.first) {
            return inputOp.first->getOperator()->getNbConsumedData(inputOp.second);
        }
        else {
            return Elts_t::NoneElts();
        }
    }
}

Aidge::Elts_t Aidge::MetaOperator_Op::getNbProducedData(IOIndex_t outputIdx) const {
    if (mImpl) {
        return mImpl->getNbProducedData(outputIdx);
    }
    else {
        const auto& outputOp = mGraph->getOrderedOutputs()[outputIdx];
        if (outputOp.first) {
            return outputOp.first->getOperator()->getNbProducedData(outputOp.second);
        }
        else {
            return Elts_t::NoneElts();
        }
    }
}

void Aidge::MetaOperator_Op::updateConsummerProducer() {
    if (mImpl) {
        mImpl->updateConsummerProducer();
    }
    else {
        if (!mScheduler) {
            // Lazy initialization
            mScheduler = std::make_shared<SequentialScheduler>(mGraph, mUpperNode.lock());
        }

        // TODO: check that generateScheduling() can be called multiple time to iteratively update the schedule.
        // It could be a good idea to unify updateConsummerProducer() and generateScheduling() into a "updateScheduling()"
        mScheduler->generateScheduling();
    }
}

void Aidge::MetaOperator_Op::forward() {
    if (mImpl) {
        // A custom implementation exists for this meta operator
        mImpl->forward();
    }
    else {
        // No custom implementation, use the individual operators implementations
        if (!mScheduler) {
            // Lazy initialization
            // TODO: should we assert that a scheduler already exists at this point?
            // => should be created in updateConsummerProducer()
            mScheduler = std::make_shared<SequentialScheduler>(mGraph, mUpperNode.lock());
            mScheduler->generateScheduling();
        }

        mScheduler->forward(false);
    }
}
