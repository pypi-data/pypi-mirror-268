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

#include "aidge/operator/Scaling.hpp"

#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Scaling_Op::Type = "Scaling";

void Aidge::Scaling_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    mImpl = Registrar<Scaling_Op>::create(name)(*this);
    mOutputs[0]->setBackend(name, device);
}