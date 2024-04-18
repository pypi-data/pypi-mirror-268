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

#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/OpArgs.hpp"


std::shared_ptr<Aidge::GraphView> Aidge::Sequential(std::vector<OpArgs> inputs) {
    std::shared_ptr<GraphView> gv = std::make_shared<GraphView>();
    for (const OpArgs& elt : inputs) {
        if(elt.node() != nullptr) {
            // >= to allow incomplete graphViews
            assert(static_cast<std::size_t>(elt.node()->getNbFreeDataInputs()) >= gv->outputNodes().size());
            /*
            *  /!\ mn.view()->outputNodes() is a set, order of Nodes cannot be guaranted.
            *  Prefer a functional description for detailed inputs
            */
            for (const std::shared_ptr<Node>& node_ptr : gv->outputNodes()) {
                node_ptr -> addChild(elt.node()); // already checks that node_ptr->nbOutput() == 1
            }
            gv->add(elt.node());
        }
        else {
            for (std::shared_ptr<Node> node_in : elt.view()->inputNodes()) {
                // >= to allow incomplete graphViews
                assert(static_cast<std::size_t>(node_in->getNbFreeDataInputs()) >= gv->outputNodes().size());
                for (std::shared_ptr<Node> node_out : gv->outputNodes()) {
                    node_out -> addChild(node_in); // assert one output Tensor per output Node
                }
            }
            gv->add(elt.view());
        }
    }
    return gv;
}


std::shared_ptr<Aidge::GraphView> Aidge::Parallel(std::vector<OpArgs> inputs) {
    std::shared_ptr<GraphView> gv = std::make_shared<GraphView>();
    for(const OpArgs& elt : inputs) {
        if (elt.node()!=nullptr)
            gv->add(elt.node());
        else
            gv->add(elt.view());
    }
    return gv;
}


std::shared_ptr<Aidge::GraphView> Aidge::Residual(std::vector<OpArgs> inputs) {
    std::shared_ptr<GraphView> gv = Sequential(inputs);
    assert(gv->outputNodes().size() == 1U && "Zero or more than one output Node for the GraphView, don't know which one to choose from for the residual connection");
    std::shared_ptr<Node> lastNode = *gv->outputNodes().begin();
    assert(gv->inputNodes().size() == 2U && "Zero or more than one input Node for the GraphView, don't know which one to choose from for the residual connection");
    std::shared_ptr<Node> firstNode = nullptr;
    for (const std::shared_ptr<Node>& node_ptr : gv->inputNodes()) {
        if (node_ptr != lastNode) {
            firstNode = node_ptr;
        }
    }
    assert(lastNode->getNbFreeDataInputs()>=1);
    gv->addChild(lastNode, firstNode, 0U, gk_IODefaultIndex);
    return gv;
}
