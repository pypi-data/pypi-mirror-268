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

#include "aidge/recipes/Recipes.hpp"
#include "aidge/operator/MetaOperator.hpp"

void Aidge::expandMetaOps(std::shared_ptr<GraphView> graph, bool recursive) {
    bool found = false;
    const auto nodes = graph->getNodes();
    for (auto node : nodes) {
        auto metaOp = std::dynamic_pointer_cast<MetaOperator_Op>(node->getOperator());

        if (metaOp != nullptr) {
            // Replace meta op by its micro-graph
            // graph will be updated accordingly in GraphView::replace()
            auto g = std::make_shared<GraphView>();
            g->add(node, false);
            GraphView::replace(g, metaOp->getMicroGraph());
            found = true;
        }
    }

    if (found && recursive) {
        expandMetaOps(graph, true);
    }
}
