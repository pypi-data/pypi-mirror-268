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

#ifndef AIDGE_CORE_OPERATOR_RESHAPE_H_
#define AIDGE_CORE_OPERATOR_RESHAPE_H_

#include <memory>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

enum class ReshapeAttr { Shape };

class Reshape_Op : public OperatorTensor,
                   public Registrable<Reshape_Op, std::string, std::shared_ptr<OperatorImpl>(const Reshape_Op&)>,
                   public StaticAttributes<ReshapeAttr, std::vector<std::int64_t>> {

public:
    static const std::string Type;

    Reshape_Op() = delete;

    using Attributes_ = StaticAttributes<ReshapeAttr, std::vector<std::int64_t>>;
    template <ReshapeAttr e>
    using attr = typename Attributes_::template attr<e>;

    Reshape_Op(const std::vector<std::int64_t>& shape)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<ReshapeAttr::Shape>(shape))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Reshape_Op(const Reshape_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Reshape_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Reshape_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Reshape_Op>(*this);
    }

    void computeOutputDims() override final;

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Reshape(const std::vector<std::int64_t>& shape,
                                   		const std::string &name = "") {
    // FIXME: properly handle default w&b initialization in every cases
    return std::make_shared<Node>(std::make_shared<Reshape_Op>(shape), name);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::ReshapeAttr>::data[] = { "Shape" };
}

#endif /* AIDGE_CORE_OPERATOR_RESHAPE_H_ */
