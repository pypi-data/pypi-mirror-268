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

#include "aidge/operator/FC.hpp"

#include <memory>
#include <string>
#include <vector>

#include "aidge/data/Data.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::FC_Op::Type = "FC";

void Aidge::FC_Op::associateInput(const Aidge::IOIndex_t inputIdx, const std::shared_ptr<Aidge::Data>& data) {
    AIDGE_ASSERT(inputIdx < 3, "Operators {} supports only {} inputs", type(), nbInputs());
    AIDGE_ASSERT(data->type() == Tensor::Type, "input data must be of Tensor type");
    // TODO: FIXME: check this, because data dims may not be initialized at this point...
    //if (inputIdx == 2) {
    //    assert(std::dynamic_pointer_cast<Tensor>(data)->size() == ((this->template getAttr<FCAttr::NoBias>()) == false ? static_cast<std::size_t>(this->template getAttr<FCAttr::OutChannels>()) : 0));
    //    assert(std::dynamic_pointer_cast<Tensor>(data)->nbDims() == 1);
    //}
    mInputs[inputIdx] = std::dynamic_pointer_cast<Tensor>(data);
    if (inputIdx == 0 && getInput(0)->nbDims() == 1)
        mInputs[inputIdx]->resize({1, getInput(inputIdx)->size()});
}

void Aidge::FC_Op::computeOutputDims() {
    bool associated = true;
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (!getInput(i)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
        }
        associated &= !(getInput(i)->empty());
    }
    if (associated) {
        // <batch, OutChannels>
        mOutputs[0]->resize({getInput(0)->dims()[0], this->template getAttr<FCAttr::OutChannels>()});
    }
}

void Aidge::FC_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(FC_Op, *this, name);
    mOutputs[0]->setBackend(name, device);

    // By default, automatically set backend for weight and bias inputs
    getInput(1)->setBackend(name, device);
    getInput(2)->setBackend(name, device);
}
