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
#include "aidge/graphRegex/matchFsm/MatchResult.hpp"

namespace py = pybind11;
namespace Aidge {
void init_MatchSolution(py::module& m){


    py::class_<MatchSolution, std::shared_ptr<MatchSolution>>(m, "MatchSolution", "MatchSolution class contains the result of one match and the associated key, the query and the start node.")
    .def("at", &MatchSolution::at, py::arg("key"),
    R"mydelimiter(
    :rtype: str
    )mydelimiter")

    .def("get_all",  &MatchSolution::getAll,
    R"mydelimiter(
    )mydelimiter")

    .def("get_query",  &MatchSolution::getQuery,
    R"mydelimiter(
    )mydelimiter")

    .def("get_start_node",  &MatchSolution::getStartNode,
    R"mydelimiter(
    )mydelimiter")
    ;
}
} // namespace Aidge
