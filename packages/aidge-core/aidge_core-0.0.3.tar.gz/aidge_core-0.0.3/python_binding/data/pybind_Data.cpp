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
#include "aidge/data/Data.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Data(py::module& m){
    // TODO : extend with more values !
    py::enum_<DataType>(m, "DataType")
    .value("Float64", DataType::Float64)
    .value("Float32", DataType::Float32)
    .value("Float16", DataType::Float16)
    .value("Int8", DataType::Int8)
    .value("Int32", DataType::Int32)
    .value("Int64", DataType::Int64)
    .value("UInt8", DataType::UInt8)
    .value("UInt32", DataType::UInt32)
    .value("UInt64", DataType::UInt64)
    ;

    py::class_<Data, std::shared_ptr<Data>>(m,"Data");


}
}
