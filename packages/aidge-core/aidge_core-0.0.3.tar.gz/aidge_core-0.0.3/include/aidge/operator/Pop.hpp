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

#ifndef AIDGE_CORE_OPERATOR_POP_H_
#define AIDGE_CORE_OPERATOR_POP_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class PopAttr { ForwardStep };

class Pop_Op : public OperatorTensor,
    public Registrable<Pop_Op, std::string, std::unique_ptr<OperatorImpl>(const Pop_Op&)>,
    public StaticAttributes<PopAttr, unsigned int> {
public:
    static const std::string Type;

    using Attributes_ = StaticAttributes<PopAttr, unsigned int>;
    template <PopAttr e>
    using attr = typename Attributes_::template attr<e>;

    Pop_Op()
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<PopAttr::ForwardStep>(0))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Pop_Op(const Pop_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Pop_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Pop_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Pop_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    void computeOutputDims() override final;
    void updateConsummerProducer() override;
    void forward() override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Pop(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Pop_Op>(), name);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::PopAttr>::data[] = {
    "ForwardStep"
};
}

#endif /* AIDGE_CORE_OPERATOR_POP_H_ */