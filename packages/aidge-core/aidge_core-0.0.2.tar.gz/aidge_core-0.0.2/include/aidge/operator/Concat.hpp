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

#ifndef AIDGE_CORE_OPERATOR_CONCAT_H_
#define AIDGE_CORE_OPERATOR_CONCAT_H_

#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

#include "aidge/utils/Registrar.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class ConcatAttr { Axis };

class Concat_Op : public OperatorTensor,
    public Registrable<Concat_Op, std::string, std::shared_ptr<OperatorImpl>(const Concat_Op&)>,
    public StaticAttributes<ConcatAttr, DimSize_t> {
public:
    static const std::string Type;

    using Attributes_ = StaticAttributes<ConcatAttr, DimSize_t>;
    template <ConcatAttr e>
    using attr = typename Attributes_::template attr<e>;

    Concat_Op(const IOIndex_t nbIn, const DimSize_t axis)
        : OperatorTensor(Type, nbIn, 0, 1),
          Attributes_(attr<ConcatAttr::Axis>(axis))
    {
        if (nbIn == 0) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Add operator should have at least one input.");
        }
    }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Concat_Op(const Concat_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Concat_Op, *this, op.backend());
        }else{
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Concat_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Concat_Op>(*this);
    }

    void computeOutputDims() override final;

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input_0", "data_input_n"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Concat(const IOIndex_t nbIn, const DimIdx_t axis = 0, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Concat_Op>(nbIn, axis), name);
}
}

namespace {
    template <>
    const char* const EnumStrings<Aidge::ConcatAttr>::data[] = {
        "Axis"
    };
}

#endif /* AIDGE_CORE_OPERATOR_CONCAT_H_ */
