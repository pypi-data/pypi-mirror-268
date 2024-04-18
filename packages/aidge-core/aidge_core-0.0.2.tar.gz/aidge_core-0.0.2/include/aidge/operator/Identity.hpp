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

#ifndef AIDGE_CORE_OPERATOR_IDENTITY_H_
#define AIDGE_CORE_OPERATOR_IDENTITY_H_

#include <cassert>
#include <memory>
#include <vector>

#include "aidge/utils/Registrar.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

namespace Aidge {

/**
 * @brief Indentity_Op is an helper operator made to ease the declaration of MetaNodes.
 * This Operator has no Implementation, it just forward its input Tensor.
 * Note: Error may occur if new methods are added in Operator which use an implementation.
 * Has we need to update this class to remove the use of Impl.
 *
 */
class Identity_Op : public OperatorTensor,
    public Registrable<Identity_Op, std::string, std::unique_ptr<OperatorImpl>(const Identity_Op&)> {
public:
    static const std::string Type;

    Identity_Op()
        : OperatorTensor(Type, 1, 0, 1)
    {
        mImpl = std::make_shared<OperatorImpl>(*this, "");
    }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Identity_Op(const Identity_Op& op)
        : OperatorTensor(op)
    {
        mImpl = std::make_shared<OperatorImpl>(*this, op.backend());
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Identity_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Identity_Op>(*this);
    }

    void computeOutputDims() override final {} // Do nothing

    /**
     * @brief Check if output dimensions have been computed.
     * @note Since Indentity has no output Tensor, this function checks if its
     * only input's dimensions have been computed.
     *
     * @return true Input has dimensions.
     * @return false Input has no dimensions or is a nullptr.
     */
    bool outputDimsForwarded() const override final {
        return mInputs[0] ? !mInputs[0]->empty() : false;
    }


    void forward() override final { runHooks(); }

    void backward() override final { }

    void setOutput(const IOIndex_t outputIdx, const std::shared_ptr<Data>& data) override final {
        AIDGE_ASSERT(data->type() == "Tensor", "{} Operator only accepts Tensors as outputs", type());
        AIDGE_ASSERT(outputIdx < nbInputs(), "{} Operator has {} outputs", type(), nbInputs());
        *mInputs[outputIdx] = *std::dynamic_pointer_cast<Tensor>(data);
    }

    void setOutput(const IOIndex_t outputIdx, std::shared_ptr<Data>&& data) override final {
        AIDGE_ASSERT(data->type() == "Tensor", "{} Operator only accepts Tensors as inputs", type());
        AIDGE_ASSERT(outputIdx < nbInputs(), "{} Operator has {} outputs", type(), nbInputs());
        *mInputs[outputIdx] = std::move(*std::dynamic_pointer_cast<Tensor>(data));
    }

    const std::shared_ptr<Tensor>& getOutput(const IOIndex_t outputIdx) const override final {
        AIDGE_ASSERT(outputIdx < nbInputs(), "{} Operator has {} outputs", type(), nbInputs());
        if (mInputs[outputIdx] == nullptr){
            return mOutputs[outputIdx]; // Input is not initialized with empty tensor
        }
        return mInputs[outputIdx]; // Identity, so Output is Input
    }
    void setBackend(const std::string& /*name*/, DeviceIdx_t /*device*/ = 0) override final {
        // setBackend do nothing, Identity node has no backend it just pass the same Tensor
    }
    void setDataType(const DataType& /*dataType*/) const override final {
        // setDatatype do nothing, Identity node has no backend it just pass the same Tensor
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Identity(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Identity_Op>(), name);
}
}

#endif /* AIDGE_CORE_OPERATOR_IDENTITY_H_ */
