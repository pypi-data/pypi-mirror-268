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
#include "aidge/graph/Connector.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"

namespace py = pybind11;
namespace Aidge {
void init_Connector(py::module& m){
    py::class_<Connector, std::shared_ptr<Connector>>(m, "Connector")
    .def(py::init<>())
    .def(py::init<std::shared_ptr<Node>>())
    .def("__getitem__", &Connector::operator[], py::arg("key"))
    ;
    m.def("generate_graph", &Aidge::generateGraph, py::arg("output_connectors"));
    // m.def("generate_graph", (std::shared_ptr<GraphView>(*)(std::vector<Connector>)) &Aidge::generateGraph, py::arg("output_connectors"));
}
}
