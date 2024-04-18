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
#include "aidge/operator/Slice.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

#include <cassert>
#include <cstddef>
#include <string>
#include <utility>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Slice_Op::Type = "Slice";

void Aidge::Slice_Op::computeOutputDims() {
    // check input have been associated
    if (!getInput(0) || (getInput(0)->empty())) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #0 should be associated with a Tensor", type());
    }

    const DimSize_t nbAxes = this->template getAttr<SliceAttr::Axes>().size();
    std::vector<DimSize_t> outDims = getInput(0)->dims();
    for (std::size_t i = 0; i < nbAxes; ++i) {
        // For each slice operation get the params and cast them to size_t
        const std::int64_t axis_ = this->template getAttr<SliceAttr::Axes>()[i];
        const std::int64_t start_ = this->template getAttr<SliceAttr::Starts>()[i];
        const std::int64_t end_ = this->template getAttr<SliceAttr::Ends>()[i];
        const std::size_t axis = axis_ >= 0 ? static_cast<std::size_t>(axis_) : static_cast<std::size_t>(axis_) + getInput(0)->nbDims();
        const std::size_t start = start_ >= 0 ? static_cast<std::size_t>(start_) : static_cast<std::size_t>(start_) + getInput(0)->dims()[axis];
        const std::size_t end = end_ >= 0 ? static_cast<std::size_t>(end_) : static_cast<std::size_t>(end_) + getInput(0)->dims()[axis];

        const std::size_t sliceLength = end - start + 1;
        // Check if slice length is valid
        if (sliceLength > getInput(0)->dims()[axis])
        {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "ROI of Slice operator out of bounds");
        }
        outDims[axis] = sliceLength;
    }
    mOutputs[0]->resize(outDims);
}
