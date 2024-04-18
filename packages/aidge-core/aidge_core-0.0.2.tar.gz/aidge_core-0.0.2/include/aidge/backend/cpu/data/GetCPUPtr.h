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

#ifndef AIDGE_CPU_DATA_GETCPUPTR_H_
#define AIDGE_CPU_DATA_GETCPUPTR_H_

#include <cstddef>
#include <memory>

#include "aidge/data/Tensor.hpp"

namespace Aidge {
inline void *getCPUPtr(std::shared_ptr<Aidge::Data> const &data, const std::size_t offset = 0) {
  const auto tensor = std::static_pointer_cast<Tensor>(data);
  return tensor->getImpl()->hostPtr(tensor->getImplOffset() + offset);
}
} // namespace Aidge

#endif // AIDGE_CPU_DATA_GETCPUPTR_H_
