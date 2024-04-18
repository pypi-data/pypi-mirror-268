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
#include <set>

#include "aidge/graph/GraphView.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/recipes/GraphViewHelper.hpp"

namespace py = pybind11;

namespace Aidge {
void init_GraphViewHelper(py::module &m) {
    m.def("producers", &producers, py::arg("graphview"));
}
} // namespace Aidge
