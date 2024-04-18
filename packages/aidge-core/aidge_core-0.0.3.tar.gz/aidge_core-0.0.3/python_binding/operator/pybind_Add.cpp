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

#include "aidge/operator/Add.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

void declare_Add(py::module &m) {
  py::class_<Add_Op, std::shared_ptr<Add_Op>, OperatorTensor>(m, "AddOp", py::multiple_inheritance())
  .def("get_inputs_name", &Add_Op::getInputsName)
  .def("get_outputs_name", &Add_Op::getOutputsName);
  declare_registrable<Add_Op>(m, "AddOp");
  m.def("Add", &Add, py::arg("nbIn"), py::arg("name") = "");
}

void init_Add(py::module &m) {
  declare_Add(m);
}
} // namespace Aidge
