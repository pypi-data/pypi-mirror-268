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

#include "aidge/stimuli/Stimulus.hpp"

#include <memory>

#include "aidge/data/Tensor.hpp"

Aidge::Stimulus::~Stimulus() = default;

std::shared_ptr<Aidge::Tensor> Aidge::Stimulus::load() {
    AIDGE_ASSERT((mImpl!=nullptr || mData!=nullptr), "No load implementation and No stored data");

    if (mLoadDataInMemory){
        if (mData == nullptr){
            mData = mImpl->load();
        }
        return mData;
    }
    return mImpl->load();
}