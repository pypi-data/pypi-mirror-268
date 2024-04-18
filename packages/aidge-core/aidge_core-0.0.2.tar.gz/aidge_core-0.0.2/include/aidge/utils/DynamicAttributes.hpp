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

#ifndef AIDGE_CORE_UTILS_DYNAMICATTRIBUTES_H_
#define AIDGE_CORE_UTILS_DYNAMICATTRIBUTES_H_

#include <map>
#include <vector>
#include <type_traits>
#include <typeinfo>
#include <cassert>
#include <string>

#include "aidge/utils/future_std/any.hpp"
#include "aidge/utils/Attributes.hpp"

#ifdef PYBIND
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/embed.h>

namespace py = pybind11;
#endif


namespace Aidge {

///\todo store also a fix-sized code that indicates the type
///\todo managing complex types or excluding non-trivial, non-aggregate types
class DynamicAttributes : public Attributes {
public:
    /**
     * \brief Returning an Attribute identified by its name
     * \tparam T expected Attribute type
     * \param name Attribute name
     * \details assert if T is not the actual Attribute type or if the Attribute does not
     *  exist
     * \note at() throws if the Attribute does not exist, using find to test for Attribute existance
     */
    template<class T> T& getAttr(const std::string& name)
    {
#ifdef PYBIND
        // If attribute does not exist in C++, it might have been created or modified in Python
        auto it = mAttrs.find(name);
        if (it == mAttrs.end()) {
            auto itPy = mAttrsPy.find(name);
            if (itPy != mAttrsPy.end()) {
                // Insert the attribute back in C++
                mAttrs.emplace(std::make_pair(name, future_std::any(itPy->second.cast<T>())));
            }
        }
#endif

        return future_std::any_cast<T&>(mAttrs.at(name));
    }

    template<class T> const T& getAttr(const std::string& name) const
    {
#ifdef PYBIND
        // If attribute does not exist in C++, it might have been created or modified in Python
        auto it = mAttrs.find(name);
        if (it == mAttrs.end()) {
            auto itPy = mAttrsPy.find(name);
            if (itPy != mAttrsPy.end()) {
                // Insert the attribute back in C++
                mAttrs.emplace(std::make_pair(name, future_std::any(itPy->second.cast<T>())));
            }
        }
#endif

        return future_std::any_cast<const T&>(mAttrs.at(name));
    }

    ///\brief Add a new Attribute, identified by its name. If it already exists, asserts.
    ///\tparam T expected Attribute type
    ///\param name Attribute name
    ///\param value Attribute value
    template<class T> void addAttr(const std::string& name, const T& value)
    {
        const auto& res = mAttrs.emplace(std::make_pair(name, future_std::any(value)));
        assert(res.second && "attribute already exists");

#ifdef PYBIND
        // We cannot handle Python object if the Python interpreter is not running
        if (Py_IsInitialized()) {
            // Keep a copy of the attribute in py::object that is updated everytime
            mAttrsPy.emplace(std::make_pair(name, py::cast(value)));
        }
#endif
    }

    ///\brief Set an Attribute value, identified by its name. If it already exists, its value (and type, if different) is changed.
    ///\tparam T expected Attribute type
    ///\param name Attribute name
    ///\param value Attribute value
    template<class T> void setAttr(const std::string& name, const T& value)
    {
        auto res = mAttrs.emplace(std::make_pair(name, future_std::any(value)));
        if (!res.second)
            res.first->second = future_std::any(value);

#ifdef PYBIND
        // We cannot handle Python object if the Python interpreter is not running
        if (Py_IsInitialized()) {
            // Keep a copy of the attribute in py::object that is updated everytime
            auto resPy = mAttrsPy.emplace(std::make_pair(name, py::cast(value)));
            if (!resPy.second)
                resPy.first->second = std::move(py::cast(value));
        }
#endif
    }

    void delAttr(const std::string& name) {
        mAttrs.erase(name);
#ifdef PYBIND
        mAttrsPy.erase(name);
#endif
    }

#ifdef PYBIND
    void addAttrPy(const std::string& name, py::object&& value)
    {
        auto it = mAttrs.find(name);
        assert(it == mAttrs.end() && "attribute already exists");

        const auto& res = mAttrsPy.emplace(std::make_pair(name, value));
        assert(res.second && "attribute already exists");
    }

    void setAttrPy(const std::string& name, py::object&& value) override final
    {
        auto resPy = mAttrsPy.emplace(std::make_pair(name, value));
        if (!resPy.second)
            resPy.first->second = std::move(value);

        // Force getAttr() to take attribute value from mAttrsPy and update mAttrs
        mAttrs.erase(name);
    }
#endif

    //////////////////////////////////////
    ///     Generic Attributes API
    //////////////////////////////////////
    bool hasAttr(const std::string& name) const override final {
#ifdef PYBIND
        // Attributes might have been created in Python, the second condition is necessary.
        return (mAttrs.find(name) != mAttrs.end() || mAttrsPy.find(name) != mAttrsPy.end());
#else
        return (mAttrs.find(name) != mAttrs.end());
#endif
    }

    std::string getAttrType(const std::string& name) const override final {
        // In order to remain consistent between C++ and Python, with or without PyBind, the name of the type is:
        // - C-style for C++ created attributes
        // - Python-style for Python created attributes
#ifdef PYBIND
        // If attribute does not exist in C++, it might have been created in Python
        auto it = mAttrs.find(name);
        if (it == mAttrs.end()) {
            auto itPy = mAttrsPy.find(name);
            if (itPy != mAttrsPy.end()) {
                return std::string(Py_TYPE(itPy->second.ptr())->tp_name);
            }
        }
#endif

        return mAttrs.at(name).type().name();
    }

    std::set<std::string> getAttrsName() const override final {
        std::set<std::string> attrsName;
        for(auto const& it: mAttrs)
            attrsName.insert(it.first);
#ifdef PYBIND
        // Attributes might have been created in Python
        for(auto const& it: mAttrsPy)
            attrsName.insert(it.first);
#endif
        return attrsName;
    }

#ifdef PYBIND
    /**
     * @detail See https://github.com/pybind/pybind11/issues/1590 as to why a
     * generic type caster for std::any is not feasable.
     * The strategy here is to keep a copy of each attribute in py::object that is updated everytime.
    */
    py::object getAttrPy(const std::string& name) const override final {
        return mAttrsPy.at(name);
    };
#endif

private:
#ifdef PYBIND
    // Stores C++ attributes (copy) and Python-only attributes
    // Code should be compiled with -fvisibility=hidden
    // See https://pybind11.readthedocs.io/en/stable/faq.html:
    // “‘SomeClass’ declared with greater visibility than the type of its
    // field ‘SomeClass::member’ [-Wattributes]”
    // This map will only be populated if Python interpreter is running
    std::map<std::string, py::object> mAttrsPy;
    // Stores C++ attributes only
    // mutable because it may be updated in getAttr() from Python
    mutable std::map<std::string, future_std::any> mAttrs;
#else
    std::map<std::string, future_std::any> mAttrs;
#endif
};

}

#endif /* AIDGE_CORE_UTILS_DYNAMICATTRIBUTES_H_ */
