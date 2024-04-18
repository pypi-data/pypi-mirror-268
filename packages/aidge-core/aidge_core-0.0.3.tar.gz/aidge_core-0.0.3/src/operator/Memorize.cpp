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

#include "aidge/operator/Memorize.hpp"

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Memorize_Op::Type = "Memorize";

void Aidge::Memorize_Op::computeOutputDims() {
    for (size_t i = 0; i < 2; ++i) {
        if (!getInput(i)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "{}: input #{} should be associated with a Tensor", type(), i);
        }
    }

    // Only require one of the input to have dims defined
    // Otherwise, forwardDims() won't converge!
    if (!(getInput(0)->empty())) {
        const auto expectedDims =  getInput(0)->dims();
        mOutputs[0]->resize(expectedDims);
    }
    else if (!(getInput(1)->empty())) {
        const auto expectedDims =  getInput(1)->dims();
        mOutputs[0]->resize(expectedDims);
    }
}

void Aidge::Memorize_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    mImpl = Registrar<Memorize_Op>::create({name})(*this);
    mOutputs[0]->setBackend(name, device);
}

bool Aidge::Memorize_Op::outputDimsForwarded() const {
    // Only check the output dims
    bool forwarded = true;
    // check outputs have been filled
    for (IOIndex_t i = 0; i < nbOutputs(); ++i) {
        forwarded &= !(getOutput(i)->empty());
    }
    return forwarded;
}

void Aidge::Memorize_Op::updateConsummerProducer() {
    Operator::updateConsummerProducer();
    ++this->template getAttr<MemorizeAttr::ScheduleStep>();
    this->template getAttr<MemorizeAttr::ForwardStep>() = 0;
}

void Aidge::Memorize_Op::forward() {
    Operator::forward();
    ++this->template getAttr<MemorizeAttr::ForwardStep>();
    this->template getAttr<MemorizeAttr::ScheduleStep>() = 0;
}
