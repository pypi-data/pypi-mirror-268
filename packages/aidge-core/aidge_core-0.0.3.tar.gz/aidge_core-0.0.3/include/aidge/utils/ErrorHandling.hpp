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


#ifndef AIDGE_ERRORHANDLING_H_
#define AIDGE_ERRORHANDLING_H_

#include <memory>
#include <cassert>

#include <fmt/format.h>
#include <fmt/ranges.h>

#include "aidge/utils/Log.hpp"

#ifdef NO_EXCEPTION
#define AIDGE_THROW_OR_ABORT(ex, ...) \
do { Aidge::Log::fatal(__VA_ARGS__); std::abort(); } while (false)
#else
#include <stdexcept>
#define AIDGE_THROW_OR_ABORT(ex, ...) \
do { Aidge::Log::fatal(__VA_ARGS__); throw ex(fmt::format(__VA_ARGS__)); } while (false)
#endif

/**
 * Macro for specified API assertions.
 * Used to check logic directly related to user's inputs.
 * If it asserts, it means an user error.
*/
#define AIDGE_ASSERT(stm, ...) \
if (!(stm)) { Aidge::Log::error("Assertion failed: " #stm " in {}:{}", __FILE__, __LINE__); \
    AIDGE_THROW_OR_ABORT(std::runtime_error, __VA_ARGS__); }

/**
 * Macro for internal assertions.
 * Used to check internal logic not directly related to API user's inputs.
 * If it asserts, it means a bug.
*/
#define AIDGE_INTERNAL_ASSERT(stm) \
assert((stm) && "Internal assertion failed")

#endif //AIDGE_ERRORHANDLING_H_
