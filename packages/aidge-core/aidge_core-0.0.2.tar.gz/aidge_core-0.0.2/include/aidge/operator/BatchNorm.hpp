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

#ifndef AIDGE_CORE_OPERATOR_BATCHNORM_H_
#define AIDGE_CORE_OPERATOR_BATCHNORM_H_

#include <array>
#include <memory>
#include <vector>

#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

enum class BatchNormAttr { Epsilon, Momentum };

template <DimIdx_t DIM>
class BatchNorm_Op : public OperatorTensor,
                public Registrable<BatchNorm_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const BatchNorm_Op<DIM> &)>,
                public StaticAttributes<BatchNormAttr, float, float> {
public:
    static const std::string Type;

    BatchNorm_Op() = delete;

    using Attributes_ = StaticAttributes<BatchNormAttr, float, float>;
    template <BatchNormAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr BatchNorm_Op(float epsilon, float momentum)
        : OperatorTensor(Type, 1, 4, 1),
          Attributes_(attr<BatchNormAttr::Epsilon>(epsilon),
                           attr<BatchNormAttr::Momentum>(momentum)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    BatchNorm_Op(const BatchNorm_Op<DIM>& op);

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::BatchNorm_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<BatchNorm_Op<DIM>>(*this);
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

    void setBackend(const std::string &name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName() {
        return {"data_input", "scale", "shift", "mean", "variance"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

extern template class Aidge::BatchNorm_Op<2>;
extern template class Aidge::BatchNorm_Op<3>;
extern template class Aidge::BatchNorm_Op<4>;

template <DimSize_t DIM>
std::shared_ptr<Node> BatchNorm(const DimSize_t nbFeatures,
                                       const float epsilon = 1.0e-5F,
                                       const float momentum = 0.1F,
                                       const std::string& name = "");

extern template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<2>(const DimSize_t, const float, const float, const std::string&);
extern template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<3>(const DimSize_t, const float, const float, const std::string&);
extern template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<4>(const DimSize_t, const float, const float, const std::string&);
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::BatchNormAttr>::data[] = { "Epsilon", "Momentum" };
}

#endif //AIDGE_CORE_OPERATOR_BATCHNORM_H_
