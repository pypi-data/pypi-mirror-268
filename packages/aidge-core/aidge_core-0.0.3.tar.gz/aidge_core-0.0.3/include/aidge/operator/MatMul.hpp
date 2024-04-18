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

#ifndef AIDGE_CORE_OPERATOR_MATMUL_H_
#define AIDGE_CORE_OPERATOR_MATMUL_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/utils/Types.h"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"

namespace Aidge {

class MatMul_Op : public OperatorTensor,
              public Registrable<MatMul_Op,
                                 std::string,
                                 std::shared_ptr<OperatorImpl>(const MatMul_Op &)> {
public:
    static const std::string Type;

    MatMul_Op() : OperatorTensor(Type, 2, 0, 1) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    MatMul_Op(const MatMul_Op& op) : OperatorTensor(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(MatMul_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::MatMul_Op
     */
    std::shared_ptr<Operator> clone() const override final {
        return std::make_shared<MatMul_Op>(*this);
    }

    /**
     * @brief Compute dimensions for the output Tensor following the same rules as
     * numpy.matmul.
     * @note - Both inputs are 2-D Tensors: classic matrix multiplication
     * @note - Either input is N-D with N > 2: it is treated as a stack of matrices residing
     * in the last two indexes and broadcast accordingly.
     * @note - First input is 1-D: it is promoted to a matrix by prepending a 1 to its
     * dimensions (D) -> (1,D). The prepended 1 is removed after computation.
     * @note - Second input is 1-D: it is promoted to a matrix by appending a 1 to its
     * dimensions (D) -> (D,1). The appended 1 is removed after computation.
     */
    void computeOutputDims() override final;


    void setBackend(const std::string& name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName() {
        return {"data_input1", "data_input2"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

inline std::shared_ptr<Node> MatMul(const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<MatMul_Op>(), name);
}
} // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_MATMUL_H_ */
