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

#include "aidge/operator/Pop.hpp"

#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"


const std::string Aidge::Pop_Op::Type = "Pop";

void Aidge::Pop_Op::computeOutputDims() {
    // check inputs have been associated
    if (!getInput(0)) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #0 should be associated with a Tensor", type());
    }
    if (!(getInput(0)->empty())) {
        auto inputDims = getInput(0)->dims();
        inputDims.erase(inputDims.begin());
        getOutput(0)->resize(inputDims);
    }
}

void Aidge::Pop_Op::updateConsummerProducer() {
    Operator::updateConsummerProducer();
    this->template getAttr<PopAttr::ForwardStep>() = 0;
}

void Aidge::Pop_Op::forward() {
    Operator::forward();
    ++this->template getAttr<PopAttr::ForwardStep>();
}

void Aidge::Pop_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(Pop_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}
