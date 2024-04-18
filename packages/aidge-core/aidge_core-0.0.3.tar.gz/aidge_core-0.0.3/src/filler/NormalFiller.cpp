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
#include <memory>
#include <random>  // normal_distribution, uniform_real_distribution

#include "aidge/data/Tensor.hpp"
#include "aidge/filler/Filler.hpp"
#include "aidge/utils/Random.hpp"

template <typename T>
void Aidge::normalFiller(std::shared_ptr<Aidge::Tensor> tensor, double mean,
                         double stdDev) {
    AIDGE_ASSERT(tensor->getImpl(),
                 "Tensor got no implementation, cannot fill it.");
    AIDGE_ASSERT(NativeType<T>::type == tensor->dataType(), "Wrong data type");

    std::normal_distribution<T> normalDist(mean, stdDev);

    std::shared_ptr<Tensor> cpyTensor;
    // Create cpy only if tensor not on CPU
    Tensor& tensorWithValues =
        tensor->refCastFrom(cpyTensor, tensor->dataType(), "cpu");

    // Setting values
    for (std::size_t idx = 0; idx < tensorWithValues.size(); ++idx) {
        tensorWithValues.set<T>(idx, normalDist(Aidge::Random::Generator::get()));
    }

    // Copy values back to the original tensors (actual copy only if needed)
    tensor->copyCastFrom(tensorWithValues);
}

template void Aidge::normalFiller<float>(std::shared_ptr<Aidge::Tensor>, double,
                                         double);
template void Aidge::normalFiller<double>(std::shared_ptr<Aidge::Tensor>,
                                          double, double);
