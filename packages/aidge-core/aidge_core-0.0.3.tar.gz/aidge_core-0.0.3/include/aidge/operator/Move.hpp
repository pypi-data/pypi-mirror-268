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

#ifndef AIDGE_CORE_OPERATOR_MOVE_H_
#define AIDGE_CORE_OPERATOR_MOVE_H_

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

class Move_Op : public OperatorTensor,
    public Registrable<Move_Op, std::tuple<std::string, std::string>, std::unique_ptr<OperatorImpl>(const Move_Op&)> {
public:
    static const std::string Type;

    Move_Op() : OperatorTensor(Type, 1, 0, 1) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Move_Op(const Move_Op& op)
        : OperatorTensor(op)
    {
        mImpl = op.mImpl ? Registrar<Move_Op>::create({mInputs[0]->getImpl()->backend(), mOutputs[0]->getImpl()->backend()})(*this) : nullptr;
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Move_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Move_Op>(*this);
    }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override {
        if (mInputs[0]->getImpl() && Registrar<Move_Op>::exists({mInputs[0]->getImpl()->backend(), name})) {
            mImpl = Registrar<Move_Op>::create({mInputs[0]->getImpl()->backend(), name})(*this);
        }
        mOutputs[0]->setBackend(name, device);
    }

    void forward() override;

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Move(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Move_Op>(), name);
}
}

#endif /* AIDGE_CORE_OPERATOR_MOVE_H_ */
