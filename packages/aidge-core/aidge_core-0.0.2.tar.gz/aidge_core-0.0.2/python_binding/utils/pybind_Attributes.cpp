#include <pybind11/pybind11.h>
#include "aidge/utils/Attributes.hpp"
#include "aidge/utils/DynamicAttributes.hpp"
#include "aidge/utils/StaticAttributes.hpp"

namespace py = pybind11;
namespace Aidge {
DynamicAttributes test_DynamicAttributes_binding() {
    DynamicAttributes attrs;
    attrs.addAttr<int>("a", 42);
    attrs.addAttr<std::string>("b", "test");
    attrs.addAttr<std::vector<bool>>("c", {true, false, true});
    return attrs;
}

double test_DynamicAttributes_binding_check(DynamicAttributes& attrs) {
    return attrs.getAttr<double>("d");
}

void init_Attributes(py::module& m){
    py::class_<Attributes, std::shared_ptr<Attributes>>(m, "Attributes")
    .def("has_attr", &Attributes::hasAttr, py::arg("name"))
    .def("get_attr_type", &Attributes::getAttrType, py::arg("name"))
    .def("get_attrs_name", &Attributes::getAttrsName)
    .def("get_attr", &Attributes::getAttrPy, py::arg("name"))
    .def("__getattr__", &Attributes::getAttrPy, py::arg("name"))
    .def("set_attr", &Attributes::setAttrPy, py::arg("name"), py::arg("value"))
    .def("__setattr__", &Attributes::setAttrPy, py::arg("name"), py::arg("value"));

    py::class_<DynamicAttributes, std::shared_ptr<DynamicAttributes>, Attributes>(m, "DynamicAttributes")
    .def("add_attr", &DynamicAttributes::addAttrPy, py::arg("name"), py::arg("value"))
    .def("del_attr", &DynamicAttributes::delAttr, py::arg("name"));

    m.def("test_DynamicAttributes_binding", &test_DynamicAttributes_binding);
    m.def("test_DynamicAttributes_binding_check", &test_DynamicAttributes_binding_check, py::arg("attrs"));
}

}

