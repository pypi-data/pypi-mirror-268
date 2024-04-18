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

#include <cstddef>
#include <string>

#include "aidge/recipes/Recipes.hpp"
#include "aidge/utils/Types.h"

namespace py = pybind11;

namespace Aidge {
void init_Recipes(py::module &m) {


  m.def("fuse_mul_add", static_cast<void(*)(std::shared_ptr<GraphView>)>(fuseMulAdd), py::arg("graph_view"), R"mydelimiter(
    Recipie to Fuse MatMul and Add operators into an :py:class:`aidge_core.FC` operator.

    :param graph_view: Graph view on which we want to apply the recipie
    :type graph_view: :py:class:`aidge_core.GraphView`
    )mydelimiter");

  // m.def("fuse_mul_add", static_cast<void(*)(std::set<std::shared_ptr<Node>>)>(fuseMulAdd), py::arg("nodes"), R"mydelimiter(
  //   Recipie to Fuse MatMul and Add operators into an :py:class:`aidge_core.FC` operator.

  //   :param nodes: The MatMul and Add nodes to fuse.
  //   :type nodes: list of :py:class:`aidge_core.Node`
  //   )mydelimiter");

  m.def("remove_dropout",static_cast<void(*)(std::shared_ptr<GraphView>)>(removeDropout), py::arg("graph_view"), R"mydelimiter(
    Recipie to remove a dropout operator.

    :param graph_view: Graph view on which we want to apply the recipie
    :type graph_view: :py:class:`aidge_core.GraphView`
    )mydelimiter");

  m.def("remove_flatten", static_cast<void(*)(std::shared_ptr<GraphView>)>(removeFlatten), py::arg("graph_view"), R"mydelimiter(
    Recipie to remove a flatten operator.

    :param graph_view: Graph view on which we want to apply the recipie
    :type graph_view: :py:class:`aidge_core.GraphView`
    )mydelimiter");

  // m.def("remove_flatten", static_cast<void(*)(std::set<std::shared_ptr<Node>>)>(removeFlatten), py::arg("nodes"), R"mydelimiter(
  //   Recipie to remove a flatten operator.

  //   :param nodes: The flatten operator to remove.
  //   :type nodes: list of :py:class:`aidge_core.Node`
  //   )mydelimiter");

  // m.def("fuse_mul_add", static_cast<void(*)(std::set<std::shared_ptr<Node>>)>(fuseMulAdd), py::arg("nodes"), R"mydelimiter(
  //   Recipie to Fuse MatMul and Add operators into an :py:class:`aidge_core.FC` operator.

  //   :param nodes: The MatMul and Add nodes to fuse.
  //   :type nodes: list of :py:class:`aidge_core.Node`
  //   )mydelimiter");

  m.def("fuse_batchnorm", static_cast<void(*)(std::shared_ptr<GraphView>)>(fuseBatchNorm), py::arg("graph_view"), R"mydelimiter(
    Recipie to remove a flatten operator.

    :param graph_view: Graph view on which we want to apply the recipie
    :type graph_view: :py:class:`aidge_core.GraphView`
    )mydelimiter");

 m.def("get_conv_horizontal_tiling", static_cast<std::set<std::shared_ptr<Node>>(*)(const std::shared_ptr<Node>&, const DimIdx_t, const std::size_t)>(getConvHorizontalTiling),
        py::arg("node"), py::arg("axis"), py::arg("nb_slices"));

  // m.def("fuse_batchnorm", static_cast<void(*)(std::set<std::shared_ptr<Node>>)>(fuseBatchNorm), py::arg("nodes"), R"mydelimiter(
  //   Recipie to remove a flatten operator.

  //   :param nodes: The flatten operator to remove.
  //   :type nodes: list of :py:class:`aidge_core.Node`
  //   )mydelimiter");
}
} // namespace Aidge
