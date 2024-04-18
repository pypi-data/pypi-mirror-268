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

#include "aidge/operator/BatchNorm.hpp"

#include <cstddef>    // std::size_t
#include <stdexcept>  // std::runtime_error
#include <string>
#include <utility>    // std::pair
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

template <Aidge::DimIdx_t DIM>
const std::string Aidge::BatchNorm_Op<DIM>::Type = "BatchNorm";

template <Aidge::DimIdx_t DIM>
Aidge::BatchNorm_Op<DIM>::BatchNorm_Op(const BatchNorm_Op<DIM>& op): OperatorTensor(op), Attributes_(op) {
    if (op.mImpl) {
        SET_IMPL_MACRO(BatchNorm_Op<DIM>, *this, op.backend());
    } else {
        mImpl = nullptr;
    }
}

template <Aidge::DimIdx_t DIM>
void Aidge::BatchNorm_Op<DIM>::computeOutputDims() {
    // check inputs have been associated
    bool associated = true;
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        associated &= !(getInput(i)->empty());
    }
    if (associated) {
        const DimSize_t nbFeatures =  getInput(0)->dims()[1];
        for (std::size_t i = nbData(); i < nbInputs(); ++i) {
            if(getInput(i)->size() != nbFeatures) {
                // /!\ Input size should be handled BEFORE calling this function
                // This should raise an error
                getInput(i)->resize({getInput(0)->dims()[1]});
            }
        }
        mOutputs[0]->resize(getInput(0)->dims());
    }
}

template <Aidge::DimIdx_t DIM>
void Aidge::BatchNorm_Op<DIM>::setBackend(const std::string &name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(BatchNorm_Op<DIM>, *this, name);
    mOutputs[0]->setBackend(name, device);

    // By default, automatically set backend for scale, shift, mean and variance
    getInput(1)->setBackend(name, device);
    getInput(2)->setBackend(name, device);
    getInput(3)->setBackend(name, device);
    getInput(4)->setBackend(name, device);
}

template class Aidge::BatchNorm_Op<2>;
template class Aidge::BatchNorm_Op<3>;
template class Aidge::BatchNorm_Op<4>;

template <Aidge::DimSize_t DIM>
inline std::shared_ptr<Aidge::Node> Aidge::BatchNorm(const DimSize_t nbFeatures,
                                       const float epsilon,
                                       const float momentum,
                                       const std::string& name) {
    static_assert(DIM<=MaxDim,"Too many kernel dimensions required by BatchNorm, not supported");
    auto batchNorm = std::make_shared<Node>(std::make_shared<BatchNorm_Op<static_cast<DimIdx_t>(DIM)>>(epsilon, momentum), name);
    addProducer(batchNorm, 1, {nbFeatures}, "scale");
    addProducer(batchNorm, 2, {nbFeatures}, "shift");
    addProducer(batchNorm, 3, {nbFeatures}, "batch_mean");
    addProducer(batchNorm, 4, {nbFeatures}, "batch_variance");
    return batchNorm;
}

template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<2>(const DimSize_t, const float, const float, const std::string&);
template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<3>(const DimSize_t, const float, const float, const std::string&);
template std::shared_ptr<Aidge::Node> Aidge::BatchNorm<4>(const DimSize_t, const float, const float, const std::string&);