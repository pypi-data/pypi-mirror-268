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
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Softmax.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Softmax(py::module& m) {
    py::class_<Softmax_Op, std::shared_ptr<Softmax_Op>, Attributes, OperatorTensor>(m, "SoftmaxOp", py::multiple_inheritance())
    .def("get_inputs_name", &Softmax_Op::getInputsName)
    .def("get_outputs_name", &Softmax_Op::getOutputsName)
    .def("attributes_name", &Softmax_Op::staticGetAttrsName);
    declare_registrable<Softmax_Op>(m, "SoftmaxOp");
    m.def("Softmax", &Softmax, py::arg("axis"), py::arg("name") = "");
}
}  // namespace Aidge
