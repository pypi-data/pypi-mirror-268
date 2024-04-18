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
#include "aidge/operator/MatMul.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

void init_MatMul(py::module &m) {
  py::class_<MatMul_Op, std::shared_ptr<MatMul_Op>, OperatorTensor>(m, "MatMulOp", py::multiple_inheritance())
  .def("get_inputs_name", &MatMul_Op::getInputsName)
  .def("get_outputs_name", &MatMul_Op::getOutputsName);
  declare_registrable<MatMul_Op>(m, "MatMulOp");
  m.def("MatMul", &MatMul, py::arg("name") = "");
}
} // namespace Aidge
