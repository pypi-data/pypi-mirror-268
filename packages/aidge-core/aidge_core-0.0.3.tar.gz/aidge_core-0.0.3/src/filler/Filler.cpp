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

#include "aidge/filler/Filler.hpp"

#include <cstdint>  // std::uint32_t
#include <memory>
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"


void Aidge::calculateFanInFanOut(std::shared_ptr<Aidge::Tensor> tensor,
                                 std::uint32_t& fanIn, std::uint32_t& fanOut) {
    AIDGE_ASSERT(
        tensor->nbDims() == 4,
        "Tensor need to have 4 dimensions to compute FanIn and FanOut.");
    // Warning: This function suppose NCXX data layout.
    // Aidge currently only support NCHW but this maybe not be true in the
    // future.
    DimSize_t batchSize = tensor->dims()[0];
    DimSize_t channelSize = tensor->dims()[1];
    AIDGE_ASSERT(batchSize != 0,
                 "Cannot calculate FanIn if tensor batch size is 0.");
    AIDGE_ASSERT(channelSize != 0,
                 "Cannot calculate FanOut if tensor channel size is 0.");
    fanIn =  static_cast<std::uint32_t>(tensor->size() / batchSize);
    fanOut = static_cast<std::uint32_t>(tensor->size() / channelSize);
}
