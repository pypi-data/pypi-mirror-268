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

#include "aidge/operator/Gather.hpp"

#include <cstddef>  // std::size_t
#include <cstdint>  // std::int64_t
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"


const std::string Aidge::Gather_Op::Type = "Gather";

void Aidge::Gather_Op::computeOutputDims() {
    // check inputs have been associated
    if (!getInput(0)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Input was not connected");
    }

    if (!getInput(0)->empty()) {
        std::vector<DimSize_t> outDims = getInput(0)->dims();
        const std::vector<DimSize_t> gatheredShape = this->template getAttr<GatherAttr::GatheredShape>();
        // TODO: check indices and gatheredShape

        const std::int64_t axisIdx = this->template getAttr<GatherAttr::Axis>() >= 0 ?
                                        this->template getAttr<GatherAttr::Axis>() :
                                        this->template getAttr<GatherAttr::Axis>() + outDims.size();
        outDims.erase(outDims.begin() + static_cast<std::size_t>(axisIdx));
        if (!gatheredShape.empty())
        {
            outDims.insert(outDims.cbegin() + static_cast<std::size_t>(axisIdx),
                            gatheredShape.cbegin(),
                            gatheredShape.cend());
        }

        mOutputs[0]->resize(outDims);
    }
}

void Aidge::Gather_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(Gather_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}
