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

#include <set>
#include <cassert>
#include <memory>
#include <string>

#include "aidge/operator/FC.hpp"
#include "aidge/recipes/Recipes.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/operator/GenericOperator.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/operator/MatMul.hpp"

//Graph Regex
#include "aidge/graphRegex/GraphRegex.hpp"


void Aidge::fuseMulAdd(std::shared_ptr<Aidge::Node> matmulNode, std::shared_ptr<Aidge::Node> addNode) { //std::set<std::shared_ptr<Node>> nodes){
    // Fuse Mulmat & Add into FC
    // Inputs : old nodes (pointers on mul & add)

    assert((matmulNode->type() == "MatMul" && addNode->type() == "Add") && "Wrong type for the nodes to replace");


    // Step 1 : Create FC
    // Fetch the output dimension throught the bias size
    std::shared_ptr<Node> bias = nullptr;
    if (addNode->getParent(0) == matmulNode) {
        AIDGE_ASSERT(matmulNode->getParent(1), "No bias detected to produce the fuseMulAdd recipe.");
        bias = addNode->getParent(1);
    }
    else if (addNode->getParent(1) == matmulNode) {
        AIDGE_ASSERT(matmulNode->getParent(0), "No bias detected to produce the fuseMulAdd recipe.");
        bias = addNode->getParent(0);
    }

    std::shared_ptr<Node> weight = nullptr;
    if ((matmulNode->getParent(1) && !matmulNode->getParent(0))
        || (matmulNode->getParent(1) && matmulNode->getParent(1)->getOperator()->type() == Producer_Op::Type
            && matmulNode->getParent(0) && matmulNode->getParent(0)->getOperator()->type() != Producer_Op::Type))
    {
        weight = matmulNode->getParent(1);
    }
    else if ((matmulNode->getParent(0) && !matmulNode->getParent(1))
        || (matmulNode->getParent(0) && matmulNode->getParent(0)->getOperator()->type() == Producer_Op::Type
            && matmulNode->getParent(1) && matmulNode->getParent(1)->getOperator()->type() != Producer_Op::Type))
    {
        weight = matmulNode->getParent(0);
    }
    else if (matmulNode->getParent(0) && matmulNode->getParent(0)->getOperator()->type() == Producer_Op::Type
        && matmulNode->getParent(1) && matmulNode->getParent(1)->getOperator()->type() == Producer_Op::Type)
    {
        // If both inputs are producers, there is an ambiguity, but both options
        // result in a correct solution.
        Log::notice("Notice: both MatMul inputs are Producers, assume data at input#0 and weights at input#1.");
        weight = matmulNode->getParent(1);
    }
    AIDGE_ASSERT(weight != nullptr, "Could not deduce weight input for MatMul operator.");

    // TODO: find another way to get OutChannels for FC operator.
    // This poor fix supposes that one of Add inputs is a const and has the same outChannels as the output
    DimSize_t outSize = 0;
    AIDGE_ASSERT(addNode->getOperator()->operatorType() == OperatorType::Tensor, "Operator must be of Tensor type.");
    const auto& op = std::static_pointer_cast<OperatorTensor>(addNode->getOperator());
    for (size_t i = 0; i < op->nbInputs(); i++)
    {
        const auto& inTensor = op->getInput(i);
        if(inTensor->nbDims() > 0) {
            outSize = inTensor->dims()[inTensor->nbDims()-1];
            break;
        }
    }
    AIDGE_ASSERT(outSize, "Couldnt get output number of channels for FC operator.");

    // Instanciate FC
    //std::shared_ptr<Node> fc = FC(dim[0], false, "Fc");
    std::shared_ptr<Node> fc = std::make_shared<Node>(std::make_shared<FC_Op>(outSize, bias ? false : true));

    // Step 2 : Branch existing producers & create the others
    // link weights & bias
    weight->cloneSharedOperators()->addChild(fc, 0, 1);
    if (bias) {
        bias->cloneSharedOperators()->addChild(fc, 0, 2);
    }


    // Step 3 : Update all graphviews that contains at least one node to replace
        // Case 1 : If all nodes are in a graph view : delete old nodes & branch input & output
        // Case 2 : If not all nodes are in a graph view : only delete the nodes from the graphview
        // Maybe create a central mechanism to update automatically all graph views rather than each node have graphview presence memory?
    auto newNodes = std::set<std::shared_ptr<Node>>({fc, fc->getParent(1), fc->getParent(2)});
    GraphView::replace({matmulNode, addNode, bias, weight}, newNodes);

}


void Aidge::fuseMulAdd(std::shared_ptr<Aidge::MatchSolution> solution){

    assert(solution->at("MatMul").size() == 1 && "Wrong number of nodes MatMul to replace\n");
    assert(solution->at("Add").size() == 1 && "Wrong number of nodes Add to replace\n");

    for (const auto& matmulNode : solution->at("MatMul")) {
        for (const auto& addNode : solution->at("Add")) {
            fuseMulAdd(matmulNode,addNode);
        }
    }
}


void Aidge::fuseMulAdd(std::shared_ptr<Aidge::GraphView> graphView){


    std::shared_ptr<GraphRegex> regex = std::make_shared<GraphRegex>();
    regex->setNodeKey("Add","getType($) =='Add'");
    regex->setNodeKey("MatMul","getType($) =='MatMul'");
    regex->addQuery("MatMul -> Add ;");

    for (const auto& solution : regex->match(graphView)) {

        fuseMulAdd(solution);



    }
}