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


#ifndef AIDGE_TYPES_H_
#define AIDGE_TYPES_H_

#include <limits>
#include <type_traits>
#include <cstddef>
#include <cstdint>

namespace Aidge
{
//////////////////////////////////////
///          Tensor
//////////////////////////////////////

/// @brief Device index in a given backend
using DeviceIdx_t = std::uint8_t;
constexpr DeviceIdx_t MaxDeviceIdx = std::numeric_limits<DeviceIdx_t>::max();

/// @brief Number of elements used for scheduling
using NbElts_t = std::size_t;
constexpr NbElts_t MaxElts = std::numeric_limits<NbElts_t>::max();

///\brief Signed dimension size for Tensor (allow for negative coordinates).
using Coord_t = std::make_signed<std::size_t>::type;
constexpr Coord_t MaxCoord = std::numeric_limits<Coord_t>::max();

///\brief Unsigned value for the size of each dimension for a Tensor.
using DimSize_t = std::size_t;
constexpr DimSize_t MaxDimSize = std::numeric_limits<DimSize_t>::max();

///\brief Unsigned index for a Tensor's number of dimension.
using DimIdx_t = std::uint8_t;
constexpr DimIdx_t MaxDim = std::numeric_limits<DimIdx_t>::max();

//////////////////////////////////////
///          Operator/Nodes
//////////////////////////////////////

///\brief Signed integral type to hold an IO index.
///\details <0 values reserved
///\todo Change it for an unsigned value with default to numeric_limit and max to numeric_limit-1
using IOIndex_t = std::uint16_t;
/// @brief Default for absence of connection
constexpr IOIndex_t gk_IODefaultIndex = std::numeric_limits<IOIndex_t>::max();
constexpr IOIndex_t gk_IOMaxIndex = std::numeric_limits<IOIndex_t>::max() - 1;

// ///\brief Number of input/output connections for a Node/Operator
// using IOIndex_t = std::uint16_t;
// constexpr IOIndex_t gk_IOMaxNb = std::numeric_limits<IOIndex_t>::max();


} // namespace Aidge

#endif //AIDGE_TYPES_H_