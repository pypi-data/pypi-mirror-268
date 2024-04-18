// /********************************************************************************
//  * Copyright (c) 2023 CEA-List
//  *
//  * This program and the accompanying materials are made available under the
//  * terms of the Eclipse Public License 2.0 which is available at
//  * http://www.eclipse.org/legal/epl-2.0.
//  *
//  * SPDX-License-Identifier: EPL-2.0
//  *
//  ********************************************************************************/

// #ifndef AIDGE_CORE_OPERATOR_TRANSMITTER_H_
// #define AIDGE_CORE_OPERATOR_TRANSMITTER_H_

// #include <cassert>
// #include <memory>
// #include <vector>

// #include "aidge/utils/Registrar.hpp"
// #include "aidge/operator/Operator.hpp"
// #include "aidge/backend/OperatorImpl.hpp"
// #include "aidge/data/Tensor.hpp"
// #include "aidge/data/Data.hpp"
// #include "aidge/graph/Node.hpp"
// #include "aidge/utils/Types.h"

// namespace Aidge {

// class Transmitter_Op : public Operator,
//     public Registrable<Transmitter_Op, std::pair<std::string, std::string>, std::unique_ptr<OperatorImpl>(const Transmitter_Op&)> {
// public:
//     // FIXME: change accessibility
//     std::shared_ptr<Tensor> mInput = std::make_shared<Tensor>();
//     const std::shared_ptr<Tensor> mOutput = std::make_shared<Tensor>();
//     const std::string mOriginBackend;
//     const std::string mTargetBackend;

// public:
//     static constexpr const char* Type = "Transmitter";

//     Transmitter_Op()
//             : Operator(Type)
//     {
//         setDatatype(DataType::Float32);
//     }

//     void associateInput(const IOIndex_t /*inputIdx*/, std::shared_ptr<Data> data) override final {
//         // (void) inputIdx; // avoid unused warning
//         assert(strcmp(data->type(), Tensor::Type)==0 && "input data must be of Tensor type");
//         mInput = std::dynamic_pointer_cast<Tensor>(data);
//     }

//     void computeOutputDims() override final {
//         if (!mInput->empty())
//             mOutput->resize(mInput->dims());
//     }

//     bool outputDimsForwarded() const override final {
//         return !(mOutput->empty());
//     }


//     inline Tensor& input(const IOIndex_t /*inputIdx*/) const override final {
//         return *(mInput.get());
//     }
//     inline Tensor& output(const IOIndex_t /*outputIdx*/) const override final { return *(mOutput.get()); }


//     inline std::shared_ptr<Tensor> getInput(const IOIndex_t inputIdx) const override final {
//         assert(inputIdx == 0 && "operator supports only 1 input");
//         (void) inputIdx; // avoid unused warning
//         return mInput;
//     }
//     inline std::shared_ptr<Tensor> getOutput(const IOIndex_t outputIdx) const override final {
//         assert((outputIdx == 0) && "Mul Operator has only 1 output");
//         (void) outputIdx; // avoid unused warning
//         return mOutput;
//     }


//     std::shared_ptr<Data> getRawInput(const IOIndex_t inputIdx) const override final {
//         assert(inputIdx == 0 && "operator supports only 1 input");
//         (void) inputIdx; // avoid unused warning
//         return std::static_pointer_cast<Data>(mInput);
//     }
//     std::shared_ptr<Data> getRawOutput(const IOIndex_t outputIdx) const override final {
//         assert(outputIdx == 0 && "operator supports only 1 output");
//         (void) outputIdx; // avoid unused warning
//         return std::static_pointer_cast<Data>(mOutput);
//     }

//     // HOW TO ADAPT SET BACKEND FOR TRANSMITTERS ?
//     void setBackend(const std::string& name) override {
//         mImpl = Registrar<Transmitter_Op>::create(name)(*this);
//         mOutput->setBackend(name);

//         // FIXME: temporary workaround
//         mInput->setBackend(name);
//     }
//     void setDatatype(const DataType& datatype) override {
//         mOutput->setDatatype(datatype);

//         // FIXME: temporary workaround
//         mInput->setDatatype(datatype);
//     }

//     inline IOIndex_t nbInputs() const noexcept override final { return 1; }
//     inline IOIndex_t nbDataInputs() const noexcept override final { return 1; }
//     inline IOIndex_t nbOutputs() const noexcept override final { return 1; }
//     static const std::vector<std::string> getInputsName(){
//         return {"data_input"};
//     }
//     static const std::vector<std::string> getOutputsName(){
//         return {"data_output"};
//     }
// };

// inline std::shared_ptr<Node> Transmitter(const std::string& name = "") {
//     return std::make_shared<Node>(std::make_shared<Transmitter_Op>(), name);
// }
// }

// #endif /* AIDGE_CORE_OPERATOR_TRANSMITTER_H_ */
