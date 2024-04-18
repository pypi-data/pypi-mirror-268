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

#ifndef AIDGE_CORE_DATA_TENSOR_H_
#define AIDGE_CORE_DATA_TENSOR_H_

#include <cstddef>      // std::size_t
#include <cstring>
#include <functional>   // std::multiplies
#include <set>
#include <memory>
#include <numeric>      // std::accumulate
#include <string>
#include <type_traits>  // std::is_arithmetic
#include <vector>

#include "aidge/backend/TensorImpl.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/operator/Add.hpp"
#include "aidge/operator/Div.hpp"
#include "aidge/operator/Mul.hpp"
#include "aidge/operator/Sub.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/ArrayHelpers.hpp"

namespace Aidge {
/**
 * @brief Description for the tensor data structure.
 * @details Sets the properties of the tensor without actually containing any data.
 * Contains a pointer to an actual contiguous implementation of data.
 */
class Tensor : public Data,
               public Registrable<Tensor, std::tuple<std::string, DataType>, std::shared_ptr<TensorImpl>(DeviceIdx_t device, std::vector<DimSize_t> dims)> {
   private:
    DataType mDataType = DataType::Float32; /** enum to specify data type. */
    std::vector<DimSize_t> mDims; /** Dimensions of the tensor. */
    std::vector<DimSize_t> mStrides; /** Stride dimensions of the tensor. */
    std::shared_ptr<TensorImpl> mImpl = nullptr; /** Pointer to the actual data implementation. */
    std::size_t mImplOffset = 0;
    std::shared_ptr<Tensor> mGrad = nullptr; /** Pointer to the associated gradient Tensor instance. */

    // Cached data
    /// @brief Number of elements in the Tensor.
    std::size_t mSize;
    /// @brief Whether or not data are contiguous in memory.
    bool mContiguous = true;

   public:
    static constexpr const char *Type = "Tensor";

    /**
     * @brief Construct a new empty Tensor object.
     * It has the features of an undefined scalar.
     */
    Tensor(DataType dtype = DataType::Float32)
        : Data(Type),
          mDataType(dtype),
          mDims(std::vector<DimSize_t>({})),
          mStrides({1}),
          mSize(1)
    {
        // ctor
    }

    /**
     * @brief Construct a new Tensor object from an arithmetic parameter.
     *
     * @tparam T Type of the input parameter.
     * @tparam VT Decayed type of the input paramter.
     * @param val Input value.
     */
    template<typename T,
             typename VT = std::enable_if_t<std::is_arithmetic<T>::value, std::decay_t<T>>>
    Tensor(T val)
        : Data(Type),
          mDataType(NativeType<VT>::type),
          mDims({}),
          mStrides({1}),
          mImpl(Registrar<Tensor>::create({"cpu", NativeType<VT>::type})(0, std::vector<std::size_t>())),
          mSize(1)
    {
        *static_cast<VT*>(mImpl->rawPtr()) = static_cast<VT>(val);
    }

    /**
     * @brief Construct a new Tensor object from dimensions.
     *
     * @param dims dimensions of the tensor
     */
    Tensor(const std::vector<DimSize_t>& dims)
        : Data(Type)
    {
        // set mDims, mStrides, mContiguous, mSize
        resize(dims);
    }

    /**
     * @brief Construct a new Tensor object from the 1-dimension Array helper.
     * @tparam T datatype
     * @tparam SIZE_0 first array dimension.
     */
    template <typename T, std::size_t SIZE_0>
    constexpr Tensor(Array1D<T, SIZE_0> &&arr)
        : Data(Type),
          mDataType(NativeType<T>::type),
          mDims({SIZE_0}),
          mStrides({1}),
          mImpl(Registrar<Tensor>::create({"cpu", NativeType<T>::type})(0, {SIZE_0})),
          mSize(SIZE_0)
    {
        mImpl->copyFromHost(&arr.data[0], SIZE_0);
    }

    /**
     * @brief Construct a new Tensor object from the 2-dimensions Array helper.
     * @tparam T datatype
     * @tparam SIZE_0 first array dimension.
     * @tparam SIZE_1 second array dimension.
     */
    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1>
    constexpr Tensor(Array2D<T, SIZE_0, SIZE_1> &&arr)
        : Data(Type),
          mDataType(NativeType<T>::type),
          mDims({SIZE_0, SIZE_1}),
          mStrides({SIZE_1, 1}),
          mImpl(Registrar<Tensor>::create({"cpu", NativeType<T>::type})(0, {SIZE_0, SIZE_1})),
          mSize(SIZE_0 * SIZE_1) {
        mImpl->copyFromHost(&arr.data[0][0], SIZE_0 * SIZE_1);
    }

    /**
     * @brief Construct a new Tensor object from the 3-dimensions Array helper.
     * @tparam T datatype
     * @tparam SIZE_0 first array dimension.
     * @tparam SIZE_1 second array dimension.
     * @tparam SIZE_2 third array dimension.
     */
    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2>
    constexpr Tensor(Array3D<T, SIZE_0, SIZE_1, SIZE_2> &&arr)
        : Data(Type),
          mDataType(NativeType<T>::type),
          mDims({SIZE_0, SIZE_1, SIZE_2}),
          mStrides({SIZE_1 * SIZE_2, SIZE_2, 1}),
          mImpl(Registrar<Tensor>::create({"cpu", NativeType<T>::type})(0, {SIZE_0, SIZE_1, SIZE_2})),
          mSize(SIZE_0 * SIZE_1 * SIZE_2) {
        mImpl->copyFromHost(&arr.data[0][0][0], SIZE_0 * SIZE_1 * SIZE_2);
    }

    /**
     * @brief Construct a new Tensor object from the 4-dimensions Array helper.
     * @tparam T datatype
     * @tparam SIZE_0 first array dimension.
     * @tparam SIZE_1 second array dimension.
     * @tparam SIZE_2 third array dimension.
     * @tparam SIZE_3 fourth array dimension.
     */
    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2, std::size_t SIZE_3>
    constexpr Tensor(Array4D<T, SIZE_0, SIZE_1, SIZE_2, SIZE_3> &&arr)
        : Data(Type),
          mDataType(NativeType<T>::type),
          mDims({SIZE_0, SIZE_1, SIZE_2, SIZE_3}),
          mStrides({SIZE_1 * SIZE_2 * SIZE_3, SIZE_2 * SIZE_3, SIZE_3, 1}),
          mImpl(Registrar<Tensor>::create({"cpu", NativeType<T>::type})(0, {SIZE_0, SIZE_1, SIZE_2, SIZE_3})),
          mSize(SIZE_0 * SIZE_1 * SIZE_2 * SIZE_3) {
        mImpl->copyFromHost(&arr.data[0][0][0][0], SIZE_0 * SIZE_1 * SIZE_2 * SIZE_3);
    }

    /**
     * @brief Copy constructor. Construct a new Tensor object from another one
     * (shallow copy). Data memory is not copied, but shared between the new
     * Tensor and the initial one.
     * @param other
     */
    Tensor(const Tensor& other) = default;

    /**
     * @brief Move constructor.
     * @param other
     */
    Tensor(Tensor&& other) = default;

    /**
     * @brief Copy dimensions, datatype and data from another Tensor.
     * If current Tensor already has an implementation, data is copied to the
     * existing implementation. Tensor backend/device remain untouched.
     * If current Tensor does not have an implementation, only a shallow copy
     * is performed and the Tensor will share data with t.
     * @param other other Tensor object.
     * @return Tensor&
     */
    Tensor &operator=(const Tensor& other);

    template <typename T, std::size_t SIZE_0>
    constexpr Tensor &operator=(Array1D<T, SIZE_0> &&arr) {
        *this = Tensor(std::move(arr));
        return *this;
    }

    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1>
    constexpr Tensor &operator=(Array2D<T, SIZE_0, SIZE_1> &&arr) {
        *this = Tensor(std::move(arr));
        return *this;
    }

    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2>
    constexpr Tensor &operator=(Array3D<T, SIZE_0, SIZE_1, SIZE_2> &&arr) {
        *this = Tensor(std::move(arr));
        return *this;
    }

    template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2, std::size_t SIZE_3>
    constexpr Tensor &operator=(Array4D<T, SIZE_0, SIZE_1, SIZE_2, SIZE_3> &&arr) {
        *this = Tensor(std::move(arr));
        return *this;
    }

    /**
     * @brief Assess data type, dimensions, backend and data are the same.
     * @param otherTensor
     */
    bool operator==(const Tensor &otherTensor) const {
        if ((!mImpl && !otherTensor.mImpl) || (dataType() != otherTensor.dataType()) ||
            (dims() != otherTensor.dims()) || (mImpl->backend() != otherTensor.mImpl->backend())) {
            return false;
        }
        return *mImpl == *(otherTensor.mImpl);
    }

    /**
     * @brief Element-wise addition operation for two ``Tensor``s.
     * @note ``Tensor``s should be stored on the same backend.
     * @todo If input ``Tensor``s have a different dataType, the output should
     * have the dataType of the ``Tensor`` with the highest precision.
     *
     * @param other
     * @return Tensor
     */
    Tensor operator+(const Tensor& other) const {
        AIDGE_ASSERT(hasImpl() && other.hasImpl(), "At least one Tensor cannot perform any binary operation because it has no implementation.");
        AIDGE_ASSERT(mImpl->backend() == other.mImpl->backend(), "Tensors must have the same backend");
        AIDGE_ASSERT(dataType() == other.dataType(), "Tensors must have the same backend");
        auto add_ = Add_Op(2);
        add_.associateInput(0, std::make_shared<Tensor>(*this));
        add_.associateInput(1, std::make_shared<Tensor>(other));
        add_.computeOutputDims();
        add_.setDataType(dataType());
        add_.setBackend(mImpl->backend());
        add_.forward();
        // using add_backend = std::remove_reference_t<decltype(*Registrar<Add_Op>::create("cpu")(std::declval<const Add_Op&>()))>;
        return add_.getOutput(0)->clone();
    }

    /**
     * @brief Element-wise substraction operation for two ``Tensor``s.
     * @note ``Tensor``s should be stored on the same backend.
     * @todo If input ``Tensor``s have a different dataType, the output should
     * have the dataType of the ``Tensor`` with the highest precision.
     *
     * @param other
     * @return Tensor
     */
    Tensor operator-(const Tensor& other) const {
        AIDGE_ASSERT(hasImpl() && other.hasImpl(), "At least one Tensor cannot perform any binary operation because it has no implementation.");
        AIDGE_ASSERT(mImpl->backend() == other.mImpl->backend(), "Tensors must have the same backend");
        AIDGE_ASSERT(dataType() == other.dataType(), "Tensors must have the same backend");
        auto sub_ = Sub_Op();
        sub_.associateInput(0, std::make_shared<Tensor>(*this));
        sub_.associateInput(1, std::make_shared<Tensor>(other));
        sub_.computeOutputDims();
        sub_.setDataType(dataType());
        sub_.setBackend(mImpl->backend());
        sub_.forward();
        // using add_backend = std::remove_reference_t<decltype(*Registrar<Add_Op>::create("cpu")(std::declval<const Add_Op&>()))>;
        return sub_.getOutput(0)->clone();
    }

    /**
     * @brief Element-wise multiplication operation for two ``Tensor``s.
     * @note ``Tensor``s should be stored on the same backend.
     * @todo If input ``Tensor``s have a different dataType, the output should
     * have the dataType of the ``Tensor`` with the highest precision.
     *
     * @param other
     * @return Tensor
     */
    Tensor operator*(const Tensor& other) const {
        AIDGE_ASSERT(hasImpl() && other.hasImpl(), "At least one Tensor cannot perform any binary operation because it has no implementation.");
        AIDGE_ASSERT(mImpl->backend() == other.mImpl->backend(), "Tensors must have the same backend");
        AIDGE_ASSERT(dataType() == other.dataType(), "Tensors must have the same backend");
        auto mul_ = Mul_Op();
        mul_.associateInput(0, std::make_shared<Tensor>(*this));
        mul_.associateInput(1, std::make_shared<Tensor>(other));
        mul_.computeOutputDims();
        mul_.setDataType(dataType());
        mul_.setBackend(mImpl->backend());
        mul_.forward();
        // using add_backend = std::remove_reference_t<decltype(*Registrar<Add_Op>::create("cpu")(std::declval<const Add_Op&>()))>;
        return mul_.getOutput(0)->clone();
    }

    /**
     * @brief Element-wise division operation for two ``Tensor``s.
     * @note ``Tensor``s should be stored on the same backend.
     * @todo If input ``Tensor``s have a different dataType, the output should
     * have the dataType of the ``Tensor`` with the highest precision.
     *
     * @param other
     * @return Tensor
     */
    Tensor operator/(const Tensor& other) const {
        AIDGE_ASSERT(hasImpl() && other.hasImpl(), "At least one Tensor cannot perform any binary operation because it has no implementation.");
        AIDGE_ASSERT(mImpl->backend() == other.mImpl->backend(), "Tensors must have the same backend");
        AIDGE_ASSERT(dataType() == other.dataType(), "Tensors must have the same backend");
        auto div_ = Div_Op();
        div_.associateInput(0, std::make_shared<Tensor>(*this));
        div_.associateInput(1, std::make_shared<Tensor>(other));
        div_.computeOutputDims();
        div_.setDataType(dataType());
        div_.setBackend(mImpl->backend());
        div_.forward();
        // using add_backend = std::remove_reference_t<decltype(*Registrar<Add_Op>::create("cpu")(std::declval<const Add_Op&>()))>;
        return div_.getOutput(0)->clone();
    }

    ~Tensor() noexcept;

public:
    /**
     * @brief Perform a deep copy of the tensor.
    */
    Tensor clone() const {
        Tensor newTensor(*this);
        if (!newTensor.isContiguous()) {
            newTensor.makeContiguous();
        }
        else {
            std::shared_ptr<TensorImpl> newImpl = Registrar<Tensor>::create({mImpl->backend(), mDataType})(mImpl->device().second, mDims);
            newImpl->copy(mImpl->rawPtr(mImplOffset), mSize);
            newTensor.setImpl(newImpl);
        }
        return newTensor;
    }

    const std::string backend() const {
        return hasImpl() ? getImpl()->backend() : "";
    }

    /**
     * @brief Set the backend of the Tensor associated implementation. If there
     * was no previous implementation set, data will be allocated, but it will
     * not be initialized to any particular value.
     * If data was already initialized in a previous backend, it will be moved
     * to the new one except if copyFrom is false.
     * @param name Backend name
     * @param device Backend device
     * @param copyFrom If true (default), move data from previous backend/device
     * to the new one. Previous data is lost otherwise.
     */
    inline void setBackend(const std::string &name, DeviceIdx_t device = 0, bool copyFrom = true) {
        if (mImpl) {
            if (mImpl->device() != std::make_pair(name, device)) {
                // Backend change: create new impl, copy from old to new and replace
                // impl
                std::shared_ptr<TensorImpl> newImpl = Registrar<Tensor>::create({name, mDataType})(device, mDims);
                if (copyFrom) {
                    newImpl->copyFrom(*mImpl, mImpl->size(), mImplOffset, 0);
                }
                setImpl(newImpl);
            }
        }
        else {
            mImpl = Registrar<Tensor>::create({name, mDataType})(device, mDims);
        }
    }

    /**
     * @brief Get a list of available backends.
     * @return std::set<std::string>
     */
    static std::set<std::string> getAvailableBackends();

    /**
     * @brief Get the data type enum.
     * @return constexpr DataType
     */
    constexpr DataType dataType() const noexcept { return mDataType; }

    /**
     * @brief Set the DataType of the Tensor and converts data
     * if the Tensor has already been initialized and copyCast is true.
     * @param dt DataType
     * @param copyCast If true (default), previous data is copy-casted. Otherwise
     * previous data is lost.
     */
    void setDataType(const DataType dt, bool copyCast = true) {
        if (mImpl && (dataType() != dt)) {
            std::shared_ptr<TensorImpl> newImpl = Registrar<Tensor>::create({mImpl->backend(), dt})(mImpl->device().second, mDims);
            if (copyCast) {
                newImpl->copyCast(mImpl->rawPtr(mImplOffset), mDataType, mImpl->size());
            }
            setImpl(newImpl);
        }
        mDataType = dt;
    }

    /**
     * @brief Get the Impl object
     * @return constexpr const std::shared_ptr<TensorImpl>&
     */
    constexpr const std::shared_ptr<TensorImpl>& getImpl() const noexcept { return mImpl; }
    constexpr std::size_t getImplOffset() const noexcept { return mImplOffset; }

    /**
     * @brief Set the Impl object
     *
     * @param impl New impl shared pointer
     * @param implOffset Storage offset in this new impl for this Tensor
     */
    void setImpl(std::shared_ptr<TensorImpl> impl, std::size_t implOffset = 0) {
        mImpl = impl;
        mImplOffset = implOffset;
    }

    /**
     * @brief Return if an implementaiton has been associated.
     * @return true
     * @return false
     */
    bool hasImpl() const noexcept { return mImpl ? true : false; }

    /**
     * @brief Get number of dimensions of the Tensor.
     * @return std::size_t
     */
    inline std::size_t nbDims() const { return mDims.size(); }

    /**
     * @brief Get dimensions of the Tensor object.
     * @tparam DIM number of dimensions.
     * @return constexpr std::array<DimSize_t, DIM>
     */
    template <DimIdx_t DIM>
    constexpr std::array<DimSize_t, DIM> dims() const {
        assert(DIM == mDims.size() && "wrong number of dimensions");
        return to_array<DIM>(mDims.cbegin());
    }

    /**
     * @brief Get dimensions of the Tensor object.
     * @return constexpr const std::vector<DimSize_t>&
     */
    constexpr inline const std::vector<DimSize_t>& dims() const noexcept { return mDims; }

    /**
     * @brief Get strides of the Tensor object.
     * @return constexpr const std::vector<DimSize_t>&
     */
    constexpr inline const std::vector<DimSize_t>& strides() const noexcept { return mStrides; }

    /**
     * @brief Return true if Tensor is contiguous in memory.
     * @return bool
     */
    constexpr bool isContiguous() const noexcept { return mContiguous; }

    /**
     * @brief Get the number of elements in the Tensor object.
     * @return constexpr std::size_t
     */
    constexpr std::size_t size() const noexcept { return mSize; }

    /**
     * @brief Change the dimensions of the Tensor object according to the given argument.
     * If the overall size is not changed (meaning we actually only performed a
     * reshape), data is garanteed to remain valid.
     * Otherwise, no garantee is provided regarding the validy of previous data
     * (unlike std::vector). If the new overall size is larger than the previous
     * one, all previous data is invalided. Otherwise, previous data may or may
     * not remain valid, depending on the backend implementation.
     * @tparam DIM Number of dimensions.
     * @param dims New dimensions
     */
    template <std::array<DimSize_t, 1>::size_type DIM> // deducing std::array size_type and declaring DIM accordingly
    inline void resize(const std::array<DimSize_t, DIM> &dims) {
        resize(std::vector<DimSize_t>(dims.begin(), dims.end()));
    }

    /**
     * @brief Change the dimensions of the Tensor object according to the given argument.
     * If the overall size is not changed (meaning we actually only performed a
     * reshape), data is garanteed to remain valid.
     * Otherwise, no garantee is provided regarding the validy of previous data
     * (unlike std::vector). If the new overall size is larger than the previous
     * one, all previous data is invalided. Otherwise, previous data may or may
     * not remain valid, depending on the backend implementation.
     * @param dims New dimensions
     * @param strides Stride of the tensor (if not specified, "nested" stride is used)
     */
    void resize(const std::vector<DimSize_t> &dims, std::vector<DimSize_t> strides = std::vector<DimSize_t>());

    /**
     * @brief Return if the Tensor object has at leastone element.
     * @return true
     * @return false
     */
    bool empty() const { return mDims.empty(); }
    // bool newempty() const noexcept {
    //     return mSize == 0;
    // }

    /**
     * @brief Set each element of the tensor to zero.
     */
    void zeros() const {
        if (mImpl) {
            mImpl->zeros();
        }
    }

    template <typename expectedType>
    const expectedType& get(std::size_t idx) const {
        AIDGE_ASSERT(NativeType<expectedType>::type == mDataType, "wrong data type");
        AIDGE_ASSERT(idx < mSize, "idx out of range");
        return *reinterpret_cast<expectedType *>(mImpl->hostPtr(mImplOffset + idx));
    }

    template <typename expectedType>
    const expectedType& get(std::vector<std::size_t> coordIdx) const {
        return get<expectedType>(getStorageIdx(coordIdx));
    }

    template <typename expectedType>
    void set(std::size_t idx, expectedType value){
        AIDGE_ASSERT(NativeType<expectedType>::type == mDataType, "wrong data type");
        AIDGE_ASSERT(idx < mSize, "idx out of range");
        expectedType* dataPtr = static_cast<expectedType*>(mImpl->hostPtr(mImplOffset + idx));
        *dataPtr = value;
    }

    template <typename expectedType>
    void set(std::vector<std::size_t> coordIdx, expectedType value){
        set<expectedType>(getStorageIdx(coordIdx), value);
    }

    std::string toString() const override;

    inline void print() const { fmt::print("{}\n", toString()); }

    std::shared_ptr<Tensor> grad() {
        // if (!mGrad && mImpl) {
        //     mGrad = std::make_shared<Tensor>(mDims);
        //     mGrad->setDataType(mDataType);
        //     mGrad->setBackend(mImpl->backend());

        //     // if (mImpl) mGrad->setBackend(mImpl->backend());
        // }

        return mGrad;
    }

    /**
     * @brief Associate the gradient with a Tensor instance and set its implementation
     * if none was previously set.
     * @note Dimensions for the Tensor instance are copied from the original current Tensor.
     * @note If a Tensor instance was already associated, only the implementation is created
     * with values set to 0.
     * @note If Tensor instance and implementation already existed for the gradient
     * nothing is done.
     */
    void initGradient() {
        if (!mGrad) {
            mGrad = std::make_shared<Tensor>(mDims);
        }
        if (!mGrad->hasImpl()) {
            mGrad->setDataType(dataType());
            mGrad->setBackend(hasImpl() ? mImpl->backend() : "cpu");
            mGrad->zeros();
        }
    }

    /**
     * @brief From the the 1D contiguous index, return the coordinate of an element in the tensor.
     * Beware: do not use this function with the storage index!
     *
     * @param flatIdx 1D contiguous index of the value considering a flatten, contiguous, tensor.
     * @return std::vector<DimSize_t>
     */
    std::vector<std::size_t> getCoord(std::size_t flatIdx) const {
        std::vector<std::size_t> coordIdx(mDims.size());
        std::size_t i = mDims.size();

        while (i-- > 0) {
            coordIdx[i] = (flatIdx % mDims[i]);
            flatIdx/=mDims[i];
        }
        return coordIdx;
    }

    /**
     * @brief From the coordinate returns the 1D contiguous index of an element in the tensor.
     * If the number of coordinates is inferior to the number of dimensions,
     * the remaining coordinates are assumed to be 0.
     * Beware: the contiguous index will only correspond to the storage index
     * if the tensor is contiguous!
     *
     * @param coordIdx Coordinate to an element in the tensor
     * @return DimSize_t Contiguous index
     */
    std::size_t getIdx(const std::vector<std::size_t>& coordIdx) const {
        AIDGE_ASSERT(coordIdx.size() <= mDims.size(), "Coordinates does not match number of dimensions");
        std::size_t flatIdx = 0;
        std::size_t i = 0;
        for(; i < coordIdx.size() - 1; ++i) {
            AIDGE_ASSERT(coordIdx[i] < mDims[i], "Coordinates dimensions does not fit the dimensions of the tensor");
            flatIdx = (flatIdx + coordIdx[i]) * mDims[i + 1];
        }
        return flatIdx + coordIdx[i];
    }

    /**
     * @brief From the coordinate returns the 1D storage index of an element in the tensor.
     * If the number of coordinates is inferior to the number of dimensions,
     * the remaining coordinates are assumed to be 0.
     *
     * @param coordIdx Coordinate to an element in the tensor
     * @return DimSize_t Storage index
     */
    std::size_t getStorageIdx(const std::vector<std::size_t>& coordIdx) const {
        for(std::size_t i = 0; i < coordIdx.size(); ++i) {
            AIDGE_ASSERT(coordIdx[i] < mDims[i], "Coordinates dimensions does not fit the dimensions of the tensor");
        }
        AIDGE_ASSERT(coordIdx.size() <= mDims.size(), "Coordinates does not match number of dimensions");
        return std::inner_product(coordIdx.cbegin(), coordIdx.cend(), mStrides.cbegin(), DimSize_t(0));
    }

    /**
     * @brief Returns a sub-tensor with equal or lower number of dimensions.
     *
     * @note For instance, ``t.extract({1})`` on a CHW tensor will return the HW tensor
     * of channel #1.
     * Likewise, ``t.extract({0, 1})`` on a NCHW tensor will return the HW tensor
     * of batch #0 and channel #1.
     * @note No memory copy is performed, the returned tensor does not own the memory.
     * @note If the number of coordinates matches the number of dimensions, a scalar
     * tensor is returned.
     * @note If current tensor was contiguous, the returned tensor is garanteed to be
     * contiguous as well.
     *
     * @param coordIdx Coordinates of the sub-tensor to extract
     * @return Tensor Sub-tensor.
    */
    Tensor extract(const std::vector<std::size_t>& coordIdx) const;

    /**
     * @brief Returns a sub-tensor at some coordinate and with some dimension.
     *
     * @note Data contiguity of the returned Tensor is not guaranted.
     *
     * @param coordIdx First coordinates of the sub-tensor to extract
     * @param dims Dimensions of the sub-tensor to extract
     * @return Tensor Sub-tensor.
    */
    Tensor extract(const std::vector<std::size_t>& coordIdx, const std::vector<std::size_t>& dims) const;

    /**
     * @brief Make the tensor's storage contiguous, if it is not already the case.
     * If not contiguous, a new memory space is allocated.
    */
    void makeContiguous();

    /**
     * Copy-cast data from a Tensor on the same device.
     * If current tensor backend/device is set and is different from src, an
     * assertion is raised.
     * @param src Source tensor to copy-cast from.
    */
    void copyCast(const Tensor& src);

    /**
     * Copy data from a Tensor from another backend/device.
     * If current tensor data type is set and is different from src, an
     * assertion is raised.
     * @param src Source tensor to copy from.
    */
    void copyFrom(const Tensor& src);

    /**
     * Copy-cast data from a Tensor.
     * @param src Source tensor to copy-cast from.
     * @param movedSrc shared_ptr to an indermediate Tensor that will
     * contain the moved data if a device change should occur AND a type
     * conversion is necessary (otherwise it remains unused).
     * Any data already present will be overwritten. No new memory allocation
     * will occur if movedSrc has already been allocated with the right
     * type/size/device.
     * If required, memory is always allocated on current (destination)
     * Tensor's device.
    */
    void copyCastFrom(const Tensor& src, std::shared_ptr<Tensor>& movedSrc);

    /**
     * Copy-cast data from a Tensor.
     * In case of both a device change AND a data type conversion, an
     * intermediate buffer on will be allocated and deallocated each time.
     * If required, buffer's memory is always allocated on current (destination)
     * Tensor's device.
     * @param src Source tensor to copy-cast from.
    */
    void copyCastFrom(const Tensor& src) {
        // Internal buffer will be allocated and deallocated at each call
        // (only if needed)
        std::shared_ptr<Tensor> movedSrc;
        copyCastFrom(src, movedSrc);
    }

    /**
     * Return a reference to a Tensor that is garanteed to be contiguous:
     * - itself, if already contiguous;
     * - the provided Tensor, overwritten with the copied data.
     * The data type, backend and device stay the same.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @return Reference to either itself or to fallback.
    */
    Tensor& refContiguous(std::shared_ptr<Tensor>& fallback);
    const Tensor& refContiguous(std::shared_ptr<Tensor>& fallback) const;

    /**
     * Return a reference to a Tensor casted to the desired data type:
     * - itself, if already at the right data type;
     * - the provided Tensor, overwritten with the copy-casted data.
     * The backend stays the same.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param dt The desired data type.
     * @return Reference to either itself or to fallback.
    */
    Tensor& refCast(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt);
    const Tensor& refCast(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt) const;

    /**
     * Return a reference to a Tensor on the desired backend/device:
     * - itself, if already on the right device;
     * - the provided Tensor, overwritten with the copied data.
     * The data type stays the same.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param backend The desired backend.
     * @param device The desired device.
     * @return Reference to either itself or to fallback.
    */
    Tensor& refFrom(std::shared_ptr<Tensor>& fallback, const std::string &backend, DeviceIdx_t device = 0);
    const Tensor& refFrom(std::shared_ptr<Tensor>& fallback, const std::string &backend, DeviceIdx_t device = 0) const;

    /**
     * Return a reference to a Tensor on desired data type and backend/device:
     * - itself, if already with the right characteristics;
     * - the provided Tensor, overwritten with the copy-casted data.
     * If required, fallback is always allocated on desired (destination)
     * device.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param dt The desired data type.
     * @param backend The desired backend.
     * @param device The desired device.
     * @return Reference to either itself or to fallback.
    */
    Tensor& refCastFrom(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt, const std::string &backend, DeviceIdx_t device = 0) {
        // First refFrom, to ensure that fallback, if required, is also on desired device
        return refFrom(fallback, backend, device).refCast(fallback, dt);
    }

    /**
     * Return a reference to a Tensor with same characteristics
     * (data type, backend/device) as targetReqs Tensor:
     * - itself, if already with the right characteristics;
     * - the provided Tensor, overwritten with the copy-casted data.
     * If required, fallback is always allocated on current (destination)
     * Tensor's device.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param targetReqs Tensor with the desired target characteristics.
     * @return Reference to either itself or to fallback.
    */
    Tensor& refCastFrom(std::shared_ptr<Tensor>& fallback, const Tensor& targetReqs) {
        const auto& device = targetReqs.getImpl()->device();
        return refCastFrom(fallback, targetReqs.dataType(), device.first, device.second);
    }

    /**
     * @brief Return a reference to a Tensor on desired data type and backend/device:
     * - itself, if already with the right characteristics;
     * - the provided Tensor, overwritten with the right characteristics.
     * @note no data is copy-casted. If it was so in a previous refCastFrom() on
     * the same fallback, it remains valid, otherwise, data is invalid.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param dt The desired data type.
     * @param backend The desired backend.
     * @param device The desired device.
     * @return Reference to either itself or to fallback.
    */
    Tensor& ref(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt, const std::string &backend, DeviceIdx_t device = 0);
    const Tensor& ref(std::shared_ptr<Tensor>& fallback, const Aidge::DataType& dt, const std::string &backend, DeviceIdx_t device = 0) const;

    /**
     * @brief Return a reference to a Tensor with same characteristics
     * (data type, backend/device) as targetReqs Tensor:
     * - itself, if already with the right characteristics;
     * - the provided Tensor, overwritten with the right characteristics.
     * @note no data is copy-casted. If it was so in a previous refCastFrom() on
     * the same fallback, it remains valid, otherwise, data is invalid.
     * @param fallback A shared_ptr to Tensor ready to be overwritten if necessary.
     * The shared_ptr does not need to be initialized. No new memory allocation
     * will occur if fallback has already been allocated with the right
     * type/size/device.
     * @param targetReqs Tensor with the desired target characteristics.
     * @return Reference to either itself or to fallback.
    */
    Tensor& ref(std::shared_ptr<Tensor>& fallback, const Tensor& targetReqs) {
        const auto& device = targetReqs.getImpl()->device();
        return ref(fallback, targetReqs.dataType(), device.first, device.second);
    }

private:
    /**
     * @brief Compute the number of elements in the Tensor.
     * @note If dimensions are not empty, they are multiplied to get the total number
     * of elements. Else, the Tensor represents a scalar and contains a single element.
     */
    void computeSize() {
        mSize = std::accumulate(mDims.begin(), mDims.end(), DimSize_t(1), std::multiplies<DimSize_t>());
    }
};
}  // namespace Aidge

#endif /* AIDGE_CORE_DATA_TENSOR_H_ */
