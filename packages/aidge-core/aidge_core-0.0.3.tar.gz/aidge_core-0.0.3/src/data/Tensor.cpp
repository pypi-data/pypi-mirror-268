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

#include <cstddef>
#include <vector>

#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

Aidge::Tensor& Aidge::Tensor::operator=(const Aidge::Tensor& other) {
    if (this == &other) {
        return *this;
    }
    resize(other.dims(), other.strides());
    setDataType(other.dataType(), false); // do not convert existing data
    if (other.hasImpl()) {
        if (hasImpl()) {
            copyFrom(other);
        }
        else {
            // Perform a shallow copy only
            setImpl(other.mImpl, other.mImplOffset);
        }
    }
    else {
        setImpl(nullptr);
    }
    return *this;
}


Aidge::Tensor::~Tensor() noexcept = default;


void Aidge::Tensor::resize(const std::vector<Aidge::DimSize_t> &dims, std::vector<Aidge::DimSize_t> strides) {
    // TODO: scalar Tensor not handled
    if (dims.empty()) { // scalar
        mDims = std::vector<DimSize_t>(0);
        mStrides = std::vector<DimSize_t>({1});
        mContiguous = true;

        computeSize();
        if (mImpl) {
            mImpl->resize(mDims);
        }
        return;
    }

    bool checkContiguous = true;
    if (strides.empty()) {
        strides.resize(dims.size());
        size_t expectedStride = 1;
        for (int dim = dims.size() - 1; dim >= 0; --dim) {
            strides[dim] = expectedStride;
            expectedStride*= dims[dim];
        }
        checkContiguous = false;
    }
    else {
        AIDGE_ASSERT(strides.size() == dims.size(), "Number of strides must match number of dims");
    }

    if (mImpl && mImpl.use_count() > 1) {
        // Here we could also create a new storage for this tensor in this case
        // But, is it more likely that the user really wants this, or that he did a mistake?
        AIDGE_ASSERT(dims == mDims && strides == mStrides, "Cannot resize Tensor with shared storage");
    }
    else {
        mDims = dims;
        mStrides = strides;

        mContiguous = true;
        if (checkContiguous) {
            std::size_t expectedStride = 1;
            // std::size_t i = dims.size();
            // while ((i-- > 0) && (strides[i] == expectedStride)) {
            //     mContiguous&= (strides[i] == expectedStride);
            //     expectedStride*= dims[i];
            // }
            for (std::size_t i = dims.size()-1; i > 0; --i) {
                if (strides[i] != expectedStride) {
                    mContiguous = false;
                    break;
                }
                expectedStride*= dims[i];
            }
            mContiguous &= (strides[0] == expectedStride);
        }

        computeSize();
        if (mImpl) {
            mImpl->resize(mDims);
        }
    }
}

std::string Aidge::Tensor::toString() const {
    AIDGE_ASSERT(mImpl && (dims().empty() || (dims() == std::vector<DimSize_t>({0})) || (mImpl->hostPtr() != nullptr)), "tensor should have a valid host pointer");

    // TODO: move lambda elsewhere?
    auto ptrToString = [](DataType dt, void* ptr, std::size_t idx) {
        switch (dt) {
        case DataType::Float64:
            return std::to_string(static_cast<double*>(ptr)[idx]);
        case DataType::Float32:
            return std::to_string(static_cast<float*>(ptr)[idx]);
        case DataType::Float16:
            return std::to_string(static_cast<half_float::half*>(ptr)[idx]);
        case DataType::Int8:
            return std::to_string(static_cast<int8_t*>(ptr)[idx]);
        case DataType::Int16:
            return std::to_string(static_cast<int16_t*>(ptr)[idx]);
        case DataType::Int32:
            return std::to_string(static_cast<int32_t*>(ptr)[idx]);
        case DataType::Int64:
            return std::to_string(static_cast<int64_t*>(ptr)[idx]);
        case DataType::UInt8:
            return std::to_string(static_cast<uint8_t*>(ptr)[idx]);
        case DataType::UInt16:
            return std::to_string(static_cast<uint16_t*>(ptr)[idx]);
        case DataType::UInt32:
            return std::to_string(static_cast<uint32_t*>(ptr)[idx]);
        case DataType::UInt64:
            return std::to_string(static_cast<uint64_t*>(ptr)[idx]);
        default:
            AIDGE_ASSERT(true, "unsupported type to convert to string");
        }
        return std::string("?");  // To make Clang happy
    };

    if (dims().empty()) { return ptrToString(mDataType, mImpl->hostPtr(), 0); }
    std::string res;
    std::size_t dim = 0;
    std::size_t counter = 0;
    if (nbDims()>=2) {
        std::vector<std::size_t> dimVals(nbDims(), 0);
        res += "{\n";
        while (counter < mSize) {
            std::string spaceString = std::string((dim+1)<<1,' ');
            if (dim < nbDims()-2) {
                if (dimVals[dim] == 0) {
                    res += spaceString + "{\n";
                    ++dim;
                } else if (dimVals[dim] < static_cast<std::size_t>(dims()[dim])) {
                    res += spaceString + "},\n" + spaceString + "{\n";
                    ++dim;
                } else {
                    res += spaceString + "}\n";
                    dimVals[dim--] = 0;
                    dimVals[dim]++;
                }
            } else {
                for (; dimVals[dim] < static_cast<std::size_t>(dims()[dim]); ++dimVals[dim]) {
                    res += spaceString + "{";
                    for (DimSize_t j = 0; j < dims()[dim + 1] - 1; ++j) {
                        res += " " + ptrToString(mDataType, mImpl->hostPtr(mImplOffset), counter++) + ",";
                    }
                    res += " " + ptrToString(mDataType, mImpl->hostPtr(mImplOffset), counter++) + "}";
                    if (dimVals[dim] < static_cast<std::size_t>(dims()[dim] - 1)) {
                        res += ",";
                    }
                    res += "\n";
                }
                if (dim == 0) {
                    break;
                }
                dimVals[dim--] = 0;
                dimVals[dim]++;
            }
        }

        for(int i = static_cast<int>(dim); i > 0; --i) {
            res += std::string((dim+1)<<1,' ') + "}\n";
        }
    } else {
        res += "{";
        for (DimSize_t j = 0; j < dims()[0]; ++j) {
            res += " " + ptrToString(mDataType, mImpl->hostPtr(mImplOffset), j) + ((j < dims()[0]-1) ? "," : " ");
        }
    }
    res += "}";
    return res;
}

Aidge::Tensor Aidge::Tensor::extract(const std::vector<std::size_t>& fixedCoord) const {
    AIDGE_ASSERT(isContiguous(), "Tensor must be contiguous");
    AIDGE_ASSERT(fixedCoord.size() <= mDims.size(), "Number of coordinates is higher than number of dimensions");

    Tensor subTensor(mDataType);
    subTensor.resize(std::vector<size_t>(mDims.cbegin() + fixedCoord.size(), mDims.cend()),
        std::vector<size_t>(mStrides.cbegin() + fixedCoord.size(), mStrides.cend()));
    subTensor.setBackend(mImpl->backend(), mImpl->device().second);
    subTensor.setImpl(mImpl, mImplOffset + getStorageIdx(fixedCoord));
    return subTensor;
}

Aidge::Tensor Aidge::Tensor::extract(const std::vector<std::size_t>& startCoord, const std::vector<std::size_t>& dims) const {
    AIDGE_ASSERT(isContiguous(), "Tensor must be contiguous");
    AIDGE_ASSERT(startCoord.size() == mDims.size(), "Coordinates does not match number of dimensions");

    Tensor subTensor(mDataType);
    subTensor.resize(dims, mStrides);
    subTensor.setBackend(mImpl->backend(), mImpl->device().second);
    subTensor.setImpl(mImpl, mImplOffset + getStorageIdx(startCoord));
    return subTensor;
}

void Aidge::Tensor::makeContiguous() {
    if (!mImpl || isContiguous()) {
        return;
    }

    // Block so that mImpl ref count is 1 for resize()
    {
        // Create a new storage that will be contiguous
        std::shared_ptr<TensorImpl> newImpl = Registrar<Tensor>::create({mImpl->backend(), mDataType})(mImpl->device().second, mDims);
        // Copy elements from old to new storage
        std::size_t idx = 0;
        while (idx < mSize) {
            const std::size_t storageIdx = getStorageIdx(getCoord(idx));

            // Determine the size of the contiguous chunk
            std::size_t copySize = 1;
            while (idx + copySize < mSize &&
                getStorageIdx(getCoord(idx + copySize)) == storageIdx + copySize)
            {
                ++copySize;
            }

            // Perform a single copy for the contiguous chunk
            newImpl->copy(mImpl->rawPtr(mImplOffset + storageIdx), copySize, idx);

            // Move to the next index after the contiguous chunk
            idx += copySize;
        }
        // Replace old storage by new, contiguous, storage
        setImpl(newImpl);
    }

    // Resize tensor without strides => tensor is now contiguous
    resize(mDims);
}

void Aidge::Tensor::copyCast(const Tensor& src) {
    if (&src == this) {
        return;
    }

    AIDGE_ASSERT(src.isContiguous(), "cannot copy-cast non-contiguous tensor");

    // Current Tensor has necessarily a data type, but may not have backend
    if (!hasImpl()) {
        // If no backend was set for the current tensor, use the same as src
        const auto deviceSrc = src.getImpl()->device();
        setBackend(deviceSrc.first, deviceSrc.second);
    }
    resize(src.dims());

    AIDGE_ASSERT(src.getImpl()->device() == getImpl()->device(), "cannot copy-cast from a different backend/device");
    getImpl()->copyCast(src.getImpl()->rawPtr(src.mImplOffset), src.dataType(), src.size(), mImplOffset);
}

void Aidge::Tensor::copyFrom(const Tensor& src) {
    if (&src == this) {
        return;
    }

    AIDGE_ASSERT(src.isContiguous(), "cannot copy from non-contiguous tensor");

    // Current Tensor has necessarily a data type, but may not have backend
    if (!hasImpl()) {
        // If no backend was set for the current tensor, use the same as src
        const auto deviceSrc = src.getImpl()->device();
        setBackend(deviceSrc.first, deviceSrc.second);
    }
    resize(src.dims());

    AIDGE_ASSERT(src.dataType() == dataType(), "cannot copy from a different data type");
    getImpl()->copyFrom(*(src.getImpl()), src.size(), src.mImplOffset, mImplOffset);
}

void Aidge::Tensor::copyCastFrom(const Tensor& src, std::shared_ptr<Tensor>& movedSrcPtr) {
    if (&src == this) {
        return;
    }

    AIDGE_ASSERT(src.isContiguous(), "cannot copy-cast from non-contiguous tensor");

    // Current Tensor has necessarily a data type, but may not have backend
    if (!getImpl()) {
        // If no backend was set for the current tensor, use the same as src
        const auto deviceSrc = src.getImpl()->device();
        setBackend(deviceSrc.first, deviceSrc.second);
    }
    resize(src.dims());

    if (dataType() != src.dataType()) {
        // First move data to the target device (only if needed)
        const auto device = getImpl()->device();
        const Tensor& movedSrc = src.refFrom(movedSrcPtr, device.first, device.second);
        // Second, copy-cast data (necessary)
        getImpl()->copyCast(movedSrc.getImpl()->rawPtr(movedSrc.mImplOffset), movedSrc.dataType(), movedSrc.size(), mImplOffset);
    }
    else {
        // Directly copy, no conversion necessary
        // Avoid making a double copy if both data type and device are the same
        getImpl()->copyFrom(*(src.getImpl()), src.size(), src.mImplOffset, mImplOffset);
    }
}

Aidge::Tensor& Aidge::Tensor::refContiguous(std::shared_ptr<Tensor>& fallback) {
    // Scott Meyers' solution to avoid code duplication
    return const_cast<Tensor&>(static_cast<const Tensor&>(*this).refContiguous(fallback));
}

const Aidge::Tensor& Aidge::Tensor::refContiguous(std::shared_ptr<Tensor>& fallback) const {
    AIDGE_ASSERT(getImpl(), "no backend was set for tensor, cannot refCast() it");

    if (isContiguous()) {
        return *this;
    }
    else {
        if (this != fallback.get()) {
            // Shallow copy to fallback
            *fallback = *this;
        }

        // Make fallback contiguous
        fallback->makeContiguous();
        return *fallback;
    }
}

Aidge::Tensor& Aidge::Tensor::refCast(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt) {
    // Scott Meyers' solution to avoid code duplication
    return const_cast<Tensor&>(static_cast<const Tensor&>(*this).refCast(fallback, dt));
}

const Aidge::Tensor& Aidge::Tensor::refCast(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt) const {
    AIDGE_ASSERT(getImpl(), "no backend was set for tensor, cannot refCast() it");

    if (dt == dataType()) {
        return *this;
    }
    else {
        if (this == fallback.get()) {
            // if refFrom() was called before, just change the type
            fallback->setDataType(dt);
        }
        else {
            AIDGE_ASSERT(isContiguous(), "cannot refCast non-contiguous tensor");

            if (!fallback) {
                fallback = std::make_shared<Tensor>(dt);
            }
            else {
                fallback->setDataType(dt, false); // don't keep previous data (no copy)
            }

            const auto device = getImpl()->device();
            fallback->setBackend(device.first, device.second, false); // don't keep previous data (no copy)
            fallback->resize(dims());
            fallback->getImpl()->copyCast(getImpl()->rawPtr(mImplOffset), dataType(), size(), fallback->mImplOffset);
        }
        return *fallback;
    }
}

Aidge::Tensor& Aidge::Tensor::refFrom(std::shared_ptr<Tensor>& fallback, const std::string &backend, DeviceIdx_t device) {
    // Scott Meyers' solution to avoid code duplication
    return const_cast<Tensor&>(static_cast<const Tensor&>(*this).refFrom(fallback, backend, device));
}

const Aidge::Tensor& Aidge::Tensor::refFrom(std::shared_ptr<Tensor>& fallback, const std::string &backend, DeviceIdx_t device) const {
    AIDGE_ASSERT(getImpl(), "no backend was set for tensor, cannot refFrom() it");

    if (std::make_pair(backend, device) == getImpl()->device()) {
        return *this;
    }
    else {
        if (this == fallback.get()) {
            // if refCast() was called before, just change the backend
            fallback->setBackend(backend, device);
        }
        else {
            AIDGE_ASSERT(isContiguous(), "cannot refFrom non-contiguous tensor");

            if (!fallback) {
                fallback = std::make_shared<Tensor>(dataType());
            }
            else {
                fallback->setDataType(dataType(), false); // don't keep previous data (no copy)
            }

            fallback->setBackend(backend, device, false); // don't keep previous data (no copy)
            fallback->resize(dims());
            fallback->getImpl()->copyFrom(*getImpl(), size(), mImplOffset, fallback->mImplOffset);
        }
        return *fallback;
    }
}

Aidge::Tensor& Aidge::Tensor::ref(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt, const std::string &backend, DeviceIdx_t device) {
    // Scott Meyers' solution to avoid code duplication
    return const_cast<Tensor&>(static_cast<const Tensor&>(*this).ref(fallback, dt, backend, device));
}

const Aidge::Tensor& Aidge::Tensor::ref(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt, const std::string &backend, DeviceIdx_t device) const {
    AIDGE_ASSERT(getImpl(), "no backend was set for tensor, cannot ref() it");

    if (dt == dataType() && std::make_pair(backend, device) == getImpl()->device()) {
        return *this;
    }
    else {
        // Change fallback type, backend & device, without any data copy
        if (!fallback) {
            fallback = std::make_shared<Tensor>(dt);
        }
        else {
            fallback->setDataType(dt, false); // don't keep previous data (no copy)
        }

        fallback->setBackend(backend, device, false); // don't keep previous data (no copy)
        fallback->resize(dims());
        return *fallback;
    }
}

std::set<std::string> Aidge::Tensor::getAvailableBackends() {
    std::set<std::string> backendsList;
    for(const auto& tupleKey : Registrar<Tensor>::getKeys())
        backendsList.insert(std::get<0>(tupleKey));
    return backendsList;
}
