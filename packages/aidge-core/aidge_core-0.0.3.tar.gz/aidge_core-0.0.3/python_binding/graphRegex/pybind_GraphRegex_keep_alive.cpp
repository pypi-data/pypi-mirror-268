// /********************************************************************************
//  * Copyright (c) 2023 CEA-List
//  *
//  * This program and the accompanying materials are made available under the
//  * terms of the Eclipse Public License 2.0 which is available at
//  * http://www.eclipse.org/legal/epl-2.0.
//  *
//  * SPDX-License-Identifier: EPL-2.0
//  *
//  ********************************************************************************/

// #include <pybind11/pybind11.h>
// #include <pybind11/functional.h>
// #include "aidge/graphRegex/GraphRegex.hpp"

// namespace py = pybind11;
// namespace Aidge {
// void init_GraphRegex(py::module& m){


//     py::class_<GraphRegex, std::shared_ptr<GraphRegex>>(m, "GraphRegex", "GraphRegex class describes a regex to test a graph.")
//     .def(py::init<>())

//     .def("add_query", &GraphRegex::addQuery, py::arg("query"), py::arg("f") = nullptr, R"mydelimiter(
//     :rtype: str
//     )mydelimiter")

//     .def("set_key_from_graph", &GraphRegex::setKeyFromGraph, R"mydelimiter(
//     :param ref: The graph use to define type of Node.
//     :type ref: :py:class:`aidge_core.GraphView`
//     )mydelimiter")

// //      void setNodeKey(const std::string key, const std::string conditionalExpressions );
// //  void setNodeKey(const std::string key,std::function<bool(NodePtr)> f);

//     .def("match", &GraphRegex::match, R"mydelimiter(
//     :param graphToMatch: The graph to perform the matching algorithm on.
//     :type graphToMatch: :py:class:`aidge_core.GraphView`
//     )mydelimiter")



//     .def("set_node_key",
//             (void (GraphRegex::*)(const std::string, const std::string )) &
//                     GraphRegex::setNodeKey,
//             py::arg("key"), py::arg("conditionalExpressions"),
//     R"mydelimiter(
//     Add a node test
//     :param key: the key of the node test to use in the query.
//     :param conditionalExpressions: the test to do .

//     )mydelimiter")


//     .def("set_node_key",
//             (void (GraphRegex::*)(const std::string, std::function<bool(NodePtr)>)) &
//                     GraphRegex::setNodeKey,
//             py::arg("key"), py::arg("f"), py::keep_alive<1, 3>(),
//     R"mydelimiter(
//     Add a node test
//     :param key: the key of the lambda test to use in the conditional expressions.
//     :param f: bool lambda (nodePtr).

//     )mydelimiter")

//     .def("apply_recipes", &GraphRegex::appliedRecipes, py::arg("graph"), R"mydelimiter(
//     :rtype: str
//     )mydelimiter")
    



//     ;
// }
// }
