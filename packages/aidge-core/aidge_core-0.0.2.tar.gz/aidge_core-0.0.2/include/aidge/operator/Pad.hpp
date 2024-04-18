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

#ifndef AIDGE_CORE_OPERATOR_PAD_H_
#define AIDGE_CORE_OPERATOR_PAD_H_

#include <array>
#include <numeric>
#include <vector>
#include <cmath>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class PadAttr { BeginEndBorders, BorderType, BorderValue };
enum class PadBorderType { Constant, Edge, Reflect, Wrap };

template <DimIdx_t DIM>
class Pad_Op : public OperatorTensor,
                public Registrable<Pad_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const Pad_Op<DIM> &)>,
                public StaticAttributes<PadAttr,
                                       std::array<DimSize_t, 2*DIM>,
                                       PadBorderType,
                                       double> {
public:
    static const std::string Type;

    Pad_Op() = delete;

    using Attributes_ = StaticAttributes<PadAttr,
                                             std::array<DimSize_t, 2*DIM>,
                                             PadBorderType,
                                             double>;
    template <PadAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr Pad_Op(const std::array<DimSize_t, 2*DIM> &beginEndTuples,
                     const PadBorderType &borderType = PadBorderType::Constant,
                     double borderValue = 0.0)
        : OperatorTensor(Type, 1, 0, 1),
          Attributes_(attr<PadAttr::BeginEndBorders>(beginEndTuples),
                           attr<PadAttr::BorderType>(borderType),
                           attr<PadAttr::BorderValue>(borderValue)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Pad_Op(const Pad_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {}

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Pad_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Pad_Op<DIM>>(*this);
    }


    void computeOutputDims() override final {
        bool associated = true;
        for (IOIndex_t i = 0; i < nbInputs(); ++i) {
            if (!getInput(i)) {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
            }
            associated &= !(getInput(i)->empty());
        }
        if (associated) {
            std::array<DimSize_t, DIM + 2> outputDims{};
            const std::array<DimSize_t, DIM + 2> inputDims = getInput(0)->template dims<DIM+2>();

            for (std::size_t dim = 0; dim < DIM; ++dim) {
                outputDims[dim+2] = this->template getAttr<PadAttr::BeginEndBorders>()[2*dim]
                                    + inputDims[dim+2]
                                    + this->template getAttr<PadAttr::BeginEndBorders>()[2*dim+1];
            }
            outputDims[1] = inputDims[1];
            outputDims[0] = inputDims[0];
            mOutputs[0]->resize(outputDims);
        }
    }

    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(Pad_Op<DIM>, *this, name);
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
const std::string Pad_Op<DIM>::Type = "Pad";

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> Pad(const std::array<DimSize_t, 2*DIM> &beginEndTuples,
                                           const std::string& name = "",
                                           const PadBorderType &borderType = PadBorderType::Constant,
                                           double borderValue = 0.0)
{
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by Pad, not supported");
    return std::make_shared<Node>(std::make_shared<Pad_Op<static_cast<DimIdx_t>(DIM)>>(beginEndTuples, borderType, borderValue), name);
}

// helper with C-style array instead of std::array for beginEndTuples to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> Pad(
    DimSize_t const (&beginEndTuples)[2*DIM],
    const std::string& name = "",
    const PadBorderType &borderType = PadBorderType::Constant,
    double borderValue = 0.0)
{
    return Pad<DIM>(to_array(beginEndTuples), name, borderType, borderValue);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::PadAttr>::data[] = {"BeginEndBorders", "BorderType", "BorderValue"};

template <>
const char *const EnumStrings<Aidge::PadBorderType>::data[] = {"Constant", "Edge", "Reflect", "Wrap"};
}

#endif /* AIDGE_CORE_OPERATOR_PAD_H_ */
