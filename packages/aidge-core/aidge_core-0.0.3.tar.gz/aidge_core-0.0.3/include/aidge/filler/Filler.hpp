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

#ifndef AIDGE_CORE_FILLER_FILLER_H_
#define AIDGE_CORE_FILLER_FILLER_H_

#include <cstdint>  // std::uint32_t
#include <memory>

#include "aidge/data/Tensor.hpp"

namespace Aidge {

void calculateFanInFanOut(std::shared_ptr<Tensor> tensor,
                                 std::uint32_t& fanIn, std::uint32_t& fanOut);

enum class VarianceNorm { FanIn, Average, FanOut };

template <typename T>
void constantFiller(std::shared_ptr<Tensor> tensor, T constantValue);

template <typename T>
void normalFiller(std::shared_ptr<Tensor> tensor, double mean = 0.0,
                  double stdDev = 1.0);

template <typename T>
void uniformFiller(std::shared_ptr<Tensor> tensor, T min, T max);

template <typename T>
void xavierUniformFiller(std::shared_ptr<Tensor> tensor, T scaling = 1.0,
                         VarianceNorm varianceNorm = VarianceNorm::FanIn);
template <typename T>
void xavierNormalFiller(std::shared_ptr<Tensor> tensor, T scaling = 1.0,
                        VarianceNorm varianceNorm = VarianceNorm::FanIn);

template <typename T>
void heFiller(std::shared_ptr<Tensor> tensor, VarianceNorm varianceNorm = VarianceNorm::FanIn,
              T meanNorm = 0.0, T scaling = 1.0);

}  // namespace Aidge

#endif /* AIDGE_CORE_FILLER_FILLER_H_ */
