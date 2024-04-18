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

#include "aidge/graph/OpArgs.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"



namespace py = pybind11;
namespace Aidge {
void init_OpArgs(py::module& m){
    py::class_<OpArgs, std::shared_ptr<OpArgs>>(m, "OpArgs")
    .def(py::init<const std::shared_ptr<GraphView>&>(), py::arg("view_"))
    .def(py::init<const std::shared_ptr<Node>&>(), py::arg("node_"))
    .def("node", &OpArgs::node)
    .def("view", &OpArgs::view)
    ;

    py::implicitly_convertible<Node, OpArgs>();
    py::implicitly_convertible<GraphView, OpArgs>();

    m.def("sequential", &Sequential, py::arg("inputs"));
    m.def("parallel", &Parallel, py::arg("inputs"));
    m.def("residual", &Residual, py::arg("inputs"));

}
}
