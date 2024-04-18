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

#include "aidge/operator/Softmax.hpp"

#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Softmax_Op::Type = "Softmax";

void Aidge::Softmax_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    mImpl = Registrar<Softmax_Op>::create(name)(*this);
    mOutputs[0]->setBackend(name, device);
}