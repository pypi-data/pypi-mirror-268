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
#include <pybind11/stl.h>

#include <string>
#include <vector>
#include <array>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Transpose.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM>
void declare_Transpose(py::module &m) {
  const std::string pyClassName("TransposeOp" + std::to_string(DIM) + "D");
  py::class_<Transpose_Op<DIM>, std::shared_ptr<Transpose_Op<DIM>>, Attributes, OperatorTensor>(
    m, ("TransposeOp" + std::to_string(DIM) + "D").c_str(), py::multiple_inheritance())
  .def("get_inputs_name", &Transpose_Op<DIM>::getInputsName)
  .def("get_outputs_name", &Transpose_Op<DIM>::getOutputsName)
  .def("attributes_name", &Transpose_Op<DIM>::staticGetAttrsName);

  declare_registrable<Transpose_Op<DIM>>(m, pyClassName);

  m.def(("Transpose" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& output_dims_order,
                                                                  const std::string& name) {
        AIDGE_ASSERT(output_dims_order.size() == DIM, "output_dims_order size [{}] does not match DIM [{}]", output_dims_order.size(), DIM);
        return Transpose<DIM>(to_array<DIM>(output_dims_order.begin()), name);
    }, py::arg("output_dims_order"),
       py::arg("name") = "");

}

void init_Transpose(py::module &m) {
  declare_Transpose<2>(m);
  declare_Transpose<3>(m);
  declare_Transpose<4>(m);
  declare_Transpose<5>(m);
  declare_Transpose<6>(m);

}
} // namespace Aidge
