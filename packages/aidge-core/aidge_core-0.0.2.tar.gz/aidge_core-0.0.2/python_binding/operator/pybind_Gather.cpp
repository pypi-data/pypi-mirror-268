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
#include "aidge/operator/Gather.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Gather(py::module& m) {
    py::class_<Gather_Op, std::shared_ptr<Gather_Op>, Attributes, OperatorTensor>(m, "GatherOp", py::multiple_inheritance())
    .def("get_inputs_name", &Gather_Op::getInputsName)
    .def("get_outputs_name", &Gather_Op::getOutputsName)
    .def("attributes_name", &Gather_Op::staticGetAttrsName);
    declare_registrable<Gather_Op>(m, "GatherOp");
    m.def("Gather", &Gather, py::arg("indices"), py::arg("gathered_shape"), py::arg("axis")= 0, py::arg("name") = "");
}
}  // namespace Aidge
