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

#include "aidge/operator/Reshape.hpp"

#include <cstddef>    // std::size_t
#include <cstdint>    // std::int64_t
#include <memory>
#include <stdexcept>  // std::runtime_error
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Reshape_Op::Type = "Reshape";

void Aidge::Reshape_Op::computeOutputDims() {
    // check input has been associated
    if (!getInput(0)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Input was not connected");
    }

    if (!getInput(0)->empty()) {
        std::vector<DimSize_t> outDims;
        // variables to handle a negative dimension
        bool foundNegativeDimension = false;
        std::size_t outSize = 1;
        DimIdx_t negativeIndex = 0;

        for(std::size_t i = 0; i < this->template getAttr<ReshapeAttr::Shape>().size(); ++i)
        {
            std::int64_t dimSize = this->template getAttr<ReshapeAttr::Shape>()[i];
            if (dimSize < 0) {
                if (foundNegativeDimension) {
                    AIDGE_THROW_OR_ABORT(std::runtime_error, "Found more than one negative dimension in Reshape Operator.");
                }
                foundNegativeDimension = true;
                dimSize = 1;
                negativeIndex = static_cast<DimIdx_t>(i);
            }
            outDims.push_back(static_cast<DimSize_t>(dimSize));
            outSize *= static_cast<DimSize_t>(dimSize);
        }

        if (foundNegativeDimension) {
            outDims[negativeIndex] = (getInput(0) -> size()) / outSize;
        }

        mOutputs[0]->resize(outDims);
    }
}

void Aidge::Reshape_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(Reshape_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}