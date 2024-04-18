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
#include "aidge/operator/MetaOperatorDefs.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_PaddedConvOp(py::module &m) {
  m.def(("PaddedConv" + std::to_string(DIM) + "D").c_str(), [](DimSize_t in_channels,
                                                         DimSize_t out_channels,
                                                         const std::vector<DimSize_t>& kernel_dims,
                                                         const std::string& name,
                                                         const std::vector<DimSize_t> &stride_dims,
                                                         const std::vector<DimSize_t> &padding_dims,
                                                         const std::vector<DimSize_t> &dilation_dims,
                                                         bool no_bias)
    {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(padding_dims.size() == 2*DIM, "padding_dims size [{}] does not match DIM [{}]", padding_dims.size(), 2*DIM);
        AIDGE_ASSERT(dilation_dims.size() == DIM, "dilation_dims size [{}] does not match DIM [{}]", dilation_dims.size(), DIM);

        return PaddedConv<DIM>(in_channels, out_channels, to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<2*DIM>(padding_dims.begin()), to_array<DIM>(dilation_dims.begin()), no_bias);
    }, py::arg("in_channels"),
       py::arg("out_channels"),
       py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("padding_dims") = std::vector<DimSize_t>(2*DIM,0),
       py::arg("dilation_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("no_bias")= false);
}

template <DimIdx_t DIM> void declare_PaddedConvDepthWiseOp(py::module &m) {
  m.def(("PaddedConvDepthWise" + std::to_string(DIM) + "D").c_str(), [](const DimSize_t nb_channels,
                                                         const std::vector<DimSize_t>& kernel_dims,
                                                         const std::string& name,
                                                         const std::vector<DimSize_t> &stride_dims,
                                                         const std::vector<DimSize_t> &padding_dims,
                                                         const std::vector<DimSize_t> &dilation_dims,
                                                         bool no_bias)
    {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(padding_dims.size() == 2*DIM, "padding_dims size [{}] does not match DIM [{}]", padding_dims.size(), 2*DIM);
        AIDGE_ASSERT(dilation_dims.size() == DIM, "dilation_dims size [{}] does not match DIM [{}]", dilation_dims.size(), DIM);

        return PaddedConvDepthWise<DIM>(nb_channels, to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<2*DIM>(padding_dims.begin()), to_array<DIM>(dilation_dims.begin()), no_bias);
    }, py::arg("nb_channels"),
       py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("padding_dims") = std::vector<DimSize_t>(2*DIM,0),
       py::arg("dilation_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("no_bias") = false);

}

template <DimIdx_t DIM> void declare_PaddedAvgPoolingOp(py::module &m) {
  m.def(("PaddedAvgPooling" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& kernel_dims,
                                                         const std::string& name,
                                                         const std::vector<DimSize_t> &stride_dims,
                                                         const std::vector<DimSize_t> &padding_dims)
    {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(padding_dims.size() == 2*DIM, "padding_dims size [{}] does not match DIM [{}]", padding_dims.size(), 2*DIM);

        return PaddedAvgPooling<DIM>(to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<2*DIM>(padding_dims.begin()));
    }, py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("padding_dims") = std::vector<DimSize_t>(2*DIM,0));

}

template <DimIdx_t DIM> void declare_PaddedMaxPoolingOp(py::module &m) {
  m.def(("PaddedMaxPooling" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& kernel_dims,
                                                         const std::string& name,
                                                         const std::vector<DimSize_t> &stride_dims,
                                                         const std::vector<DimSize_t> &padding_dims,
                                                         bool ceil_mode)
    {
        AIDGE_ASSERT(kernel_dims.size() == DIM, "kernel_dims size [{}] does not match DIM [{}]", kernel_dims.size(), DIM);
        AIDGE_ASSERT(stride_dims.size() == DIM, "stride_dims size [{}] does not match DIM [{}]", stride_dims.size(), DIM);
        AIDGE_ASSERT(padding_dims.size() == 2*DIM, "padding_dims size [{}] does not match DIM [{}]", padding_dims.size(), 2*DIM);

        return PaddedMaxPooling<DIM>(to_array<DIM>(kernel_dims.begin()), name, to_array<DIM>(stride_dims.begin()), to_array<2*DIM>(padding_dims.begin()), ceil_mode);
    }, py::arg("kernel_dims"),
       py::arg("name") = "",
       py::arg("stride_dims") = std::vector<DimSize_t>(DIM,1),
       py::arg("padding_dims") = std::vector<DimSize_t>(2*DIM,0),
       py::arg("ceil_mode") = false);

}

void declare_LSTMOp(py::module &m) {
  m.def("LSTM", &LSTM, py::arg("in_channels"),
       py::arg("hidden_channels"),
       py::arg("seq_length"),
       py::arg("nobias") = false,
       py::arg("name") = "");
}

void init_MetaOperatorDefs(py::module &m) {
  declare_PaddedConvOp<1>(m);
  declare_PaddedConvOp<2>(m);
  declare_PaddedConvOp<3>(m);
  declare_PaddedConvDepthWiseOp<1>(m);
  declare_PaddedConvDepthWiseOp<2>(m);
  declare_PaddedConvDepthWiseOp<3>(m);
  declare_PaddedAvgPoolingOp<1>(m);
  declare_PaddedAvgPoolingOp<2>(m);
  declare_PaddedAvgPoolingOp<3>(m);
  declare_PaddedMaxPoolingOp<1>(m);
  declare_PaddedMaxPoolingOp<2>(m);
  declare_PaddedMaxPoolingOp<3>(m);
  declare_LSTMOp(m);

  py::class_<MetaOperator_Op, std::shared_ptr<MetaOperator_Op>, OperatorTensor>(m, "MetaOperator_Op", py::multiple_inheritance())
  .def(py::init<const char *, const std::shared_ptr<GraphView>&>(),
          py::arg("type"),
          py::arg("graph"))
  .def("get_micro_graph", &MetaOperator_Op::getMicroGraph);

  m.def("meta_operator", &MetaOperator,
    py::arg("type"),
    py::arg("graph"),
    py::arg("name") = ""
  );

}
} // namespace Aidge
