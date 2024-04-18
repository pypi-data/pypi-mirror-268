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
#include <stdexcept>  // std::runtime_error
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Add.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"

const std::string Aidge::Add_Op::Type = "Add";

Aidge::Add_Op::Add_Op(const Add_Op& op)
    : OperatorTensor(op)
{
    if (op.mImpl) {
        SET_IMPL_MACRO(Add_Op, *this, op.backend());
    } else {
        mImpl = nullptr;
    }
}

void Aidge::Add_Op::computeOutputDims() {
    // check inputs have been associated
    bool associated = (nbInputs() > 0); // do not compute anything if no input
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (!getInput(i)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Every input should be associated with a Tensor");
        }
        associated &= !(getInput(i)->empty());
    }
    if (associated) {
        std::vector<std::vector<std::size_t>> inputsDims(nbInputs());
        for (std::size_t i = 0; i < nbInputs(); i++) {
            inputsDims[i] = getInput(i)->dims();
        }

        std::size_t outNbDims = 1;
        for(std::size_t i = 0; i < nbInputs(); ++i) {
            outNbDims = (inputsDims[i].size() > outNbDims) ? inputsDims[i].size() : outNbDims;
        }

        std::vector<std::size_t> outDims(outNbDims, 1);

        for (auto it = outDims.rbegin(); it != outDims.rend(); ++it) {
            for (std::size_t i = 0; i < nbInputs(); ++i) {
                if(!inputsDims[i].empty()) {
                    const std::size_t dim = inputsDims[i].back();
                    inputsDims[i].pop_back();
                    if (*it == 1) {
                        *it = dim;
                    }
                    else if ((dim != *it) && (dim != 1)) {
                        AIDGE_THROW_OR_ABORT(std::runtime_error, "Unsopported Tensor shape for Add operation");
                    }
                }
            }
        }
        mOutputs[0]->resize(outDims);
    }
}

void Aidge::Add_Op::setBackend(const std::string& name, DeviceIdx_t device) {
    SET_IMPL_MACRO(Add_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}