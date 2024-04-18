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
#include "aidge/operator/Sub.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Sub(py::module& m) {
    py::class_<Sub_Op, std::shared_ptr<Sub_Op>, OperatorTensor>(m, "SubOp", py::multiple_inheritance())
    .def("get_inputs_name", &Sub_Op::getInputsName)
    .def("get_outputs_name", &Sub_Op::getOutputsName);
    declare_registrable<Sub_Op>(m, "SubOp");
    m.def("Sub", &Sub, py::arg("name") = "");
}
}  // namespace Aidge
