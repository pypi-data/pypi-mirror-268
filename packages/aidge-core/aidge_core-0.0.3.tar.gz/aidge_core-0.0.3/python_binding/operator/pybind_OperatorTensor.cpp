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

#include <memory>
#include <string>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Operator.hpp"

namespace py = pybind11;
namespace Aidge {
void init_OperatorTensor(py::module& m){
    py::class_<OperatorTensor, std::shared_ptr<OperatorTensor>, Operator>(m, "OperatorTensor")
    .def("get_output", &OperatorTensor::getOutput, py::arg("outputIdx"))
    .def("get_input", &OperatorTensor::getInput, py::arg("inputIdx"))

    .def("set_output", (void (OperatorTensor::*)(const IOIndex_t, const std::shared_ptr<Data>&)) &OperatorTensor::setOutput, py::arg("outputIdx"), py::arg("data"))
    .def("set_input", (void (OperatorTensor::*)(const IOIndex_t, const std::shared_ptr<Data>&)) &OperatorTensor::setInput, py::arg("outputIdx"), py::arg("data"))
    .def("compute_output_dims", &OperatorTensor::computeOutputDims)
    .def("output_dims_forwarded", &OperatorTensor::outputDimsForwarded)
    ;
}
}
