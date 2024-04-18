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
#include "aidge/operator/MaxPooling.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_MaxPoolingOp(py::module &m) {
  const std::string pyClassName("MaxPoolingOp" + std::to_string(DIM) + "D");
  py::class_<MaxPooling_Op<DIM>, std::shared_ptr<MaxPooling_Op<DIM>>, Attributes, OperatorTensor>(
    m, ("MaxPoolingOp" + std::to_string(DIM) + "D").c_str(),
    py::multiple_inheritance())
  .def(py::init<const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &,
                bool>(),
        py::arg("kernel_dims"),
        py::arg("stride_dims"),
        py::arg("ceil_mode"))
  .def("get_inputs_name", &MaxPooling_Op<DIM>::getInputsName)
  .def("get_outputs_name", &MaxPooling_Op<DIM>::getOutputsName)
  .def("attributes_name", &MaxPooling_Op<DIM>::staticGetAttrsName);
  declare_registrable<MaxPooling_Op<DIM>>(m, pyClassName);
  m.def(("MaxPooling" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& kernel_dims,
                                                                  const std::string& name,
                                                                  const std::vector<DimSize_t> &stride_dims,
                                                                  bool ceil_mode) {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);

        return MaxPooling<DIM>(to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), ceil_mode);
    }, py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("ceil_mode") = false);

}


void init_MaxPooling(py::module &m) {
  declare_MaxPoolingOp<1>(m);
  declare_MaxPoolingOp<2>(m);
  declare_MaxPoolingOp<3>(m);

}
} // namespace Aidge
