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

#ifndef AIDGE_CORE_OPERATOR_SUB_H_
#define AIDGE_CORE_OPERATOR_SUB_H_

#include <memory>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

class Sub_Op : public OperatorTensor,
    public Registrable<Sub_Op, std::string, std::shared_ptr<OperatorImpl>(const Sub_Op&)> {
public:
    // FIXME: change accessibility
    std::array<std::shared_ptr<Tensor>, 2> mInputs = {std::make_shared<Tensor>(), std::make_shared<Tensor>()};
    const std::shared_ptr<Tensor> mOutput = std::make_shared<Tensor>();

public:
    static const std::string Type;

    Sub_Op() : OperatorTensor(Type, 2, 0, 1) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Sub_Op(const Sub_Op& op)
        : OperatorTensor(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Sub_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Sub_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Sub_Op>(*this);
    }

    void computeOutputDims() override final;


    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName(){
        return {"data_input_1", "data_input_2"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Sub(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Sub_Op>(), name);
}
} // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_SUB_H_ */
