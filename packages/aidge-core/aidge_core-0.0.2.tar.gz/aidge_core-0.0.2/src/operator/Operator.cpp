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

#include <cassert>
#include <cstddef>
#include <vector>
#include <utility>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

// constexpr Aidge::Operator::Operator(const char* type)
//     : mType(type)
// {
// 	// ctor
// }

Aidge::Operator::~Operator() noexcept = default;

///////////////////////////////////////////////////////
//        IMPLEMENTATION
///////////////////////////////////////////////////////

Aidge::Elts_t Aidge::Operator::getNbRequiredData(const Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(mImpl != nullptr, "getNbRequiredData(): an implementation is required for {}!", type());
    return mImpl->getNbRequiredData(inputIdx);
}

Aidge::Elts_t Aidge::Operator::getNbRequiredProtected(const Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(mImpl != nullptr, "getNbRequiredProtected(): an implementation is required for {}!", type());
    return mImpl->getNbRequiredProtected(inputIdx);
}

Aidge::Elts_t Aidge::Operator::getRequiredMemory(const IOIndex_t outputIdx, const std::vector<DimSize_t> &inputsSize) const {
    AIDGE_ASSERT(mImpl != nullptr, "getRequiredMemory(): an implementation is required for {}!", type());
    return mImpl->getRequiredMemory(outputIdx, inputsSize);
}

Aidge::Elts_t Aidge::Operator::getNbConsumedData(Aidge::IOIndex_t inputIdx) const {
    AIDGE_ASSERT(mImpl != nullptr, "getNbConsumedData(): an implementation is required for {}!", type());
    return mImpl->getNbConsumedData(inputIdx);
}

Aidge::Elts_t Aidge::Operator::getNbProducedData(Aidge::IOIndex_t outputIdx) const {
    AIDGE_ASSERT(mImpl != nullptr, "getNbProducedData(): an implementation is required for {}!", type());
    return mImpl->getNbProducedData(outputIdx);
}
void Aidge::Operator::updateConsummerProducer(){
    AIDGE_ASSERT(mImpl != nullptr, "updateConsummerProducer(): an implementation is required for {}!", type());
    mImpl->updateConsummerProducer();
}
void Aidge::Operator::resetConsummerProducer(){
    AIDGE_ASSERT(mImpl != nullptr, "resetConsummerProducer(): an implementation is required for {}!", type());
    mImpl->resetConsummerProducer();
}

void Aidge::Operator::runHooks() const {
    for (auto& hook : mHooks) {
        hook.second->call();
    }
}
void Aidge::Operator::forward() {
    AIDGE_ASSERT(mImpl != nullptr, "forward(): an implementation is required for {}!", type());
    mImpl->forward();
    runHooks();
}

void Aidge::Operator::backward() {
    AIDGE_ASSERT(mImpl != nullptr, "backward(): an implementation is required for {}!", type());
    mImpl->backward(); 
}
