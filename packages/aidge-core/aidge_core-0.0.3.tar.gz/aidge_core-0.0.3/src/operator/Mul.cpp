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

#include <cstddef>    // std::size_t
#include <memory>
#include <stdexcept>  // std::runtime_error
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Mul.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Mul_Op::Type = "Mul";

void Aidge::Mul_Op::computeOutputDims() {
    // check inputs have been associated
    if (!getInput(0) || !getInput(1)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "At least one input was not connected");
    }

    if (!getInput(0)->empty() && !getInput(1)->empty()) {

        const std::vector<std::size_t>& inputsDims0 = getInput(0)->dims();
        const std::vector<std::size_t>& inputsDims1 = getInput(1)->dims();

        std::vector<std::size_t> outDims = (inputsDims0.size() >= inputsDims1.size()) ? inputsDims0 : inputsDims1;
        const std::vector<std::size_t>& lowDims = (inputsDims0.size() < inputsDims1.size()) ? inputsDims0 : inputsDims1;

        std::size_t out_id = outDims.size() - 1;
        std::size_t low_id = lowDims.size() - 1;
        std::size_t i = 0;
        while (i++ < lowDims.size()) {
            if (outDims[out_id] == 1) {
                outDims[out_id] = lowDims[low_id];
            }
            else if ((lowDims[low_id] != 1) && (lowDims[low_id] != outDims[out_id])) {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "Unsopported Tensor shape for Div Operation");
            }
            --out_id;
            --low_id;
        }
        mOutputs[0]->resize(outDims);
    }
    else if (!getInput(0)->empty() && !getInput(1)->empty()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Incompatible input dimensions for Operator Mul: {} and {}", getInput(0)->dims(), getInput(1)->dims());
    }
}

void Aidge::Mul_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(Mul_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}
