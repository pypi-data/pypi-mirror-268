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

#include "aidge/operator/GlobalAveragePooling.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Attributes.hpp"

namespace py = pybind11;
namespace Aidge {

const std::string pyClassName("GlobalAveragePoolingOp");
void init_GlobalAveragePooling(py::module &m) {
  py::class_<GlobalAveragePooling_Op, std::shared_ptr<GlobalAveragePooling_Op>,
             OperatorTensor>(m, pyClassName.c_str(),
                             py::multiple_inheritance())
      .def("get_inputs_name", &GlobalAveragePooling_Op::getInputsName)
      .def("get_outputs_name", &GlobalAveragePooling_Op::getOutputsName);
  declare_registrable<GlobalAveragePooling_Op>(m, pyClassName);
  m.def("globalaveragepooling", &GlobalAveragePooling, py::arg("name") = "");
}
} // namespace Aidge
