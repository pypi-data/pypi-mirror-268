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

#ifndef AIDGE_CORE_OPERATOR_FC_H_
#define AIDGE_CORE_OPERATOR_FC_H_

#include <array>
#include <memory>
#include <vector>

#include "aidge/utils/Types.h"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"

namespace Aidge {
enum class FCAttr { OutChannels, NoBias };

class FC_Op : public OperatorTensor,
              public Registrable<FC_Op,
                                 std::string,
                                 std::shared_ptr<OperatorImpl>(const FC_Op &)>,
              public StaticAttributes<FCAttr, DimSize_t, bool> {
public:
    static const std::string Type;

    FC_Op() = delete;

    using Attributes_ = StaticAttributes<FCAttr, DimSize_t, bool>;
    template <FCAttr e> using attr = typename Attributes_::template attr<e>;

    FC_Op(DimSize_t out_channels, bool noBias)
    : OperatorTensor(Type, 1, 2, 1),
      Attributes_(
        attr<FCAttr::OutChannels>(out_channels),
        attr<FCAttr::NoBias>(noBias))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    FC_Op(const FC_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(FC_Op, *this, op.backend());
        }else{
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::FC_Op
     */
    std::shared_ptr<Operator> clone() const override final {
        return std::make_shared<FC_Op>(*this);
    }

    void associateInput(const IOIndex_t inputIdx, const std::shared_ptr<Data>& data) override final;

    void computeOutputDims() override final;

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    static const std::vector<std::string> getInputsName() {
        return {"data_input", "weight", "bias"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> FC(DimSize_t inChannels, DimSize_t outChannels, bool noBias = false, const std::string& name = "") {
    // FIXME: properly handle default w&b initialization in every cases
    auto fc = std::make_shared<Node>(std::make_shared<FC_Op>(outChannels, noBias), name);
    addProducer(fc, 1, {outChannels, inChannels}, "w");
    addProducer(fc, 2, {(noBias ? 0 : outChannels)}, "b"); // already sets bias dims
    return fc;
}
} // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::FCAttr>::data[] = {"OutChannels",
                                                        "NoBias"};
}

#endif /* AIDGE_CORE_OPERATOR_FC_H_ */
