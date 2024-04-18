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

#ifndef AIDGE_CORE_OPERATOR_GATHER_H_
#define AIDGE_CORE_OPERATOR_GATHER_H_

#include <cstdint>  // std::int64_t
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
enum class GatherAttr { Indices, GatheredShape, Axis };

class Gather_Op : public OperatorTensor,
                public Registrable<Gather_Op,
                                   std::string,
                                   std::shared_ptr<OperatorImpl>(const Gather_Op&)>,
                public StaticAttributes<GatherAttr, std::vector<std::int64_t>, std::vector<DimSize_t>, std::int64_t> {

public:
    static const std::string Type;

    Gather_Op() = delete;

    using Attributes_ = StaticAttributes<GatherAttr, std::vector<std::int64_t>, std::vector<DimSize_t>, std::int64_t>;
    template <GatherAttr e> using attr = typename Attributes_::template attr<e>;
    Gather_Op(const std::vector<std::int64_t>& indices, const std::vector<DimSize_t>& gatheredShape, std::int64_t axis)
            : OperatorTensor(Type, 1, 0, 1),
            Attributes_(
                attr<GatherAttr::Indices>(indices),
                attr<GatherAttr::GatheredShape>(gatheredShape),
                attr<GatherAttr::Axis>(axis))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Gather_Op(const Gather_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Gather_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Gather_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Gather_Op>(*this);
    }

    void computeOutputDims() override final;

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Gather( const std::vector<std::int64_t>& indices, const std::vector<DimSize_t>& gatheredShape, std::int64_t axis = 0, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Gather_Op>(indices, gatheredShape, axis), name);
}
} // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::GatherAttr>::data[] = {"Indices", "GatheredShape", "Axis"};
}

#endif /* AIDGE_CORE_OPERATOR_GATHER_H_ */
