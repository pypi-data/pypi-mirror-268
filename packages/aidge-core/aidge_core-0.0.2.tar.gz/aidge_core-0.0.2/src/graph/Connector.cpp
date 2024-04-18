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

#include "aidge/graph/Connector.hpp"

#include <map>

#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"

Aidge::Connector::Connector(std::shared_ptr<Aidge::Node> node) {
    mNode = node;
    if (mNode->nbOutputs() == 1U) {
        mOutputId = 0;
    }
}

Aidge::IOIndex_t Aidge::Connector::size() const { return mNode->nbOutputs(); }

std::shared_ptr<Aidge::GraphView> Aidge::generateGraph(std::vector<Connector> ctors) {
    std::shared_ptr<GraphView> graph = std::make_shared<GraphView>();
    std::vector<std::shared_ptr<Node>> nodesToAdd = std::vector<std::shared_ptr<Node>>();
    for (const Connector& ctor : ctors) {
        nodesToAdd.push_back(ctor.node());
    }
    std::vector<std::shared_ptr<Node>> buffer = {};

    while (!nodesToAdd.empty()) {
        while (!nodesToAdd.empty()) {
            graph->add(nodesToAdd.back());  // only add, connection already done
                                            // between nodes
            std::vector<std::shared_ptr<Node>> parents = nodesToAdd.back()->getParents();
            const std::set<std::shared_ptr<Node>>& alreadyAdded = graph->getNodes();
            for (std::shared_ptr<Node> parent : parents) {
                if (!parent) continue;
                if (alreadyAdded.find(parent) == alreadyAdded.end()) {
                    buffer.push_back(parent);
                }
            }
            nodesToAdd.pop_back();
        }
        nodesToAdd.insert(nodesToAdd.end(), buffer.begin(), buffer.end());
        buffer = {};
    }
    return graph;
}
