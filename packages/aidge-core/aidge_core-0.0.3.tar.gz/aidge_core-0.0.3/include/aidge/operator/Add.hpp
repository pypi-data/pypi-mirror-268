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

#ifndef AIDGE_CORE_OPERATOR_ADD_H_
#define AIDGE_CORE_OPERATOR_ADD_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

namespace Aidge {

class Add_Op : public OperatorTensor,
    public Registrable<Add_Op, std::string, std::shared_ptr<OperatorImpl>(const Add_Op&)> {
public:
    static const std::string Type;

    Add_Op(const IOIndex_t nbIn)
        : OperatorTensor(Type, nbIn, 0, 1)
    {
        if (nbIn == 0) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Add operator should have at least one input.");
        }
    }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Add_Op(const Add_Op& op);

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Add_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Add_Op>(*this);
    }

    // Data operator[](const char* inputName) override final {
    //     std::shared_ptr<Tensor> in = (strcmp(inputName, "data")) ? mInputs[0] :
    //         (strcmp(inputName, "weight") ? mInputs[1] :
    //         (strcmp(inputName, "bias") ? mInputs[2] :
    //         nullptr));
    //     assert((in!=nullptr) && "No such parameter");
    //     return *in;
    // }


    void computeOutputDims() override final;

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    static const std::vector<std::string> getInputsName() {
        return {"data_input_0", "data_input_n"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> Add(const IOIndex_t nbIn, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Add_Op>(nbIn), name);
}
}

#endif /* AIDGE_CORE_OPERATOR_ADD_H_ */
