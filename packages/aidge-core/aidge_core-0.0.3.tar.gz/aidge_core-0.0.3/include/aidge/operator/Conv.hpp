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

#ifndef AIDGE_CORE_OPERATOR_CONV_H_
#define AIDGE_CORE_OPERATOR_CONV_H_

#include <array>
#include <cmath>    // std::floor
#include <cstddef>  // std::size_t
#include <string>
#include <utility>  // std::pair
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/ArrayHelpers.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp" // SET_IMPL_MACRO
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class ConvAttr { StrideDims, DilationDims, InChannels, OutChannels, KernelDims, NoBias };

template <DimIdx_t DIM>
class Conv_Op : public OperatorTensor,
                public Registrable<Conv_Op<DIM>, std::string, std::shared_ptr<OperatorImpl>(const Conv_Op<DIM> &)>,
                public StaticAttributes<ConvAttr,
                                        std::array<DimSize_t, DIM>,
                                        std::array<DimSize_t, DIM>,
                                        DimSize_t,
                                        DimSize_t,
                                        std::array<DimSize_t, DIM>,
                                        bool> {

public:
    static const std::string Type;

    Conv_Op() = delete;

    using Attributes_ = StaticAttributes<ConvAttr,
                                        std::array<DimSize_t, DIM>,
                                        std::array<DimSize_t, DIM>,
                                        DimSize_t,
                                        DimSize_t,
                                        std::array<DimSize_t, DIM>,
                                        bool>;
    template <ConvAttr e>
    using attr = typename Attributes_::template attr<e>;

    constexpr Conv_Op(DimSize_t inChannels,
                      DimSize_t outChannels,
                      const std::array<DimSize_t, DIM> &kernelDims,
                      const std::array<DimSize_t, DIM> &strideDims = create_array<DimSize_t,DIM>(1),
                      const std::array<DimSize_t, DIM> &dilationDims = create_array<DimSize_t,DIM>(1),
                      bool noBias = false)
        : OperatorTensor(Type, 1, 2, 1),
          Attributes_(attr<ConvAttr::StrideDims>(strideDims),
                      attr<ConvAttr::DilationDims>(dilationDims),
                      attr<ConvAttr::InChannels>(inChannels),
                      attr<ConvAttr::OutChannels>(outChannels),
                      attr<ConvAttr::KernelDims>(kernelDims),
                      attr<ConvAttr::NoBias>(noBias)) {}

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    Conv_Op(const Conv_Op<DIM>& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        if (op.mImpl) {
            SET_IMPL_MACRO(Conv_Op<DIM>, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Conv_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Conv_Op<DIM>>(*this);
    }

    // Data operator[](const char* inputName) override final {
    //     std::shared_ptr<Tensor> in = (strcmp(inputName, "data")) ? getInput(0) :
    //         (strcmp(inputName, "weight") ? getInput(1) :
    //         (strcmp(inputName, "bias") ? getInput(2) :
    //         nullptr));
    //     assert((in!=nullptr) && "No such parameter");
    //     return *in;
    // }

    // std::shared_ptr<Conv_Op> clone() const override final {

    // }

    void computeOutputDims() override final {
        // check inputs have been associated
        bool associated = true;
        for (IOIndex_t i = 0; i < 3; ++i) {
            if (!getInput(i)) {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
            }
            associated &= !(getInput(i)->empty());
        }
        if (associated) {
            std::array<DimSize_t, DIM + 2> outputDims{};
            const std::array<DimSize_t, DIM + 2> inputDims(getInput(0)->template dims<DIM+2>());

            for (std::size_t dim = 0; dim < this->template getAttr<ConvAttr::KernelDims>().size() ; ++dim) {
                const DimSize_t kernelExtent = this->template getAttr<ConvAttr::DilationDims>()[dim] *
                                                       (this->template getAttr<ConvAttr::KernelDims>()[dim] - 1) +
                                               1;

                outputDims[dim+2] = 1 + static_cast<DimSize_t>(
                        floor(static_cast<float>(inputDims[dim+2] - kernelExtent) /
                              static_cast<float>(this->template getAttr<ConvAttr::StrideDims>()[dim])));
            }

            outputDims[1] = this->template getAttr<ConvAttr::OutChannels>();
            outputDims[0] = inputDims[0];
            mOutputs[0]->resize(outputDims);
        }
    }

    std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>>
    computeReceptiveField(const std::vector<DimSize_t>& firstEltDims,
                          const std::vector<DimSize_t>& outputDims,
                          const IOIndex_t outputIdx = 0) const override {
        if (outputIdx != 0) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Conv_Op Operator has got only one output Tensor.");
        }
        if (firstEltDims.size() != outputDims.size()) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "outputDims and firstEltDims should have the size of the output Tensor dimensions.");
        }
        if ((outputDims.size() == (DIM+2)) && outputDimsForwarded()) {
            // Offset
            auto inputIdxDims = firstEltDims; // batch idx is the same
            inputIdxDims[1] = 0; // each channel is used so start with the first one

            for (DimIdx_t i = 0; i < (DIM+2); ++i) {
                if (((outputDims[i] + firstEltDims[i]) > mOutputs[0]->template dims<DIM+2>()[i]) || (outputDims[i] == 0)) {
                    AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range for dimension {} ({} + {})", static_cast<std::size_t>(i), firstEltDims[i], outputDims[i]);
                }
            }

            // padding is not a parameter of Conv_Op. It is handled in Pad_Op Operator
            // Input
            // same batch value, every input channel is used
            std::vector<DimSize_t> inputDims{outputDims[0], getInput(0)->dims()[1]};
            for (DimIdx_t i = 0; i < DIM; ++i) {
                inputDims.push_back((outputDims[2+static_cast<std::size_t>(i)] - 1)
                            * this->template getAttr<ConvAttr::StrideDims>()[static_cast<std::size_t>(i)]
                            + 1
                            + (this->template getAttr<ConvAttr::KernelDims>()[static_cast<std::size_t>(i)] - 1)
                            * this->template getAttr<ConvAttr::DilationDims>()[static_cast<std::size_t>(i)]);
                inputIdxDims[2+i] *= this->template getAttr<ConvAttr::StrideDims>()[static_cast<std::size_t>(i)];
            }

            // Weight
            // same output value, every input channel is used
            std::vector<DimSize_t> weightDims{outputDims[1], getInput(0)->dims()[1]};
            for (std::size_t i = 0; i < DIM; ++i) {
                weightDims.push_back(this->template getAttr<ConvAttr::KernelDims>()[i]);
            }
            std::vector<DimSize_t> weightIdxDims = std::vector<DimSize_t>(DIM+2, 0);
            weightIdxDims[0] = firstEltDims[1];

            // Result
            std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>> res;
            res.push_back(std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>(inputIdxDims, inputDims));
            res.push_back(std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>(weightIdxDims, weightDims));

            // Bias
            if (! this->template getAttr<ConvAttr::NoBias>()){
                const std::vector<DimSize_t> biasDims{outputDims[1]}; // the number of output channel
                const std::vector<DimSize_t> biasIdxDims{firstEltDims[1]};
                res.push_back(std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>(biasIdxDims, biasDims));
            }
            return res;
        }
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range or output dim not forwarded yet.");
    }


    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        SET_IMPL_MACRO(Conv_Op<DIM>, *this, name);
        mOutputs[0]->setBackend(name, device);

        // By default, automatically set backend for weight and bias inputs
        getInput(1)->setBackend(name, device);
        getInput(2)->setBackend(name, device);
    }

    static const std::vector<std::string> getInputsName(){
        return {"data_input", "weight", "bias"};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }
};

template <DimIdx_t DIM>
const std::string Conv_Op<DIM>::Type = "Conv";

/**
 * @brief Perform a convolution on the input Tensor.
 *
 * @tparam DIM Number of dimensions for the feature map.
 * @param inChannels Number of input channels.
 * @param outChannels Number of output channels.
 * @param kernelDims Dimensions of the kernel. Must be the same number of dimensions as the feature map.
 * @param name Name of the operator.
 * @param strideDims Dimensions of the stride attribute. Must be the same number of dimensions as the feature map.
 * @param dilationDims Dimensions of the dilation attribute. Must be the same number of dimensions as the feature map.
 * @return std::shared_ptr<Node> A Node containing the operator.
 */
template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> Conv(DimSize_t inChannels,
                                  DimSize_t outChannels,
                                  const std::array<DimSize_t, DIM> &kernelDims,
                                  const std::string& name = "",
                                  const std::array<DimSize_t, DIM> &strideDims = create_array<DimSize_t,DIM>(1),
                                  const std::array<DimSize_t, DIM> &dilationDims = create_array<DimSize_t,DIM>(1),
                                  bool noBias = false) {
    // FIXME: properly handle default w&b initialization in every cases
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by Conv, not supported");
    auto conv = std::make_shared<Node>(std::make_shared<Conv_Op<static_cast<DimIdx_t>(DIM)>>(inChannels, outChannels, kernelDims, strideDims, dilationDims, noBias), name);
    addProducer(conv, 1, append(outChannels, append(inChannels, kernelDims)), "w");
    addProducer(conv, 2, {(noBias ? 0 : outChannels)}, "b"); // already sets bias dims

    return conv;
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> Conv(
    DimSize_t inChannels,
    DimSize_t outChannels,
    DimSize_t const (&kernelDims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &strideDims = create_array<DimSize_t,DIM>(1),
    const std::array<DimSize_t, DIM> &dilationDims = create_array<DimSize_t,DIM>(1),
    bool noBias = false) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by Conv, not supported");
    return Conv(inChannels, outChannels, to_array(kernelDims), name, strideDims, dilationDims, noBias);
}
}  // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::ConvAttr>::data[] = {
    "StrideDims",
    "DilationDims",
    "InChannels",
    "OutChannels",
    "KernelDims",
    "NoBias"
};
}

#endif /* AIDGE_CORE_OPERATOR_CONV_H_ */
