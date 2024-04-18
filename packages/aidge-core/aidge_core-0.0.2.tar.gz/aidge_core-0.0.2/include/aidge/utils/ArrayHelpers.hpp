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

#ifndef AIDGE_CORE_UTILS_ARRAYHELPERS_H_
#define AIDGE_CORE_UTILS_ARRAYHELPERS_H_

#include <array>

namespace Aidge {

// Helper to create default arrays
template <typename T, std::size_t ... Is>
constexpr std::array<T, sizeof...(Is)>
create_array_impl(T value, std::index_sequence<Is...>)
{
    // cast Is to void to remove the warning: unused value
    return {{(static_cast<void>(Is), value)...}};
}

template <typename T, std::size_t N>
constexpr std::array<T, N> create_array(const T& value)
{
    return create_array_impl(value, std::make_index_sequence<N>());
}


// Helper to convert vector to array
template <typename T, typename Iter, std::size_t... Is>
constexpr auto to_array(Iter &iter, std::index_sequence<Is...>) -> std::array<T, sizeof...(Is)> {
    return {{((void)Is, T(*iter++))...}};
}

/**
 * @brief Convert an object with an iterator to an std::array.
 */
template <std::size_t N, typename U = void, typename Iter, typename V = typename std::iterator_traits<Iter>::value_type,
          typename T = std::conditional_t<std::is_same<U, void>{}, V, U>>
constexpr auto to_array(Iter iter) -> std::array<T, N> {
    return to_array<T>(iter, std::make_index_sequence<N>{});
}

namespace detail {

template <class T, std::size_t N, std::size_t... I>
constexpr std::array<std::remove_cv_t<T>, N> to_array_impl(T (&a)[N], std::index_sequence<I...>) {
    return {{a[I]...}};
}

}  // namespace detail

/**
 * @brief Convert a C-stype array into a C++ std::array.
 *
 * @tparam T Data type.
 * @tparam N Number of elements.
 * @param a C-style array to convert.
 * @return constexpr std::array<std::remove_cv_t<T>, N>
 */
template <class T, std::size_t N>
constexpr std::array<std::remove_cv_t<T>, N> to_array(T (&a)[N]) {
    return detail::to_array_impl(a, std::make_index_sequence<N>{});
}

template <typename T, std::size_t N, std::size_t... I>
constexpr std::array<T, N + 1> append(std::array<T, N> a, T t, std::index_sequence<I...>) {
    return std::array<T, N + 1>{a[I]..., t};
}

template <typename T, std::size_t N, std::size_t... I>
constexpr std::array<T, N + 1> append(T t, std::array<T, N> a, std::index_sequence<I...>) {
    return std::array<T, N + 1>{t, a[I]...};
}

/**
 * @brief Create a new array concatenating the initial one with the value to
 * add.
 * @details append({1,2,7}, 3) -> {1,2,7,3}
 *
 * @tparam T Data type.
 * @tparam N Number of elements in the initilial array.
 * @param a Initial array.
 * @param t Element to add.
 * @return constexpr std::array<T, N + 1>
 */
template <typename T, std::size_t N>
constexpr std::array<T, N + 1> append(std::array<T, N> a, T t) {
    return append(a, t, std::make_index_sequence<N>());
}

template <typename T, std::size_t N>
constexpr std::array<T, N + 1> append(T t, std::array<T, N> a) {
    return append(t, a, std::make_index_sequence<N>());
}

// Generic helper for initializing a Tensor
template <typename T, std::size_t SIZE_0>
struct Array1D {
    T data[SIZE_0];
};

template <typename T, std::size_t SIZE_0, std::size_t SIZE_1>
struct Array2D {
    T data[SIZE_0][SIZE_1];
};

template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2>
struct Array3D {
    T data[SIZE_0][SIZE_1][SIZE_2];
};

template <typename T, std::size_t SIZE_0, std::size_t SIZE_1, std::size_t SIZE_2, std::size_t SIZE_3>
struct Array4D {
    T data[SIZE_0][SIZE_1][SIZE_2][SIZE_3];
};
}

#endif /* AIDGE_CORE_UTILS_ARRAYHELPERS_H_ */
