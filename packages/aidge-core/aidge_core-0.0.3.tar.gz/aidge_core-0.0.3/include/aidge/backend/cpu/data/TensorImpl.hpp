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

#ifndef AIDGE_CPU_DATA_TENSORIMPL_H_
#define AIDGE_CPU_DATA_TENSORIMPL_H_

#include "aidge/backend/TensorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/future_std/span.hpp"

namespace Aidge {

template <class T>
class TensorImpl_cpu : public TensorImpl {
private:
    /// Pointer to the data and its capacity
    future_std::span<T> mData;
    /// If this instance own the data, std::unique_ptr manages it
    std::unique_ptr<T[]> mDataOwner;

public:
    static const std::string Backend;

public:
    TensorImpl_cpu(DeviceIdx_t device, std::vector<DimSize_t> dims) : TensorImpl(Backend, device, dims) {}

    bool operator==(const TensorImpl &other) const override final;

    static std::shared_ptr<TensorImpl_cpu> create(DeviceIdx_t device, std::vector<DimSize_t> dims) {
        return std::make_shared<TensorImpl_cpu<T>>(device, dims);
    }

    inline std::size_t scalarSize() const noexcept override final { return sizeof(T); }

    void zeros() override final;

    void copy(const void *src, NbElts_t length, NbElts_t offset = 0) override final {
        const T* srcT = static_cast<const T *>(src);
        T* dstT = static_cast<T *>(rawPtr(offset));

        AIDGE_ASSERT(length <= mData.size() || length <= mNbElts, "copy length is above capacity");
        AIDGE_ASSERT(dstT < srcT || dstT >= srcT + length, "overlapping copy is not supported");
        std::copy(srcT, srcT + length, dstT);
    }

    void copyCast(const void *src, const DataType srcDt, NbElts_t length, NbElts_t offset = 0) override final;

    void copyFromDevice(const void *src, const std::pair<std::string, DeviceIdx_t>& device, NbElts_t length, NbElts_t offset = 0) override final {
        AIDGE_ASSERT(device.first == Backend, "backend must match");
        AIDGE_ASSERT(device.second == 0, "device cannot be != 0 for CPU backend");
        copy(src, length, offset);
    }

    inline void copyFromHost(const void *src, NbElts_t length, NbElts_t offset = 0) override final {
        copy(src, length, offset);
    }

    void copyToHost(void *dst, NbElts_t length, NbElts_t offset = 0) const override final {
        const T* src = static_cast<const T*>(rawPtr(offset));
        AIDGE_ASSERT(length <= mData.size() || length <= mNbElts, "copy length is above capacity");
        std::copy(src, src + length, static_cast<T *>(dst));
    }

    void *rawPtr(NbElts_t offset = 0) override final {
        lazyInit();
        return (mData.data() + offset);
    };

    const void *rawPtr(NbElts_t offset = 0) const override final {
        AIDGE_ASSERT(mData.size() >= mNbElts, "accessing uninitialized const rawPtr");
        return (mData.data() + offset);
    };

    void *hostPtr(NbElts_t offset = 0) override final {
        lazyInit();
        return (mData.data() + offset);
    };

    const void *hostPtr(NbElts_t offset = 0) const override final {
        AIDGE_ASSERT(mData.size() >= mNbElts, "accessing uninitialized const hostPtr");
        return (mData.data() + offset);
    };

    void setRawPtr(void *ptr, NbElts_t length) override final {
        AIDGE_ASSERT(length >= mNbElts, "trying to set raw pointer of insufficient capacity");
        mData = future_std::span<T>(static_cast<T *>(ptr), length);
        mDataOwner.reset();
    };

    virtual ~TensorImpl_cpu() = default;

private:
    void lazyInit() {
        if (mData.size() < mNbElts) {
            // Need more data, a re-allocation will occur
            AIDGE_ASSERT(mData.empty() || mDataOwner != nullptr, "trying to enlarge non-owned data");
            mDataOwner.reset(new T[mNbElts]);
            mData = future_std::span<T>(mDataOwner.get(), mNbElts);
        }
    }
};


template <typename T>
const std::string TensorImpl_cpu<T>::Backend = "cpu";

namespace {
static Registrar<Tensor> registrarTensorImpl_cpu_Float64(
        {"cpu", DataType::Float64}, Aidge::TensorImpl_cpu<double>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Float32(
        {"cpu", DataType::Float32}, Aidge::TensorImpl_cpu<float>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Float16(
        {"cpu", DataType::Float16}, Aidge::TensorImpl_cpu<half_float::half>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Int64(
        {"cpu", DataType::Int64}, Aidge::TensorImpl_cpu<long>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Int32(
        {"cpu", DataType::Int32}, Aidge::TensorImpl_cpu<int>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Int16(
        {"cpu", DataType::Int16}, Aidge::TensorImpl_cpu<int16_t>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_UInt16(
        {"cpu", DataType::UInt16}, Aidge::TensorImpl_cpu<uint16_t>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_Int8(
        {"cpu", DataType::Int8}, Aidge::TensorImpl_cpu<int8_t>::create);
static Registrar<Tensor> registrarTensorImpl_cpu_UInt8(
        {"cpu", DataType::UInt8}, Aidge::TensorImpl_cpu<uint8_t>::create);
}  // namespace
}  // namespace Aidge

#endif /* AIDGE_CPU_DATA_TENSORIMPL_H_ */
