
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

#include <memory>
#include <string>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {
void init_Operator(py::module& m){
    py::class_<Operator, std::shared_ptr<Operator>>(m, "Operator")
    .def("set_output", py::overload_cast<const IOIndex_t, const std::shared_ptr<Data>&>(&Operator::setOutput), py::arg("outputIdx"), py::arg("data"))
    .def("set_input", py::overload_cast<const IOIndex_t, const std::shared_ptr<Data>&>(&Operator::setInput), py::arg("inputIdx"), py::arg("data"))
    .def("get_raw_output", &Operator::getRawOutput, py::arg("outputIdx"))
    .def("set_input", py::overload_cast<const IOIndex_t, const std::shared_ptr<Data>&>(&Operator::setInput), py::arg("inputIdx"), py::arg("data"))
    .def("get_raw_input", &Operator::getRawInput, py::arg("inputIdx"))
    .def("nb_inputs", &Operator::nbInputs)
    .def("nb_data", &Operator::nbData)
    .def("nb_param", &Operator::nbParam)
    .def("nb_outputs", &Operator::nbOutputs)
    .def("associate_input", &Operator::associateInput, py::arg("inputIdx"), py::arg("data"))
    .def("set_datatype", &Operator::setDataType, py::arg("dataType"))
    .def("set_backend", &Operator::setBackend, py::arg("name"), py::arg("device") = 0)
    .def("forward", &Operator::forward)
    // py::keep_alive forbide Python to garbage collect the implementation lambda as long as the Operator is not deleted !
    .def("set_impl", &Operator::setImpl, py::arg("implementation"), py::keep_alive<1, 2>())
    .def("get_impl", &Operator::getImpl)
    .def("get_hook", &Operator::getHook)
    .def("add_hook", &Operator::addHook)
    ;
}
}
