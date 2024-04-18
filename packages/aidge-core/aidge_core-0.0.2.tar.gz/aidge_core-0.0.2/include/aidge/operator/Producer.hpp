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

#ifndef AIDGE_CORE_OPERATOR_PRODUCER_H_
#define AIDGE_CORE_OPERATOR_PRODUCER_H_

#include <cstddef>
#include <array>
#include <memory>
#include <vector>

#include "aidge/utils/Types.h"
#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/Registrar.hpp"

namespace Aidge {

enum class ProdAttr { Constant };

class Producer_Op
    : public OperatorTensor,
      public Registrable<Producer_Op, std::string, std::shared_ptr<OperatorImpl>(
                                          const Producer_Op &)>,
      public StaticAttributes<ProdAttr, bool> {
public:
    static const std::string Type;

    using Attributes_ = StaticAttributes<ProdAttr, bool>;
    template <ProdAttr e>
    using attr = typename Attributes_::template attr<e>;

    template <std::size_t DIM>
    Producer_Op(const std::array<DimSize_t, DIM>& dims,
                bool constant = false)
        : OperatorTensor(Type, 0, 0, 1),
          Attributes_(attr<ProdAttr::Constant>(constant))
    {
        mOutputs[0]->resize(dims);
        mImpl = std::make_shared<OperatorImpl>(*this, "");
    }

    /**
     * @brief Construct a new Producer_Op object from a Tensor.
     *
     * @param tensor Tensor to set in the Prducer.
     * @param constant Whether the Producer should be considered constant.
     */
    Producer_Op(const std::shared_ptr<Tensor> tensor, bool constant = false);

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s),
     * but not its input tensors (the new operator has no input associated).
     * @param op OperatorTensor to copy.
     */
    Producer_Op(const Producer_Op& op);

public:
    /**
     * @brief Conversion operator from Producer to Tensor.
     *
     * @return std::shared_ptr<Tensor>
     */
    operator std::shared_ptr<Tensor>() const { return mOutputs[0]; }

public:
    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::Producer_Op(const Producer_Op&)
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<Producer_Op>(*this);
    }

    void associateInput(const IOIndex_t /*inputIdx*/, const std::shared_ptr<Data>& /*data*/) override final {
        AIDGE_THROW_OR_ABORT(std::runtime_error, "Producer operator takes no input.");
    }

    void computeOutputDims() noexcept override final {}

    inline bool outputDimsForwarded() const noexcept override final { return true; }


    inline const std::vector<DimSize_t> dims() const noexcept { return mOutputs[0]->dims(); }

    void setBackend(const std::string& name, DeviceIdx_t device = 0) override;

    static const std::vector<std::string> getInputsName(){
        return {};
    }
    static const std::vector<std::string> getOutputsName(){
        return {"data_output"};
    }

    void forward() override final {
        fmt::print("Basic Producer forward() function.\n");
    }
    void backward() override final {
        fmt::print("Basic Producer backward() function.\n");
    }
    void setOutput(const Aidge::IOIndex_t outputIdx, std::shared_ptr<Aidge::Data>&& data) override {
        if (getAttr<ProdAttr::Constant>()) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Producer is constant, cannot update output.");
        }
        OperatorTensor::setOutput(outputIdx, std::move(data));
    }

    void setOutput(const Aidge::IOIndex_t outputIdx, const std::shared_ptr<Aidge::Data>& data) override {
        if (getAttr<ProdAttr::Constant>()) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Producer is constant, cannot update output.");
        }
        OperatorTensor::setOutput(outputIdx, data);
    }
};

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> Producer(const std::array<DimSize_t, DIM> &dims, const std::string& name = "", bool constant = false) {
  static_assert(DIM<=MaxDim,"Too many tensor dimensions required by Producer, not supported");
  return std::make_shared<Node>(std::make_shared<Producer_Op>(dims, constant), name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <std::size_t DIM>
inline std::shared_ptr<Node> Producer(DimSize_t const (&dims)[DIM], const std::string& name = "", bool constant = false) {
  return Producer(to_array(dims), name, constant);
}

inline std::shared_ptr<Node> Producer(const std::shared_ptr<Tensor> tensor, const std::string& name = "", bool constant = false) {
  return std::make_shared<Node>(std::make_shared<Producer_Op>(tensor, constant), name);
}

template <std::array<DimSize_t, 1>::size_type DIM>
void addProducer(std::shared_ptr<Node>& otherNode, const IOIndex_t inputIdx, const std::array<DimSize_t, DIM>& dims, const std::string& extension) {
    assert(inputIdx != gk_IODefaultIndex);
    static_assert(DIM<=MaxDim,"Too many tensor dimensions required by addProducer, not supported");
    const std::string prodName = (otherNode->name().empty()) ? "" : (otherNode->name() + std::string("_") + extension);
    auto prod = Producer(dims, prodName);
    prod->addChild(otherNode, 0, inputIdx);
    otherNode->getOperator()->associateInput(inputIdx, prod->getOperator()->getRawOutput(0));
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <std::size_t DIM>
void addProducer(std::shared_ptr<Node>& otherNode, const IOIndex_t inputIdx, DimSize_t const (&dims)[DIM], const std::string& extension) {
    addProducer(otherNode, inputIdx, to_array(dims), extension);
}
} // namespace Aidge

namespace {
template <>
const char *const EnumStrings<Aidge::ProdAttr>::data[] = {
    "Constant"
};
}
#endif /* AIDGE_CORE_OPERATOR_PRODUCER_H_ */
