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
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/ReduceMean.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

void declare_ReduceMeanOp(py::module &m) {
  const std::string pyClassName("ReduceMeanOp");
  py::class_<ReduceMean_Op, std::shared_ptr<ReduceMean_Op>, Attributes, OperatorTensor>(
    m, pyClassName.c_str(), py::multiple_inheritance())
    .def("get_inputs_name", &ReduceMean_Op::getInputsName)
    .def("get_outputs_name", &ReduceMean_Op::getOutputsName)
    .def("attributes_name", &ReduceMean_Op::staticGetAttrsName)
    ;
  declare_registrable<ReduceMean_Op>(m, pyClassName);

  m.def("ReduceMean", [](const std::vector<int>& axes,
                                                                DimSize_t keepDims,
                                                                const std::string& name) {
        // AIDGE_ASSERT(axes.size() == DIM, "axes size [{}] does not match DIM [{}]", axes.size(), DIM);

        return ReduceMean(axes, keepDims, name);
    }, py::arg("axes"),
       py::arg("keep_dims") = 1,
       py::arg("name") = "");
}


void init_ReduceMean(py::module &m) {
  declare_ReduceMeanOp(m);
//   declare_ReduceMeanOp<2>(m);
//   declare_ReduceMeanOp<3>(m);

  // FIXME:
  // m.def("ReduceMean1D", static_cast<NodeAPI(*)(const char*, int, int, int const
  // (&)[1])>(&ReduceMean));
}
} // namespace Aidge
