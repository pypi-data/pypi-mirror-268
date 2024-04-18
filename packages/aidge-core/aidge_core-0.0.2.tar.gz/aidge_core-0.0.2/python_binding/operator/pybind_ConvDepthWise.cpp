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
#include "aidge/operator/ConvDepthWise.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"
#include "aidge/data/Tensor.hpp"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_ConvDepthWiseOp(py::module &m) {
  const std::string pyClassName("ConvDepthWiseOp" + std::to_string(DIM) + "D");
  py::class_<ConvDepthWise_Op<DIM>, std::shared_ptr<ConvDepthWise_Op<DIM>>, Attributes, OperatorTensor>(
    m, pyClassName.c_str(),
    py::multiple_inheritance())
  .def(py::init<const DimSize_t,
                const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &,
                bool>(),
        py::arg("nb_channels"),
        py::arg("kernel_dims"),
        py::arg("stride_dims"),
        py::arg("dilation_dims"),
        py::arg("no_bias"))
  .def("get_inputs_name", &ConvDepthWise_Op<DIM>::getInputsName)
  .def("get_outputs_name", &ConvDepthWise_Op<DIM>::getOutputsName)
  .def("attributes_name", &ConvDepthWise_Op<DIM>::staticGetAttrsName);
  declare_registrable<ConvDepthWise_Op<DIM>>(m, pyClassName);
  m.def(("ConvDepthWise" + std::to_string(DIM) + "D").c_str(), [](const DimSize_t nb_channels,
                                                                  const std::vector<DimSize_t>& kernel_dims,
                                                                  const std::string& name,
                                                                  const std::vector<DimSize_t> &stride_dims,
                                                                  const std::vector<DimSize_t> &dilation_dims,
                                                                  bool no_bias) {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(dilation_dims.size() == DIM, "dilation_dims size [{}] does not match DIM [{}]", dilation_dims.size(), DIM);

        return ConvDepthWise<DIM>(nb_channels, to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<DIM>(dilation_dims.begin()), no_bias);
    }, py::arg("nb_channenls"),
       py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("dilation_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("no_bias")= false);

}


void init_ConvDepthWise(py::module &m) {
  declare_ConvDepthWiseOp<1>(m);
  declare_ConvDepthWiseOp<2>(m);
  declare_ConvDepthWiseOp<3>(m);

  // FIXME:
  // m.def("ConvDepthWise1D", static_cast<NodeAPI(*)(const char*, int, int, int const
  // (&)[1])>(&ConvDepthWise));
}
} // namespace Aidge
