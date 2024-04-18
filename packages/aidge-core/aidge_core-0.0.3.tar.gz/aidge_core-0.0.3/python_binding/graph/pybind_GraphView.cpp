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
#include <string>
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"
#include "aidge/data/Data.hpp"

namespace py = pybind11;
namespace Aidge {
void init_GraphView(py::module& m) {
    py::class_<GraphView, std::shared_ptr<GraphView>>(m, "GraphView")
          .def(py::init<>())
          .def("save", &GraphView::save, py::arg("path"), py::arg("verbose") = false, py::arg("show_producers") = true,
          R"mydelimiter(
          Save the GraphView as a Mermaid graph in a .md file at the specified location.

          :param path: save location
          :type path: str
          )mydelimiter")
          .def("log_outputs", &GraphView::logOutputs, py::arg("path"))
          .def("get_ordered_inputs", &GraphView::getOrderedInputs)
          .def("get_ordered_outputs", &GraphView::getOrderedOutputs)
          .def("get_output_nodes", &GraphView::outputNodes,
          R"mydelimiter(
          Get set of output Nodes.

          :rtype: list[Node]
          )mydelimiter")

          .def("get_input_nodes", &GraphView::inputNodes,
          R"mydelimiter(
          Get set of input Nodes.

          :rtype: list[Node]
          )mydelimiter")

          .def("set_ordered_inputs", &GraphView::setOrderedInputs, py::arg("inputs"))
          .def("set_ordered_outputs", &GraphView::setOrderedOutputs, py::arg("outputs"))

          .def("add", (void (GraphView::*)(std::shared_ptr<Node>, bool)) & GraphView::add,
               py::arg("other_node"), py::arg("include_learnable_parameters") = true,
          R"mydelimiter(
          Include a Node to the current GraphView object.

          :param other_node: Node to add
          :type other_node: Node
          :param include_learnable_parameters: include non-data inputs, like weights and biases, default True.
          :type include_learnable_parameters: bool, optional
          )mydelimiter")

          .def("add", (bool (GraphView::*)(std::shared_ptr<GraphView>)) & GraphView::add,
               py::arg("other_graph"),
          R"mydelimiter(
          Include a GraphView to the current GraphView object.

          :param other_graph: GraphView to add
          :type other_graph: GraphView
          )mydelimiter")

          .def("add_child",
               (void (GraphView::*)(std::shared_ptr<Node>,
                                   std::shared_ptr<Node>,
                                   const IOIndex_t,
                                   IOIndex_t)) &
                    GraphView::addChild,
               py::arg("to_other_node"), py::arg("from_out_node") = nullptr,
               py::arg("from_tensor") = 0U, py::arg("to_tensor") = gk_IODefaultIndex,
          R"mydelimiter(
          Include a Node to the current GraphView object.

          :param to_other_node: Node to add
          :type to_other_node: Node
          :param from_out_node: Node inside the GraphView the new Node will be linked to (it will become a parent of the new Node). If the GraphView only has one output Node, then default to this Node.
          :type from_out_node: Node
          :param from_tensor: Ouput Tensor ID of the already included Node. Default to 0.
          :type from_tensor: int
          :param to_tensor: Input Tensor ID of the new Node. Default to gk_IODefaultIndex, meaning first available data input for the Node.
          :type to_tensor: int
          )mydelimiter")

          .def_static("replace", py::overload_cast<const std::shared_ptr<GraphView>&, const std::shared_ptr<GraphView>&>(&GraphView::replace), py::arg("old_graph"), py::arg("new_graph"),
          R"mydelimiter(
          Replace the old set of Nodes in a GraphView with the new set of given Nodes in a GraphView if possible in every GraphView.

          :param old_graph: GraphView of Nodes actually connected in GraphViews.
          :type old_graph: GraphView
          :param new_graph: GraphView of Nodes with inner connections already taken care of.
          :type new_graph: GraphView
          :return: Whether any replacement has been made.
          :rtype: bool
          )mydelimiter")

          .def_static("replace", py::overload_cast<const std::set<NodePtr>&, const std::set<NodePtr>&>(&GraphView::replace), py::arg("old_nodes"), py::arg("new_nodes"),
          R"mydelimiter(
          Replace the old set of Nodes with the new set of given Nodes if possible in every GraphView.

          :param old_nodes: Nodes actually connected in GraphViews.
          :type old_nodes: Node
          :param new_nodes: Nodes with inner connections already taken care of.
          :type new_nodes: Node
          :return: Whether any replacement has been made.
          :rtype: bool
          )mydelimiter")

          .def("get_nodes", &GraphView::getNodes)
          .def("get_node", &GraphView::getNode, py::arg("node_name"))
          .def("forward_dims", &GraphView::forwardDims, py::arg("dims")=std::vector<std::vector<DimSize_t>>())
          .def("compile", &GraphView::compile, py::arg("backend"), py::arg("datatype"), py::arg("device") = 0, py::arg("dims")=std::vector<std::vector<DimSize_t>>())
          .def("__call__", &GraphView::operator(), py::arg("connectors"))
          .def("set_datatype", &GraphView::setDataType, py::arg("datatype"))
          .def("set_backend", &GraphView::setBackend, py::arg("backend"), py::arg("device") = 0)
          //   .def("__getitem__", [](Tensor& b, size_t idx)-> py::object {
          //      // TODO : Should return error if backend not compatible with get
          //      if (idx >= b.size()) throw py::index_error();
          //      switch(b.dataType()){
          //           case DataType::Float32:
          //                return py::cast(static_cast<float*>(b.getImpl()->rawPtr())[idx]);
          //           case DataType::Int32:
          //                return py::cast(static_cast<int*>(b.getImpl()->rawPtr())[idx]);
          //           default:
          //                return py::none();
          //           }
          //      })
            ;

     m.def("get_connected_graph_view", &getConnectedGraphView);
}
}  // namespace Aidge
