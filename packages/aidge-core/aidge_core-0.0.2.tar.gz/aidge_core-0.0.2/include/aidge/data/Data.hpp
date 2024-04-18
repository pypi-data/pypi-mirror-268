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

#ifndef AIDGE_DATA_H_
#define AIDGE_DATA_H_

#include "aidge/data/half.hpp"
#include "aidge/utils/Attributes.hpp"

namespace Aidge {
enum class DataType {
    Float64,
    Float32,
    Float16,
    BFloat16,
    Binary,
    Ternary,
    Int2,
    Int3,
    Int4,
    Int5,
    Int6,
    Int7,
    Int8,
    Int16,
    Int32,
    Int64,
    UInt2,
    UInt3,
    UInt4,
    UInt5,
    UInt6,
    UInt7,
    UInt8,
    UInt16,
    UInt32,
    UInt64
};

class Data {
public:
    Data(const std::string& type): mType(type) {};
    constexpr const std::string& type() const {
        return mType;
    }
    virtual ~Data() = default;
    virtual std::string toString() const = 0;

private:
    const std::string mType;
};
}

namespace {
template <typename T> struct NativeType { static const Aidge::DataType type; };
template <> const Aidge::DataType NativeType<double>::type = Aidge::DataType::Float64;
template <> const Aidge::DataType NativeType<float>::type = Aidge::DataType::Float32;
template <> const Aidge::DataType NativeType<half_float::half>::type = Aidge::DataType::Float16;
template <> const Aidge::DataType NativeType<int8_t>::type = Aidge::DataType::Int8;
template <> const Aidge::DataType NativeType<int16_t>::type = Aidge::DataType::Int16;
template <> const Aidge::DataType NativeType<int32_t>::type = Aidge::DataType::Int32;
template <> const Aidge::DataType NativeType<int64_t>::type = Aidge::DataType::Int64;
template <> const Aidge::DataType NativeType<uint8_t>::type = Aidge::DataType::UInt8;
template <> const Aidge::DataType NativeType<uint16_t>::type = Aidge::DataType::UInt16;
template <> const Aidge::DataType NativeType<uint32_t>::type = Aidge::DataType::UInt32;
template <> const Aidge::DataType NativeType<uint64_t>::type = Aidge::DataType::UInt64;

template <>
const char* const EnumStrings<Aidge::DataType>::data[]
    = {"Float64", "Float32", "Float16", "BFloat16", "Binary", "Ternary",
       "Int2", "Int3", "Int4", "Int5", "Int6", "Int7", "Int8", "Int16",
       "Int32", "Int64", "UInt2", "UInt3", "UInt4", "UInt5", "UInt6",
       "UInt7", "UInt8", "UInt16", "UInt32", "UInt64"};
}

namespace Aidge {
inline auto format_as(DataType dt) { return EnumStrings<Aidge::DataType>::data[static_cast<int>(dt)]; }
}

#endif /* AIDGE_DATA_H_ */
