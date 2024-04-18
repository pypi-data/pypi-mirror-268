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

#include "aidge/operator/ReLU.hpp"

#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::ReLU_Op::Type = "ReLU";

void Aidge::ReLU_Op::setBackend(const std::string& name, DeviceIdx_t device) {
    SET_IMPL_MACRO(ReLU_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}