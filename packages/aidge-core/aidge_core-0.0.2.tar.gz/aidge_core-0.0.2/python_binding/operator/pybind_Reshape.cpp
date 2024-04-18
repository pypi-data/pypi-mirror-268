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

#include <pybind11/pybind11.h>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Reshape.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Reshape(py::module& m) {
    py::class_<Reshape_Op, std::shared_ptr<Reshape_Op>, Attributes, OperatorTensor>(m, "ReshapeOp", py::multiple_inheritance())
    .def("get_inputs_name", &Reshape_Op::getInputsName)
    .def("get_outputs_name", &Reshape_Op::getOutputsName);
    declare_registrable<Reshape_Op>(m, "ReshapeOp");
    m.def("Reshape", &Reshape, py::arg("shape"), py::arg("name") = "");
}
}  // namespace Aidge
