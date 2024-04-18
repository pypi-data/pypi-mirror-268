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

#ifndef AIDGE_CORE_OPERATOR_LEAKYRELU_H_
#define AIDGE_CORE_OPERATOR_LEAKYRELU_H_

#include <vector>
#include <memory>

#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class LeakyReLUAttr {
    NegativeSlope
};

class LeakyReLU_Op : public OperatorTensor,
    public Registrable<LeakyReLU_Op, std::string, std::shared_ptr<OperatorImpl>(const LeakyReLU_Op&)>,
    public StaticAttributes<LeakyReLUAttr, float> {
public:
    static const std::string Type;

    LeakyReLU_Op() = delete;

    using Attributes_ = StaticAttributes<LeakyReLUAttr, float>;
    template <LeakyReLUAttr e> using attr = typename Attributes_::template attr<e>;

    LeakyReLU_Op(float negativeSlope)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(
            attr<LeakyReLUAttr::NegativeSlope>(negativeSlope))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    LeakyReLU_Op(const LeakyReLU_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(LeakyReLU_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::LeakyReLU_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<LeakyReLU_Op>(*this);
    }



    void setBackend(const std::string& name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(LeakyReLU_Op, *this, name);
        mOutputs[0]->setBackend(name, device);
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> LeakyReLU(float negativeSlope = 0.0f, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<LeakyReLU_Op>(negativeSlope), name);
}
}

namespace {
template <>
const char* const EnumStrings<Aidge::LeakyReLUAttr>::data[]
    = {"NegativeSlope"};
}

#endif /* AIDGE_CORE_OPERATOR_RELU_H_ */
