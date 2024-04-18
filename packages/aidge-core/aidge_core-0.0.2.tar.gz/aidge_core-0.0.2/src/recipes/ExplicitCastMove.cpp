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

#include "aidge/recipes/Recipes.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Cast.hpp"
#include "aidge/operator/Move.hpp"

void Aidge::explicitCastMove(std::shared_ptr<GraphView> graph) {
    // First, remove existing Cast and Move operators, if not needed anymore
    auto nodes = graph->getNodes();
    for (auto node : nodes) {
        // TODO: currently, Operator data type is only reflected in its output tensor data type.
        // But an Operator might have multiple outputs of different data type(?)
        AIDGE_ASSERT(node->getOperator()->operatorType() == OperatorType::Tensor, "Operator must be of Tensor type.");
        const auto& output = std::static_pointer_cast<OperatorTensor>(node->getOperator())->getOutput(0);
        if (output->getImpl() == nullptr) {
            continue;
        }
        const auto& device = output->getImpl()->device();

        if (node->type() == Cast_Op::Type || node->type() == Move_Op::Type) {
            // Remove existing Cast and Move operators, if not needed anymore
            AIDGE_INTERNAL_ASSERT(node->inputs().size() == 1);
            const auto parent = node->inputs()[0];
            // Check parent is not nullptr, as this Operator may be an entry point of the graph without parent
            if (parent.first != nullptr) {
                AIDGE_ASSERT(parent.first->getOperator()->operatorType() == OperatorType::Tensor, "Operator must be of Tensor type.");
                const auto& input = std::static_pointer_cast<OperatorTensor>(parent.first->getOperator())->getOutput(parent.second);

                if ((node->type() == Cast_Op::Type && input->dataType() == output->dataType())
                    || (node->type() == Move_Op::Type && input->getImpl() != nullptr && input->getImpl()->device() == device))
                {
                    // Add direct connection bypassing Cast/Move node
                    const auto childs = node->outputs()[0];
                    for (const auto& child : childs) {
                        parent.first->addChild(child.first, parent.second, child.second);
                    }

                    // Remove all node connections
                    node->resetConnections();
                    // Remove node from view
                    graph->remove(node);
                }
            }
        }
    }

    // Note: why two steps and not merge the two node loops?
    // User may have changed some data type/backends on top of existing Cast/Move operators
    // This may lead to situation where a Cast should be removed but a Move should
    // be inserted at the same place. In this case, some conversion may be missed
    // depending on the order of iteration over the nodes (which are non ordered!).

    // Second, insert Cast and/or Move operator between node inputs and parent output, if needed
    nodes = graph->getNodes();
    for (auto node : nodes) {
        // TODO: currently, Operator data type is only reflected in its output tensor data type.
        // But an Operator might have multiple outputs of different data type(?)
        const auto& output = std::static_pointer_cast<OperatorTensor>(node->getOperator())->getOutput(0);
        if (output->getImpl() == nullptr) {
            continue;
        }
        const auto& device = output->getImpl()->device();

        IOIndex_t inputIdx = 0;
        for (auto parent : node->inputs()) {
            // TODO: possible optimization: currently, a Cast/Move Operator may 
            // be added several time to the same output, if it has multiple childs,
            // even if it is the same conversion each time.
            if (parent.first != nullptr) {
                const auto& input = std::static_pointer_cast<OperatorTensor>(parent.first->getOperator())->getOutput(parent.second);

                NodePtr moveOp = nullptr;
                NodePtr castOp = nullptr;

                if (node->type() != Move_Op::Type && input->getImpl()->device() != device) {
                    // Change of backend => a Move operator is required
                    moveOp = Move();
                    moveOp->getOperator()->setDataType(input->dataType());
                    castOp = moveOp;
                }

                if (node->type() != Cast_Op::Type && input->dataType() != output->dataType()) {
                    // Change of date type => a Cast operator is required
                    castOp = Cast();
                    castOp->getOperator()->setDataType(output->dataType());
                    castOp->getOperator()->setBackend(device.first, device.second);

                    if (moveOp == nullptr) {
                        moveOp = castOp;
                    }
                    else {
                        moveOp->addChild(castOp, 0, 0);
                    }
                }

                if (moveOp != nullptr && castOp != nullptr) {
                    // Move and/or Cast Operator(s) are needed
                    castOp->addChild(node, 0, inputIdx);
                    parent.first->addChild(moveOp, parent.second, 0);
                    // Set backend AFTER connection in case a specific implementation
                    // of the operator exists for the input type.
                    moveOp->getOperator()->setBackend(device.first, device.second);

                    // Add/update nodes in the GraphView
                    graph->add(moveOp);
                    graph->add(castOp);
                    graph->add(parent.first);
                    graph->add(node);
                }
            }

            ++inputIdx;
        }
    }
}
