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
#include <memory>

#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"


Aidge::OperatorTensor::OperatorTensor(const std::string& type,
                                                            const IOIndex_t nbData,
                                                            const IOIndex_t nbParam,
                                                            const IOIndex_t nbOut)
: Operator(type, nbData, nbParam, nbOut, OperatorType::Tensor),
        mInputs(std::vector<std::shared_ptr<Tensor>>(nbData + nbParam, nullptr)),
        mOutputs(std::vector<std::shared_ptr<Tensor>>(nbOut)) {
    for (std::size_t i = 0; i < static_cast<std::size_t>(nbOut); ++i) {
        mOutputs[i] = std::make_shared<Tensor>();
        mOutputs[i]->setDataType(DataType::Float32);
    }
}


Aidge::OperatorTensor::OperatorTensor(const OperatorTensor& other)
    : Operator(other),
        mInputs(std::vector<std::shared_ptr<Tensor>>(other.nbInputs(), nullptr)),
        mOutputs(std::vector<std::shared_ptr<Tensor>>(other.nbOutputs())) {
    for (std::size_t i = 0; i < static_cast<std::size_t>(nbOutputs()); ++i) {
        mOutputs[i] = std::make_shared<Tensor>();
        // mOutputs[i] = std::make_shared<Tensor>(*(other.getOutput(i)));
        // datatype already copied
    }
}


void Aidge::OperatorTensor::associateInput(const Aidge::IOIndex_t inputIdx, const std::shared_ptr<Aidge::Data>& data) {
    AIDGE_ASSERT(inputIdx < nbInputs(), "{} Operator has {} inputs", type(), nbInputs());
    AIDGE_ASSERT(data->type() == Tensor::Type, "Input data must be of Tensor type");
    mInputs[inputIdx] = std::dynamic_pointer_cast<Tensor>(data);
}

void Aidge::OperatorTensor::setInput(const Aidge::IOIndex_t inputIdx, const std::shared_ptr<Aidge::Data>& data) {
    AIDGE_ASSERT(data->type() == Tensor::Type, "{} Operator only accepts Tensors as inputs", type());
    if (getInput(inputIdx)) {
        *mInputs[inputIdx] = *std::dynamic_pointer_cast<Tensor>(data);
    } else {
        mInputs[inputIdx] = std::make_shared<Tensor>(*std::dynamic_pointer_cast<Tensor>(data));
    }
}

Aidge::OperatorTensor::~OperatorTensor() = default;

void Aidge::OperatorTensor::setInput(const Aidge::IOIndex_t inputIdx, std::shared_ptr<Aidge::Data>&& data) {
    AIDGE_ASSERT(data->type() == Tensor::Type, "{} Operator only accepts Tensors as inputs", type());
    if (getInput(inputIdx)) {
        *mInputs[inputIdx] = std::move(*std::dynamic_pointer_cast<Tensor>(data));
    } else {
        mInputs[inputIdx] = std::make_shared<Tensor>(std::move(*std::dynamic_pointer_cast<Tensor>(data)));
    }
}

std::shared_ptr<Aidge::Data> Aidge::OperatorTensor::getRawInput(const Aidge::IOIndex_t inputIdx) const {
    return std::static_pointer_cast<Data>(getInput(inputIdx));
}
const std::shared_ptr<Aidge::Tensor>& Aidge::OperatorTensor::getInput(const Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(inputIdx < nbInputs(), "{} Operator has {} inputs", type(), nbInputs());
    return mInputs[inputIdx];
}

void Aidge::OperatorTensor::setOutput(const Aidge::IOIndex_t outputIdx, const std::shared_ptr<Aidge::Data>& data) {
    AIDGE_ASSERT(data->type() == Tensor::Type, "{} Operator only accepts Tensors as inputs", type());
    AIDGE_ASSERT(outputIdx < nbOutputs(), "{} Operator has {} outputs", type(), nbOutputs());
    const auto& data_tensor = std::dynamic_pointer_cast<Tensor>(data);
    // if (mImpl)
    //     AIDGE_ASSERT(data_tensor->getImpl()->backend() == backend(), "Data parameter and Operator have different backends: {} and {}", data_tensor->getImpl()->backend(), backend());
    *mOutputs[outputIdx] = *data_tensor;
}

void Aidge::OperatorTensor::setOutput(const Aidge::IOIndex_t outputIdx, std::shared_ptr<Aidge::Data>&& data) {
    AIDGE_ASSERT(data->type() == Tensor::Type, "{} Operator only accepts Tensors as inputs", type());
    AIDGE_ASSERT(outputIdx < nbOutputs(), "{} Operator has {} outputs", type(), nbOutputs());
    auto&& data_tensor = std::dynamic_pointer_cast<Tensor>(data);
    // if (mImpl)
    //     AIDGE_ASSERT(data_tensor->getImpl()->backend() == backend(), "Data parameter and Operator have different backends: {} and {}", data_tensor->getImpl()->backend(), backend());
    *mOutputs[outputIdx] = std::move(*data_tensor);
}

std::shared_ptr<Aidge::Data> Aidge::OperatorTensor::getRawOutput(const Aidge::IOIndex_t outputIdx) const {
    return std::static_pointer_cast<Data>(getOutput(outputIdx));
}

const std::shared_ptr<Aidge::Tensor>& Aidge::OperatorTensor::getOutput(const Aidge::IOIndex_t outputIdx) const {
    AIDGE_ASSERT(outputIdx < nbOutputs(), "{} Operator has {} outputs", type(), nbOutputs());
    return mOutputs[outputIdx];
}


std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<Aidge::DimSize_t>>> Aidge::OperatorTensor::computeReceptiveField(
        const std::vector<DimSize_t>& firstEltDims,
        const std::vector<Aidge::DimSize_t>& outputDims,
        const Aidge::IOIndex_t outputIdx) const
{
    static_cast<void>(outputIdx);
    if (outputIdx >= nbOutputs()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Operator output index out of range.");
    }
    if (nbInputs() != nbData()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Operator has attributes. Must be handled in an overrided function.");
    }
    if (!outputDimsForwarded() || getOutput(0)->nbDims() != outputDims.size()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range or output dim not forwarded yet.");
    }
    for (DimIdx_t i = 0; i < outputDims.size(); ++i) {
        if (((outputDims[i] + firstEltDims[i]) > getOutput(0)->dims()[i]) || (outputDims[i] == 0)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range for dimension {} ({} + {})", static_cast<std::size_t>(i), firstEltDims[i], outputDims[i]);
        }
    }
    // return the same Tensor description as given in function parameter for each data input
    return std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<Aidge::DimSize_t>>>(nbData(),std::pair<std::vector<Aidge::DimSize_t>, std::vector<Aidge::DimSize_t>>(firstEltDims, outputDims));
}

void Aidge::OperatorTensor::computeOutputDims() {
    // check inputs have been associated
    bool associated = (nbInputs() > 0); // do not compute anything if no input
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (!getInput(i)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
        }
        associated &= !(getInput(i)->empty());
    }
    if (associated) {
        const auto expectedDims =  getInput(0)->dims();
        for (std::size_t i = 1; i < nbInputs(); ++i) {
            if (expectedDims != getInput(i)->dims()) {
                AIDGE_THROW_OR_ABORT(std::runtime_error,
                    "{} operator's inputs should have the same dimensions: expected {} (input #0), given {} (input #{})",
                    type(), expectedDims, getInput(i)->dims(), i);
            }
        }
        mOutputs[0]->resize(expectedDims);
    }
}

bool Aidge::OperatorTensor::outputDimsForwarded() const {
    bool forwarded = true;
    // check both inputs and outputs have been filled
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        forwarded &= mInputs[i] ? !(getInput(i)->empty()) : false;
    }
    for (IOIndex_t i = 0; i < nbOutputs(); ++i) {
        // If getOutput(i) is nullptr, ignore this output (it may be a dummy
        // output in a MetaOperator)
        forwarded &= (getOutput(i)) ? !(getOutput(i)->empty()) : true;
    }
    return forwarded;
}

void Aidge::OperatorTensor::setDataType(const DataType& dataType) const {
    for (IOIndex_t i = 0; i < nbOutputs(); ++i) {
        getOutput(i)->setDataType(dataType);
    }

    for (IOIndex_t i = nbData(); i < nbInputs(); ++i) {
        AIDGE_ASSERT(getInput(i) != nullptr, "Missing input#{} for operator {}", i, type());
        getInput(i)->setDataType(dataType);
    }
}