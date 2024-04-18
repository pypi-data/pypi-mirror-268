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

#include <algorithm>
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/MatMul.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

const std::string Aidge::MatMul_Op::Type = "MatMul";

void Aidge::MatMul_Op::computeOutputDims() {
    if (!getInput(0) || !getInput(1)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Missing input. Cannot compute output dimensions for MatMul Operator.");
    }
    if (getInput(0)->empty() && getInput(1)->empty()) {
        // both inputs are scalar
        mOutputs[0]->resize({});
    }
    else if (!getInput(0)->empty() && !getInput(1)->empty())
    {
        std::vector<std::size_t> dims0 = getInput(0)->dims();
        std::vector<std::size_t> dims1 = getInput(1)->dims();

        // keep second-to-last dimension of dims0
        const bool keepDim0 = dims0.size() > 1;
        // keep last dimension of dims1
        const bool keepDim1 = dims1.size() > 1;

        if (dims0.size() == 1) {
            dims0.insert(dims0.cbegin(), 1);
        }
        if (dims1.size() == 1) {
            dims1.push_back(1);
        }
        const std::size_t dims_size = std::max(dims0.size(), dims1.size());


        if (dims0.size() > dims1.size()) {
            dims1.insert(dims1.cbegin(), dims0.size() - dims1.size(), std::size_t(1));
        }
        else if (dims1.size() > dims0.size()) {
            dims0.insert(dims0.cbegin(), dims1.size() - dims0.size(), std::size_t(1));
        }

        AIDGE_ASSERT(dims0[dims_size-1] == dims1[dims_size-2], "Incompatible matrices sizes.");

        std::vector<std::size_t> outDims = std::vector<std::size_t>(dims_size-2, 1);
        for (std::size_t i = 0; i < dims_size-2; ++i) {
            AIDGE_ASSERT((dims0[i] == dims1[i]) || (dims0[i] == 1) || (dims1[i] == 1), "Bad vector dimension.");
            outDims[i] = std::max(dims0[i], dims1[i]);
        }

        // use keepDim0 instead of dims0.size() because dims0 has been modified
        if (keepDim0)
            outDims.push_back(dims0[dims_size-2]);
        if (keepDim1)
            outDims.push_back(dims1[dims_size-1]);

        mOutputs[0]->resize(outDims);
    }
}

void Aidge::MatMul_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(MatMul_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}
