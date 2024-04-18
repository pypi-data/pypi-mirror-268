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

#include <cassert>
#include <string>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"

Aidge::OperatorImpl::OperatorImpl(const Operator& op, const std::string& backend):
    mOp(op),
    mBackend(backend),
    mNbConsumedData(mOp.nbInputs(), Elts_t::NoneElts()),
    mNbProducedData(mOp.nbOutputs(), Elts_t::NoneElts())
{
    //ctor
}

Aidge::Elts_t Aidge::OperatorImpl::getNbRequiredData(const Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(mOp.getRawInput(inputIdx),
        "a valid input is required at index {} for operator type {}",
        inputIdx, mOp.type());

    if (mOp.getRawInput(inputIdx)) {
        const auto input = std::static_pointer_cast<Tensor>(mOp.getRawInput(inputIdx));
        if (!input->empty()) {
            // Known amount of data: requires the whole tensor by default
            return Elts_t::DataElts(input->size());
        }
        else {
            // Unknown amount of data: require a single token by default
            return Elts_t::TokenElts(1);
        }
    }

    // Input not connected, meaning it is an optional input: do no require anything!
    return Elts_t::NoneElts();
}

Aidge::Elts_t Aidge::OperatorImpl::getNbRequiredProtected(IOIndex_t inputIdx) const {
    AIDGE_ASSERT(mOp.getRawInput(inputIdx),
        "a valid input is required at index {} for operator type {}",
        inputIdx, mOp.type());

    if (mOp.getRawInput(inputIdx)) {
        const auto input = std::static_pointer_cast<Tensor>(mOp.getRawInput(inputIdx));
        if (!input->empty()) {
            // Known amount of data: protect the whole tensor by default
            return Elts_t::DataElts(input->size());
        }
        else {
            // Unknown amount of data: protect a single token by default
            // (this does not really make sense for now, as getNbRequiredProtected()
            // is supposed to give a precise amount of data to protect for
            // memory management purpose...)
            return Elts_t::TokenElts(1);
        }
    }

    // Input not connected, meaning it is an optional input: do no require anything!
    return Elts_t::NoneElts();
}

Aidge::Elts_t Aidge::OperatorImpl::getRequiredMemory(const Aidge::IOIndex_t outputIdx,
                                                         const std::vector<Aidge::DimSize_t> &/*inputsSize*/) const {
    AIDGE_ASSERT(mOp.getRawOutput(outputIdx),
        "a valid output is required at index {} for operator type {}",
        outputIdx, mOp.type());

    if (mOp.getRawOutput(outputIdx)) {
        const auto output = std::static_pointer_cast<Tensor>(mOp.getRawOutput(outputIdx));
        if (!output->empty()) {
            // Known amount of data: requires the whole tensor by default,
            // regardless of available data on inputs
            return Elts_t::DataElts(output->size());
        }
        else {
            // Unknown amount of data: require a single token by default
            // (this does not really make sense for now, as getRequiredMemory()
            // is supposed to give a precise amount of data to allocate for
            // memory management purpose...)
            return Elts_t::TokenElts(1);
        }
    }

    // Output not set, meaning it is an optional output: do no require anything!
    return Elts_t::NoneElts();
}

Aidge::Elts_t Aidge::OperatorImpl::getNbConsumedData(Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(static_cast<std::size_t>(inputIdx) < mNbConsumedData.size(),
        "input index ({}) is out of bound ({}) for operator type {}",
        inputIdx, mNbConsumedData.size(), mOp.type());
    return mNbConsumedData[static_cast<std::size_t>(inputIdx)];
}

Aidge::Elts_t Aidge::OperatorImpl::getNbProducedData(Aidge::IOIndex_t outputIdx) const {
    AIDGE_ASSERT(static_cast<std::size_t>(outputIdx) < mNbProducedData.size(),
        "output index ({}) is out of bound ({}) for operator type {}",
        outputIdx, mNbProducedData.size(), mOp.type());
    return mNbProducedData[static_cast<std::size_t>(outputIdx)];
}

void Aidge::OperatorImpl::updateConsummerProducer(){
    // Update producer-consumer data
    for (std::size_t inputIdx = 0; inputIdx < mNbConsumedData.size(); ++inputIdx) {
        // each input is consumed by the minimum amount for a forward pass
        mNbConsumedData[inputIdx] += getNbRequiredData(static_cast<IOIndex_t>(inputIdx));
    }

    for (std::size_t outputIdx = 0; outputIdx < mNbProducedData.size(); ++outputIdx) {
        mNbProducedData[outputIdx] += getRequiredMemory(outputIdx, {});
    }
}

void Aidge::OperatorImpl::resetConsummerProducer(){
    std::fill(mNbConsumedData.begin(), mNbConsumedData.end(), Elts_t::NoneElts());
    std::fill(mNbProducedData.begin(), mNbProducedData.end(), Elts_t::NoneElts());
}

void Aidge::OperatorImpl::forward() {
    AIDGE_THROW_OR_ABORT(std::runtime_error, "forward() not implemented");
}

void Aidge::OperatorImpl::backward() {
    AIDGE_THROW_OR_ABORT(std::runtime_error, "backward() not implemented");
}
