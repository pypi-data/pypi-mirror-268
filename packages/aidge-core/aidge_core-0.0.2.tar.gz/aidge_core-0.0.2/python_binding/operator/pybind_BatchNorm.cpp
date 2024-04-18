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
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/BatchNorm.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimSize_t DIM>
void declare_BatchNormOp(py::module& m) {
    const std::string pyClassName("BatchNormOp" + std::to_string(DIM) + "D");
    py::class_<BatchNorm_Op<DIM>, std::shared_ptr<BatchNorm_Op<DIM>>, Attributes, OperatorTensor>(m, pyClassName.c_str(), py::multiple_inheritance())
    .def(py::init<float, float>(),
        py::arg("epsilon"),
        py::arg("momentum"))
    .def("get_inputs_name", &BatchNorm_Op<DIM>::getInputsName)
    .def("get_outputs_name", &BatchNorm_Op<DIM>::getOutputsName)
    .def("attributes_name", &BatchNorm_Op<DIM>::staticGetAttrsName);
    declare_registrable<BatchNorm_Op<DIM>>(m, pyClassName);

    m.def(("BatchNorm" + std::to_string(DIM) + "D").c_str(), &BatchNorm<DIM>, py::arg("nbFeatures"), py::arg("epsilon") = 1.0e-5F, py::arg("momentum") = 0.1F, py::arg("name") = "");
}

void init_BatchNorm(py::module &m) {
    declare_BatchNormOp<2>(m);
}
}  // namespace Aidge
