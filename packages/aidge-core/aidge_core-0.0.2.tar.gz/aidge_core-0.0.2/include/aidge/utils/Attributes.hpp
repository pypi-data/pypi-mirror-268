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

#ifndef AIDGE_CORE_UTILS_ATTRIBUTES_H_
#define AIDGE_CORE_UTILS_ATTRIBUTES_H_

#ifdef PYBIND
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#endif
#include <vector>
#include <string>
#include <set>

#ifdef PYBIND
namespace py = pybind11;
#endif

namespace {
// This is the type that will hold all the strings. Each enumerate type will
// declare its own specialization.
template <typename T> struct EnumStrings {
    static const char* const data[];
};
}

namespace Aidge {
template<class T, std::size_t N>
constexpr std::size_t size(T (&)[N]) { return N; }

/* This abstract class allows to avoid binding Attributes.
*  Otherwise we would need to bind every template possible of Attributes.
*  Every operators can access the methods of this class by inheriting from
*  Attributes in the binding code.
*/
class Attributes {
public:
    /**
     * @brief Check if the attribute exists.
     * @param name Name of the attribute to check.
     * @return bool True if the attribute exists, false otherwise.
    */
    virtual bool hasAttr(const std::string& name) const = 0;

    /**
     * @brief Get the (implementation defined) name of the type of an attribute, returned by std::type_info::name.
     * @param name Name of the attribute.
     * @return std::string Name of the type as returned by std::type_info::name.
    */
    virtual std::string getAttrType(const std::string& name) const = 0;

    /**
     * @brief Get the attribute's name list.
     * @return std::set<std::string> Vector of names of the attributes.
    */
    virtual std::set<std::string> getAttrsName() const = 0;

#ifdef PYBIND
    /* Bindable get function, does not recquire any templating.
    *  This is thanks to py::object which allow the function to
    *  be agnostic from its return type.
    */
    virtual py::object getAttrPy(const std::string& name) const = 0;
    /* Bindable set function, does not recquire any templating.
    *  This is thanks to py::object which allow the function to
    *  be agnostic from ``value`` type.
    */
    virtual void setAttrPy(const std::string& name, py::object&& value) = 0;
#endif
    virtual ~Attributes() {}
};
}

#endif /* AIDGE_CORE_UTILS_ATTRIBUTES_H_ */
