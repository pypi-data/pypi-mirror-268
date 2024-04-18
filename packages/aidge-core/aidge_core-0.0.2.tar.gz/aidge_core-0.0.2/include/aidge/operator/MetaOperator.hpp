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

#ifndef AIDGE_CORE_OPERATOR_METAOPERATOR_H_
#define AIDGE_CORE_OPERATOR_METAOPERATOR_H_

#include <array>
#include <memory>
#include <string>

#include "aidge/data/Data.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/OpArgs.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/scheduler/SequentialScheduler.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
class MetaOperator_Op : public OperatorTensor,
                public Registrable<MetaOperator_Op, std::array<std::string, 2>, std::unique_ptr<OperatorImpl>(const MetaOperator_Op &)> {
public:
    // outputs shared with micro-graph output Tensors
    // Micro-graph handling:
    std::shared_ptr<GraphView> mGraph; // Meta operator micro-graph
    std::shared_ptr<SequentialScheduler> mScheduler;
    std::weak_ptr<Node> mUpperNode;

   public:
    MetaOperator_Op(const std::string& type, const std::shared_ptr<GraphView>& graph);

    /**
     * @brief Copy-constructor. Copy the operator attributes and its output tensor(s), but not its input tensors (the new operator has no input associated).
     * @param op Operator to copy.
     */
    MetaOperator_Op(const MetaOperator_Op& op)
        : OperatorTensor(op),
          mGraph(op.mGraph->clone())
    {}

    /**
     * Set the node that should be used for the scheduling.
    */
    void setUpperNode(std::shared_ptr<Node> node) {
        mUpperNode = node;
    }

    /**
     * @brief Clone the operator using its copy-constructor.
     * @see Operator::MetaOperator_Op
     */
    std::shared_ptr<Operator> clone() const override {
        return std::make_shared<MetaOperator_Op>(*this);
    }

    inline const std::shared_ptr<GraphView>& getMicroGraph() const noexcept {
        return mGraph;
    }

    inline const std::shared_ptr<SequentialScheduler>& getMicroGraphScheduler() const noexcept {
        return mScheduler;
    }

    void associateInput(const IOIndex_t inputIdx, const std::shared_ptr<Data>& data) override final {
        AIDGE_ASSERT(data->type() == Tensor::Type, "input data must be of Tensor type");
        AIDGE_ASSERT(inputIdx < mGraph->getOrderedInputs().size(), "associateInput(): inputIdx ({}) out of bound for MetaOperator", inputIdx);

        const auto& inputOp = mGraph->getOrderedInputs()[inputIdx];
        inputOp.first->getOperator()->associateInput(inputOp.second, data);

        // Associate inputs for custom implementation
        mInputs[inputIdx] = std::dynamic_pointer_cast<Tensor>(data);
    }

    void computeOutputDims() override final {
        // Check first that all required inputs are available, otherwise
        // mGraph->forwardDims() will fail!
        bool forwarded = true;
        for (IOIndex_t i = 0; i < nbInputs(); ++i) {
            forwarded &= mInputs[i] ? !(getInput(i)->empty()) : false;
        }

        if (forwarded) {
            // Forward dims of micro-graph
            mGraph->forwardDims();
        }
    }


    void setBackend(const std::string &name, DeviceIdx_t device = 0) override {
        if (Registrar<MetaOperator_Op>::exists({name, type()})) {
            // A custom implementation exists for this meta operator
            mImpl = Registrar<MetaOperator_Op>::create({name, type()})(*this);
        }

        // The micro-graph should always be set to the right backend, since it
        // shares input/output tensors.
        // Input/output tensors backend are updated here.
        mGraph->setBackend(name, device);
    }

    void setDataType(const DataType &datatype) const override {
        // The micro-graph should always be set to the right data type, since it
        // shares input/output tensors.
        // Input/output tensors data type are updated here.
        mGraph->setDataType(datatype);
    }

    Elts_t getNbRequiredData(const IOIndex_t inputIdx) const override;
    Elts_t getNbRequiredProtected(const IOIndex_t inputIdx) const override;
    Elts_t getRequiredMemory(const IOIndex_t outputIdx, const std::vector<DimSize_t> &inputsSize) const override;
    Elts_t getNbConsumedData(IOIndex_t inputIdx) const override;
    Elts_t getNbProducedData(IOIndex_t outputIdx) const override;

    void updateConsummerProducer() override;
    void forward() override;
    void backward() override {
        assert(false && "not implemented");
    }

    inline bool isAtomic() const noexcept override final { return false; }

};

inline std::shared_ptr<Node> MetaOperator(const char *type,
                                  const std::shared_ptr<GraphView>& graph,
                                  const std::string& name = "")
{
    auto op = std::make_shared<MetaOperator_Op>(type, graph);
    auto node = std::make_shared<Node>(op, name);
    op->setUpperNode(node);
    return node;
}
}  // namespace Aidge

#endif /* MetaOperator_H_ */
