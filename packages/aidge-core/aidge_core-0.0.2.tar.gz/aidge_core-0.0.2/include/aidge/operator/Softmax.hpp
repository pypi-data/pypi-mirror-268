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

#ifndef AIDGE_CORE_OPERATOR_SOFTMAX_H_
#define AIDGE_CORE_OPERATOR_SOFTMAX_H_

#include <memory>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class SoftmaxAttr { AxisIdx };

class Softmax_Op : public OperatorTensor,
                public Registrable<Softmax_Op,
                                   std::string,
                                   std::shared_ptr<OperatorImpl>(const Softmax_Op&)>,
                public StaticAttributes<SoftmaxAttr, int> {

public:
    static const std::string Type;

    Softmax_Op() = delete;

    using Attributes_ = StaticAttributes<SoftmaxAttr, int>;
    template <SoftmaxAttr e> using attr = typename Attributes_::template attr<e>;
    Softmax_Op(int axis)
            :  OperatorTensor(Type, 1, 0, 1),
            Attributes_(attr<SoftmaxAttr::AxisIdx>(axis)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Softmax_Op(const Softmax_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Softmax_Op, *this, op.backend());
        }else{
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Softmax_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Softmax_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Softmax(int axis, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Softmax_Op>(axis), name);
}
} // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::SoftmaxAttr>::data[] = {"Axis"};
}

#endif /* AIDGE_CORE_OPERATOR_SOFTMAX_H_ */
