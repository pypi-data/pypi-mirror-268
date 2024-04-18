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
    void removeFlatten(std::shared_ptr<Node> flatten) {
        GraphView::replace({flatten}, {});
    }

    void removeFlatten(std::shared_ptr<MatchSolution> solution){

        assert(solution->at("FC").size() == 1 && "Wrong number of nodes FC to replace\n");
        assert(solution->at("Flatten").size() == 1 && "Wrong number of nodes Flatten to replace\n");

        for (const auto& flatten : solution->at("Flatten")) {
            removeFlatten(flatten);
        }
    }



    void removeFlatten(std::shared_ptr<GraphView> graphView){
      

        std::shared_ptr<GraphRegex> regex = std::make_shared<GraphRegex>();
        regex->setNodeKey("Flatten","getType($) =='Flatten'");
        regex->setNodeKey("FC","getType($) =='FC'");
        regex->addQuery("Flatten->FC");

        for (const auto& solution : regex->match(graphView)) {
            removeFlatten(solution);
        }


    }
}
