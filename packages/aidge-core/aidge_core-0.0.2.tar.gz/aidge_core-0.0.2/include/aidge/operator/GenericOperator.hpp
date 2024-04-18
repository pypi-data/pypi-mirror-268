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

#ifndef AIDGE_CORE_OPERATOR_GENERICOPERATOR_H_
#define AIDGE_CORE_OPERATOR_GENERICOPERATOR_H_

#include <memory>
#include <vector>
#include <string>

#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/DynamicAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"


namespace Aidge {
class GenericOperator_Op
    : public OperatorTensor,
      public Registrable<GenericOperator_Op, std::string, std::unique_ptr<OperatorImpl>(std::shared_ptr<GenericOperator_Op>)>,
      public DynamicAttributes {
private:
    using ComputeDimsFunc = std::function<std::vector<std::vector<size_t>>(const std::vector<std::vector<size_t>>&)>;

    ComputeDimsFunc mComputeOutputDims;

public:
    GenericOperator_Op(const std::string& type, IOIndex_t nbData, IOIndex_t nbParam, IOIndex_t nbOut)
        : OperatorTensor(type, nbData, nbParam, nbOut)
    {
        mImpl = std::make_shared<OperatorImpl>(*this, "");
    }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    GenericOperator_Op(const GenericOperator_Op& op)
        : OperatorTensor(op)
    {
        mImpl = std::make_shared<OperatorImpl>(*this, op.backend());
    }

    ~GenericOperator_Op() = default;

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::GenericOperator_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<GenericOperator_Op>(*this);
    }

public:
    void computeOutputDims() override final;

    bool outputDimsForwarded() const override final;

    void setBackend(const std::string & /*name*/, DeviceIdx_t /*device*/ = 0) override { fmt::print("setBackend: not available yet.\n"); }
    void setDataType(const DataType& /*datatype*/) const override { fmt::print("setDataType: not available yet.\n"); }

    // Helper functions that can be used with setComputeOutputDims():
    static const ComputeDimsFunc Identity;
    static const ComputeDimsFunc InputIdentity(IOIndex_t inputIdx, IOIndex_t nbOutputs);
    inline void setComputeOutputDims(ComputeDimsFunc func) {
        mComputeOutputDims = func;
    }
};

/**
 * @brief Fictive custom operator not associated with any implementation.
 * Allows to import unknown operators and simulate new ones.
 * @param type Type of the fictive operator.
 * @param nbData Number of input data.
 * @param nbParam Number of parameters.
 * @param nbOut Number of output data.
 * @param name (optional) name of the Operator.
 * @return std::shared_ptr<Node> Node associated with the Generic Operator.
 */
inline std::shared_ptr<Node> GenericOperator(const std::string& type, IOIndex_t nbData, IOIndex_t nbParam, IOIndex_t nbOut,
                                             const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<GenericOperator_Op>(type, nbData, nbParam, nbOut), name);
}
}  // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_GENERICOPERATOR_H_ */
