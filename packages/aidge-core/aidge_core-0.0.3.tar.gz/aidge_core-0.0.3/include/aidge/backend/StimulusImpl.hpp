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

#ifndef AIDGE_CORE_BACKEND_STIMULUSIMPL_H_
#define AIDGE_CORE_BACKEND_STIMULUSIMPL_H_

#include <memory>

#include "aidge/data/Tensor.hpp"

namespace Aidge {

/**
 * @brief Base class to implement data loading functions.
 */
class StimulusImpl {
public:
    virtual ~StimulusImpl() noexcept = default;

    virtual std::shared_ptr<Tensor> load() const = 0;
};
} // namespace Aidge

#endif /* AIDGE_CORE_BACKEND_STIMULUSIMPL_H_ */
