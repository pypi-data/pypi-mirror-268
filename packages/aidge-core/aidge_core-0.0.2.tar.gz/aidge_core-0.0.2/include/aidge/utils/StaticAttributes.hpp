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

#ifndef AIDGE_CORE_UTILS_STATICATTRIBUTES_H_
#define AIDGE_CORE_UTILS_STATICATTRIBUTES_H_

#include <tuple>
#include <cassert>
#include <cstddef>
#include <typeinfo>
#include <array>

#include "aidge/utils/Attributes.hpp"
#include "aidge/utils/ErrorHandling.hpp"

namespace Aidge {
/**
 * @brief This class is designed to handle static attributes (i.e. known at compile-time)
 * with named accessors, with minimal overhead (the name strings are not stored in each object
 * instance and it remains possible to access attribute without overhead at compile-time).
*/
template <class ATTRS_ENUM, class ...T>
class StaticAttributes : public Attributes {
public:
    using Attrs = std::tuple<T...>;

    // Helper class to pass to the constructor
    template <ATTRS_ENUM attrsEnum>
    class attr {
    public:
        constexpr attr(const typename std::tuple_element<static_cast<std::size_t>(attrsEnum),std::tuple<T...>>::type& v) : value(v) {}
        const typename std::tuple_element<static_cast<std::size_t>(attrsEnum),std::tuple<T...>>::type value;
    };

/*
    // Direct tuple initialization
    StaticAttributes(T... attrs) : mAttrs({attrs...}) {

    }
*/

    // Constructor for Attributes initialization.
    // Compile-time garantee that every attribute is initialized.
    template <ATTRS_ENUM ...attrsEnum> // non-type attribute pack
    constexpr StaticAttributes(const attr<attrsEnum>&&... attrs) {
        // Check number of attrs consistency
        static_assert(sizeof...(attrs) == std::tuple_size<std::tuple<T...>>::value, "wrong number of attributes in constructor");
        // static_assert(size(EnumStrings<ATTRS_ENUM>::data) == std::tuple_size<std::tuple<T...>>::value, "wrong number of attributes in enum string");

        // Check no duplicates
        constexpr std::array<ATTRS_ENUM, std::tuple_size<std::tuple<T...>>::value> pe = { attrsEnum... };
        static_assert(!hasDuplicates(pe), "duplicate attribute"); // requires C++14

        // Init attrs with constructor arguments
        const std::array<ATTRS_ENUM, std::tuple_size<std::tuple<T...>>::value> p = { ((void)(getAttr<attrsEnum>() = attrs.value), attrsEnum) ... };
        (void)p; // avoid unused warning
    }

    // Compile-time access with enum
    template <ATTRS_ENUM attrsEnum>
    constexpr typename std::tuple_element<static_cast<std::size_t>(attrsEnum),std::tuple<T...>>::type& getAttr() {
        return std::get<static_cast<std::size_t>(attrsEnum)>(mAttrs);
    }

    template <ATTRS_ENUM attrsEnum>
    constexpr const typename std::tuple_element<static_cast<std::size_t>(attrsEnum),std::tuple<T...>>::type& getAttr() const {
        return std::get<static_cast<std::size_t>(attrsEnum)>(mAttrs);
    }

    // Runtime access with enum
    template <typename R>
    constexpr R& getAttr(ATTRS_ENUM attrsEnum) {
        return getAttr<R>(static_cast<std::size_t>(attrsEnum));
    }

    template <typename R>
    constexpr const R& getAttr(ATTRS_ENUM attrsEnum) const {
        return getAttr<R>(static_cast<std::size_t>(attrsEnum));
    }

    // Runtime access with name
    template <typename R>
    R& getAttr(const std::string& name) {
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                return getAttr<R>(i);
            }
        }

        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute \"{}\" not found", name);
    }

    template <typename R>
    const R& getAttr(const std::string& name) const {
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                return getAttr<R>(i);
            }
        }

        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute \"{}\" not found", name);
    }

    template <typename R, std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    typename std::enable_if<(SIZE > 0), R&>::type getAttr(std::size_t i) {
        if (i == SIZE-1) {
            if (std::is_same<R, typename std::tuple_element<SIZE-1,std::tuple<T...>>::type>::value) {
                return reinterpret_cast<R&>(std::get<SIZE-1>(mAttrs));
            }
            else {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "wrong type for attribute with index {}", i);
            }
        }
        else {
            return getAttr<R, SIZE-1>(i);
        }
    }

    template <typename R, std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    [[noreturn]] typename std::enable_if<(SIZE == 0), R&>::type getAttr(std::size_t /*i*/) {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute not found");
    }

    template <typename R, std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    typename std::enable_if<(SIZE > 0), const R&>::type getAttr(std::size_t i) const {
        if (i == SIZE-1) {
            if (std::is_same<R, typename std::tuple_element<SIZE-1,std::tuple<T...>>::type>::value) {
                return reinterpret_cast<const R&>(std::get<SIZE-1>(mAttrs));
            }
            else {
                AIDGE_THROW_OR_ABORT(std::runtime_error, "wrong type for attribute with index {}", i);
            }
        }
        else {
            return getAttr<R, SIZE-1>(i);
        }
    }

    template <typename R, std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    [[noreturn]] typename std::enable_if<(SIZE == 0), const R&>::type getAttr(std::size_t /*i*/) const {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute not found");
    }

    template <std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    constexpr typename std::enable_if<(SIZE > 0), const std::type_info&>::type getAttrType(std::size_t i) const {
        if (i == SIZE-1) {
            return typeid(typename std::tuple_element<SIZE-1,std::tuple<T...>>::type);
        }
        else {
            return getAttrType<SIZE-1>(i);
        }
    }

    template <std::size_t SIZE = std::tuple_size<std::tuple<T...>>::value>
    [[noreturn]] typename std::enable_if<(SIZE == 0), const std::type_info&>::type getAttrType(std::size_t /*i*/) const {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute not found");
    }

    constexpr const std::tuple<T...>& getStaticAttributes() const {
        return mAttrs;
    }

    //////////////////////////////////////
    ///     Generic Attributes API
    //////////////////////////////////////
    // Runtime existance check with name
    bool hasAttr(const std::string& name) const override final {
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                return true;
            }
        }

        return false;
    }

    // Runtime type access with name
    std::string getAttrType(const std::string& name) const override final {
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                return getAttrType(i).name();
            }
        }

        AIDGE_THROW_OR_ABORT(std::runtime_error, "attribute \"{}\" not found", name);
    }

    std::set<std::string> getAttrsName() const override final {
        std::set<std::string> attrsName;
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            attrsName.insert(EnumStrings<ATTRS_ENUM>::data[i]);
        }
        return attrsName;
    }

    #ifdef PYBIND
    /**
     * @brief Return a set of attributes defined.
     * This method is used to automatically retrieve attributes in the documentation.
     * This method is a duplicate of ``getAttrsName`` but static.
     *
     * @return std::set<std::string>
     */
    static std::set<std::string> staticGetAttrsName() {
        std::set<std::string> attrsName;
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            attrsName.insert(EnumStrings<ATTRS_ENUM>::data[i]);
        }
        return attrsName;
    }


    py::object getAttrPy(const std::string& name) const override {
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                // https://github.com/pybind/pybind11/blob/f3e0602802c7840992c97f4960515777cad6a5c7/include/pybind11/pytypes.h#L1119-L1138
                // Normal accessor would not work has we convert the tuple to a py::object which can be anything
                return py::detail::accessor_policies::tuple_item::get(py::cast(mAttrs), static_cast<py::size_t>(i));
            }
        }

        AIDGE_THROW_OR_ABORT(py::value_error, "attribute \"{}\" not found", name);
    }


    void setAttrPy(const std::string& name, py::object&& value) override final{
        for (std::size_t i = 0; i < size(EnumStrings<ATTRS_ENUM>::data); ++i) {
            if (name == EnumStrings<ATTRS_ENUM>::data[i]) {
                // Cannot update attribute using reference has it would require templating
                // Use a dirty
                auto tmpAttr = py::cast(mAttrs);
                py::detail::accessor_policies::tuple_item::set(tmpAttr, static_cast<py::size_t>(i), value);
                mAttrs = py::cast<std::tuple<T...>>(tmpAttr);
                return;
            }
        }
        AIDGE_THROW_OR_ABORT(py::value_error, "attribute \"{}\" not found", name);
    }
    #endif

private:
    template <typename V, std::size_t N>
    static constexpr bool hasDuplicates(const std::array<V, N>& array) {
        for (std::size_t i = 1; i < N; i++) {
            for (std::size_t j = 0; j < i; j++) {
                if (array[i] == array[j]) {
                    return true;
                }
            }
        }

        return false;
    }

    std::tuple<T...> mAttrs;
};
}

#endif /* AIDGE_CORE_UTILS_STATICATTRIBUTES_H_ */
