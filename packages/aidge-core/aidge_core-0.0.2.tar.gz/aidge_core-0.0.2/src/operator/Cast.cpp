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

#include "aidge/operator/Cast.hpp"

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::Cast_Op::Type = "Cast";

void Aidge::Cast_Op::forward() {
    if (mImpl) {
        mImpl->forward();
    }
    else {
        mOutputs[0]->copyCast(*(mInputs[0]));
    }

    runHooks();
}

void Aidge::Cast_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    if (Registrar<Cast_Op>::exists({name})) {
        SET_IMPL_MACRO(Cast_Op, *this, name);
    }
    mOutputs[0]->setBackend(name, device);
}
