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

#include "aidge/operator/Concat.hpp"

#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Concat_Op::Type = "Concat";

void Aidge::Concat_Op::computeOutputDims() {
    // Every input is non-empty with the same number of dimensions
    bool associated = (getInput(0) != nullptr);
    associated &= !(getInput(0)->empty()) && (getAttr<ConcatAttr::Axis>() < getInput(0)->nbDims()); // do not compute anything if no input
    auto outputDims =  getInput(0)->dims();
    const auto firstInputNbDims = getInput(0) -> nbDims();
    for (IOIndex_t i = 1; i < nbInputs(); ++i) {
        if (!getInput(i)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
        }

        if (getInput(i)->nbDims() == firstInputNbDims) {
            for (DimSize_t dim = 0; dim < firstInputNbDims; ++dim) {
                if (dim == getAttr<ConcatAttr::Axis>()) {
                    outputDims[dim] += getInput(i)->dims()[dim];
                }
                else {
                    associated &= (getInput(i)->dims()[dim] == outputDims[dim]);
                }
            }
        }
        else {
            associated = false;
            break;
        }
    }
    if (associated) {
        getOutput(0)->resize(outputDims);
    }
}

void Aidge::Concat_Op::setBackend(const std::string& name, DeviceIdx_t device) {
    SET_IMPL_MACRO(Concat_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}
