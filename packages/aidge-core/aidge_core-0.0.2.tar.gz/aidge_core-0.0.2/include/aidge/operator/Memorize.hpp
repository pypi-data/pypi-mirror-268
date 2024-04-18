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

#ifndef AIDGE_CORE_OPERATOR_MEMORIZE_H_
#define AIDGE_CORE_OPERATOR_MEMORIZE_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class MemorizeAttr { ScheduleStep, ForwardStep, EndStep };

class Memorize_Op : public OperatorTensor,
    public Registrable<Memorize_Op, std::string, std::unique_ptr<OperatorImpl>(const Memorize_Op&)>,
    public StaticAttributes<MemorizeAttr, unsigned int, unsigned int, unsigned int> {
public:
    static const std::string Type;

    using Attributes_ = StaticAttributes<MemorizeAttr, unsigned int, unsigned int, unsigned int>;
    template <MemorizeAttr e>
    using attr = typename Attributes_::template attr<e>;

    Memorize_Op(const unsigned int endStep)
        : OperatorTensor(Type, 1, 1, 2),
          Attributes_(attr<MemorizeAttr::ScheduleStep>(0),
                      attr<MemorizeAttr::ForwardStep>(0),
                      attr<MemorizeAttr::EndStep>(endStep))
    {
        mOutputs[1] = mOutputs[0];
    }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s),
     * but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Memorize_Op(const Memorize_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl) {
            SET_IMPL_MACRO(Memorize_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
        mOutputs[1] = mOutputs[0];
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Memorize_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Memorize_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    void computeOutputDims() override;
    bool outputDimsForwarded() const override;
    void updateConsummerProducer() override;
    void forward() override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input", "data_input_init"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output", "data_output_rec"};
    }
};

inline std::shared_ptr<Node> Memorize(const unsigned int endStep, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Memorize_Op>(endStep), name);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::MemorizeAttr>::data[] = {
    "ScheduleStep",
    "ForwardStep",
    "EndStep"
};
}

#endif /* AIDGE_CORE_OPERATOR_MEMORIZE_H_ */
