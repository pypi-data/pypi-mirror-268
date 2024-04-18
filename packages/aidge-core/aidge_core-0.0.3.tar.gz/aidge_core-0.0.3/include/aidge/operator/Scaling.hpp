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

#ifndef AIDGE_CORE_OPERATOR_SCALING_H_
#define AIDGE_CORE_OPERATOR_SCALING_H_

#include <vector>
#include <memory>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class ScalingAttr {
    scalingFactor, quantizedNbBits, isOutputUnsigned
};

class Scaling_Op : public OperatorTensor,
    public Registrable<Scaling_Op, std::string, std::unique_ptr<OperatorImpl>(const Scaling_Op&)>,
    public StaticAttributes<ScalingAttr, float, size_t, bool> {
public:
    static const std::string Type;

    Scaling_Op() = delete;

    using Attributes_ = StaticAttributes<ScalingAttr, float, std::size_t, bool>;
    template <ScalingAttr e> using attr = typename Attributes_::template attr<e>;

    Scaling_Op(float scalingFactor, std::size_t nbBits, bool isOutputUnsigned)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(
            attr<ScalingAttr::scalingFactor>(scalingFactor),
            attr<ScalingAttr::quantizedNbBits>(nbBits),
            attr<ScalingAttr::isOutputUnsigned>(isOutputUnsigned))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Scaling_Op(const Scaling_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Scaling_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Scaling_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Scaling_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName() {
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

/*
inline std::shared_ptr<Node> Scaling(float scalingFactor = 1.0f, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Scaling_Op>(scalingFactor), name);
}
*/
inline std::shared_ptr<Node> Scaling(float scalingFactor = 1.0f, std::size_t quantizedNbBits=8, bool isOutputUnsigned=true, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Scaling_Op>(scalingFactor,quantizedNbBits, isOutputUnsigned), name);
}
} // namespace Aidge

namespace {
template <>
const char* const EnumStrings<Aidge::ScalingAttr>::data[]
    = {"scalingFactor", "quantizedNbBits", "isOutputUnsigned"};
}

#endif /* AIDGE_CORE_OPERATOR_SCALING_H_ */
