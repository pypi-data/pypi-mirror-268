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
#include <pybind11/functional.h>
#include <stdio.h>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/GenericOperator.hpp"
#include "aidge/operator/OperatorTensor.hpp"
namespace py = pybind11;
namespace Aidge {

void init_GenericOperator(py::module& m) {
    py::class_<GenericOperator_Op, std::shared_ptr<GenericOperator_Op>, DynamicAttributes, OperatorTensor>(m, "GenericOperatorOp",
                                                                                  py::multiple_inheritance())
    .def_readonly_static("identity", &GenericOperator_Op::Identity)
    .def("set_compute_output_dims", &GenericOperator_Op::setComputeOutputDims, py::arg("computation_function"));

    // &GenericOperator
    m.def("GenericOperator",
        []( const std::string& type,
            IOIndex_t nbData,
            IOIndex_t nbParam,
            IOIndex_t nbOut,
            const std::string& name,
            const py::kwargs kwargs){
            std::shared_ptr<Node> genericNode = GenericOperator(
                type,
                nbData,
                nbParam,
                nbOut,
                name
            );
            if (kwargs){
                std::shared_ptr<GenericOperator_Op> gop = std::static_pointer_cast<GenericOperator_Op>(genericNode->getOperator());
                for (auto item : kwargs) {
                    std::string key = py::cast<std::string>(item.first);
                    py::object value = py::reinterpret_borrow<py::object>(item.second);
                    gop->setAttrPy(key, std::move(value));
                }
            }
            return genericNode;
        }, py::arg("type"), py::arg("nb_data"), py::arg("nb_param"), py::arg("nb_out"), py::arg("name") = "");
}
}  // namespace Aidge
