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
#include "aidge/operator/ReLU.hpp"
#include "aidge/operator/OperatorTensor.hpp"

namespace py = pybind11;
namespace Aidge {

void init_ReLU(py::module& m) {
    py::class_<ReLU_Op, std::shared_ptr<ReLU_Op>, OperatorTensor>(m, "ReLUOp", py::multiple_inheritance())
    .def("get_inputs_name", &ReLU_Op::getInputsName)
    .def("get_outputs_name", &ReLU_Op::getOutputsName);
    declare_registrable<ReLU_Op>(m, "ReLUOp");

    m.def("ReLU", &ReLU, py::arg("name") = "");
}
}  // namespace Aidge
