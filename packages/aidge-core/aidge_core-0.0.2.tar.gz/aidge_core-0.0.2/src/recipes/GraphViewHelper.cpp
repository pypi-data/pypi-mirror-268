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
#include <set>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/recipes/GraphViewHelper.hpp"


std::set<std::shared_ptr<Aidge::Tensor>> Aidge::producers(std::shared_ptr<Aidge::GraphView> graphview) {
    std::set<std::shared_ptr<Tensor>> res;
    const auto& nodes = graphview->getNodes();
    for (const auto& node : nodes) {
        if (node->type() == "Producer") {
            const auto& param = std::static_pointer_cast<OperatorTensor>(node->getOperator());
            res.insert(param->getOutput(0));
        }
    }
    return res;
}


std::set<std::shared_ptr<Aidge::Tensor>> Aidge::parameters(std::shared_ptr<Aidge::GraphView> graphview) {
    std::set<std::shared_ptr<Tensor>> res;
    const auto& nodes = graphview->getNodes();
    for (const auto& node : nodes) {
        const auto& param = std::static_pointer_cast<OperatorTensor>(node->getOperator());
        for (std::size_t o = 0; o < param->nbOutputs(); ++o) {
            res.insert(param->getOutput(o));
        }
    }
    return res;
}

void Aidge::compile_gradient(std::shared_ptr<Aidge::GraphView> gv) {
    for (const auto& node : gv->getNodes()) {
        // TODO: check that each node is an OperatorTensor
        AIDGE_ASSERT(node->getOperator()->operatorType() == OperatorType::Tensor, "Cannot instanciate gradient of an Operator ({}) that doesn't use Tensor.", node->getOperator()->type());
        const std::shared_ptr<OperatorTensor> op = std::dynamic_pointer_cast<OperatorTensor>(node -> getOperator());
        for (std::size_t o = 0; o < node -> nbOutputs(); ++o) {
            op->getOutput(o)->initGradient();
        }
    }
}