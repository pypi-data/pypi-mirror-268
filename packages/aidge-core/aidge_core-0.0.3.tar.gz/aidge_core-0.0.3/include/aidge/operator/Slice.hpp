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

#ifndef AIDGE_CORE_OPERATOR_SLICE_H_
#define AIDGE_CORE_OPERATOR_SLICE_H_

#include <memory>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class SliceAttr { Starts, Ends, Axes };

class Slice_Op
    : public OperatorTensor,
      public Registrable<Slice_Op, std::string, std::shared_ptr<OperatorImpl>(const Slice_Op &)>,
      public StaticAttributes<SliceAttr, std::vector<std::int64_t>, std::vector<std::int64_t>, std::vector<std::int64_t>> {
public:
    static const std::string Type;

    Slice_Op() = delete;

    using Attributes_ = StaticAttributes<SliceAttr, std::vector<std::int64_t>, std::vector<std::int64_t>, std::vector<std::int64_t>>;
    template <SliceAttr e>
    using attr = typename Attributes_::template attr<e>;

    Slice_Op(const std::vector<std::int64_t>& starts, const std::vector<std::int64_t>&  ends, const std::vector<std::int64_t>& axes)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<SliceAttr::Starts>(starts),
                      attr<SliceAttr::Ends>(ends),
                      attr<SliceAttr::Axes>(axes))
    {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its
     * input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Slice_Op(const Slice_Op &op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl){
            SET_IMPL_MACRO(Slice_Op, *this, op.backend());
        }else{
            mImpl = nullptr;
        }
    }

public:
    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Slice_Op
     */
    std::shared_ptr<Operator> clone() const override { return std::make_shared<Slice_Op>(*this); }

    void computeOutputDims() override final;

    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(Slice_Op, *this, name);
        mOutputs[0]->setBackend(name, device);
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

/**
 * @brief Exract a sub-Tensor from a bigger original Tensor.
 * @param starts Indexes for each dimension of the first element.
 * Can be a negative value. Negative values start their reference from the last index.
 * ``-1`` referes to the last index of a dimension.
 * @param ends Indexes for each dimension of the last element.
 * Can be a negative value. Negative values start their reference from the last index.
 * ``-1`` referes to the last index of a dimension.
 * @param axes Dimensions for which start/end indexes apply. Not specifying a dimensions
 * means the whole dimensions is extracted.
 * @param name Name of the Operator.
 * @return std::shared_ptr<Node> A Node containing the Operator.
 */
inline std::shared_ptr<Node> Slice(const std::vector<std::int64_t> starts,
                                   const std::vector<std::int64_t> ends,
                                   const std::vector<std::int64_t> axes,
                                   const std::string &name = "") {
    // FIXME: properly handle default w&b initialization in every cases
    return std::make_shared<Node>(std::make_shared<Slice_Op>(starts, ends, axes), name);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::SliceAttr>::data[] = { "Starts", "Ends", "Axes" };
}

#endif /* AIDGE_CORE_OPERATOR_RELU_H_ */
