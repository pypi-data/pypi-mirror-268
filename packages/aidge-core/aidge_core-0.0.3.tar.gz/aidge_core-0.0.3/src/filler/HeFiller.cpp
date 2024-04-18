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
void Aidge::heFiller(std::shared_ptr<Aidge::Tensor> tensor,
                     Aidge::VarianceNorm varianceNorm, T meanNorm, T scaling) {
    AIDGE_ASSERT(tensor->getImpl(),
                 "Tensor got no implementation, cannot fill it.");
    AIDGE_ASSERT(NativeType<T>::type == tensor->dataType(), "Wrong data type");

    unsigned int fanIn, fanOut = 0;
    Aidge::calculateFanInFanOut(tensor, fanIn, fanOut);

    const T n((varianceNorm == Aidge::VarianceNorm::FanIn) ? fanIn
              : (varianceNorm == Aidge::VarianceNorm::Average)
                  ? (fanIn + fanOut) / 2.0
                  : fanOut);

    const T stdDev(std::sqrt(2.0 / n));

    const T mean(varianceNorm == Aidge::VarianceNorm::FanIn ? meanNorm / fanIn
                 : (varianceNorm == Aidge::VarianceNorm::Average)
                     ? meanNorm / ((fanIn + fanOut) / 2.0)
                     : meanNorm / fanOut);

    std::normal_distribution<T> normalDist(mean, stdDev);

    std::shared_ptr<Tensor> cpyTensor;
    // Create cpy only if tensor not on CPU
    Tensor& tensorWithValues =
        tensor->refCastFrom(cpyTensor, tensor->dataType(), "cpu");

    // Setting values
    for (std::size_t idx = 0; idx < tensorWithValues.size(); ++idx) {
        tensorWithValues.set<T>(idx, scaling*normalDist(Aidge::Random::Generator::get()));
    }

    // Copy values back to the original tensors (actual copy only if needed)
    tensor->copyCastFrom(tensorWithValues);
}

template void Aidge::heFiller<float>(std::shared_ptr<Aidge::Tensor>,
                                     Aidge::VarianceNorm, float, float);
template void Aidge::heFiller<double>(std::shared_ptr<Aidge::Tensor>,
                                      Aidge::VarianceNorm, double, double);
