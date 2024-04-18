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

#include "aidge/data/Tensor.hpp"
#include "aidge/backend/TensorImpl.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

void Aidge::TensorImpl::copyFrom(const TensorImpl& srcImpl, NbElts_t length, NbElts_t srcOffset, NbElts_t dstOffset) {
    if (&srcImpl == this && srcOffset == dstOffset) {
        return;
    }

    if (srcImpl.device() != device()) {
        if (srcImpl.backend() == backend()) {
            // Same backend, but different device
            copyFromDevice(srcImpl.rawPtr(srcOffset), srcImpl.device(), length, dstOffset);
        }
        else if (srcImpl.hostPtr() != nullptr) {
            // Different backend, but input is valid on host
            copyFromHost(srcImpl.hostPtr(srcOffset), length, dstOffset);
        }
        else if (hostPtr() != nullptr) {
            // Different backend, but dst is valid on host
            srcImpl.copyToHost(hostPtr(srcOffset), length, dstOffset);
        }
        else {
            // No direct link possible from src to dst device
            // SLOW SOLUTION: must pass through the host, requires TWO copies
            // Allocate a temporary host buffer just for the copy
            // We might reuse a pre-allocated buffer, but for now this feature is not provided because:
            // - There is currently no concrete use case
            // - Just providing a pointer would be unsafe (risk of buffer overflow...)
            auto tmpHostBuffer = std::unique_ptr<char[]>(new char[scalarSize() * length]);
            srcImpl.copyToHost(tmpHostBuffer.get(), length, srcOffset);
            copyFromHost(tmpHostBuffer.get(), length, dstOffset);
        }
    }
    else {
        // Same device: simple copy on device
        copy(srcImpl.rawPtr(srcOffset), length, dstOffset);
    }
}
