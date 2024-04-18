/********************************************************************************
 * Copyright (c) 2024 CEA-List
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 ********************************************************************************/

#include <pybind11/pybind11.h>
#include <string>

#include "aidge/operator/Hardmax.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Attributes.hpp"
#include "aidge/utils/Attributes.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Hardmax(py::module& m) {
    py::class_<Hardmax_Op, std::shared_ptr<Hardmax_Op>, OperatorTensor, Attributes>(m, "HarmaxOp", py::multiple_inheritance())
    // Here we bind the methods of the Hardmax_Op that wil want to access
    .def("get_inputs_name", &Hardmax_Op::getInputsName)
    .def("get_outputs_name", &Hardmax_Op::getOutputsName);
    // Here we bind the constructor of the Hardmax Node. We add an argument for each attribute of the operator (in here we only have 'axis') and the last argument is the node's name.
    m.def("Hardmax", &Hardmax, py::arg("axis"), py::arg("name") = "");
}
}  // namespace Aidge