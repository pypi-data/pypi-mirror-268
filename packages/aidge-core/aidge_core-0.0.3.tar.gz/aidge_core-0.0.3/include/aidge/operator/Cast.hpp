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

#ifndef AIDGE_CORE_OPERATOR_CAST_H_
#define AIDGE_CORE_OPERATOR_CAST_H_

#include <cassert>
#include <memory>
#include <vector>

#include "aidge/utils/Registrar.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

class Cast_Op : public OperatorTensor,
    public Registrable<Cast_Op, std::string, std::unique_ptr<OperatorImpl>(const Cast_Op&)> {
public:
    static const std::string Type;

    Cast_Op() : OperatorTensor(Type, 1, 0, 1) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Cast_Op(const Cast_Op& op)
        : OperatorTensor(op)
    {
        if (op.mImpl) {
            SET_IMPL_MACRO(Cast_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Cast_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Cast_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    void forward() override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Cast(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Cast_Op>(), name);
}
}

#endif /* AIDGE_CORE_OPERATOR_CAST_H_ */