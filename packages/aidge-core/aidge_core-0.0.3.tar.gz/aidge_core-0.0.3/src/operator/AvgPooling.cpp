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

#include "aidge/operator/AvgPooling.hpp"

#include <cmath>      // std::floor
#include <cstddef>    // std::size_t
#include <stdexcept>  // std::runtime_error
#include <string>
#include <utility>    // std::pair
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

template <Aidge::DimIdx_t DIM>
const std::string Aidge::AvgPooling_Op<DIM>::Type = "AvgPooling";

template <Aidge::DimIdx_t DIM>
Aidge::AvgPooling_Op<DIM>::AvgPooling_Op(const AvgPooling_Op<DIM>& op): OperatorTensor(op), Attributes_(op) {
    if (op.mImpl) {
        SET_IMPL_MACRO(AvgPooling_Op<DIM>, *this, op.backend());
    } else {
        mImpl = nullptr;
    }
}

template <Aidge::DimIdx_t DIM>
void Aidge::AvgPooling_Op<DIM>::computeOutputDims() {
    // check inputs have been associated
    if (!getInput(0)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #0 should be associated with a Tensor", type());
    }
    if (!(getInput(0)->empty())) {
        std::array<DimSize_t, DIM + 2> outputDims;
        const std::array<DimSize_t, DIM + 2> inputDims(getInput(0)->template dims<DIM+2>());
        outputDims[0] = inputDims[0];
        outputDims[1] = inputDims[1];

        for (std::size_t dim = 0; dim < this->template getAttr<AvgPoolingAttr::KernelDims>().size() ; ++dim) {
            outputDims[dim+2] = 1 + static_cast<DimSize_t>(
                                        std::floor(static_cast<float>(inputDims[dim+2] -
                                                                this->template getAttr<AvgPoolingAttr::KernelDims>()[dim]) /
                                        static_cast<float>(this->template getAttr<AvgPoolingAttr::StrideDims>()[dim])));
        }
        getOutput(0)->resize(outputDims);
    }
}


template <Aidge::DimIdx_t DIM>
std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<Aidge::DimSize_t>>>
Aidge::AvgPooling_Op<DIM>::computeReceptiveField(const std::vector<Aidge::DimSize_t>& firstEltDims,
                        const std::vector<Aidge::DimSize_t>& outputDims,
                        const Aidge::IOIndex_t outputIdx) const {
    if (outputIdx != 0) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Conv_Op Operator has got only one output Tensor.");
    }
    if (firstEltDims.size() != outputDims.size()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "outputDims and firstEltDims should have the size of the output Tensor dimensions.");
    }
    if ((outputDims.size() == (DIM+2)) && outputDimsForwarded()) {
        // Offset
        std::vector<DimSize_t> inputIdxDims = firstEltDims;

        for (DimIdx_t i = 0; i < (DIM+2); ++i) {
            if (((outputDims[i] + firstEltDims[i]) > mOutputs[0]->template dims<DIM+2>()[i]) || (outputDims[i] == 0)) {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range for dimension {} ({} + {})", static_cast<std::size_t>(i), firstEltDims[i], outputDims[i]);
            }
        }

        // padding is not a parameter of Conv_Op. It is handled in Pad_Op Operator
        // Width
        std::vector<DimSize_t> inputDims;
        inputDims.push_back(outputDims[0]); // same batch value
        inputDims.push_back(outputDims[1]); // same channel value

        for (DimIdx_t i = 0; i < DIM; ++i) {
            inputDims.push_back((outputDims[2+static_cast<std::size_t>(i)] - 1)
                        * this->template getAttr<AvgPoolingAttr::StrideDims>()[static_cast<std::size_t>(i)]
                        + 1
                        + (this->template getAttr<AvgPoolingAttr::KernelDims>()[static_cast<std::size_t>(i)] - 1));
            inputIdxDims[2+i] *= this->template getAttr<AvgPoolingAttr::StrideDims>()[static_cast<std::size_t>(i)];
        }
        std::vector<std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>> res;
        res.push_back(std::pair<std::vector<Aidge::DimSize_t>, std::vector<DimSize_t>>(inputIdxDims, inputDims));
        return res;
    }
    AIDGE_THROW_OR_ABORT(std::runtime_error, "Given outputDim out of range or output dim not forwarded yet.");
}


template <Aidge::DimIdx_t DIM>
void Aidge::AvgPooling_Op<DIM>::setBackend(const std::string &name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(AvgPooling_Op<DIM>, *this, name);
    mOutputs[0]->setBackend(name, device);
}

template class Aidge::AvgPooling_Op<1>;
template class Aidge::AvgPooling_Op<2>;
template class Aidge::AvgPooling_Op<3>;
template class Aidge::AvgPooling_Op<4>;