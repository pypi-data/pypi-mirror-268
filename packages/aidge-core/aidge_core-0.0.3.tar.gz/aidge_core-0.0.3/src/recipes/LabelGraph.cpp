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

#include <memory>

#include "aidge/recipes/LabelGraph.hpp"
#include "aidge/operator/Conv.hpp"
#include "aidge/operator/ConvDepthWise.hpp"
#include "aidge/operator/AvgPooling.hpp"
#include "aidge/operator/MaxPooling.hpp"

Aidge::NodePtr Aidge::nodeLabel(NodePtr node) {
    // Conv => MaxPooling
    if (node->type() == Conv_Op<2>::Type) {
        auto op = std::dynamic_pointer_cast<Conv_Op<2>>(node->getOperator());

        auto newOp = std::make_shared<MaxPooling_Op<2>>(op->template getAttr<ConvAttr::KernelDims>(), op->template getAttr<ConvAttr::StrideDims>());
        return std::make_shared<Node>(newOp, node->name());
    }

    // ConvDepthWise => MaxPooling
    if (node->type() == ConvDepthWise_Op<2>::Type) {
        auto op = std::dynamic_pointer_cast<ConvDepthWise_Op<2>>(node->getOperator());

        auto newOp = std::make_shared<MaxPooling_Op<2>>(op->template getAttr<ConvDepthWiseAttr::KernelDims>(), op->template getAttr<ConvDepthWiseAttr::StrideDims>());
        return std::make_shared<Node>(newOp, node->name());
    }

    // AvgPooling => MaxPooling
    if (node->type() == AvgPooling_Op<2>::Type) {
        auto op = std::dynamic_pointer_cast<AvgPooling_Op<2>>(node->getOperator());

        auto newOp = std::make_shared<MaxPooling_Op<2>>(op->template getAttr<AvgPoolingAttr::KernelDims>(), op->template getAttr<AvgPoolingAttr::StrideDims>());
        return std::make_shared<Node>(newOp, node->name());
    }

    // MaxPooling => MaxPooling
    if (node->type() == MaxPooling_Op<2>::Type) {
        return node->clone();
    }

    // By default, remove the node from the graph
    return nullptr;
}

std::shared_ptr<Aidge::GraphView> Aidge::labelGraph(std::shared_ptr<GraphView> graph) {
    return graph->cloneCallback(&nodeLabel);
}
