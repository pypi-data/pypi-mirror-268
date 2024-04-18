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

#include <memory>
#include <vector>

#include "aidge/graph/GraphView.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/Types.h"

Aidge::Node::Node(std::shared_ptr<Operator> op, const std::string& name)
    : mName(name),
      mOperator(op),
      mParents(std::vector<std::shared_ptr<Node>>(static_cast<std::size_t>(op->nbInputs()),
                                                  nullptr)),
      mChildren(std::vector<std::vector<std::weak_ptr<Node>>>(
              static_cast<std::size_t>(op->nbOutputs()), std::vector<std::weak_ptr<Node>>())),
      mIdInChildren(std::vector<std::vector<IOIndex_t>>(static_cast<std::size_t>(op->nbOutputs()),
                                                        std::vector<IOIndex_t>())),
      mIdOutParents(
              std::vector<IOIndex_t>(static_cast<std::size_t>(op->nbInputs()), gk_IODefaultIndex)) {
    // ctor
}

///////////////////////////////////////////////////////
//        FUNCTIONAL DESCRIPTION
///////////////////////////////////////////////////////

Aidge::Connector Aidge::Node::operator()(const std::vector<Connector>& ctors) {
    assert((ctors.size() == nbData()) && "Wrong number of arguments.\n");
    for (std::pair<std::shared_ptr<Node>, IOIndex_t>& input : inputs()) {
        assert((gk_IODefaultIndex == input.second) &&
               "At least one input connection is not free.\n");
        (void)input;  // avoid unused warning
    }
    IOIndex_t i = 0;
    for (const Connector& ctor : ctors) {
        if (ctor.node() != nullptr) {  // ctor must be associated with a node
            ctor.node()->addChild(shared_from_this(), ctor.index(), i++);
        }
    }
    return Connector(shared_from_this());
}

///////////////////////////////////////////////////////
//        INNER
///////////////////////////////////////////////////////

void Aidge::Node::setName(const std::string& name) { mName = name; }

///////////////////////////////////////////////////////
//        OPERATORS
///////////////////////////////////////////////////////

void Aidge::Node::forward() {
    assert((mOperator != nullptr) && "No Operator interface provided, can't run forward().\n");
    mOperator->forward();
}

void Aidge::Node::backward() {
    assert((mOperator != nullptr) && "No Operator interface provided, can't run backward().\n");
    mOperator->backward();
}

///////////////////////////////////////////////////////
//        TENSOR MANAGEMENT
///////////////////////////////////////////////////////

bool Aidge::Node::valid() const {
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (mIdOutParents[static_cast<std::size_t>(i)] == gk_IODefaultIndex) {
            return false;
        }
    }
    return true;
}

Aidge::IOIndex_t Aidge::Node::getNbFreeDataInputs() const {
    IOIndex_t nbFreeDataIn = 0;
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (input(i).second == gk_IODefaultIndex) {
            ++nbFreeDataIn;
        }
    }
    return nbFreeDataIn;
}

std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>> Aidge::Node::dataInputs()
        const {
    std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> res =
            std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>(nbData());
    for (std::size_t i = 0; i < static_cast<std::size_t>(nbData()); ++i) {
        res[i] = std::pair<std::shared_ptr<Node>, IOIndex_t>(mParents[i], mIdOutParents[i]);
    }
    return res;
}

std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>> Aidge::Node::inputs() const {
    std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> res =
            std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>(nbInputs());
    for (std::size_t i = 0; i < nbInputs(); ++i) {
        res[i] = std::pair<std::shared_ptr<Node>, IOIndex_t>(mParents[i], mIdOutParents[i]);
    }
    return res;
}

// void Aidge::Node::setInput(const Aidge::IOIndex_t idx, const std::shared_ptr<Aidge::Tensor>
// tensor) {
//     assert(((idx != gk_IODefaultIndex) && (idx < nbInputs())) && "Parent index out of bound.");
//     if (mParents[idx] != nullptr) {
//         mParents[idx]->removeChild(shared_from_this(), mIdOutParents[idx]);
//         removeParent(idx);
//     }
//     std::shared_ptr<Node> newConstantNode = Producer(tensor);
//     newConstantNode->addChild(shared_from_this(), 0, idx);
//     for (auto& graphPtr : views()) {
//         graphPtr->add(newConstantNode);
//     }
// }

std::vector<std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>>
Aidge::Node::outputs() const {
    std::vector<std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>> listOutputs =
            std::vector<std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>>(
                    mIdInChildren.size());
    for (std::size_t i = 0; i < mIdInChildren.size(); ++i) {
        listOutputs[i] = output(static_cast<IOIndex_t>(i));
    }
    return listOutputs;
}

std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>> Aidge::Node::output(
        Aidge::IOIndex_t outId) const {
    std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> listOutputs =
            std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>(mIdInChildren[outId].size());
    for (std::size_t i = 0; i < mIdInChildren[outId].size(); ++i) {
        listOutputs[i] = std::pair<std::shared_ptr<Node>, IOIndex_t>(mChildren[outId][i].lock(),
                                                                     mIdInChildren[outId][i]);
    }
    return listOutputs;
}

Aidge::IOIndex_t Aidge::Node::nbValidInputs() const {
    IOIndex_t counter = 0;
    for (IOIndex_t i = 0; i < nbInputs(); ++i) {
        if (mIdOutParents[static_cast<std::size_t>(i)] == gk_IODefaultIndex) ++counter;
    }
    return counter;
}

Aidge::IOIndex_t Aidge::Node::nbValidOutputs() const {
    IOIndex_t counter = 0;
    if (mIdInChildren.size() == 0) return 0;
    for (std::size_t i = 0; i < nbOutputs(); ++i) {
        if (mIdInChildren[i].size() > 0U) counter++;
    }
    return counter;
}

void Aidge::Node::setInputId(const IOIndex_t inId, const IOIndex_t newNodeoutId) {
    AIDGE_ASSERT(inId != gk_IODefaultIndex && inId < nbInputs(),
        "Input index ({}) is out of bound ({}) for node {} (of type {})",
        inId, nbInputs(), name(), type());
    if (mIdOutParents[inId] != gk_IODefaultIndex) {
        Log::notice("Notice: filling a Tensor already attributed");
        auto originalParent = input(inId);
        // remove original parent reference to child
        // find the output ID for original Parent
        // find first occurence of child in the output's children
        originalParent.first->removeChild(shared_from_this(), originalParent.second);
    }
    mIdOutParents[inId] = newNodeoutId;
}

///////////////////////////////////////////////////////
// TOPOLOGY
///////////////////////////////////////////////////////

void Aidge::Node::addChildOp(std::shared_ptr<Node> otherNode, const IOIndex_t outId,
                             const IOIndex_t otherInId) {
    AIDGE_ASSERT(otherInId < otherNode->nbInputs(),
        "Input index (#{}) of the node {} (of type {}) is out of bound (it has {} inputs), when trying to add it as a child of node {} (of type {})",
        otherInId, otherNode->name(), otherNode->type(), otherNode->nbInputs(), name(), type());
    AIDGE_ASSERT(outId < nbOutputs(),
        "Output index (#{}) of the node {} (of type {}) is out of bound (it has {} outputs), when trying to add the child node {} (of type {})",
        outId, name(), type(), nbOutputs(), otherNode->name(), otherNode->type());
    if (otherNode->input(otherInId).second != gk_IODefaultIndex) {
        Log::notice("Notice: the {}-th Parent of the child node {} (of type {}) already existed", otherInId, otherNode->name(), otherNode->type());
    }
    // manage tensors and potential previous parent
    otherNode->setInputId(otherInId, outId);
    otherNode->getOperator()->associateInput(otherInId, getOperator()->getRawOutput(outId));
    // manage nodes
    mChildren[outId].push_back(std::weak_ptr<Node>(otherNode));
    mIdInChildren[outId].push_back(otherInId);
    otherNode->addParent(shared_from_this(), otherInId);
}

void Aidge::Node::addChildView(std::shared_ptr<GraphView> otherGraph, const IOIndex_t outId,
                               std::pair<std::shared_ptr<Node>, IOIndex_t> otherInId) {
    const auto inNodes = otherGraph->inputNodes();
    AIDGE_ASSERT(otherInId.first != nullptr && inNodes.find(otherInId.first) != inNodes.end(),
        "Node {} (of type {}) is not a valid input node of GraphView {}, when trying to add it as a child of node {} (of type {})",
        (otherInId.first) ? otherInId.first->name() : "#nullptr", (otherInId.first) ? otherInId.first->type() : "", otherGraph->name(), name(), type());
    addChildOp(otherInId.first, outId, otherInId.second);
}

void Aidge::Node::addChild(std::shared_ptr<Node> otherNode, const IOIndex_t outId,
                           IOIndex_t otherInId) {
    if (otherNode) {
        otherInId =
                (otherInId != gk_IODefaultIndex) ? otherInId : otherNode->getFirstFreeDataInput();
        addChildOp(otherNode, outId, otherInId);
    }
}

void Aidge::Node::addChild(std::shared_ptr<GraphView> otherView, const IOIndex_t outId,
                           std::pair<std::shared_ptr<Node>, IOIndex_t> otherInId) {
    if (!otherInId.first) {
        AIDGE_ASSERT(otherView->inputNodes().size() == 1U,
            "Input node of GraphView {} need to be specified, because it has more than one input ({} inputs), when trying to add it as a child of node {} (of type {})",
            otherView->name(), otherView->inputNodes().size(), name(), type());
        otherInId.first = *(otherView->inputNodes().begin());
    }
    otherInId.second = (otherInId.second != gk_IODefaultIndex)
                               ? otherInId.second
                               : otherInId.first->getFirstFreeDataInput();
    addChildView(otherView, outId, otherInId);
}

void Aidge::Node::addParent(const std::shared_ptr<Node> other_node, const IOIndex_t inId) {
    if (getParent(inId) != nullptr) {
        Log::notice("Notice: you are replacing an existing parent for node {} (of type {})", name(), type());
    }
    AIDGE_ASSERT(inId != gk_IODefaultIndex && inId < nbInputs(),
        "Input index ({}) is out of bound ({}) for node {} (of type {})",
        inId, nbInputs(), name(), type());
    mParents[inId] = other_node;
}

std::vector<std::shared_ptr<Aidge::Node>> Aidge::Node::getParents() const { return mParents; }

std::shared_ptr<Aidge::Node> Aidge::Node::popParent(const IOIndex_t inId) {
    AIDGE_ASSERT(inId != gk_IODefaultIndex && inId < nbInputs(),
        "Input index ({}) is out of bound ({}) for node {} (of type {})",
        inId, nbInputs(), name(), type());
    std::shared_ptr<Node> val = mParents[inId];
    removeParent(inId);
    return val;
}

bool Aidge::Node::removeParent(const IOIndex_t inId) {
    AIDGE_ASSERT(inId != gk_IODefaultIndex && inId < nbInputs(),
        "Input index ({}) is out of bound ({}) for node {} (of type {})",
        inId, nbInputs(), name(), type());
    if (mParents[inId]) {
        mParents[inId] = nullptr;
        mIdOutParents[inId] = gk_IODefaultIndex;
        return true;
    }
    return false;
}

std::set<std::shared_ptr<Aidge::Node>> Aidge::Node::getChildren() const {
    std::set<std::shared_ptr<Node>> children;
    for (const auto& childrenOfOneOutput : mChildren) {
        for (const auto& oneChild : childrenOfOneOutput) {
            children.insert(oneChild.lock());
        }
    }
    return children;
}

std::vector<std::vector<std::shared_ptr<Aidge::Node>>> Aidge::Node::getOrderedChildren() const {
    auto children =
            std::vector<std::vector<std::shared_ptr<Node>>>(mChildren.size());
    for (std::size_t outId = 0; outId < mChildren.size(); ++outId) {
        children[outId] = getChildren(outId);
    }
    return children;
}

std::vector<std::shared_ptr<Aidge::Node>> Aidge::Node::getChildren(const IOIndex_t outId) const {
    assert((outId < nbOutputs()) && "Output index out of bound.");
    std::vector<std::shared_ptr<Node>> children;
    for (std::size_t i = 0; i < mChildren[outId].size(); ++i) {
        children.push_back(mChildren[outId][i].lock());
    }
    return children;
}

bool Aidge::Node::removeChild(const std::shared_ptr<Aidge::Node> nodePtr,
                              const Aidge::IOIndex_t outId) {
    assert((outId < nbOutputs()) && "Child index out of bound.");
    bool removed = false;
    for (std::size_t j = 0; j < mChildren[outId].size(); ++j) {
        if (mChildren[outId][j].lock() == nodePtr) {
            mChildren[outId].erase(mChildren[outId].begin() + j);
            mIdInChildren[outId].erase(mIdInChildren[outId].begin() + j);
            removed = true;
            break;
        }
    }
    return removed;
}

void Aidge::Node::resetConnections(bool includeLearnableParam) {
    // remove every parents reference to it
    IOIndex_t nbRemovedInputs = includeLearnableParam ? nbInputs() : nbData();
    for (IOIndex_t i = 0; i < nbRemovedInputs; ++i) {
        std::pair<std::shared_ptr<Node>, IOIndex_t> parent = input(i);
        if (parent.first) {
            // number of children linked to the parent's output
            while (parent.first->removeChild(shared_from_this(), parent.second) == true) {
            }
        }
        // every reference to this object as child has been removed
        // removing reference to parents.
        mParents[i] = nullptr;
        mIdOutParents[i] = gk_IODefaultIndex;
    }
    for (IOIndex_t i = 0; i < nbOutputs(); ++i) {
        for (std::pair<std::shared_ptr<Node>, IOIndex_t> child : output(i)) {
            child.first->removeParent(child.second);
        }
        mChildren[i] = std::vector<std::weak_ptr<Node>>();
        mIdInChildren[i] = std::vector<IOIndex_t>();
    }
    // removing this Node from every GraphView it belongs to
    // for (auto& graph : views()) {
    //     // if keeping connections with LEarnable Parameters, then also remove them from graph
    //     graph->remove(shared_from_this(), !includeLearnableParam);
    // }
}

///////////////////////////////////////////////////////
//        CLONE
///////////////////////////////////////////////////////

Aidge::NodePtr Aidge::Node::cloneSharedOperators() const {
    return std::make_shared<Node>(mOperator, mName);
}

Aidge::NodePtr Aidge::Node::cloneSharedProducers() const {
    std::shared_ptr<Operator> op =
            (mOperator->type() == Producer_Op::Type) ? mOperator : mOperator->clone();

    return std::make_shared<Node>(op, mName);
}

Aidge::NodePtr Aidge::Node::clone() const {
    return std::make_shared<Node>(mOperator->clone(), mName);
}

std::set<Aidge::NodePtr> Aidge::Node::getNodeDelta(int delta, std::set<Aidge::NodePtr> nodeSee) {
    std::set<Aidge::NodePtr> out;
    nodeSee.insert(shared_from_this());

    if (delta == 0) {
        out.insert(shared_from_this());

    } else if (delta > 0) {
        for (const NodePtr& node : getChildren()) {
            if (nodeSee.find(node) == nodeSee.end()) {  // loop avoidance
                for (const NodePtr& ch : node->getNodeDelta(delta - 1, nodeSee)) {
                    out.insert(ch);
                }
            }
        }
    } else {
        for (const NodePtr& node : getParents()) {
            if (nodeSee.find(node) == nodeSee.end()) {  // loop avoidance
                for (const NodePtr& pr : node->getNodeDelta(delta + 1, nodeSee)) {
                    out.insert(pr);
                }
            }
        }
    }

    return out;
}

// namespace Aidge {
// std::ostream& operator << (std::ostream& os, Aidge::Node& n) {
//     using namespace std;
//     os << "Node :\tName :\t\"" << n.name() << "\"\tType : \"" << n.getOperator()->type()<< "\"\tIN/OUTputs : "<< n.nbInputs() <<"/"<< n.nbOutputs() <<endl;
//     os << "\tParents :\t" ;
//     for (const auto & p : n.getParents())
//     {
//         os << "\"" <<p->name() << "\"\t";
//     }
//     os << endl;
//     os << "\tChildren :\t" ;
//     for (const auto & c : n.getChildren())
//     {
//         os << "\"" << c->name() << "\"\t";
//     }
//     os << endl;
//     return os;
// }
// }
/////////////////////////////////////////////////////////////////////////////////////////////
// private

///////////////////////////////////////////////////////
//        FUNCTIONAL DESCRIPTION
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
//        OPERATORS
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
//        TENSOR MANAGEMENT
///////////////////////////////////////////////////////
