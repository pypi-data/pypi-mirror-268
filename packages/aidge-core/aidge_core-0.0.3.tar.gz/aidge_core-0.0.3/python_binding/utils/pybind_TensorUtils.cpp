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

#include <string>

#include "aidge/utils/TensorUtils.hpp"

namespace py = pybind11;

namespace Aidge {

template<typename T>
void addTensorUtilsFunction(py::module &m){
    m.def("approx_eq",
    & approxEq<T>,
    py::arg("t1"),
    py::arg("t2"),
    py::arg("relative"),
    py::arg("absolute"),
    R"mydelimiter(
        Compare two :cpp:class:`Aidge::Tensor` value wise. The comparison function is:
            |t1-t2| <= absolute + relative * |t2|

        If a tensor value is different from the other tensor return False
        If the tensor does not have the same size, return False
        If the datatype is not the same between each tensor return False
        If the templated type does not correspond to the datatype of each tensor, raise an assertion error

        :param t1: first tensor to test
        :type t1: :py:class:`aidge_core.Tensor`
        :param t2: second tensor to test
        :type t2: :py:class:`aidge_core.Tensor`
        :param relative: relative difference allowed (should be betwen 0 and 1)
        :type relative: float
        :param absolute: absolute error allowed (shoulmd be positive)
        :type absolute: float
        )mydelimiter");
}

void init_TensorUtils(py::module &m) {
    addTensorUtilsFunction<float>(m);
    addTensorUtilsFunction<double>(m);
    addTensorUtilsFunction<int32_t>(m);
    addTensorUtilsFunction<int64_t>(m);
}
} // namespace Aidge
