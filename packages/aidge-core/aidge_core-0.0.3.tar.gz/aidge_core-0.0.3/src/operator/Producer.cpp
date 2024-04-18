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

#include "aidge/operator/Producer.hpp"

#include <cstddef>
#include <array>
#include <memory>
#include <string>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"


const std::string Aidge::Producer_Op::Type = "Producer";


Aidge::Producer_Op::Producer_Op(const std::shared_ptr<Aidge::Tensor> tensor, bool constant)
    : OperatorTensor(Type, 0, 0, 1),
      Attributes_(attr<ProdAttr::Constant>(constant))
{
    mOutputs[0] = tensor; // copy the pointer of the Tensor
#ifdef PYBIND
    if(Py_IsInitialized()) {
        auto obj = py::cast(&(*this));
        setImpl((mOutputs[0]->hasImpl()) ?
            (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
            std::make_shared<OperatorImpl>(*this, ""));
    } else {
        setImpl((mOutputs[0]->hasImpl()) ?
            (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
            std::make_shared<OperatorImpl>(*this, ""));
    }
#else
    setImpl((mOutputs[0]->hasImpl()) ?
                (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                    Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                    std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
                std::make_shared<OperatorImpl>(*this, ""));
#endif
}

/**
 * @brief Copy-constructor. Copy the operator attributes and its output tensor(s),
 * but not its input tensors (the new operator has no input associated).
 * @param op OperatorTensor to copy.
 */
Aidge::Producer_Op::Producer_Op(const Aidge::Producer_Op& op)
    : OperatorTensor(op),
      Attributes_(op)
{
    mOutputs[0] = std::make_shared<Tensor>(*(op.getOutput(0)));
#ifdef PYBIND
    if(Py_IsInitialized()) {
            auto obj = py::cast(&(*this));
            setImpl((mOutputs[0]->hasImpl()) ?
                (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                    Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                    std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
                std::make_shared<OperatorImpl>(*this, ""));
        } else {
            setImpl((mOutputs[0]->hasImpl()) ?
                (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                    Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                    std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
                std::make_shared<OperatorImpl>(*this, ""));
        }
#else
    setImpl((mOutputs[0]->hasImpl()) ?
                (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()}) ?
                    Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this) :
                    std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend())) :
                std::make_shared<OperatorImpl>(*this, ""));
#endif
    // if (mOutputs[0]->hasImpl()) {
        // if (Registrar<Producer_Op>::exists({mOutputs[0]->getImpl()->backend()})){
        //     setImpl(Registrar<Producer_Op>::create(mOutputs[0]->getImpl()->backend())(*this));
        // }
        // else  {
        //     mImpl = std::make_shared<OperatorImpl>(*this, mOutputs[0]->getImpl()->backend());
        // }

    // } else {
    //     mImpl = nullptr;
    // }
}

void Aidge::Producer_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
#ifdef PYBIND
    if(Py_IsInitialized()) {
            auto obj = py::cast(&(*this));
            setImpl((Registrar<Producer_Op>::exists({name})) ?
                    Registrar<Producer_Op>::create(name)(*this) :
                    std::make_shared<OperatorImpl>(*this, ""));
        } else {
            setImpl((Registrar<Producer_Op>::exists({name})) ?
                    Registrar<Producer_Op>::create(name)(*this) :
                    std::make_shared<OperatorImpl>(*this, ""));
        }
#else
    setImpl((Registrar<Producer_Op>::exists({name})) ?
        Registrar<Producer_Op>::create(name)(*this) :
        std::make_shared<OperatorImpl>(*this, ""));
#endif
    mOutputs[0]->setBackend(name, device);
}