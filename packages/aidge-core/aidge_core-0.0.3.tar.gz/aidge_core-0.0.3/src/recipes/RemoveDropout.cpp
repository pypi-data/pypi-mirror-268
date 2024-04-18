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

#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/recipes/Recipes.hpp"

//Graph Regex
#include "aidge/graphRegex/GraphRegex.hpp"


namespace Aidge {
    void removeDropout(std::shared_ptr<Node> dropout) {

        std::set<NodePtr> nodesToRemove;
        for (auto nodePtr: dropout->getParents())
        {
            if(nodePtr->type() == "Producer")
            {
                nodesToRemove.insert(nodePtr);
            }
        }
        nodesToRemove.insert(dropout);
        GraphView::replace(nodesToRemove, {});
    }

    void removeDropout(std::shared_ptr<MatchSolution> solution){

        assert(solution->at("Dropout").size() == 1 && "Wrong number of nodes Dropout to replace\n");

        for (const auto& dropout : solution->at("Dropout")) {

            removeDropout(dropout);
        }
    }

    void removeDropout(std::shared_ptr<GraphView> graphView){
        std::shared_ptr<GraphRegex> regex = std::make_shared<GraphRegex>();
        regex->setNodeKey("Dropout","getType($) =='Dropout'");
        regex->addQuery("Dropout#");

        for (const auto& solution : regex->match(graphView)) {
            removeDropout(solution);
        }
    }
}
