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

#ifndef AIDGE_CORE_OPERATOR_OPERATORTENSOR_H_
#define AIDGE_CORE_OPERATOR_OPERATORTENSOR_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

class Tensor;
class OperatorTensor : public Operator {
    /* TODO: Add an attribute specifying the type of Data used by the Operator.
     * The same way ``Type`` attribute specifies the type of Operator. Hence this
     * attribute could be checked in the forwardDims function to assert Operators
     * being used work with Tensors and cast them to OpertorTensor instead of
     * Operator.
     */
    /* TODO: Maybe change type attribute of Data object by an enum instead of an
     * array of char. Faster comparisons.
     */
protected:
    std::vector<std::shared_ptr<Tensor>> mInputs;
    std::vector<std::shared_ptr<Tensor>> mOutputs;

public:
    OperatorTensor() = delete;

    OperatorTensor(const std::string& type, const IOIndex_t nbData, const IOIndex_t nbParam,
                   const IOIndex_t nbOut);

    OperatorTensor(const OperatorTensor& other);

    ~OperatorTensor();

public:
    ///////////////////////////////////////////////////
    virtual void associateInput(const IOIndex_t inputIdx,
                                const std::shared_ptr<Data>& data) override;
    ///////////////////////////////////////////////////

    ///////////////////////////////////////////////////
    // Tensor access
    // input management
    void setInput(const IOIndex_t inputIdx, const std::shared_ptr<Data>& data) override final;
    void setInput(const IOIndex_t inputIdx, std::shared_ptr<Data>&& data) override final;
    const std::shared_ptr<Tensor>& getInput(const IOIndex_t inputIdx) const;
    std::shared_ptr<Data> getRawInput(const IOIndex_t inputIdx) const override final;

    // output management
    void setOutput(const IOIndex_t outputIdx, const std::shared_ptr<Data>& data) override;
    void setOutput(const IOIndex_t outputIdx, std::shared_ptr<Data>&& data) override;
    virtual const std::shared_ptr<Tensor>& getOutput(const IOIndex_t outputIdx) const;
    std::shared_ptr<Aidge::Data> getRawOutput(const Aidge::IOIndex_t outputIdx) const override final;
    ///////////////////////////////////////////////////

    ///////////////////////////////////////////////////
    // Tensor dimensions
    /**
     * @brief For a given output feature area, compute the associated receptive
     * field for each data input.
     * @param firstIdx First index of the output feature.
     * @param outputDims Size of output feature.
     * @param outputIdx Index of the output. Default 0.
     * @return std::vector<std::pair<std::size_t, std::vector<DimSize_t>>>
     * For each dataInput Tensor of the Operator, the first index and dimensions of the feature area.
     */
    virtual std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>> computeReceptiveField(const std::vector<DimSize_t>& firstEltDims, const std::vector<DimSize_t>& outputDims, const IOIndex_t outputIdx = 0) const;
    virtual void computeOutputDims();
    virtual bool outputDimsForwarded() const;
    ///////////////////////////////////////////////////

    virtual void setDataType(const DataType& dataType) const override;
};
}  // namespace Aidge

#endif  // AIDGE_CORE_OPERATOR_OPERATORTENSOR_H_