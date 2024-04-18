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
#include "aidge/operator/LeakyReLU.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_LeakyReLU(py::module& m) {
    py::class_<LeakyReLU_Op, std::shared_ptr<LeakyReLU_Op>, Attributes, OperatorTensor>(m, "LeakyReLUOp", py::multiple_inheritance())
    .def("get_inputs_name", &LeakyReLU_Op::getInputsName)
    .def("get_outputs_name", &LeakyReLU_Op::getOutputsName)
    .def("attributes_name", &LeakyReLU_Op::staticGetAttrsName);
    declare_registrable<LeakyReLU_Op>(m, "LeakyReLUOp");
    m.def("LeakyReLU", &LeakyReLU, py::arg("negative_slope") = 0.0f, py::arg("name") = "");
}
}  // namespace Aidge
