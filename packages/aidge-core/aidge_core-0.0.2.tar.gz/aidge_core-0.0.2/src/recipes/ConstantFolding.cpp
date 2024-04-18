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
#include <cassert>
#include <memory>
#include <set>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/recipes/Recipes.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

void Aidge::constantFolding(std::shared_ptr<GraphView> graph) {
    bool folded;
    do {
        folded = false;
        std::set<std::shared_ptr<Node>> candidates;
        for (const std::shared_ptr<Node>& nodePtr : graph->getNodes()) {
            if (nodePtr->type() == Producer_Op::Type) {
                const auto& childs = nodePtr->getChildren();
                candidates.insert(childs.begin(), childs.end());
            }
        }

        for (const auto& node : candidates) {
            bool foldable = true;
            auto replaceGraph = std::make_shared<GraphView>();
            for (const auto& input : node->inputs()) {
                if (input.first) {
                    if (input.first->type() != Producer_Op::Type) {
                        foldable = false;
                        break;
                    }

                    const auto& producer = std::static_pointer_cast<Producer_Op>(input.first->getOperator());
                    if (!producer->getAttr<bool>("Constant")) {
                        Log::info("Node {} (of type {}) not foldable because Producer input {} not Constant",
                            node->name(), node->type(), input.first->name());
                        foldable = false;
                        break;
                    }

                    replaceGraph->add(input.first, false);
                }
            }

            if (foldable) {
                Log::info("Folding node {} (of type {})", node->name(), node->type());
                replaceGraph->add(node, false);

                node->forward();

                auto prodGraph = std::make_shared<GraphView>();
                const auto op = std::static_pointer_cast<OperatorTensor>(node->getOperator());

                for (IOIndex_t output = 0; output < node->nbOutputs(); ++output) {
                    const auto computedOutput = std::make_shared<Tensor>(op->getOutput(output)->clone());
                    const auto newProd = Producer(computedOutput, node->name() + "_" + std::to_string(output), true);

                    // Add output in right order
                    prodGraph->add(newProd);
                }

                if (GraphView::replace(replaceGraph, prodGraph)) {
                    folded = true;
                }
                else {
                    Log::warn("Error with replace when folding node {} (of type {})",
                        node->name(), node->type());
                }
            }
        }
    }
    while (folded);
}
