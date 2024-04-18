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

#include "aidge/operator/Operator.hpp"
#include "aidge/backend/OperatorImpl.hpp"

namespace py = pybind11;
namespace Aidge {

/**
 * @brief Trampoline class for binding
 *
 */
class pyOperatorImpl: public OperatorImpl {
public:
    using OperatorImpl::OperatorImpl; // Inherit constructors

    void forward() override {
        PYBIND11_OVERRIDE(
            void,
            OperatorImpl,
            forward,

        );
    }
    void backward() override {
        PYBIND11_OVERRIDE(
            void,
            OperatorImpl,
            backward,

        );
    }
    Elts_t getNbRequiredData(const IOIndex_t inputIdx) const override {
        PYBIND11_OVERRIDE_NAME(
            Elts_t,
            OperatorImpl,
            "get_nb_required_data",
            getNbRequiredData,
            inputIdx
        );
    }
    Elts_t getNbRequiredProtected(const IOIndex_t inputIdx) const override {
        PYBIND11_OVERRIDE_NAME(
            Elts_t,
            OperatorImpl,
            "get_nb_required_protected",
            getNbRequiredProtected,
            inputIdx

        );
    }
    Elts_t getRequiredMemory(const IOIndex_t outputIdx,
    const std::vector<DimSize_t> &inputsSize) const override {
        PYBIND11_OVERRIDE_NAME(
            Elts_t,
            OperatorImpl,
            "get_required_memory",
            getRequiredMemory,
            outputIdx,
            inputsSize

        );
    }
    Elts_t getNbConsumedData(const IOIndex_t inputIdx) const override {
        PYBIND11_OVERRIDE_NAME(
            Elts_t,
            OperatorImpl,
            "get_nb_consumed_data",
            getNbConsumedData,
            inputIdx

        );
    }
    Elts_t getNbProducedData(const IOIndex_t outputIdx) const override {
        PYBIND11_OVERRIDE_NAME(
            Elts_t,
            OperatorImpl,
            "get_nb_produced_data",
            getNbProducedData,
            outputIdx

        );
    }
    void updateConsummerProducer() override {
        PYBIND11_OVERRIDE_NAME(
            void,
            OperatorImpl,
            "update_consummer_producer",
            updateConsummerProducer,

        );
    }
    void resetConsummerProducer() override {
        PYBIND11_OVERRIDE_NAME(
            void,
            OperatorImpl,
            "reset_consummer_producer",
            resetConsummerProducer,

        );
    }
};

void init_OperatorImpl(py::module& m){

    py::class_<OperatorImpl, std::shared_ptr<OperatorImpl>, pyOperatorImpl>(m, "OperatorImpl", py::dynamic_attr())
    .def(py::init<const Operator&, const std::string&>(), py::keep_alive<1, 1>(), py::keep_alive<1, 2>(), py::keep_alive<1,3>())
    .def("forward", &OperatorImpl::forward)
    .def("backward", &OperatorImpl::backward)
    .def("get_nb_required_data", &OperatorImpl::getNbRequiredData)
    .def("get_nb_required_protected", &OperatorImpl::getNbRequiredProtected)
    .def("get_required_memory", &OperatorImpl::getRequiredMemory)
    .def("get_nb_consumed_data", &OperatorImpl::getNbConsumedData)
    .def("get_nb_produced_data", &OperatorImpl::getNbProducedData)
    .def("update_consummer_producer", &OperatorImpl::updateConsummerProducer)
    .def("reset_consummer_producer", &OperatorImpl::resetConsummerProducer)
    ;
}
}
