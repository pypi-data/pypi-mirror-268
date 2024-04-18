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

#ifndef AIDGE_CORE_OPERATOR_REDUCEMEAN_H_
#define AIDGE_CORE_OPERATOR_REDUCEMEAN_H_

#include <cstdint>    // std::int32_t
#include <memory>
#include <string>
#include <vector>

#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class ReduceMeanAttr { Axes, KeepDims };

class ReduceMean_Op : public OperatorTensor,
                public Registrable<ReduceMean_Op, std::string, std::shared_ptr<OperatorImpl>(const ReduceMean_Op &)>,
                public StaticAttributes<ReduceMeanAttr, std::vector<std::int32_t>, DimSize_t> {

   public:
    static const std::string Type;

    ReduceMean_Op() = delete;

    using Attributes_ = StaticAttributes<ReduceMeanAttr, std::vector<std::int32_t>, DimSize_t>;
    template <ReduceMeanAttr e>
    using attr = typename Attributes_::template attr<e>;

    ReduceMean_Op(const std::vector<std::int32_t>& axes, DimSize_t keep_dims)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<ReduceMeanAttr::Axes>(axes),
                      attr<ReduceMeanAttr::KeepDims>(keep_dims)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    ReduceMean_Op(const ReduceMean_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(ReduceMean_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::ReduceMean_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<ReduceMean_Op>(*this);
    }

    void computeOutputDims() override final;

    void setBackend(const std::string &name, DeviceIdx_t device = 0) override final;

    static const std::vector<std::string> getInputsName() {
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName() {
        return {"data_output"};
    }
};

/**
 * @brief Compute the mean value of a Tensor over the provided axes. Dimensions
 * may be reduced by erasing the provided axes or not.
 *
 * @param axes Dimensions over which data mean should be computed.
 * @param keep_dims Whether or not reduced dimensions are to be erased.
 * @param name Name of the Operator.
 * @return std::shared_ptr<Node> Node containing the Operator.
 */
inline std::shared_ptr<Node> ReduceMean(const std::vector<std::int32_t> &axes,
                                        DimSize_t keep_dims=1,
                                        const std::string& name = "") {
    // FIXME: properly handle default w&b initialization in every cases
    AIDGE_ASSERT(axes.size()<=MaxDim, "Too many kernel dimensions required by ReduceMean, not supported");
    return std::make_shared<Node>(std::make_shared<ReduceMean_Op>(axes, keep_dims), name);

}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
// template <DimSize_t DIM>
// inline std::shared_ptr<Node> ReduceMean(
//     std::int32_t const (&axes)[DIM],
//     DimSize_t keep_dims = 1,
//     const std::string& name = "") {
//     static_assert(DIM<=MaxDim,"Too many kernel dimensions required by ReduceMean, not supported");
//     return ReduceMean(to_array(axes), keep_dims, name);
// }

// template <DimIdx_t DIM>
// const std::string ReduceMean_Op::Type = "ReduceMean";

}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::ReduceMeanAttr>::data[] = {"Axes", "KeepDims"};
}

#endif /* AIDGE_CORE_OPERATOR_REDUCEMEAN_H_ */
