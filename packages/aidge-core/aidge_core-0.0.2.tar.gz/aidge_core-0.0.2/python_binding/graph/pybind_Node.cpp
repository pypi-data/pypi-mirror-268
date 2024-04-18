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

#include <memory>

#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/graph/Connector.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;
namespace Aidge {
void init_Node(py::module& m) {
    py::class_<Node, std::shared_ptr<Node>>(m, "Node")
    .def(py::init<std::shared_ptr<Operator>, const std::string&>(), py::arg("op"), py::arg("name") = "")
    .def("name", &Node::name,
    R"mydelimiter(
    Name of the Node.
    )mydelimiter")

    .def("type", &Node::type,
    R"mydelimiter(
    Type of the node.
    )mydelimiter")

    .def("get_operator", &Node::getOperator,
    R"mydelimiter(
    Get the Operator object of the Node.
    )mydelimiter")

    .def("set_name", &Node::setName, py::arg("name"),
    R"mydelimiter(
    Set the Node name.

    :param name: New name for the node.
    :type name: str
    :rtype: str
    )mydelimiter")

    .def("add_child",
         (void (Node::*)(std::shared_ptr<Node>, const IOIndex_t, IOIndex_t)) &
                 Node::addChild,
         py::arg("other_node"), py::arg("out_id") = 0, py::arg("other_in_id") = gk_IODefaultIndex,
    R"mydelimiter(
    Link another Node to an output of the current Node.

    :param other_node: Pointer to the other Node.
    :type other_node: :py:class: Node
    :param out_id: ID of the output of the current Node to connect to the other Node. (If Node has 1 output max ID is 0). Default to 0.
    :type out_id: int
    :param other_in_id: ID of the input of the other Node to connect to the current Node (If the node is a Mul op it has 2 input then Max ID is 1).Default to the first avaible data input.
    :type other_in_id: int
    )mydelimiter")

    .def("add_child",
        [](Node &self, std::shared_ptr<GraphView> other_graph, const IOIndex_t out_id=0,
                        py::object other_in_id = py::none()) {
            std::pair<NodePtr, IOIndex_t> cpp_other_in_id;
            // Note: PyBind on windows does not support conversion of nullptr -> std::shared_ptr, using this trampoline to change the default arg to a py::none(). If signature change, we would be able to directly bind the function.

            if (other_in_id.is_none()) {
                cpp_other_in_id = std::pair<NodePtr, IOIndex_t>(nullptr, gk_IODefaultIndex);
            }else{
                cpp_other_in_id = other_in_id.cast<std::pair<NodePtr, IOIndex_t>>();
            }
            self.addChild(other_graph, out_id, cpp_other_in_id);
        },
        py::arg("other_graph"), py::arg("out_id") = 0,
        py::arg("other_in_id") = py::none(),
               R"mydelimiter(
    Link a Node from a specific GraphView to the current Node.

    :param other_view: Pointer to the GraphView whose content should be linked to the current Node.
    :type other_view: :py:class: GraphView
    :param out_id: ID of the current Node output to connect to the other Node. Default to 0.
    :type out_id: int
    :param other_in_id: Pair of Node and input connection ID for specifying the connection. If the GraphView whose content is linked has only one input Node, then it defaults to the first available data input ID of this Node.
    :type other_in_id: tuple[:py:class: Node, int]
    )mydelimiter")

    .def("inputs", &Node::inputs,
    R"mydelimiter(
    Get ordered list of parent Node and the associated output index connected to the current Node's inputs.

    :return: List of connections. When an input is not linked to any parent, the default value is (None, default_index)
    :rtype: list[tuple[Node, int]]
    )mydelimiter")

    .def("input", &Node::input, py::arg("in_id"),
    R"mydelimiter(
    Get the parent Node and the associated output index connected to the i-th input of the current Node.

    :param in_id: input index of the current Node object.
    :type in_id: int
    :return: i-th connection. When an input is not linked to any parent, the default value is (None, default_index)
    :rtype: tuple[Node, int]
    )mydelimiter")

    .def("outputs", &Node::outputs,
    R"mydelimiter(
    Get, for each output of the Node, a list of the children Node and the associated input index connected to it.

    :return: List of a list of connections. When an outut is not linked to any child,  its list a empty.
    :rtype: list[list[tuple[Node, int]]]
    )mydelimiter")

    .def("output", &Node::output, py::arg("out_id"),
    R"mydelimiter(
    Get a list of the children Node for a specific output and the associated input index connected to it.

    :param out_id: input index of the current Node object.
    :type out_id: int
    :return: i-th connection. When an input is not linked to any parent, the default value is (None, default_index)
    :rtype: list[tuple[Node, int]]
    )mydelimiter")

    .def("get_nb_inputs", &Node::nbInputs,
    R"mydelimiter(
    Number of inputs.

    :rtype: int
    )mydelimiter")

    .def("get_nb_data", &Node::nbData,
    R"mydelimiter(
    Number of data inputs.

    :rtype: int
    )mydelimiter")

    .def("get_nb_outputs", &Node::nbOutputs,
    R"mydelimiter(
    Number of outputs.

    :rtype: int
    )mydelimiter")

    .def("get_parent", &Node::getParent, py::arg("in_id"))

    .def("get_parents", &Node::getParents,
    R"mydelimiter(
    Get parents.
    )mydelimiter")

    .def("get_children", (std::set<std::shared_ptr<Node>> (Node::*)() const) &Node::getChildren,
    R"mydelimiter(
    Get children.
    )mydelimiter")

    .def("__call__",
        [](Node &self, pybind11::args args) {
            std::vector<Connector> connectors;
            for (const auto &arg : args) {
                // Check if the argument is an instance of Connector
                if (pybind11::isinstance<Connector>(arg)) {
                    // Convert Python object to C++ object adn push it ot vector
                    connectors.push_back(arg.cast<Connector>());
                } else {
                    throw std::runtime_error("One of the arguments was not a Connector.");
                }
            }
            return self(connectors);
        });
}
}  // namespace Aidge
