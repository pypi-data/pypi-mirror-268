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
#include "aidge/operator/Slice.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Slice(py::module& m) {
    py::class_<Slice_Op, std::shared_ptr<Slice_Op>, OperatorTensor>(m, "SliceOp", py::multiple_inheritance())
    .def("get_inputs_name", &Slice_Op::getInputsName)
    .def("get_outputs_name", &Slice_Op::getOutputsName);
    declare_registrable<Slice_Op>(m, "SliceOp");
    m.def("Slice", &Slice, py::arg("starts"), py::arg("ends"), py::arg("axes"), py::arg("name") = "");
}
}  // namespace Aidge
