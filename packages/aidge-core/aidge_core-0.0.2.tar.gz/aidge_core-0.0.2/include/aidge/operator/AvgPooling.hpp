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

#ifndef AIDGE_CORE_OPERATOR_AVGPOOLING_H_
#define AIDGE_CORE_OPERATOR_AVGPOOLING_H_

#include <array>
#include <string>
#include <vector>

#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/ArrayHelpers.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class AvgPoolingAttr { StrideDims, KernelDims };

template <DimIdx_t DIM>
class AvgPooling_Op : public OperatorTensor,
                public Registrable<AvgPooling_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const AvgPooling_Op<DIM> &)>,
                public StaticAttributes<AvgPoolingAttr,
                                       std::array<DimSize_t, DIM>,
                                       std::array<DimSize_t, DIM>> {

public:
    static const std::string Type;

    AvgPooling_Op() = delete;

    using Attributes_ = StaticAttributes<AvgPoolingAttr,
                                             std::array<DimSize_t, DIM>,
                                             std::array<DimSize_t, DIM>>;
    template <AvgPoolingAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr AvgPooling_Op(const std::array<DimSize_t, DIM> &kernel_dims,
                            const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1))
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<AvgPoolingAttr::StrideDims>(stride_dims),
                      attr<AvgPoolingAttr::KernelDims>(kernel_dims)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    AvgPooling_Op(const AvgPooling_Op<DIM>& op);

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::AvgPooling_Op
     */
    std::shared_ptr<Operator> clone() const override final {
        return std::make_shared<AvgPooling_Op<DIM>>(*this);
    }


    void computeOutputDims() override final;


    std::vector<std::pair<std::vector<DimSize_t>, std::vector<DimSize_t>>>
    computeReceptiveField(const std::vector<DimSize_t>& firstEltDims,
                            const std::vector<DimSize_t>& outputDims,
                            const IOIndex_t outputIdx = 0) const override final;


    void setBackend(const std::string &name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName() {
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> AvgPooling(const std::array<DimSize_t, DIM> &kernel_dims,
                                           const std::string& name = "",
                                           const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1)) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by AvgPooling, not supported");
    return std::make_shared<Node>(std::make_shared<AvgPooling_Op<static_cast<DimIdx_t>(DIM)>>(kernel_dims, stride_dims), name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> AvgPooling(
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1)) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by AvgPooling, not supported");
    return AvgPooling(to_array(kernel_dims), name, stride_dims);
}

extern template class Aidge::AvgPooling_Op<1>;
extern template class Aidge::AvgPooling_Op<2>;
extern template class Aidge::AvgPooling_Op<3>;
extern template class Aidge::AvgPooling_Op<4>;

}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::AvgPoolingAttr>::data[] = {"StrideDims",
                                                          "KernelDims"};
}

#endif /* AIDGE_CORE_OPERATOR_AVGPOOLING_H_ */
