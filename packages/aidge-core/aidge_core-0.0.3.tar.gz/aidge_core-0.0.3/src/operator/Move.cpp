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

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/operator/Move.hpp"

const std::string Aidge::Move_Op::Type = "Move";

void Aidge::Move_Op::forward() {
    if (mImpl) {
        mImpl->forward();
    }
    else {
        mOutputs[0]->copyFrom(*(mInputs[0]));
    }

    runHooks();
}
