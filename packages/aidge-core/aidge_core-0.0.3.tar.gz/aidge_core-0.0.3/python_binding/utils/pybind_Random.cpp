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
#include "aidge/utils/Random.hpp"

namespace py = pybind11;

namespace Aidge {

void init_Random(py::module &m) {
    auto mRand = m.def_submodule("random", "Random module.");
    py::class_<Random::Generator>(mRand, "Generator")
    .def_static("set_seed", Random::Generator::setSeed);
}
}  // namespace Aidge
