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

#include <array>
#include <string>
#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/AvgPooling.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_AvgPoolingOp(py::module &m) {
  const std::string pyClassName("AvgPoolingOp" + std::to_string(DIM) + "D");
  py::class_<AvgPooling_Op<DIM>, std::shared_ptr<AvgPooling_Op<DIM>>, Attributes, OperatorTensor>(
    m, pyClassName.c_str(),
    py::multiple_inheritance())
  .def(py::init<const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &>(),
        py::arg("kernel_dims"),
        py::arg("stride_dims"))
  .def("get_inputs_name", &AvgPooling_Op<DIM>::getInputsName)
  .def("get_outputs_name", &AvgPooling_Op<DIM>::getOutputsName)
  .def("attributes_name", &AvgPooling_Op<DIM>::staticGetAttrsName);
  declare_registrable<AvgPooling_Op<DIM>>(m, pyClassName);
  m.def(("AvgPooling" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& kernel_dims,
                                                                  const std::string& name,
                                                                  const std::vector<DimSize_t> &stride_dims) {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);

        return AvgPooling<DIM>(to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()));
    }, py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1));

}


void init_AvgPooling(py::module &m) {
  declare_AvgPoolingOp<1>(m);
  declare_AvgPoolingOp<2>(m);
  declare_AvgPoolingOp<3>(m);

  // FIXME:
  // m.def("AvgPooling1D", static_cast<NodeAPI(*)(const char*, int, int, int const
  // (&)[1])>(&AvgPooling));
}
} // namespace Aidge
