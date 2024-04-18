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
#include "aidge/operator/Conv.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"
#include "aidge/utils/Registrar.hpp" // declare_registrable

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_ConvOp(py::module &m) {
  const std::string pyClassName("ConvOp" + std::to_string(DIM) + "D");
  py::class_<Conv_Op<DIM>, std::shared_ptr<Conv_Op<DIM>>, Attributes, OperatorTensor>(
    m, pyClassName.c_str(),
    py::multiple_inheritance())
  .def(py::init<DimSize_t,
                DimSize_t,
                const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &,
                const std::array<DimSize_t, DIM> &,
                bool>(),
        py::arg("in_channels"),
        py::arg("out_channels"),
        py::arg("kernel_dims"),
        py::arg("stride_dims"),
        py::arg("dilation_dims"),
        py::arg("no_bias"))
    .def("get_inputs_name", &Conv_Op<DIM>::getInputsName)
    .def("get_outputs_name", &Conv_Op<DIM>::getOutputsName)
    .def("attributes_name", &Conv_Op<DIM>::staticGetAttrsName)
    ;
  declare_registrable<Conv_Op<DIM>>(m, pyClassName);


  m.def(("Conv" + std::to_string(DIM) + "D").c_str(), [](DimSize_t in_channels,
                                                         DimSize_t out_channels,
                                                         const std::vector<DimSize_t>& kernel_dims,
                                                         const std::string& name,
                                                         const std::vector<DimSize_t> &stride_dims,
                                                         const std::vector<DimSize_t> &dilation_dims,
                                                         bool noBias) {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(dilation_dims.size() == DIM, "dilation_dims size [{}] does not match DIM [{}]", dilation_dims.size(), DIM);

        return Conv<DIM>(in_channels, out_channels, to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<DIM>(dilation_dims.begin()), noBias);
    }, py::arg("in_channels"),
       py::arg("out_channels"),
       py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("dilation_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("no_bias") = false);
}


void init_Conv(py::module &m) {
  declare_ConvOp<1>(m);
  declare_ConvOp<2>(m);
  declare_ConvOp<3>(m);
}
} // namespace Aidge
