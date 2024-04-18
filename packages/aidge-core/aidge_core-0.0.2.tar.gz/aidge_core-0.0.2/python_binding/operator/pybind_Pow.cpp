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
#include "aidge/operator/Pow.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Pow(py::module& m) {
    py::class_<Pow_Op, std::shared_ptr<Pow_Op>, OperatorTensor>(m, "PowOp", py::multiple_inheritance())
    .def("get_inputs_name", &Pow_Op::getInputsName)
    .def("get_outputs_name", &Pow_Op::getOutputsName);
    declare_registrable<Pow_Op>(m, "PowOp");

    m.def("Pow", &Pow, py::arg("name") = "");
}
}  // namespace Aidge
