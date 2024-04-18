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
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/Pad.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM> void declare_PadOp(py::module &m) {
  const std::string pyClassName("PadOp" + std::to_string(DIM) + "D");
  py::class_<Pad_Op<DIM>, std::shared_ptr<Pad_Op<DIM>>, Attributes, Operator>(
    m, pyClassName.c_str(),
    py::multiple_inheritance())
  .def(py::init<const std::array<DimSize_t, 2*DIM> &,
                const PadBorderType &,
                double>(),
        py::arg("beginEndTuples"),
        py::arg("borderType") = PadBorderType::Constant,
        py::arg("borderValue") = 0.0)
    .def("get_inputs_name", &Pad_Op<DIM>::getInputsName)
    .def("get_outputs_name", &Pad_Op<DIM>::getOutputsName)
    .def("attributes_name", &Pad_Op<DIM>::staticGetAttrsName)
    ;
  declare_registrable<Pad_Op<DIM>>(m, pyClassName);
  m.def(("Pad" + std::to_string(DIM) + "D").c_str(), [](const std::vector<DimSize_t>& beginEndTuples,
                                                        const std::string& name,
                                                        const PadBorderType &borderType = PadBorderType::Constant,
                                                        double borderValue = 0.0) {
        AIDGE_ASSERT(beginEndTuples.size() == 2*DIM, "begin_end_tuples size [{}] does not match DIM [{}]", beginEndTuples.size(), 2*DIM);
        return Pad<DIM>(to_array<2*DIM>(beginEndTuples.begin()), name, borderType, borderValue);
    },
       py::arg("begin_end_tuples"),
       py::arg("name") = "",
       py::arg("border_type") = PadBorderType::Constant,
       py::arg("border_value") = 0.0);
}


void init_Pad(py::module &m) {
  py::enum_<PadBorderType>(m, "pad_border_type")
    .value("Constant", PadBorderType::Constant)
    .value("Edge",     PadBorderType::Edge)
    .value("Reflect",  PadBorderType::Reflect)
    .value("Wrap",     PadBorderType::Wrap)
    .export_values();
  declare_PadOp<1>(m);
  declare_PadOp<2>(m);
  declare_PadOp<3>(m);
}
} // namespace Aidge
