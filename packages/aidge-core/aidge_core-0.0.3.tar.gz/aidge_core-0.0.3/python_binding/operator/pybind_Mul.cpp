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
#include "aidge/operator/Mul.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Mul(py::module& m) {
    py::class_<Mul_Op, std::shared_ptr<Mul_Op>, OperatorTensor>(m, "MulOp", py::multiple_inheritance())
    .def("get_inputs_name", &Mul_Op::getInputsName)
    .def("get_outputs_name", &Mul_Op::getOutputsName);
    declare_registrable<Mul_Op>(m, "MulOp");
    m.def("Mul", &Mul, py::arg("name") = "");
}
}  // namespace Aidge
