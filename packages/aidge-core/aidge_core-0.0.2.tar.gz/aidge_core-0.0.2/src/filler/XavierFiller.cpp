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
void Aidge::xavierUniformFiller(std::shared_ptr<Aidge::Tensor> tensor,
                                T scaling, Aidge::VarianceNorm varianceNorm) {
    AIDGE_ASSERT(tensor->getImpl(),
                 "Tensor got no implementation, cannot fill it.");
    AIDGE_ASSERT(NativeType<T>::type == tensor->dataType(), "Wrong data type");

    unsigned int fanIn, fanOut = 0;
    Aidge::calculateFanInFanOut(tensor, fanIn, fanOut);

    const T n((varianceNorm == Aidge::VarianceNorm::FanIn) ? fanIn
              : (varianceNorm == Aidge::VarianceNorm::Average)
                  ? (fanIn + fanOut) / 2.0
                  : fanOut);
    const T scale(std::sqrt(3.0 / n));

    std::uniform_real_distribution<T> uniformDist(-scale, scale);

    std::shared_ptr<Aidge::Tensor> cpyTensor;
    // Create cpy only if tensor not on CPU
    Aidge::Tensor& tensorWithValues =
        tensor->refCastFrom(cpyTensor, tensor->dataType(), "cpu");
    // Setting values
    for (std::size_t idx = 0; idx < tensorWithValues.size(); ++idx) {
        tensorWithValues.set<T>(
            idx, scaling * uniformDist(Aidge::Random::Generator::get()));
    }

    // Copy values back to the original tensors (actual copy only if needed)
    tensor->copyCastFrom(tensorWithValues);
}
template <typename T>
void Aidge::xavierNormalFiller(std::shared_ptr<Aidge::Tensor> tensor, T scaling,
                               Aidge::VarianceNorm varianceNorm) {
    AIDGE_ASSERT(tensor->getImpl(),
                 "Tensor got no implementation, cannot fill it.");
    AIDGE_ASSERT(NativeType<T>::type == tensor->dataType(), "Wrong data type");

    unsigned int fanIn, fanOut = 0;
    Aidge::calculateFanInFanOut(tensor, fanIn, fanOut);

    const T n((varianceNorm == Aidge::VarianceNorm::FanIn) ? fanIn
              : (varianceNorm == Aidge::VarianceNorm::Average)
                  ? (fanIn + fanOut) / 2.0
                  : fanOut);
    const double stdDev(std::sqrt(1.0 / n));

    std::normal_distribution<T> normalDist(0.0, stdDev);

    std::shared_ptr<Aidge::Tensor> cpyTensor;
    // Create cpy only if tensor not on CPU
    Aidge::Tensor& tensorWithValues =
        tensor->refCastFrom(cpyTensor, tensor->dataType(), "cpu");

    // Setting values
    for (std::size_t idx = 0; idx < tensorWithValues.size(); ++idx) {
        tensorWithValues.set<T>(
            idx, scaling * normalDist(Aidge::Random::Generator::get()));
    }

    // Copy values back to the original tensors (actual copy only if needed)
    tensor->copyCastFrom(tensorWithValues);
}

template void Aidge::xavierUniformFiller<float>(std::shared_ptr<Aidge::Tensor>,
                                                float, Aidge::VarianceNorm);
template void Aidge::xavierUniformFiller<double>(std::shared_ptr<Aidge::Tensor>,
                                                 double, Aidge::VarianceNorm);

template void Aidge::xavierNormalFiller<float>(std::shared_ptr<Aidge::Tensor>,
                                               float, Aidge::VarianceNorm);
template void Aidge::xavierNormalFiller<double>(std::shared_ptr<Aidge::Tensor>,
                                                double, Aidge::VarianceNorm);
