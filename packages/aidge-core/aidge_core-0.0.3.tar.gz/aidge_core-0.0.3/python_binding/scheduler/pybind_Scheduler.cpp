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
#include "aidge/scheduler/Scheduler.hpp"
#include "aidge/scheduler/SequentialScheduler.hpp"
#include "aidge/scheduler/ParallelScheduler.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/data/Tensor.hpp"

namespace py = pybind11;
namespace Aidge {
void init_Scheduler(py::module& m){
    py::class_<Scheduler, std::shared_ptr<Scheduler>>(m, "Scheduler")
    .def(py::init<std::shared_ptr<GraphView>&>(), py::arg("graph_view"))
    .def("save_scheduling_diagram", &Scheduler::saveSchedulingDiagram, py::arg("file_name"))
    .def("resetScheduling", &Scheduler::resetScheduling)
    .def("generate_scheduling", &Scheduler::generateScheduling)
    .def("get_static_scheduling", &Scheduler::getStaticScheduling, py::arg("step") = 0)
    ;

    py::class_<SequentialScheduler, std::shared_ptr<SequentialScheduler>, Scheduler>(m, "SequentialScheduler")
    .def(py::init<std::shared_ptr<GraphView>&>(), py::arg("graph_view"))
    .def("forward", &SequentialScheduler::forward, py::arg("forward_dims")=true, py::arg("data")=std::vector<Tensor>())
    .def("backward", &SequentialScheduler::backward, py::arg("data"), py::arg("instanciate_grad")=true)
    ;

    py::class_<ParallelScheduler, std::shared_ptr<ParallelScheduler>, Scheduler>(m, "ParallelScheduler")
    .def(py::init<std::shared_ptr<GraphView>&>(), py::arg("graph_view"))
    .def("forward", &ParallelScheduler::forward, py::arg("forward_dims")=true, py::arg("data")=std::vector<Tensor>())
    ;
}
}

