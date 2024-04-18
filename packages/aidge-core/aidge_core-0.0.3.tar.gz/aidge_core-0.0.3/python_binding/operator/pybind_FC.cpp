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

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/FC.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

void declare_FC(py::module &m) {
  py::class_<FC_Op, std::shared_ptr<FC_Op>, Attributes, OperatorTensor>(m, "FCOp", py::multiple_inheritance())
  .def("get_inputs_name", &FC_Op::getInputsName)
  .def("get_outputs_name", &FC_Op::getOutputsName)
  .def("attributes_name", &FC_Op::staticGetAttrsName);
  declare_registrable<FC_Op>(m, "FCOp");
  m.def("FC", &FC, py::arg("in_channels"), py::arg("out_channels"), py::arg("nobias") = false, py::arg("name") = "");
}

void init_FC(py::module &m) {
  declare_FC(m);
}
} // namespace Aidge
