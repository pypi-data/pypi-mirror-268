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

#include "aidge/data/Tensor.hpp"
#include "aidge/filler/Filler.hpp"

namespace py = pybind11;

namespace Aidge {

void init_Filler(py::module &m) {
    py::enum_<enum VarianceNorm>(m, "VarianceNorm")
        .value("FanIn", VarianceNorm::FanIn)
        .value("Average", VarianceNorm::Average)
        .value("FanOut", VarianceNorm::FanOut)
        .export_values();

    m.def(
         "constant_filler",
         [](std::shared_ptr<Tensor> tensor, py::object value) -> void {
             switch (tensor->dataType()) {
                 case DataType::Float64:
                     constantFiller<double>(tensor, value.cast<double>());
                     break;
                 case DataType::Float32:
                     constantFiller<float>(tensor, value.cast<float>());
                     break;
                 default:
                     AIDGE_THROW_OR_ABORT(
                         py::value_error,
                         "Data type is not supported for Constant filler.");
             }
         },
         py::arg("tensor"), py::arg("value"))
        .def(
            "normal_filler",
            [](std::shared_ptr<Tensor> tensor, double mean,
               double stdDev) -> void {
                switch (tensor->dataType()) {
                    case DataType::Float64:
                        normalFiller<double>(tensor, mean, stdDev);
                        break;
                    case DataType::Float32:
                        normalFiller<float>(tensor, mean, stdDev);
                        break;
                    default:
                        AIDGE_THROW_OR_ABORT(
                            py::value_error,
                            "Data type is not supported for Normal filler.");
                }
            },
            py::arg("tensor"), py::arg("mean") = 0.0, py::arg("stdDev") = 1.0)
        .def(
            "uniform_filler",
            [](std::shared_ptr<Tensor> tensor, double min, double max) -> void {
                switch (tensor->dataType()) {
                    case DataType::Float64:
                        uniformFiller<double>(tensor, min, max);
                        break;
                    case DataType::Float32:
                        uniformFiller<float>(tensor, min, max);
                        break;
                    default:
                        AIDGE_THROW_OR_ABORT(
                            py::value_error,
                            "Data type is not supported for Uniform filler.");
                }
            },
            py::arg("tensor"), py::arg("min"), py::arg("max"))
        .def(
            "xavier_uniform_filler",
            [](std::shared_ptr<Tensor> tensor, py::object scaling,
               VarianceNorm varianceNorm) -> void {
                switch (tensor->dataType()) {
                    case DataType::Float64:
                        xavierUniformFiller<double>(
                            tensor, scaling.cast<double>(), varianceNorm);
                        break;
                    case DataType::Float32:
                        xavierUniformFiller<float>(
                            tensor, scaling.cast<float>(), varianceNorm);
                        break;
                    default:
                        AIDGE_THROW_OR_ABORT(
                            py::value_error,
                            "Data type is not supported for Uniform filler.");
                }
            },
            py::arg("tensor"), py::arg("scaling") = 1.0,
            py::arg("varianceNorm") = VarianceNorm::FanIn)
        .def(
            "xavier_normal_filler",
            [](std::shared_ptr<Tensor> tensor, py::object scaling,
               VarianceNorm varianceNorm) -> void {
                switch (tensor->dataType()) {
                    case DataType::Float64:
                        xavierNormalFiller<double>(
                            tensor, scaling.cast<double>(), varianceNorm);
                        break;
                    case DataType::Float32:
                        xavierNormalFiller<float>(tensor, scaling.cast<float>(),
                                                  varianceNorm);
                        break;
                    default:
                        AIDGE_THROW_OR_ABORT(
                            py::value_error,
                            "Data type is not supported for Uniform filler.");
                }
            },
            py::arg("tensor"), py::arg("scaling") = 1.0,
            py::arg("varianceNorm") = VarianceNorm::FanIn)
        .def(
            "he_filler",
            [](std::shared_ptr<Tensor> tensor, VarianceNorm varianceNorm,
               py::object meanNorm, py::object scaling) -> void {
                switch (tensor->dataType()) {
                    case DataType::Float64:
                        heFiller<double>(tensor, varianceNorm,
                                         meanNorm.cast<double>(),
                                         scaling.cast<double>());
                        break;
                    case DataType::Float32:
                        heFiller<float>(tensor, varianceNorm,
                                        meanNorm.cast<float>(),
                                        scaling.cast<float>());
                        break;
                    default:
                        AIDGE_THROW_OR_ABORT(
                            py::value_error,
                            "Data type is not supported for Uniform filler.");
                }
            },
            py::arg("tensor"), py::arg("varianceNorm") = VarianceNorm::FanIn,
            py::arg("meanNorm") = 0.0, py::arg("scaling") = 1.0)
        ;
}
}  // namespace Aidge
