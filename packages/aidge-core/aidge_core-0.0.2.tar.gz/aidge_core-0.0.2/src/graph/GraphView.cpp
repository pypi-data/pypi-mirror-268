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

#include "aidge/graph/GraphView.hpp"

#include <algorithm>     // std::find, std::set_intersection, std::transform
#include <cassert>
#include <stdexcept>     // std::runtime_error
#include <cstddef>       // std::size_t
#include <cstdio>        // std::fclose, std::fopen
#include <fmt/format.h>
#include <iterator>      // std::back_inserter, std::distance, std::inserter,
                         // std::next
#include <map>
#include <memory>        // std::dynamic_pointer_cast, std::static_pointer_cast
#include <set>
#include <string>        // std::to_string
#include <utility>       // std::make_pair, std::pair
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/GenericOperator.hpp"
#include "aidge/operator/MetaOperator.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/utils/Directories.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"


const std::shared_ptr<Aidge::Node> Aidge::GraphView::operator[](const std::string& nodeName) const {
    return (mNodeRegistry.find(nodeName) != mNodeRegistry.cend()) ? mNodeRegistry.at(nodeName) : nullptr;
}

///////////////////////////////////////////////////////
//        FUNCTIONAL DESCRIPTION
///////////////////////////////////////////////////////

Aidge::Connector Aidge::GraphView::operator()(
    const std::vector<Aidge::Connector> ctors) {
  // TODO: allow for multiple inputNodes?
  assert((inputNodes().size() == 1U) && "Too many input Nodes for the GraphView, undefined behaviour");
  std::shared_ptr<Node> inNode = *inputNodes().begin();
  assert((ctors.size() == static_cast<std::size_t>(inNode->nbData())) && "Wrong number of arguments.\n");
  for (std::pair<std::shared_ptr<Node>, IOIndex_t> &input : inNode->inputs()) {
    assert((gk_IODefaultIndex == input.second) && "At least one input connection is not free.\n");
    (void)input; // avoid unused warning
  }

  IOIndex_t inID = 0;
  for (const Connector &ctor : ctors) {
    assert((ctor.node() != nullptr) &&
           "Input Connector must be associated with a node");
    ctor.node()->addChild(shared_from_this(), static_cast<std::size_t>(ctor.index()),
                          {inNode, inID++});
  }
  return Connector(*(outputNodes().begin()));
}

///////////////////////////////////////////////////////
//        INNER
///////////////////////////////////////////////////////

bool Aidge::GraphView::inView(const std::shared_ptr<Aidge::Node>& nodePtr) const {
    return mNodes.find(nodePtr) != mNodes.cend();
}


void Aidge::GraphView::save(const std::string& path, bool verbose, bool showProducers) const {
    auto fp = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen((path + ".mmd").c_str(), "w"), &std::fclose);

    if (!fp) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create graph view log file: {}", path + ".mmd");
    }

    fmt::print(fp.get(),
                "%%{{init: {{'flowchart': {{ 'curve': 'monotoneY'}}, "
                "'fontFamily': 'Verdana' }} }}%%\nflowchart TB\n\n");

    // Start by creating every node
    const auto namePtrTable = getRankedNodesName("{3}");

    for (const std::shared_ptr<Node> &node_ptr : mNodes) {
        std::string givenName =
            (node_ptr->name().empty())
                ? "<em>" + node_ptr->type() + "#" + namePtrTable.at(node_ptr) + "</em>"
                : "\"" + node_ptr->name() + "\\n<sub><em>(" + node_ptr->type() + "#" + namePtrTable.at(node_ptr) + ")</em></sub>\"";

        std::string nodeCls = "";
        if (node_ptr->type() == "Producer") {
          nodeCls = ":::producerCls";
        }
        else if (std::dynamic_pointer_cast<GenericOperator_Op>(node_ptr->getOperator())) {
          nodeCls = ":::genericCls";
        }
        else if (const auto metaOp = std::dynamic_pointer_cast<MetaOperator_Op>(node_ptr->getOperator())) {
          nodeCls = ":::metaCls";

          if (verbose) {
            metaOp->getMicroGraph()->save(path + "_" + node_ptr->type() + "#" + namePtrTable.at(node_ptr), verbose, showProducers);
          }
        }

        if (node_ptr == mRootNode) {
          if (nodeCls.empty()) {
            nodeCls = ":::rootCls";
          }
          else {
            nodeCls += "_rootCls";
          }
        }

        if (node_ptr == mRootNode || node_ptr->type() != "Producer" || showProducers) {
          fmt::print(fp.get(), "{}_{}({}){}\n", node_ptr->type(), namePtrTable.at(node_ptr),
                      givenName, nodeCls);
        }
    }

    // Write every link
    for (const std::shared_ptr<Node> &node_ptr : mNodes) {
      if ((node_ptr -> type() == "Producer") && !showProducers) {
        continue;
      }
      IOIndex_t outputIdx = 0;
      for (const auto& childs : node_ptr->getOrderedChildren()) {
        for (const auto& child : childs) {
          if (child != nullptr) {
            IOIndex_t inputIdx = 0;
            for (auto parent : child->inputs()) {
              if (parent.first == node_ptr && parent.second == outputIdx) {
                // Add-on to display the operator's output dimensions
                std::string dims = "";
                const auto op = std::dynamic_pointer_cast<OperatorTensor>(node_ptr->getOperator());
                if (op && !op->getOutput(outputIdx)->dims().empty()) {
                  dims += " " + fmt::format("{}", op->getOutput(outputIdx)->dims());
                }

                if (mNodes.find(child) != mNodes.end()) {
                  fmt::print(fp.get(), "{}_{}-->|\"{}{}&rarr;{}\"|{}_{}\n", node_ptr->type(), namePtrTable.at(node_ptr),
                              outputIdx, dims, inputIdx, child->type(), namePtrTable.at(child));
                }
                else if (verbose) {
                  fmt::print(fp.get(), "{}_{}-->|\"{}{}&rarr;{}\"|{}:::externalCls\n", node_ptr->type(), namePtrTable.at(node_ptr),
                              outputIdx, dims, inputIdx, static_cast<void*>(child.get()));
                }
                break;
              }
              ++inputIdx;
            }
          }
        }
        ++outputIdx;
      }
    }

    size_t inputIdx = 0;
    for (auto input : mInputNodes) {
      if (input.first != nullptr) {
        fmt::print(fp.get(), "input{}((in#{})):::inputCls--->|\"&rarr;{}\"|{}_{}\n", inputIdx, inputIdx,
                    input.second, input.first->type(), namePtrTable.at(input.first));
      }
      else {
        fmt::print(fp.get(), "input{}((in#{})):::inputCls\n", inputIdx, inputIdx);
      }
      ++inputIdx;
    }

    size_t outputIdx = 0;
    for (auto output : mOutputNodes) {
      if (output.first != nullptr) {
        // Add-on to display the operator's output dimensions
        std::string dims = "";
        const auto op = std::dynamic_pointer_cast<OperatorTensor>(output.first->getOperator());
        if (op && op->getOutput(output.second) && !op->getOutput(output.second)->dims().empty()) {
          dims += " " + fmt::format("{}", op->getOutput(output.second)->dims());
        }

        fmt::print(fp.get(), "{}_{}--->|\"{}{}&rarr;\"|output{}((out#{})):::outputCls\n",
                    output.first->type(), namePtrTable.at(output.first), output.second,
                    dims, outputIdx, outputIdx);
      }
      else {
        fmt::print(fp.get(), "output{}((out#{})):::outputCls\n", outputIdx, outputIdx);
      }
      ++outputIdx;
    }

    fmt::print(fp.get(), "classDef inputCls fill:#afa\n");
    fmt::print(fp.get(), "classDef outputCls fill:#ffa\n");
    fmt::print(fp.get(), "classDef externalCls fill:#ccc\n");
    fmt::print(fp.get(), "classDef producerCls fill:#ccf\n");
    fmt::print(fp.get(), "classDef genericCls fill:#f9f9ff,stroke-width:1px,stroke-dasharray: 5 5\n");
    fmt::print(fp.get(), "classDef metaCls stroke-width:5px\n");
    fmt::print(fp.get(), "classDef rootCls stroke:#f00\n");
    fmt::print(fp.get(), "classDef producerCls_rootCls stroke:#f00,fill:#ccf\n");
    fmt::print(fp.get(), "classDef genericCls_rootCls stroke:#f00,fill:#f9f9ff,stroke-width:1px,stroke-dasharray: 5 5\n");
    fmt::print(fp.get(), "classDef metaCls_rootCls stroke:#f00,stroke-width:5px\n");
    fmt::print(fp.get(), "\n");
}

void Aidge::GraphView::logOutputs(const std::string& dirName) const {
  if (!Aidge::createDirectories(dirName)){
    AIDGE_THROW_OR_ABORT(std::runtime_error, "Failed to create directory: {}.", dirName);
  }
  for (std::shared_ptr<Node> nodePtr : getNodes()) {

    const std::string& nodePath = dirName + "/" + Aidge::filePath(nodePtr->name()) +"/";
    if (!Aidge::createDirectories(nodePath)){
      AIDGE_THROW_OR_ABORT(std::runtime_error, "Failed to create directory: {}.", nodePath);
    }

    for (IOIndex_t outIdx = 0; outIdx < nodePtr->nbOutputs(); ++outIdx) {
      const std::string& inputPath = nodePath +"output_" + std::to_string(outIdx) + ".log";
      auto fp = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen(inputPath.c_str(), "w"), &std::fclose);
      if (!fp) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create graph view log file: {}", inputPath);
      }
      fmt::print(fp.get(), "{}\n", nodePtr->getOperator()->getRawOutput(outIdx)->toString().c_str());
    }
  }
}

void Aidge::GraphView::setRootNode(NodePtr node) {
  AIDGE_ASSERT(mNodes.find(node) != mNodes.end(), "Root node is not in the GraphView!");
  mRootNode = node;
}

///////////////////////////////////////////////////////
//        TENSOR MANAGEMENT
///////////////////////////////////////////////////////

std::set<std::shared_ptr<Aidge::Node>> Aidge::GraphView::inputNodes() const {
    std::set<std::shared_ptr<Aidge::Node>> nodes;
    for (const auto& node : mInputNodes) {
        nodes.insert(node.first);
    }
    return nodes;
}

std::set<std::shared_ptr<Aidge::Node>> Aidge::GraphView::outputNodes() const {
    std::set<std::shared_ptr<Aidge::Node>> nodes;
    for (const auto& node : mOutputNodes) {
        nodes.insert(node.first);
    }
    return nodes;
}

bool Aidge::GraphView::isInputNode(const std::shared_ptr<Aidge::Node>& nodePtr) const {
    const auto nodes = inputNodes();
    return (nodes.find(nodePtr) != nodes.cend());
}

bool Aidge::GraphView::isOutputNode(const std::shared_ptr<Aidge::Node>& nodePtr) const {
    const auto nodes = outputNodes();
    return (nodes.find(nodePtr) != nodes.cend());
}


void Aidge::GraphView::setOrderedInputs(const std::vector<std::pair<NodePtr, IOIndex_t>>& inputs) {
  size_t nbInputs = 0;
  std::vector<std::pair<NodePtr, IOIndex_t>> ignoredInputs(mInputNodes);
  for (auto input : inputs) {
    // Allow to specify dummy inputs (nullptr), but this will only be reflected
    // in mInputNodes. All other functions (nbInputs(), inputs()) will not take
    // it into account.
    if (input.first != nullptr) {
      auto it = std::find(ignoredInputs.begin(), ignoredInputs.end(), input);
      AIDGE_ASSERT(it != ignoredInputs.end(), "unknown or duplicate input");
      ignoredInputs.erase(it);
      ++nbInputs;
    }
  }

  AIDGE_ASSERT(nbInputs <= mInputNodes.size(), "too many specified number of inputs");

  mInputNodes = inputs;
  mInputNodes.insert(mInputNodes.end(), ignoredInputs.begin(), ignoredInputs.end());
}

void Aidge::GraphView::setOrderedOutputs(const std::vector<std::pair<NodePtr, IOIndex_t>>& outputs) {
  size_t nbOutputs = 0;
  std::vector<std::pair<NodePtr, IOIndex_t>> ignoredOutputs(mOutputNodes);
  for (auto output : outputs) {
    // Allow to specify dummy outputs (nullptr), but this will only be reflected
    // in mOutputNodes. All other functions (nbOutputs(), outputs()) will not take
    // it into account.
    if (output.first != nullptr) {
      auto it = std::find(ignoredOutputs.begin(), ignoredOutputs.end(), output);
      AIDGE_ASSERT(it != ignoredOutputs.end(), "unknown or duplicate output");
      ignoredOutputs.erase(it);
      ++nbOutputs;
    }
  }

  AIDGE_ASSERT(nbOutputs <= mOutputNodes.size(), "too many specified number of outputs");

  mOutputNodes = outputs;
  mOutputNodes.insert(mOutputNodes.end(), ignoredOutputs.begin(), ignoredOutputs.end());
}

Aidge::IOIndex_t Aidge::GraphView::getNbDataInputs() const {
  IOIndex_t nbDataInput = 0;
  for (const std::shared_ptr<Node> &inNode : inputNodes()) {
    // We cannot simply add inNode->nbDataInputs(), as input nodes may already
    // have some inputs connected within the GraphView, which would therefore not
    // constitue inputs (from outside) for the GraphView!
    const std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> inputNodeinputs =
        inNode->dataInputs();

    for (const auto& input : inputNodeinputs) {
      if (input.first == nullptr || mNodes.find(input.first) == mNodes.end()) {
        ++nbDataInput;
      }
    }
  }
  return nbDataInput;
}

Aidge::IOIndex_t Aidge::GraphView::getNbFreeDataInputs() const {
  IOIndex_t nbIn = 0;
  // Free inputs within the GraphView are logically also free inputs from outside
  // the GraphView.
  for (const std::shared_ptr<Node>& inputNode : inputNodes()) {
    nbIn += inputNode->getNbFreeDataInputs();
  }
  return nbIn;
}


std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>
Aidge::GraphView::dataInputs() const {
  std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> res;

  for (const std::shared_ptr<Node>& inputNode : inputNodes()) {
    const std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> inputNodeinputs =
        inputNode->dataInputs();

    for (const auto& input : inputNodeinputs) {
      if (input.first == nullptr || mNodes.find(input.first) == mNodes.end()) {
        res.push_back(input);
      }
    }
  }
  return res;
}


std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>
Aidge::GraphView::inputs() const {
  std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> res;

  for (const std::shared_ptr<Node>& inputNode : inputNodes()) {
    const std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> inputNodeinputs =
        inputNode->inputs();

    for (const auto& input : inputNodeinputs) {
      if (input.first == nullptr || mNodes.find(input.first) == mNodes.end()) {
        res.push_back(input);
      }
    }
  }
  return res;
}


std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>
Aidge::GraphView::inputs(const std::string& name) const {
  return mNodeRegistry.at(name)->inputs();
}

void Aidge::GraphView::compile(const std::string& backend, const Aidge::DataType datatype, DeviceIdx_t device, const std::vector<std::vector<DimSize_t>> dims) {
    // Backend
    // TODO: add Backend attribute to Operator
    setBackend(backend, device);
    // Data type
    // TODO: manage Datatype attribute in OperatorImpl
    setDataType(datatype);
    // Data Format
    // TODO: check actual parent output data format and the needed one. Add a Transpose Operator if necessary
    // Forward dimensions
    forwardDims(dims);
}

void Aidge::GraphView::forwardDims(const std::vector<std::vector<Aidge::DimSize_t>> dims) {
    // setInputs
    // Link every tensor to the right pointer
    // following parent - children informations
    if (!dims.empty()){
      AIDGE_ASSERT(dims.size() == mInputNodes.size(), "GraphView forwardDims error - Inconsistent number of given dimensions ({}) and graph inputs ({})", dims.size(), mInputNodes.size());
      for (std::size_t i = 0; i < dims.size(); ++i){
        auto tensor = std::make_shared<Tensor>(dims[i]);
        mInputNodes[i].first->getOperator()->setInput(mInputNodes[i].second, tensor);
      }
    }

    // Ensure every node in the graph is correctly connected
    for (std::shared_ptr<Node> nodePtr : getNodes()) {
        for (IOIndex_t i = 0; i < nodePtr->nbInputs(); ++i) {
            // assess if the input was not already set and is a Tensor then link it to parent output
            std::pair<std::shared_ptr<Node>, IOIndex_t> inputI = nodePtr->input(i);
            if (inputI.first) {
                if ( std::static_pointer_cast<Tensor>(nodePtr->getOperator()->getRawInput(i)) != inputI.first->getOperator()->getRawOutput(inputI.second)) {
                    if (nodePtr->getOperator()->operatorType() == OperatorType::Tensor) {
                        // assert provided Data is of "Tensor" type
                        nodePtr->getOperator()->associateInput(i, inputI.first->getOperator()->getRawOutput(inputI.second));
                    }
                    else {
                        AIDGE_ASSERT(false, "Non-tensor entries not handled yet, for node {} (of type {}).", nodePtr->name(), nodePtr->type());
                    }
                }
            } else {
                AIDGE_ASSERT(nodePtr->getOperator()->getRawInput(i)
                    && !std::static_pointer_cast<Tensor>(nodePtr->getOperator()->getRawInput(i))->empty(),
                  "Missing input#{} for node {} ({})", i, nodePtr->name(), nodePtr->type());
            }

        }
    }

    // Compute dimensions of every node
    std::set<std::shared_ptr<Node>> listNodes = getNodes();
    do {
        std::set<std::shared_ptr<Node>> nextList;
        for (std::shared_ptr<Node> nodePtr : listNodes) {
            if (nodePtr->getOperator()->operatorType() == OperatorType::Tensor) {
              const auto op = std::static_pointer_cast<OperatorTensor>(nodePtr->getOperator());
              // Recompute everytime, even if it was already computed in a
              // previous call of forwardDims(), as the graph may have changed!
              op->computeOutputDims();
              if (!op->outputDimsForwarded()) {
                  nextList.insert(nodePtr);
              }
            }
        }

        // Internal check to make sure we won't enter in an infinite loop!
        if (nextList == listNodes) {
            // We are stuck!
            std::vector<std::string> nodesName;
            std::transform(nextList.begin(), nextList.end(),
                std::back_inserter(nodesName),
                [](auto val){ return val->name() + " (" + val->type() + ")"; });
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Unable to forward dimensions (circular dependency and/or wrong dimensions?). Unable to compute output dims for nodes {}.", nodesName);
        }

        listNodes.swap(nextList);
    }
    while (!listNodes.empty());
}

void Aidge::GraphView::setBackend(const std::string &backend, const DeviceIdx_t device) const {
    for (const auto& node : getNodes()) {
        node->getOperator()->setBackend(backend, device);
    }
}

void Aidge::GraphView::setDataType(const Aidge::DataType &datatype) const {
    for (const auto& node : getNodes()) {
        node->getOperator()->setDataType(datatype);
    }
}

std::vector<
    std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>>
Aidge::GraphView::outputs() const {
  std::vector<std::vector<std::pair<std::shared_ptr<Node>, Aidge::IOIndex_t>>>
      outsideOutputs;
  for (const std::shared_ptr<Node>& outputNode : outputNodes()) {
    const std::vector<std::vector<std::pair<std::shared_ptr<Node>, Aidge::IOIndex_t>>>
        outputNodeOutputs = outputNode->outputs();

    for (const auto& outputPos : outputNodeOutputs) {
      // Keep only the nodes connected at this output position that are outside the GraphView
      std::vector<std::pair<std::shared_ptr<Node>, Aidge::IOIndex_t>> outsideOutputPos;
      for (const auto& output : outputPos) {
        if (output.first == nullptr || mNodes.find(output.first) == mNodes.end()) {
          outsideOutputPos.push_back(output);
        }
      }

      if (outputPos.empty() || !outsideOutputPos.empty()) {
        outsideOutputs.push_back(outsideOutputPos);
      }
    }
  }
  return outsideOutputs;
}

std::vector<
    std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>>>
Aidge::GraphView::outputs(const std::string& nodeName) const {
  return mNodeRegistry.at(nodeName)->outputs();
}

void Aidge::GraphView::setInputId(Aidge::IOIndex_t /*inID*/,
                               Aidge::IOIndex_t /*newNodeOutID*/) {
  AIDGE_THROW_OR_ABORT(std::runtime_error, "Not implemented yet.");
}

void Aidge::GraphView::add(std::shared_ptr<Node> node, bool includeLearnableParam) {
  AIDGE_ASSERT(node != nullptr, "Trying to add non-existant node!");

  // first node to be added to the graph is the root node by default
  if (mRootNode == nullptr) {
    mRootNode = node;
  }

  // add to the GraphView nodes
  node->addView(shared_from_this());
  mNodes.insert(node);
  if (!(node->name()).empty())
    mNodeRegistry.insert(std::make_pair(node->name(), node));

  // check if the node is an input/output node
  updateInputsOutputsNew(node);

  // add learnable parameters to the graph
  if (includeLearnableParam) {
    for (IOIndex_t i = node->nbData(); i < node->nbInputs(); ++i) {
      std::shared_ptr<Node> parentNode = node->getParent(static_cast<IOIndex_t>(i));
      if (parentNode) {
          parentNode->addView(shared_from_this());
          mNodes.insert(parentNode);
          if (!(parentNode->name()).empty())
            mNodeRegistry.insert(std::make_pair(parentNode->name(), parentNode));
          // check if the parentNode is an input/output node
          updateInputsOutputsNew(parentNode);
      }
    }
  }
}

std::pair<std::vector<Aidge::NodePtr>, size_t> Aidge::GraphView::getRankedNodes() const {
  std::set<NodePtr> nodesToRank(mNodes);
  nodesToRank.erase(mRootNode);
  std::vector<NodePtr> rankedNodes;
  rankedNodes.push_back(mRootNode);

  for (size_t curNodeIdx = 0; curNodeIdx < rankedNodes.size(); ++curNodeIdx) {
    NodePtr curNode = rankedNodes[curNodeIdx];

    for (auto childs : curNode->getOrderedChildren()) {
      for (auto child : childs) {
        if (child != nullptr && nodesToRank.find(child) != nodesToRank.end()) {
          rankedNodes.push_back(child);
          nodesToRank.erase(child);
        }
      }
    }

    for (auto parent : curNode->getParents()) {
      if (parent != nullptr && nodesToRank.find(parent) != nodesToRank.end()) {
        rankedNodes.push_back(parent);
        nodesToRank.erase(parent);
      }
    }
  }

  const size_t orderUnicityLimit = rankedNodes.size();
  if (!nodesToRank.empty()) {
    rankedNodes.insert(rankedNodes.end(), nodesToRank.begin(), nodesToRank.end());
  }

  return std::make_pair(rankedNodes, orderUnicityLimit);
}

std::map<Aidge::NodePtr, std::string> Aidge::GraphView::getRankedNodesName(const std::string& format, bool markNonUnicity) const {
  const auto rankedNodes = getRankedNodes();
  std::map<NodePtr, std::string> rankedNodesName;
  size_t rank = 0;
  std::map<std::string, size_t> typeRank;
  for (const auto& rankedNode : rankedNodes.first) {
    std::map<std::string, size_t>::iterator it;
    std::tie(it, std::ignore) = typeRank.insert(std::make_pair(rankedNode->type(), 0));

    const auto name = (markNonUnicity && rank < rankedNodes.second)
      ? fmt::format(format, rankedNode->name(), rankedNode->type(), rank, it->second)
      : fmt::format(format, rankedNode->name(), rankedNode->type(), fmt::format("?{}", rank), fmt::format("?{}", it->second));
    rankedNodesName.insert(std::make_pair(rankedNode, name));
    ++it->second;
    ++rank;
  }
  return rankedNodesName;
}

bool Aidge::GraphView::add(std::set<std::shared_ptr<Node>> otherNodes, bool includeLearnableParam) {
  if (otherNodes.empty()) {
    return true;
  }

  bool orderUnicity = true;

  // List only the nodes that are not already present in current graph
  std::set<NodePtr> nodesToAdd;
  std::set_difference(otherNodes.begin(), otherNodes.end(), mNodes.begin(), mNodes.end(), std::inserter(nodesToAdd, nodesToAdd.begin()));

  // List the nodes to rank, initially all the nodes in the GraphView
  std::set<NodePtr> nodesToRank(mNodes);
  nodesToRank.insert(nodesToAdd.begin(), nodesToAdd.end());
  std::vector<NodePtr> rankedNodesToAdd;

  if (mRootNode == nullptr) {
    std::set<NodePtr> noParentNodes;

    // If no root node is defined, check nodes without parents
    for (auto node : nodesToRank) {
      bool noParent = true;
      for (auto parent : node->getParents()) {
        if (parent != nullptr && nodesToRank.find(parent) != nodesToRank.end()) {
          noParent = false;
          break;
        }
      }

      if (noParent) {
        noParentNodes.insert(node);
      }
    }

    // Take the first one found (this is an arbitrary choice)
    mRootNode = *noParentNodes.begin();

    if (noParentNodes.size() > 1) {
      // If there is more than one, order unicity cannot be garanteed!
      orderUnicity = false;
    }

    rankedNodesToAdd.push_back(mRootNode);
  }

  nodesToRank.erase(mRootNode);
  std::vector<NodePtr> rankedNodes;
  rankedNodes.push_back(mRootNode);

  for (size_t curNodeIdx = 0; curNodeIdx < rankedNodes.size(); ++curNodeIdx) {
    NodePtr curNode = rankedNodes[curNodeIdx];

    for (auto childs : curNode->getOrderedChildren()) {
      for (auto child : childs) {
        if (child != nullptr && nodesToRank.find(child) != nodesToRank.end()) {
          rankedNodes.push_back(child);
          nodesToRank.erase(child);

          if (nodesToAdd.find(child) != nodesToAdd.end()) {
            rankedNodesToAdd.push_back(child);
            nodesToAdd.erase(child);
          }
        }
      }
    }

    for (auto parent : curNode->getParents()) {
      if (parent != nullptr && nodesToRank.find(parent) != nodesToRank.end()) {
        rankedNodes.push_back(parent);
        nodesToRank.erase(parent);

        if (nodesToAdd.find(parent) != nodesToAdd.end()) {
          rankedNodesToAdd.push_back(parent);
          nodesToAdd.erase(parent);
        }
      }
    }
  }

  if (!nodesToAdd.empty()) {
    // There are remaining nodes without path to the root node
    orderUnicity = false;

    while (!nodesToAdd.empty()) {
      const auto it = nodesToAdd.begin();
      rankedNodesToAdd.push_back(*it);
      nodesToAdd.erase(it);
    }
  }

  for (auto node_ptr : rankedNodesToAdd) {
    add(node_ptr, includeLearnableParam);
  }

  return orderUnicity;
}

bool Aidge::GraphView::add(std::pair<NodePtr, std::set<NodePtr>> nodes, bool includeLearnableParam) {
  if (nodes.first != nullptr) {
    mRootNode = nodes.first;
    add(nodes.first, includeLearnableParam);
  }
  return add(nodes.second, includeLearnableParam);
}

bool Aidge::GraphView::add(std::shared_ptr<GraphView> graph) {
    // set the rootNode to the other graphView rootNode if no rootNode yet
    mRootNode = mRootNode ? mRootNode : graph->rootNode();
    return add(graph->getNodes(), false);
}

void Aidge::GraphView::addChild(std::shared_ptr<Node> toOtherNode,
                               std::shared_ptr<Node> fromOutNode,
                               const Aidge::IOIndex_t fromTensor,
                               Aidge::IOIndex_t toTensor) {
  if (fromOutNode)
    assert(inView(fromOutNode) && "Output Node not found in the GraphView.");
  else {
    assert((outputNodes().size() == 1U) &&
           "Must specify an outputNode or have only one.");
    fromOutNode = *(outputNodes().begin());
  }
  fromOutNode->addChild(toOtherNode, fromTensor, toTensor);
  add(toOtherNode);
}

void Aidge::GraphView::addChild(
    std::shared_ptr<GraphView> toOtherView,
    std::pair<std::shared_ptr<Node>, Aidge::IOIndex_t> fromOutNode,
    std::pair<std::shared_ptr<Node>, Aidge::IOIndex_t> toNode) {
  // assert output node is valid
  if (!fromOutNode.first) {
    assert(outputNodes().size() == 1U &&
           "If no output node is provided, the graph should have only one to "
           "make the choice explicit.");
    fromOutNode.first = *(outputNodes().begin());
  } else
    assert(inView(fromOutNode.first));
  // assert input node is valid
  if (!toNode.first) {
    assert(toOtherView->inputNodes().size() == 1U &&
           "If no intput node is provided, the other graph should have only "
           "one to make the choice explicit.");
    toNode.first = *(toOtherView->inputNodes().begin());
  } else {
    assert(toOtherView->inView(toNode.first));
  }
  // Tensor assertions are performed in the Node adChild method
  fromOutNode.first->addChild(toNode.first, fromOutNode.second, toNode.second);
  // once linking performed, add other graph to current graph
  add(toOtherView);
}

std::set<std::shared_ptr<Aidge::Node>> Aidge::GraphView::getParents() const {
  // TODO: choose if we return a set or a vector
  std::set<std::shared_ptr<Node>> parents;
  for (const std::shared_ptr<Node>& inputNode : inputNodes()) {
    parents.insert(inputNode->getParents().begin(),
                   inputNode->getParents().end());
  }
  return parents;
}

std::vector<std::shared_ptr<Aidge::Node>> Aidge::GraphView::getParents(const std::string nodeName) const {
  std::map<std::string, std::shared_ptr<Node>>::const_iterator it = mNodeRegistry.find(nodeName);
  AIDGE_ASSERT(it != mNodeRegistry.end(), "No node named {} in graph {}.", nodeName, name());
  return (it->second)->getParents();
}

std::vector<std::vector<std::shared_ptr<Aidge::Node>>>
Aidge::GraphView::getOrderedParents() const {
  std::vector<std::vector<std::shared_ptr<Node>>> parents;
  for (const std::shared_ptr<Node>& inputNode : inputNodes()) {
    parents.push_back(inputNode->getParents());
  }
  return parents;
}

std::set<std::shared_ptr<Aidge::Node>> Aidge::GraphView::getChildren() const {
  std::set<std::shared_ptr<Node>> children;
  for (const std::shared_ptr<Node>& outputNode : outputNodes()) {
    children.insert((outputNode->getChildren()).begin(),
                    (outputNode->getChildren()).end());
  }
  return children;
}

std::vector<std::vector<std::shared_ptr<Aidge::Node>>>
Aidge::GraphView::getChildren(const std::string nodeName) const {
  std::map<std::string, std::shared_ptr<Node>>::const_iterator it =
      mNodeRegistry.find(nodeName);
  AIDGE_ASSERT(it != mNodeRegistry.end(), "No node named {} in graph {}.", nodeName, name());
  return (it->second)->getOrderedChildren();
}

std::set<std::shared_ptr<Aidge::Node>>
Aidge::GraphView::getChildren(const std::shared_ptr<Node> otherNode) const {
  std::set<std::shared_ptr<Node>>::const_iterator it = mNodes.find(otherNode);
  AIDGE_ASSERT(it != mNodes.end(), "The node {} (of type {}) is not in graph {}.",
    (otherNode) ? otherNode->name() : "#nullptr", (otherNode) ? otherNode->type() : "", name());
  return (*it)->getChildren();
}


std::shared_ptr<Aidge::Node>
Aidge::GraphView::getNode(const std::string& nodeName) const {
  std::map<std::string, std::shared_ptr<Node>>::const_iterator it =
      mNodeRegistry.find(nodeName);
  if (it != mNodeRegistry.cend()) {
    return it->second;
  } else {
    Log::warn("No Node named {} in the current GraphView {}.", nodeName, name());
    return nullptr;
  }
}


void Aidge::GraphView::remove(std::shared_ptr<Node> nodePtr, bool includeLearnableParam) {
  // remove learnable params
  if (includeLearnableParam) {
    for (IOIndex_t i = nodePtr->nbData(); i < nodePtr->nbInputs(); ++i) {
      auto inputI = nodePtr->input(i);
      if (inputI.first != nullptr) {
        bool removeNode = true;
        for (const auto& parentOutput : inputI.first->outputs()) {
          for (const auto& childOfParentOutput : parentOutput) {
            // only remove the learnable parameter if not related to any other Node in the GraphView
            if (childOfParentOutput.first != nodePtr) {
              removeNode = false;
              break;
            }
          }
        }
        if (removeNode) {
          // assert Learnable Parameter in the GraphView scope
          if (mNodes.find(inputI.first) != mNodes.end()) {
            mNodes.erase(inputI.first);
            inputI.first->removeView(shared_from_this());
          }
          if (!inputI.first->name().empty()) { mNodeRegistry.erase(inputI.first->name()); }

          // check if the node was an input/output node
          updateInputsOutputsDelete(inputI.first);
        }
      }
    }
  }

  if (mNodes.find(nodePtr) != mNodes.end()) {
    mNodes.erase(nodePtr);
    nodePtr->removeView(shared_from_this());

    // check if the nodePtr was an input/output node
    updateInputsOutputsDelete(nodePtr);
  }
  if (!nodePtr->name().empty()) { mNodeRegistry.erase(nodePtr->name()); }
}


bool Aidge::GraphView::swap(Node & /*node*/, Node & /*otherNode*/) {
  fmt::print("Swap() not implementated yet. Return false.\n");
  return false;
}

void Aidge::GraphView::link(const std::string& /*name1_inID*/,
                           const std::string& /*name2_outID*/) {
  fmt::print("Not implemented yet.\n");
}

void Aidge::GraphView::insertParent(NodePtr childNode,
                  NodePtr newParentNode,
                  IOIndex_t childInputTensorIdx,
                  IOIndex_t newParentInputTensorIdx,
                  IOIndex_t newParentOutputTensorIdx){
  NodePtr currentParentNode = childNode->getParent(childInputTensorIdx);
  const IOIndex_t currentParentOutputTensorIdx = childNode->input(childInputTensorIdx).second;
  // Remove child from current parent & current Parent from child
  currentParentNode->removeChild(childNode, currentParentOutputTensorIdx);

  // Add child
  currentParentNode->addChild(newParentNode,currentParentOutputTensorIdx, newParentInputTensorIdx);
  newParentNode->addChild(childNode, newParentOutputTensorIdx, childInputTensorIdx);

  add(newParentNode);
}

bool Aidge::GraphView::replace(const std::set<Aidge::NodePtr>& oldNodes, const std::set<Aidge::NodePtr>& newNodes) {
    // (1) create GraphViews from both sets of Nodes
    auto oldG = std::make_shared<GraphView>("oldG");
    oldG->add(oldNodes, false);
    auto newG = std::make_shared<GraphView>("newG");
    newG->add(newNodes, false);

    return GraphView::replace(oldG, newG);
}

bool Aidge::GraphView::replace(const std::shared_ptr<GraphView>& oldGraph, const std::shared_ptr<GraphView>& newGraph) {
    // TODO: handle case where an oldNodes parameter does not come from a Producer but another Node (not included in oldNodes)
    // How to distinguish it from data input?
    // TODO: Parameter Tensors could be identified with their dimensions
    // TODO: Take GraphView as input parameters since new Nodes should be connected whatever.
    // It also avoids specifying each producer since they are automatically included
    const std::set<NodePtr>&  oldNodes = oldGraph->getNodes();
    const std::set<NodePtr>&  newNodes = newGraph->getNodes();

    const std::vector<std::pair<NodePtr, IOIndex_t>> oldOIn =
                                                     oldGraph->getOrderedInputs();
    const std::vector<std::pair<NodePtr, IOIndex_t>> oldOOut =
                                                     oldGraph->getOrderedOutputs();
    const std::vector<std::pair<NodePtr, IOIndex_t>> newOIn =
                                                     newGraph->getOrderedInputs();
    const std::vector<std::pair<NodePtr, IOIndex_t>> newOOut =
                                                     newGraph->getOrderedOutputs();

    auto inputParents = std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>(oldOIn.size());
    auto outputChildren = std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>(oldOOut.size());

    // keep in memory every node related to the node to replace :
    // Parent
    for (std::size_t i = 0; i < oldOIn.size(); ++i) {
        std::pair<NodePtr, IOIndex_t> inputParent =
                  oldOIn[i].first -> input(oldOIn[i].second);
        inputParents[i]= inputParent;
        // inputParent.first -> addChild(newOI[i].first, inputParent.second, newOI[i].second);
    }
    // Children
    for (std::size_t i = 0; i < oldOOut.size();) {
        std::vector<std::pair<std::shared_ptr<Aidge::Node>, Aidge::IOIndex_t>> outputChild =
              oldOOut[i].first -> output(oldOOut[i].second);
        if (outputChild.empty()) {
            outputChildren[i] = std::pair<std::shared_ptr<Node>, IOIndex_t>({nullptr, gk_IODefaultIndex});
            ++i;
        }
        else {
            for (const auto& child : outputChild) {
                if (oldNodes.find(child.first) == oldNodes.cend()) {
                    outputChildren[i] = child;
                    ++i;
                }
            }
        }
    }

    // only keep common views to each node for the new set
    // set of common GraphView for oldNodes' Nodes
    std::set<std::shared_ptr<GraphView>> commonGraphViews =  (*oldNodes.begin())->views();
    for (const auto& nodePtr : oldNodes) {
        const std::set<std::shared_ptr<GraphView>> nodeView = nodePtr->views();
        std::set<std::shared_ptr<GraphView>> intersection;
        std::set_intersection(commonGraphViews.begin(), commonGraphViews.end(),
                            nodeView.begin(), nodeView.end(),
                            std::inserter(intersection, intersection.begin()));
        commonGraphViews = intersection;
    }
    commonGraphViews.erase(oldGraph);
    commonGraphViews.erase(newGraph);

    if ((newNodes.size() > 0) && (oldOIn.size() != newOIn.size()) && (oldOOut.size() != newOOut.size())) {
        for (const auto& nodePtr : oldNodes) {
            nodePtr->removeView(oldGraph);
        }
        for (const auto& nodePtr : newNodes) {
            nodePtr->removeView(newGraph);
        }
        return false;
    }

    if ((oldOIn.size() == newOIn.size()) &&
        (oldOOut.size() == newOOut.size())) {
        // Case 1
        for (std::size_t i = 0; i < oldOIn.size(); ++i) {
            if (inputParents[i].first) {
                inputParents[i].first -> addChild(newOIn[i].first, inputParents[i].second, newOIn[i].second);
            }
        }
        for (std::size_t o = 0; o < oldOOut.size(); ++o) {
            if (outputChildren[o].first) {
                newOOut[o].first -> addChild(outputChildren[o].first, newOOut[o].second, outputChildren[o].second);
            }
        }
    }
    else {
        // get the number of Parents for oldG->inputNodes()
        // get the number of Children for oldg->outputNodes()
        if (newNodes.size() == 0) {
            // Case 3
            if (oldOIn.size() == oldOOut.size()) {
                for (std::size_t i = 0; i < oldOIn.size(); ++i) {
                    if (inputParents[i].first) {
                      inputParents[i].first -> addChild(outputChildren[i].first, inputParents[i].second, outputChildren[i].second);
                    }
                }
            }
            else if ((oldOIn.size() == 1) && (inputParents[0].first)) {
                for (std::size_t i = 0; i < oldOIn.size(); ++i) {
                    inputParents[0].first -> addChild(outputChildren[i].first, inputParents[0].second, outputChildren[i].second);
                }
            }
        }
        else if ( // for tiling-like cases. The number of inputNodes changes but not outputNodes
            ((oldOIn.size() == 1) || (newOIn.size() == 1)) && // (oldOIn.size() == newOI.size()) already handled in Case 1
            ((oldOOut.size() == newOOut.size()))
        ) {
            // Case 2
            if ((oldOIn.size() == 1) && (inputParents[0].first)) {
                for (std::size_t i = 0; i < newOIn.size(); ++i) {
                    inputParents[0].first -> addChild(newOIn[i].first, inputParents[0].second, newOIn[i].second);
                }
            } else {
                for (std::size_t i = 0; i < oldOIn.size(); ++i) {
                    if (inputParents[i].first) {
                        inputParents[i].first -> addChild(newOIn[0].first, inputParents[i].second, newOIn[0].second);
                    }
                }
            }
            for (std::size_t o = 0; o < oldOOut.size(); ++o) {
                if (outputChildren[o].first) {
                    newOOut[o].first -> addChild(outputChildren[o].first, newOOut[o].second, outputChildren[o].second);
                }
            }
        }
        else {
            for (const auto& nodePtr : oldNodes) {
                nodePtr->removeView(oldGraph);
            }
            for (const auto& nodePtr : newNodes) {
                nodePtr->removeView(newGraph);
            }
            return false;
        }
    }

    auto oldGOutputs = oldGraph->outputNodes();
    for (const auto& nodePtr : oldNodes) {
        bool removeFromGraphs = true;
        if (std::find(oldGOutputs.cbegin(), oldGOutputs.cend(), nodePtr) == oldGOutputs.cend()) {
            for (const auto& chPtr : nodePtr->getChildren()) {
                if (oldNodes.find(chPtr) == oldNodes.cend()) {
                    removeFromGraphs = false;
                }
            }
        }
        if (removeFromGraphs) {
            for (const auto& g : commonGraphViews) {
                g -> remove(nodePtr, false);
                g -> updateInputsOutputsDelete(nodePtr);
            }
            nodePtr -> resetConnections(true);
        }

    }

    for (const auto& nodePtr : newNodes) {
        for (const auto& g : commonGraphViews) {
            g -> add(nodePtr);
        }
    }
    for (const auto& nodePtr : oldNodes) {
        nodePtr -> removeView(oldGraph);
    }
    for (const auto& nodePtr : newNodes) {
        nodePtr -> removeView(newGraph);
    }
    return true;
}

void Aidge::GraphView::updateInputsOutputsNew(std::shared_ptr<Node> newNode) {
  // Can be called several times with the same node, e.g. when addChild() is
  // called on a node already part of the GraphView. In this case, inputs/outputs
  // need to be updated!
  std::vector<std::pair<NodePtr, IOIndex_t>>::const_iterator newInputsInsertionPoint = mInputNodes.cend();

  // Remove inputs that are not input anymore because connected to newNode
  for (auto orderedChilds : newNode->getOrderedChildren()) {
    for (auto ch_ptr : orderedChilds) {
      // Check that newNode child is in current GraphView
      if (mNodes.find(ch_ptr) != mNodes.cend()) {
        IOIndex_t inputIdx = 0;
        for (const std::shared_ptr<Node>& pa_ptr : ch_ptr->getParents()) {
          // If newNode is connected to it
          if (pa_ptr == newNode) {
            const auto val = std::make_pair(ch_ptr, inputIdx);
            const auto iter = std::find(mInputNodes.cbegin(), mInputNodes.cend(), val);

            // Check that it was not already the case (if node UPDATE)
            if (iter != mInputNodes.cend()) { // newNode is linked to an actual inputNode to an input connection
              // The first old (removed) input becomes the insertion point for newNode GraphView inputs
              if (std::distance(newInputsInsertionPoint, iter) <= 0) {
                newInputsInsertionPoint = mInputNodes.erase(iter);
              }
              else {
                mInputNodes.erase(iter);
              }
            }
          }
          ++inputIdx;
        }
      }
    }
  }

    // Manage newNode parents
    // Check if any input connection is an input for the GraphView
    IOIndex_t inputIdx = 0U;
    for (const std::shared_ptr<Node>& pa_ptr : newNode->getParents()) {
        const auto val = std::make_pair(newNode, inputIdx);
        const auto it = std::find(mInputNodes.cbegin(), mInputNodes.cend(), val);
        if ((pa_ptr == nullptr) ||
            (mNodes.find(pa_ptr) == mNodes.cend())) {
            // Parent doesn't exist || Parent not in the graph
            if (it == mInputNodes.cend()) {
                // If node's inputs are inputs for the GraphView: add them to the input list
                // Addition rule:
                // - Inputs addition order follows node inputs order
                // - Inputs are inserted at the position of the first input removed
                newInputsInsertionPoint = mInputNodes.insert(newInputsInsertionPoint, val);
                newInputsInsertionPoint = std::next(newInputsInsertionPoint);
            }
        } else if (it != mInputNodes.cend()) {
            // Parent already in the graph SO edge is not an input anymore for the graph
            mInputNodes.erase(it);
        }
        ++inputIdx;
    }

  std::vector<std::pair<NodePtr, IOIndex_t>>::const_iterator newOutputsInsertionPoint = mOutputNodes.cend();

  // Remove outputs that are not output anymore because connected to newNode
  for (const std::shared_ptr<Node>& parent : newNode->getParents()) {
    // Check that newNode parent is in current GraphView
    if (mNodes.find(parent) != mNodes.cend()) {
      IOIndex_t outputIdx = 0;
      for (auto orderedChilds : parent->getOrderedChildren()) {
        for (auto ch_ptr : orderedChilds) {
          // If newNode is connected to it
          if (ch_ptr == newNode) {
            const auto val = std::make_pair(parent, outputIdx);
            const auto iter = std::find(mOutputNodes.cbegin(), mOutputNodes.cend(), val);

            if (iter != mOutputNodes.cend()) {
              // The first old (removed) output becomes the insertion point for newNode GraphView outputs
              if (std::distance(newOutputsInsertionPoint, iter) <= 0) {
                newOutputsInsertionPoint = mOutputNodes.erase(iter);
              }
              else {
                mOutputNodes.erase(iter);
              }
            }
          }
        }
        ++outputIdx;
      }
    }
  }

  // Check if node outputs are outputs for the GraphView and add them to the output list if so
  IOIndex_t outputIdx = 0;
  for (const auto& orderedChilds : newNode->getOrderedChildren()) {
    bool noInsideConnection = true;
    for (const auto& ch_ptr : orderedChilds) {
      if (mNodes.find(ch_ptr) != mNodes.cend()) {
        noInsideConnection = false;
        break;
      }
    }

    if (noInsideConnection) {
      const auto val = std::make_pair(newNode, outputIdx);
      // Output may be already be present (see addChild() with a node already in GraphView)
      if (std::find(mOutputNodes.cbegin(), mOutputNodes.cend(), val) == mOutputNodes.cend()) {
        newOutputsInsertionPoint = mOutputNodes.insert(newOutputsInsertionPoint, val);
        newOutputsInsertionPoint = std::next(newOutputsInsertionPoint);
      }
    }
    ++outputIdx;
  }
}

void Aidge::GraphView::updateInputsOutputsDelete(std::shared_ptr<Node> deletedNode) {
  std::vector<std::pair<NodePtr, IOIndex_t>>::const_iterator newInputsInsertionPoint = mInputNodes.cend();

  // Check if node inputs were inputs for the GraphView and remove them from the list if so
  for (IOIndex_t inputIdx = 0; inputIdx < deletedNode->getParents().size(); ++inputIdx) {
    const auto val = std::make_pair(deletedNode, inputIdx);
    const auto iter = std::find(mInputNodes.cbegin(), mInputNodes.cend(), val);

    if (iter != mInputNodes.cend()) {
      // The first old (removed) input becomes the insertion point for new GraphView inputs
      if (std::distance(newInputsInsertionPoint, iter) <= 0) {
        newInputsInsertionPoint = mInputNodes.erase(iter);
      }
      else {
        mInputNodes.erase(iter);
      }
    }
  }

  // Add child node inputs that become GraphView input following the removal of the node
  // Inputs addition order follows deletedNode outputs order
  for (auto orderedChilds : deletedNode->getOrderedChildren()) {
    for (auto ch_ptr : orderedChilds) {
      // Check that deletedNode child is in current GraphView
      if (mNodes.find(ch_ptr) != mNodes.cend()) {
        IOIndex_t inputIdx = 0;
        for (const std::shared_ptr<Node>& pa_ptr : ch_ptr->getParents()) {
          // If newNode was connected to it
          if (pa_ptr == deletedNode) {
            const auto val = std::make_pair(ch_ptr, inputIdx);
            if (std::find(mInputNodes.cbegin(), mInputNodes.cend(), val) == mInputNodes.cend()) {
              newInputsInsertionPoint = mInputNodes.insert(newInputsInsertionPoint, val);
              newInputsInsertionPoint = std::next(newInputsInsertionPoint);
            }
          }
          ++inputIdx;
        }
      }
    }
  }

  std::vector<std::pair<NodePtr, IOIndex_t>>::const_iterator newOutputsInsertionPoint = mOutputNodes.cend();

  // Check if node outputs were outputs for the GraphView and remove them from the list if so
  for (IOIndex_t outputIdx = 0; outputIdx < deletedNode->getOrderedChildren().size(); ++outputIdx) {
    const auto val = std::make_pair(deletedNode, outputIdx);
    const auto iter = std::find(mOutputNodes.cbegin(), mOutputNodes.cend(), val);

    if (iter != mOutputNodes.cend()) {
      // The first old (removed) output becomes the insertion point for newNode GraphView outputs
      if (std::distance(newOutputsInsertionPoint, iter) <= 0) {
        newOutputsInsertionPoint = mOutputNodes.erase(iter);
      }
      else {
        mOutputNodes.erase(iter);
      }
    }
  }

  // Add parent node outputs that become GraphView output following the removal of the node
  // Outputs addition order follows deletedNode inputs order
  for (const std::shared_ptr<Node>& parent : deletedNode->getParents()) {
    if (mNodes.find(parent) != mNodes.end()) {
      IOIndex_t outputIdx = 0;
      for (auto orderedChilds : parent->getOrderedChildren()) {
        bool noInsideConnection = true;
        for (auto ch_ptr : orderedChilds) {
          if (mNodes.find(ch_ptr) != mNodes.end()) {
            noInsideConnection = false;
            break;
          }
        }

        if (noInsideConnection) {
          const auto val = std::make_pair(parent, outputIdx);
          if (std::find(mOutputNodes.cbegin(), mOutputNodes.cend(), val) == mOutputNodes.cend()) {
            newOutputsInsertionPoint = mOutputNodes.insert(newOutputsInsertionPoint, val);
            newOutputsInsertionPoint = std::next(newOutputsInsertionPoint);
          }
        }
        ++outputIdx;
      }
    }
  }

  if (deletedNode == mRootNode) {
    const std::pair<std::vector<NodePtr>, size_t> ranked_nodes = getRankedNodes();
    if(ranked_nodes.second== 0 || ranked_nodes.first.size() <= 1)
    {
      mRootNode = nullptr;
    } else {
      // The new root node will be the second node in the order of ranked nodes
      setRootNode(*std::next(ranked_nodes.first.cbegin(),1));
    }
  }
}


std::shared_ptr<Aidge::GraphView> Aidge::GraphView::cloneCallback(NodePtr(*cloneNode)(NodePtr)) const {
  std::shared_ptr<GraphView> newGraph = std::make_shared<GraphView>(mName);

  // Map for old node -> new node correspondance
  std::map<NodePtr, NodePtr> oldToNewNodes;

  for (const std::shared_ptr<Node> &node_ptr : mNodes) {
    auto clonedNode = cloneNode(node_ptr);
    if (clonedNode == nullptr) {
      AIDGE_ASSERT(node_ptr->getChildren().size() <= 1, "deleted nodes in GraphView::clone() cannot have multiple children");
      AIDGE_ASSERT(node_ptr->nbData() <= 1, "deleted nodes in GraphView::clone() cannot have multiple data input parents");
    }
    oldToNewNodes[node_ptr] = clonedNode;
  }

  // For each node, convert old node -> new node connections
  for (auto &oldToNewNode : oldToNewNodes) {
    if (oldToNewNode.second == nullptr) {
      continue;  // deleted node
    }

    // Connect parent nodes. Nodes that were removed with cloneNode() are set to nullptr
    size_t parentId = 0;
    for (auto parent : oldToNewNode.first->inputs()) {
      if (parent.first != nullptr) {
        while (oldToNewNodes[parent.first] == nullptr) {
          // Find next valid parent in line, going backward in the graph
          AIDGE_INTERNAL_ASSERT(parent.first->getChildren().size() == 1);
          AIDGE_INTERNAL_ASSERT(parent.first->nbData() <= 1);
          const auto& parents = parent.first->dataInputs();

          if (!parents.empty() && parents[0].first != nullptr // a valid parent exists
            && oldToNewNodes.find(parents[0].first) != oldToNewNodes.end()) // parent is in the GraphView
          {
            parent = parents[0];
          }
          else {
            break;
          }
        }

        if (oldToNewNodes[parent.first]) {
          AIDGE_INTERNAL_ASSERT(oldToNewNodes[parent.first]->nbOutputs() == parent.first->nbOutputs());
          oldToNewNodes[parent.first]->addChild(oldToNewNode.second, parent.second, parentId);
        }
      }

      ++parentId;
    }
  }

  // Once connected, add each new nodes to new GraphView
  // This has to be done in a second step to ensure that new GraphView inputs/outputs
  // are properly set (otherwise, some node's inputs/outputs may be wrongly registered as
  // GraphView inputs/outputs because not yet connected to other nodes)
  if (oldToNewNodes[mRootNode] != nullptr) {
    // Add root node first if is still exists!
    newGraph->add(oldToNewNodes[mRootNode], false);
  }

  for (auto &oldToNewNode : oldToNewNodes) {
    if (oldToNewNode.second == nullptr)
      continue;  // deleted node

    newGraph->add(oldToNewNode.second, false);
  }

  // Update cloned graph inputs/outputs order to match initial graph order
  auto newInputNodes = mInputNodes;
  for (auto it = newInputNodes.begin(); it != newInputNodes.end(); ) {
    // If input node was removed, find next valid input
    while (oldToNewNodes[it->first] == nullptr) {
      // Removed node should have only one connected output, otherwise cloning is invalid
      AIDGE_INTERNAL_ASSERT(it->first->getChildren().size() <= 1);
      bool found = false;

      if (it->first->getChildren().size() == 1) {
        auto child = *it->first->getChildren().begin();

        std::size_t inputIdx = 0;
        for (auto parent : child->getParents()) {
          if (parent == it->first) {
            it->first = child;
            it->second = inputIdx;
            found = true;
            break;
          }
          ++inputIdx;
        }
      }

      if (!found) {
        break;
      }
    }

    if (oldToNewNodes[it->first] == nullptr) {
      it = newInputNodes.erase(it);
    }
    else {
      it->first = oldToNewNodes[it->first];
      ++it;
    }
  }
  newGraph->setOrderedInputs(newInputNodes);

  auto newOutputNodes = mOutputNodes;
  for (auto it = newOutputNodes.begin(); it != newOutputNodes.end(); ) {
    // If output node was removed, find previous valid output
    while (oldToNewNodes[it->first] == nullptr) {
      // Removed node should have only one connected data input, otherwise cloning is invalid
      AIDGE_INTERNAL_ASSERT(it->first->nbData() <= 1);
      auto parents = it->first->dataInputs();

      if (!parents.empty() && parents[0].first != nullptr // a valid parent exists
        && oldToNewNodes.find(parents[0].first) != oldToNewNodes.end()) // parent is in the GraphView
      {
        *it = parents[0];
      }
      else {
        break;
      }
    }

    if (oldToNewNodes[it->first] == nullptr) {
      it = newOutputNodes.erase(it);
    }
    else {
      it->first = oldToNewNodes[it->first];
      ++it;
    }
  }
  newGraph->setOrderedOutputs(newOutputNodes);

  return newGraph;
}

std::shared_ptr<Aidge::GraphView> Aidge::getConnectedGraphView(std::shared_ptr<Node> node) {
  std::vector<NodePtr> foundNodes;
  foundNodes.push_back(node);

  for (size_t curNodeIdx = 0; curNodeIdx < foundNodes.size(); ++curNodeIdx) {
    NodePtr curNode = foundNodes[curNodeIdx];

    for (auto childs : curNode->getOrderedChildren()) {
      for (auto child : childs) {
        if (child != nullptr && std::find(foundNodes.begin(), foundNodes.end(), child) == foundNodes.end()) {
          foundNodes.push_back(child);
        }
      }
    }

    for (auto parent : curNode->getParents()) {
      if (parent != nullptr && std::find(foundNodes.begin(), foundNodes.end(), parent) == foundNodes.end()) {
        foundNodes.push_back(parent);
      }
    }
  }

  auto graph = std::make_shared<GraphView>();
  graph->add(node);
  graph->add({foundNodes.cbegin(), foundNodes.cend()});
  return graph;
}
