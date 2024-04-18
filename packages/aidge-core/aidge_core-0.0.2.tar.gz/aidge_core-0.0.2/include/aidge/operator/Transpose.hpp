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

#ifndef AIDGE_CORE_OPERATOR_TRANSPOSE_H_
#define AIDGE_CORE_OPERATOR_TRANSPOSE_H_

#include <array>
#include <cmath>
#include <numeric>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class TransposeAttr { OutputDimsOrder };

template <DimIdx_t DIM>
class Transpose_Op : public OperatorTensor,
                public Registrable<Transpose_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const Transpose_Op<DIM> &)>,
                public StaticAttributes<TransposeAttr,
                                       std::array<DimSize_t, DIM>> {

   public:
    static const std::string Type;

    Transpose_Op() = delete;

    using Attributes_ = StaticAttributes<TransposeAttr,
                                             std::array<DimSize_t, DIM>>;
    template <TransposeAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr Transpose_Op(const std::array<DimSize_t, DIM> &output_dims_order)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<TransposeAttr::OutputDimsOrder>(output_dims_order)) { }

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Transpose_Op(const Transpose_Op<DIM>& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Transpose_Op<DIM>, *this, op.backend());
        }else{
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Transpose_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Transpose_Op<DIM>>(*this);
    }

    void computeOutputDims() override final {
        if (!getInput(0)->empty()) {
            auto attr = (this)->getStaticAttributes();
            const std::array<DimSize_t, DIM>& outDimsOrder = static_cast<const std::array<DimSize_t, DIM>&>(std::get<0>(attr));
            std::vector<DimSize_t> outputDims;
            for (std::size_t i = 0; i < DIM; ++i) {
                outputDims.push_back(getInput(0)->dims()[outDimsOrder[i]]);
            }
            mOutputs[0]->resize(outputDims);
        }
    }

    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(Transpose_Op<DIM>, *this, name);
        mOutputs[0]->setBackend(name, device);
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> Transpose(const std::array<DimSize_t, DIM> &output_dims_order,
                                           const std::string& name = "") {
    // FIXME: properly handle default w&b initialization in every cases
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by Transpose, not supported");
    return std::make_shared<Node>(std::make_shared<Transpose_Op<static_cast<DimIdx_t>(DIM)>>(output_dims_order), name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> Transpose(
    DimSize_t const (&output_dims_order)[DIM],
    const std::string& name = "") {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by Transpose, not supported");
    return Transpose(to_array(output_dims_order), name);
}

template <DimIdx_t DIM>
const std::string Transpose_Op<DIM>::Type = "Transpose";

}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::TransposeAttr>::data[] = {"OutputDimsOrder"};
}

#endif /* AIDGE_CORE_OPERATOR_TRANSPOSE_H_ */
