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

#include "aidge/backend/cpu/data/TensorImpl.hpp"

#include <algorithm>  // std::copy
#include <cstddef>    // std::size_t
#include <cstdint>    // std::uint8_t, std::int8_t, std::uint16_t, std::int16_t,
                      // std::uint32_t, std::int32_t, std::uint64_t, std::int64_t
#include <string>

#include "aidge/data/half.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"


template <typename T>
bool Aidge::TensorImpl_cpu<T>::operator==(const Aidge::TensorImpl &other) const {
    const auto& typedOtherImpl = reinterpret_cast<const TensorImpl_cpu<T>&>(other);
    AIDGE_INTERNAL_ASSERT(typedOtherImpl.size() >= mNbElts);

    std::size_t i = 0;
    for (;
        i < mNbElts &&
            *static_cast<const T*>(rawPtr(i)) == *static_cast<const T*>(typedOtherImpl.rawPtr(i));
        ++i)
    {}
    return i == mNbElts;
}

template <typename T>
void Aidge::TensorImpl_cpu<T>::zeros() {
    if (mData.empty()) {
        lazyInit();
    }
    for (std::size_t i = 0; i < mData.size(); ++i) {
        *(mData.data() + i) = T(0);
    }
}

template <typename T>
void Aidge::TensorImpl_cpu<T>::copyCast(const void *src, const Aidge::DataType srcDt, Aidge::NbElts_t length, Aidge::NbElts_t offset) {
    if (length == 0) {
        return;
    }

    T* dstT = static_cast<T *>(rawPtr(offset));
    AIDGE_ASSERT(length <= mData.size() || length <= mNbElts, "copy length is above capacity");
    switch (srcDt)
    {
        case DataType::Float64:
            std::copy(static_cast<const double*>(src), static_cast<const double*>(src) + length,
                    dstT);
            break;
        case DataType::Float32:
            std::copy(static_cast<const float*>(src), static_cast<const float*>(src) + length,
                    dstT);
            break;
        case DataType::Float16:
            std::copy(static_cast<const half_float::half*>(src), static_cast<const half_float::half*>(src) + length,
                    dstT);
            break;
        case DataType::Int64:
            std::copy(static_cast<const int64_t*>(src), static_cast<const int64_t*>(src) + length,
                    dstT);
            break;
        case DataType::UInt64:
            std::copy(static_cast<const uint64_t*>(src), static_cast<const uint64_t*>(src) + length,
                    dstT);
            break;
        case DataType::Int32:
            std::copy(static_cast<const int32_t*>(src), static_cast<const int32_t*>(src) + length,
                    dstT);
            break;
        case DataType::UInt32:
            std::copy(static_cast<const uint32_t*>(src), static_cast<const uint32_t*>(src) + length,
                    dstT);
            break;
        case DataType::Int16:
            std::copy(static_cast<const int16_t*>(src), static_cast<const int16_t*>(src) + length,
                    dstT);
            break;
        case DataType::UInt16:
            std::copy(static_cast<const uint16_t*>(src), static_cast<const uint16_t*>(src) + length,
                    dstT);
            break;
        case DataType::Int8:
            std::copy(static_cast<const int8_t*>(src), static_cast<const int8_t*>(src) + length,
                    dstT);
            break;
        case DataType::UInt8:
            std::copy(static_cast<const uint8_t*>(src), static_cast<const uint8_t*>(src) + length,
                    dstT);
            break;
        default:
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Unsupported data type.");
            break;
    }
}