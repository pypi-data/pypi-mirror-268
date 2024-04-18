/********************************************************************************
 * Copyright (c) 2024 CEA-List
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 ********************************************************************************/

#ifndef AIDGE_CORE_OPERATOR_HARDMAX_H_
#define AIDGE_CORE_OPERATOR_HARDMAX_H_

#include <cassert>
#include <memory>
#include <vector>

#include "aidge/utils/Registrar.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
// First we declare an Enum for the attributes, Hardmax has one attribute which is Axis
enum class HardmaxAttr { Axis };

// Then we define the class Hardmax_Op. The third parent is only used if we want our operator to have attributes which is the case for Hardmax (Axis)
//
// The registrable inheritance creates a static class attribute of Registrable : Registrar<HardMax_Op> that will hold a map.
// This map will have as key a backend and as value a list of unique ids for every operator HardMax_Op created
// The registrable inheritance creates a static class attribute of Registrable : Registrar<HardMax_Op> that will hold a map.
// This map will have as key a string describing de the backend (e.g. "cuda") and as value a function which will create an HardMax implementation for the aforementioned backend.
class Hardmax_Op : public OperatorTensor,
                public Registrable<Hardmax_Op,
                                   std::string,
                                   std::unique_ptr<OperatorImpl>(const Hardmax_Op&)>,
                public StaticAttributes<HardmaxAttr, int> {

public:
    static const std::string Type;
    // We need to delete the default constructor because the axis attribute is mandatory
    Hardmax_Op() = delete;

    // Now we call our constructor
    using Attributes_ = StaticAttributes<HardmaxAttr, int>;
    template <HardmaxAttr e> using attr = typename Attributes_::template attr<e>;
    Hardmax_Op(int axis) : OperatorTensor(Type, 1, 0, 1),
                           Attributes_(attr<HardmaxAttr::Axis>(axis))
    {}
    // Notice how we called the parent constructor OperatorTensor(Type, 1, 0, 1). The meaning of the arguments are : 
    // 1. The operation Type : here "Hardmax".
    // 2. The number of Tensor Inputs, here hardmax takes only the input tensor to compute so the argument is 1.
    // 3. The number of (learnable) parameter Tensor inputs : 
    //           Here, a hardmax is a constant operation so none are used
    //           But for a 2D convolution operator, the value is 2: 1 for the filters & 1 for the biases.
    // 4. The number of Tensor outputs.

    //Then we define the copy and clone constructors
    Hardmax_Op(const Hardmax_Op& op)
        : OperatorTensor(op),
          Attributes_(op)
    {
        // mImpl is the implementation of the operator. It contains its data, memory size and backend. 
        // Since each tensorOperator has a unique id in the registrar we cannot simply copy op.mImpl. 
        // Hence here we retrieve the backend of the output tensor of op to create a new implementation object.
        // The output tensor is chosen by convention to get the backend since not all operators have inputs but all have at least one output.
        mImpl = op.mImpl ? Registrar<Hardmax_Op>::create(op.mOutputs[0]->getImpl()->backend())(*this) : nullptr;
    }

    std::shared_ptr<Operator> clone() const override { return std::make_shared<Hardmax_Op>(*this); }

    // Next is to define the output dimensions. For the case of Hardmax, the output has the same shape as input so we dont need to override the OperatorTensor's computeOutputDims. Otherwise, we need to override it in the cpp file. 
    // void computeOutputDims() override final;

    // We also need to define the method to set the backend for the operator
    void setBackend(const std::string& name, DeviceIdx_t device = 0) override {
        mImpl = Registrar<Hardmax_Op>::create(name)(*this);
        mOutputs[0]->setBackend(name, device);
    }

    // The last methods are getInputsName and getOutputsName
    static const std::vector<std::string> getInputsName(){ return {"data_input"}; }
    static const std::vector<std::string> getOutputsName(){ return {"data_output"}; }
};

// Finally, we declare the function to create the node for this operator
inline std::shared_ptr<Node> Hardmax(int axis = 0, const std::string& name = "") {
    return std::make_shared<Node>(std::make_shared<Hardmax_Op>(axis), name);
}

namespace {
template <>
const char *const EnumStrings<Aidge::HardmaxAttr>::data[] = {"Axis"};
}
}
#endif /* AIDGE_CORE_OPERATOR_HARDMAX_H_ */
