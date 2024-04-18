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

#ifndef AIDGE_CORE_OPERATOR_MAXPOOLING_H_
#define AIDGE_CORE_OPERATOR_MAXPOOLING_H_

#include <array>
#include <cmath>       // std::ceil, std::floor
#include <cstddef>     // std::size_t
#include <functional>
#include <memory>
#include <stdexcept>   // std::runtime_error
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/ArrayHelpers.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class MaxPoolingAttr { StrideDims, KernelDims, CeilMode };

template <DimIdx_t DIM>
class MaxPooling_Op : public OperatorTensor,
                public Registrable<MaxPooling_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const MaxPooling_Op<DIM> &)>,
                public StaticAttributes<MaxPoolingAttr,
                                       std::array<DimSize_t, DIM>,
                                       std::array<DimSize_t, DIM>,
                                       bool> {
public:
    static const std::string Type;

    MaxPooling_Op() = delete;

    using Attributes_ = StaticAttributes<MaxPoolingAttr,
                                             std::array<DimSize_t, DIM>,
                                             std::array<DimSize_t, DIM>,
                                             bool>;
    template <MaxPoolingAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr MaxPooling_Op(const std::array<DimSize_t, DIM> &kernel_dims,
                            const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                            bool ceil_mode = false)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<MaxPoolingAttr::StrideDims>(stride_dims),
                      attr<MaxPoolingAttr::KernelDims>(kernel_dims),
                      attr<MaxPoolingAttr::CeilMode>(ceil_mode))
        {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    MaxPooling_Op(const MaxPooling_Op<DIM>& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl) {
            SET_IMPL_MACRO(MaxPooling_Op<DIM>, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::MaxPooling_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<MaxPooling_Op<DIM>>(*this);
    }


    void computeOutputDims() override final {
        if (!getInput(0)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #0 should be associated with a Tensor", type());
        }
        if (!(getInput(0)->empty())) {
            std::array<DimSize_t, DIM + 2> outputDims{};
            const std::array<DimSize_t, DIM + 2> inputDims(getInput(0)->template dims<DIM+2>());

            std::function<float(float)> roundingFunction;
            if (this->template getAttr<MaxPoolingAttr::CeilMode>()) {
                roundingFunction = [](float x) { return std::ceil(x); };
            } else {
                roundingFunction = [](float x) { return std::floor(x); };
            }

            for (std::size_t dim = 0; dim < this->template getAttr<MaxPoolingAttr::KernelDims>().size() ; ++dim) {
                outputDims[dim+2] = 1 + static_cast<DimSize_t>(
                                            roundingFunction(static_cast<float>(inputDims[dim+2] -
                                                                    this->template getAttr<MaxPoolingAttr::KernelDims>()[dim]) /
                                            static_cast<float>(this->template getAttr<MaxPoolingAttr::StrideDims>()[dim])));
            }
            outputDims[1] = inputDims[1];
            outputDims[0] = inputDims[0];
            mOutputs[0]->resize(outputDims);
        }
    }


    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(MaxPooling_Op<DIM>, *this, name);
        mOutputs[0]->setBackend(name, device);
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

template <DimIdx_t DIM>
const std::string MaxPooling_Op<DIM>::Type = "MaxPooling";

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> MaxPooling(const std::array<DimSize_t, DIM> &kernel_dims,
                                           const std::string& name = "",
                                           const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                                           bool ceil_mode=false) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by MaxPooling, not supported");
    return std::make_shared<Node>(std::make_shared<MaxPooling_Op<static_cast<DimIdx_t>(DIM)>>(kernel_dims, stride_dims, ceil_mode), name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> MaxPooling(
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
    bool ceil_mode = false) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by MaxPooling, not supported");
    return MaxPooling(to_array(kernel_dims), name, stride_dims, ceil_mode);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::MaxPoolingAttr>::data[] = {"StrideDims", "KernelDims", "CeilMode"};
}

#endif /* AIDGE_CORE_OPERATOR_MAXPOOLING_H_ */
