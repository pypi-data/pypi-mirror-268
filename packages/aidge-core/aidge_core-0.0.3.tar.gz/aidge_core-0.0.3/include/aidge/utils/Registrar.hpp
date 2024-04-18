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

#ifndef AIDGE_CORE_UTILS_REGISTRAR_H_
#define AIDGE_CORE_UTILS_REGISTRAR_H_

#ifdef PYBIND
#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // declare_registrable key can recquire stl
#include <pybind11/functional.h>// declare_registrable allow binding of lambda fn

#endif

#include "aidge/utils/ErrorHandling.hpp"

#include <functional>
#include <map>
#include <vector>

namespace Aidge {
#ifdef PYBIND
namespace py = pybind11;
#endif

// Abstract class used to test if a class is Registrable.
class AbstractRegistrable {};

template <class DerivedClass, class Key, class Func> // curiously rucurring template pattern
class Registrable {
public:
    typedef Key registrar_key;
    typedef std::function<Func> registrar_type;

    static std::map<Key, std::function<Func>>& registry()
    {
        #ifdef PYBIND
        #define _CRT_SECURE_NO_WARNINGS
        if (Py_IsInitialized()){
            std::string name = std::string("registrar_")+typeid(Registrable<DerivedClass, Key, Func>).name();
            static auto shared_data = reinterpret_cast<std::map<Key, std::function<Func>> *>(py::get_shared_data(name));
            if (!shared_data)
                shared_data = static_cast<std::map<Key, std::function<Func>> *>(py::set_shared_data(name, new std::map<Key, std::function<Func>>()));
            return *shared_data;
        }
        #endif // PYBIND
        static std::map<Key, std::function<Func>> rMap;
        return rMap;
    }

};

template <class C>
struct Registrar {
    typedef typename C::registrar_key registrar_key;
    typedef typename C::registrar_type registrar_type;

    Registrar(const registrar_key& key, registrar_type func) {
        //fmt::print("REGISTRAR: {}\n", key);
        // bool newInsert;
        // std::tie(std::ignore, newInsert) = C::registry().insert(std::make_pair(key, func));
        C::registry().erase(key);
        C::registry().insert(std::make_pair(key, func));
        //assert(newInsert && "registrar already exists");
    }

    static bool exists(const registrar_key& key) {
        return (C::registry().find(key) != C::registry().cend());
    }

    static auto create(const registrar_key& key){
        const auto it = C::registry().find(key);
        AIDGE_ASSERT(it != C::registry().cend(), "missing or invalid registrar key: {}\nDid you include/import the corresponding module?", key);

        return (*it).second;
    }
    static std::vector<registrar_key> getKeys(){
        std::vector<registrar_key> keys;
        for(const auto& keyValue : C::registry())
            keys.push_back(keyValue.first);
        return keys;
    }
};

#ifdef PYBIND
/**
 * @brief Function to define register function for a registrable class
 * Defined here to have access to this function in every module who wants
 * to create a new registrable class.
 *
 * @tparam C registrable class
 * @param m pybind module
 * @param class_name python name of the class
 */
template <class C>
void declare_registrable(py::module& m, const std::string& class_name){
    typedef typename C::registrar_key registrar_key;
    typedef typename C::registrar_type registrar_type;
    m.def(("register_"+ class_name).c_str(), [](registrar_key& key, registrar_type function){
        Registrar<C>(key, function);
    })
    .def(("get_keys_"+ class_name).c_str(), [](){
        return Registrar<C>::getKeys();
    });
}
#endif

/*
* This macro allow to set an implementation to an operator
* This macro is mandatory for using implementation registered in python
* PyBind when calling create method will do a call to the copy ctor if
* op is not visible to the python world (if the create method return a python function)
* See this issue for more information https://github.com/pybind/pybind11/issues/4417
* Note: using a method to do this is not possible has any call to a function will call
* the cpy ctor. This is why I used a macro
* Note: I duplicated
*             (op).setImpl(Registrar<T_Op>::create(backend_name)(op)); \
* This is because the py::cast need to be done in the same scope.
* I know this only empyrically not sure what happens under the hood...
*
* If someone wants to find an alternative to this Macro, you can contact me:
*   cyril.moineau@cea.fr
*/
#ifdef PYBIND
#define SET_IMPL_MACRO(T_Op, op, backend_name) \
    if(Py_IsInitialized()) { \
        auto obj = py::cast(&(op)); \
        (op).setImpl(Registrar<T_Op>::create(backend_name)(op)); \
    } else { \
        (op).setImpl(Registrar<T_Op>::create(backend_name)(op)); \
    }
#else
#define SET_IMPL_MACRO(T_Op, op, backend_name)                   \
    (op).setImpl(Registrar<T_Op>::create(backend_name)(op));
#endif

}

#endif //AIDGE_CORE_UTILS_REGISTRAR_H_
