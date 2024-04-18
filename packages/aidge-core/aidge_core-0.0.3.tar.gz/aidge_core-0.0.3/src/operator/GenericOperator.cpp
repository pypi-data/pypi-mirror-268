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

#include "aidge/operator/GenericOperator.hpp"

#include <cstddef>  // std::size_t
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

const Aidge::GenericOperator_Op::ComputeDimsFunc Aidge::GenericOperator_Op::Identity
    = [](const std::vector<std::vector<std::size_t>>& inputsDims) { return inputsDims; };

const Aidge::GenericOperator_Op::ComputeDimsFunc Aidge::GenericOperator_Op::InputIdentity(IOIndex_t inputIdx, IOIndex_t nbOutputs) {
    return [nbOutputs, inputIdx](const std::vector<std::vector<std::size_t>>& inputsDims) { return std::vector<std::vector<std::size_t>>(nbOutputs, inputsDims[inputIdx]); };
}

void Aidge::GenericOperator_Op::computeOutputDims() {
    if (mComputeOutputDims) {
        std::vector<std::vector<std::size_t>> inputsDims(nbInputs(), std::vector<std::size_t>());
        for (std::size_t i = 0; i < nbInputs(); ++i) {
            if (getInput(i)) {
                inputsDims[i] = getInput(i)->dims();
            }
        }

        const auto& outputsDims = mComputeOutputDims(inputsDims);
        AIDGE_ASSERT((outputsDims.size() == nbOutputs()), "The provided ComputeDimsFunc function returns the wrong number of outputs");
        for (std::size_t i = 0; i < nbOutputs(); ++i) {
            mOutputs[i]->resize(outputsDims[i]);
        }
    }
    else {
        AIDGE_ASSERT(false, "Cannot compute output dim of a GenericOperator");
    }
}

bool Aidge::GenericOperator_Op::outputDimsForwarded() const {
    if (mComputeOutputDims) {
        return !(mOutputs[0]->empty());
    }
    else {
        AIDGE_ASSERT(false, "GenericOperator cannot forward dims");
        return false;
    }
}