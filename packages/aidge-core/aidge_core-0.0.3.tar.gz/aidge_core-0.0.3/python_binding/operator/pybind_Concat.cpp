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
#include "aidge/operator/Concat.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Concat(py::module& m) {
    py::class_<Concat_Op, std::shared_ptr<Concat_Op>, Attributes, OperatorTensor>(m, "ConcatOp", py::multiple_inheritance())
    .def("get_inputs_name", &Concat_Op::getInputsName)
    .def("get_outputs_name", &Concat_Op::getOutputsName)
    .def("attributes_name", &Concat_Op::staticGetAttrsName);

    declare_registrable<Concat_Op>(m, "ConcatOp");
    m.def("Concat", &Concat, py::arg("nbIn"), py::arg("axis"), py::arg("name") = "");
}
}  // namespace Aidge
