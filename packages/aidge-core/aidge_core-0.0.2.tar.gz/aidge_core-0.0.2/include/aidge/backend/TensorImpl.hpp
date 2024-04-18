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

#ifndef AIDGE_TENSORIMPL_H_
#define AIDGE_TENSORIMPL_H_

#include <numeric>     // std::accumulate
#include <cstddef>     // std::size_t
#include <functional>  // std::multiplies
#include <vector>
#include <utility>     // std::pair, std::make_pair

#include "aidge/data/Data.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"

namespace Aidge {
/**
 * This is a thin wrapper around std::any that can only hold pointers.
 * It also handles the case where a U* pointer is stored and a const U* pointer
 * is requested, which is legit (std::any would throw a bad_cast exception in
 * this case).
 * Note: not used yet, put in reserve here for possible future use.
*/
/*
class AnyPtr {
public:
    template <typename T, typename = std::enable_if_t<std::is_pointer<T>::value>>
    constexpr inline AnyPtr(T value) : data(value), ptrToConst(std::is_const<std::remove_pointer_t<T>>::value) {}

    // Requested T is "U*"
    template <typename T, typename std::enable_if<std::is_same<std::remove_pointer_t<T>, std::remove_const_t<std::remove_pointer_t<T>>>::value>::type* = nullptr>
    constexpr inline T get() const {
        // data has to be "U*"
        return future_std::any_cast<T>(data);
    }

    // Requested T is "const U*"
    template <typename T, typename std::enable_if<!std::is_same<std::remove_pointer_t<T>, std::remove_const_t<std::remove_pointer_t<T>>>::value>::type* = nullptr>
    constexpr inline T get() const {
        if (ptrToConst) {
            // data is "const U*" => OK, no bad cast
            return future_std::any_cast<T>(data);
        }
        else {
            // data is "U*" => need to remove const from request to avoid bad cast
            return future_std::any_cast<std::add_pointer_t<std::remove_const_t<std::remove_pointer_t<T>>>>(data);
        }
    }

private:
    const future_std::any data;
    const bool ptrToConst;
};
*/

/**
 * @class TensorImpl
 * @brief Class to manage the raw data storage of a Tensor and provide generic copy
 * primitives from other devices and from/to host.
 * @note It can own the data or not (use ``setRawPtr()`` to set an external data owner).
 * @note It only knows the data type and data capacity, but does not handle anything else.
*/
class TensorImpl {
protected:

    const std::string mBackend;
    /// @brief Device id.
    const DeviceIdx_t mDevice;
    /// Number of elements (to be) stored.
    NbElts_t mNbElts;

public:
    TensorImpl() = delete;

    TensorImpl(const std::string& backend, DeviceIdx_t device, std::vector<DimSize_t> dims)
        : mBackend(backend),
          mDevice(device)
    {
        resize(dims);
    };

    virtual ~TensorImpl() = default;

    virtual bool operator==(const TensorImpl &othImpl) const = 0;

public:
    /**
     * Return the (backend, device) pair for this implementation.
    */
    std::pair<std::string, DeviceIdx_t> device() const noexcept {
        return std::make_pair(mBackend, mDevice);
    }

    /**
     * Copy data from the same device.
     * @param src Pointer on current implementation device.
     * @param length Number of elements to copy.
     * @param offset Destination offset (in number of elements).
    */
    virtual void copy(const void *src, NbElts_t length, NbElts_t offset = 0) = 0;

    /**
     * Copy-convert data from the same device.
     * @param srcDt Source data type.
     * @param src Pointer on current implementation device.
     * @param length Number of elements to copy.
     * @param offset Destination offset (in number of elements).
    */
    virtual void copyCast(const void *src, const DataType srcDt, NbElts_t length, NbElts_t offset = 0) = 0;

    /**
     * Copy data from an other device on the same backend.
     * @param device (backend, device) pair to copy from. The backend must match current implementation backend.
     * @param src Pointer on current implementation backend.
     * @param length Number of elements to copy.
     * @param offset Destination offset (in number of elements).
    */
    virtual void copyFromDevice(const void *src, const std::pair<std::string, DeviceIdx_t>& device, NbElts_t length, NbElts_t offset = 0) = 0;

    /**
     * Copy data from host.
     * @param src Host pointer to copy from.
     * @param length Number of elements to copy.
     * @param offset Destination offset (in number of elements).
    */
    virtual void copyFromHost(const void *src, NbElts_t length, NbElts_t offset = 0) = 0;

    /**
     * Copy data to host.
     * @param src Host pointer to copy to.
     * @param length Number of elements to copy.
     * @param offset Source offset (in number of elements).
    */
    virtual void copyToHost(void *dst, NbElts_t length, NbElts_t offset = 0) const = 0;

    /**
     * Return the raw device pointer.
     * The raw pointer is garanteed to be valid only on the *same* device.
     * @param offset Offset, in number of elements.
    */
    virtual void* rawPtr(NbElts_t offset = 0) = 0;
    virtual const void* rawPtr(NbElts_t offset = 0) const = 0;

    /**
     * Return the host pointer.
     * If the implementation does not have a valid host pointer, nullptr is returned.
     * @param offset Offset, in number of elements.
    */
    virtual void* hostPtr(NbElts_t /*offset*/ = 0) { return nullptr; };
    virtual const void* hostPtr(NbElts_t /*offset*/ = 0) const { return nullptr; };

    /**
     * Sets the device pointer. The previously owned data is deleted.
     * UNSAFE: directly setting the device pointer may lead to undefined behavior
     * if it does not match the required storage.
     * @param ptr A valid device pointer.
     * @param length Storage capacity at the provided pointer
    */
    virtual void setRawPtr(void* /*ptr*/, NbElts_t /*length*/)
    {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Cannot set raw pointer for backend {}", mBackend);
    };

    /**
     * @brief Set the size, in number of elements, that must be stored.
    */
    virtual void resize(std::vector<DimSize_t> dims) {
        mNbElts = std::accumulate(dims.cbegin(), dims.cend(), std::size_t(1), std::multiplies<std::size_t>());
    }

    /**
     * @brief Return the number of elements stored.
    */
    inline std::size_t size() const noexcept { return mNbElts; }

    /**
     * @brief Return the size (in bytes) of one element (scalar).
    */
    virtual std::size_t scalarSize() const noexcept = 0;

    /**
     * @brief Set every element of the implementation to zero.
     */
    virtual void zeros() {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Function not implented");
    }

    const std::string backend() const { return mBackend; }

    /**
     * @brief Copy from another backend.
     * @param srcImpl Source TensorImpl to copy from.
     * @param length Number of elements of size scalarSize() to copy
     * @param srcOffset Source offset (in number of elements).
     * @param dstOffset Destination offset (in number of elements).
    */
    void copyFrom(const TensorImpl& srcImpl, NbElts_t length, NbElts_t srcOffset = 0, NbElts_t dstOffset = 0);
};

} // namespace Aidge

#endif /* AIDGE_TENSORIMPL_H_ */
