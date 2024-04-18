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

// #include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {

template <DimIdx_t DIM>
void declare_Producer(py::module &m) {
    // m.def(("Producer_" + std::to_string(DIM)+"D").c_str(), py::overload_cast<shared_ptr<Node>&>(&Producer<DIM>), py::arg("dims"), py::arg("name"));
    m.def("Producer", static_cast<std::shared_ptr<Node>(*)(const std::array<DimSize_t, DIM>&, const std::string&, bool)>(&Producer), py::arg("dims"), py::arg("name") = "", py::arg("constant") = false);


}


void init_Producer(py::module &m) {
    py::class_<Producer_Op,  std::shared_ptr<Producer_Op>, Attributes, OperatorTensor>(
        m,
        "ProducerOp",
        py::multiple_inheritance())
    .def("dims", &Producer_Op::dims)
    .def("get_inputs_name", &Producer_Op::getInputsName)
    .def("get_outputs_name", &Producer_Op::getOutputsName)
    .def("attributes_name", &Producer_Op::staticGetAttrsName);
    m.def("Producer", static_cast<std::shared_ptr<Node>(*)(const std::shared_ptr<Tensor>, const std::string&, bool)>(&Producer), py::arg("tensor"), py::arg("name") = "", py::arg("constant") = false);
    declare_registrable<Producer_Op>(m, "ProducerOp");
    declare_Producer<1>(m);
    declare_Producer<2>(m);
    declare_Producer<3>(m);
    declare_Producer<4>(m);
    declare_Producer<5>(m);
    declare_Producer<6>(m);

    // m.def(("Producer_" + std::to_string(DIM)+"D").c_str(), py::overload_cast<shared_ptr<Node>&>(&Producer<DIM>), py::arg("dims"), py::arg("name"));
}
}
