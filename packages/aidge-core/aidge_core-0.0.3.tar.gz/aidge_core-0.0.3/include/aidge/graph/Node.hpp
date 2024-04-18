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

#ifndef AIDGE_CORE_GRAPH_NODE_H_
#define AIDGE_CORE_GRAPH_NODE_H_

#include <cassert>
#include <memory>
#include <set>
#include <string>
#include <vector>
#include <utility>

#include "aidge/graph/Connector.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

using NodePtr = std::shared_ptr<Node>;

class GraphView;

/**
 * @brief Object carrying the topological information of the computational graph.
 */
class Node : public std::enable_shared_from_this<Node> {
private:
  struct weakCompare {
      bool operator()(const std::weak_ptr<Aidge::GraphView>& a, const std::weak_ptr<Aidge::GraphView>& b) const {
          // Compare the content of the weak_ptrs
          auto sharedA = a.lock();
          auto sharedB = b.lock();
          if (!sharedB) return false; // nothing after expired pointer
          if (!sharedA) return true;
          return sharedA < sharedB; // shared_ptr has a valid comparison operator
      }
  };
  std::string mName; /** Name of the Node. Should be unique. */

  std::set<std::weak_ptr<GraphView>, weakCompare> mViews; /** Set of pointers to GraphView instances including this Node instance. */
  const std::shared_ptr<Operator> mOperator; // Pointer to the associated Operator

  std::vector<NodePtr> mParents; /** List of parent node for each input (Parent --> Node --> Child) */
  std::vector<std::vector<std::weak_ptr<Node>>> mChildren; /** List of children nodes for each output (Parent --> Node --> Child) */
  std::vector<std::vector<IOIndex_t>> mIdInChildren; /** List of input index for each Node linked to each output of the Node. */
  std::vector<IOIndex_t> mIdOutParents; /** index of the output linked to each input of the Node. Default: gk_IODefaultIndex. */

public:
  Node() = delete;

  /**
   * @brief Construct a new Node object associated with the input Operator.
   * @param op Operator giving the Node its number of connections.
   * @param name (optional) name for the Node.
   */
  Node(std::shared_ptr<Operator> op, const std::string& name = "");

  virtual ~Node() = default;

  friend bool operator==(const Node &lhs, const Node &rhs) {
    return lhs.shared_from_this() == rhs.shared_from_this();
  }

public:
  ///////////////////////////////////////////////////////
  //        FUNCTIONAL DESCRIPTION
  ///////////////////////////////////////////////////////

  /**
   * @brief Functional operator for user-friendly connection interface using an ordered set of Connectors.
   * @param ctors Ordered Connectors linking their associated Node to the input of the current Node with the same index.
   * @return Connector
   */
  Connector operator()(const std::vector<Connector> &ctors);

public:
  ///////////////////////////////////////////////////////
  //        INNER
  ///////////////////////////////////////////////////////

  /**
   * @brief Name of the Node.
   * @return std::string
   */
  inline std::string name() const noexcept { return mName; }

  /**
   * @brief Set the Node name.
   * @warning Undefined behaviour when several Nodes have the same name.
   * @param name New name for the node.
   */
  void setName(const std::string &name);

  /**
   * @brief Type of the node.
   * @return std::string
   */
  inline std::string type() const { return mOperator->type(); }

  ///////////////////////////////////////////////////////
  //        OPERATORS
  ///////////////////////////////////////////////////////

  /**
   * @brief Run forward() function of the associated Operator.
   */
  void forward();

  /**
   * @brief Run backward() function of the associated Operator.
   */
  void backward();

  /**
   * @brief Get the Operator object of the Node.
   * @return std::shared_ptr<Operator>
   */
  inline std::shared_ptr<Operator> getOperator() const { return mOperator; }

  ///////////////////////////////////////////////////////
  //        TENSOR MANAGEMENT
  ///////////////////////////////////////////////////////

  /**
   * @brief Whether or not every input of the Node is linked to a Parent.
   * If true then the Node is ready to be executed.
   * @return true
   * @return false
   */
  bool valid() const;

  /**
   * @brief List of pair <Parent, ID of the data intput>. When an input is not
   * linked to any Parent, the pair is <nullptr, gk_IODefaultIndex>.
   * Data inputs exclude inputs expecting parameters (weights or bias).
   * @return std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>
   */
  std::vector<std::pair<NodePtr, IOIndex_t>> dataInputs() const;

  /**
   * @brief List of pair <Parent, ID of the parent output>. When an input is not linked
   * to any Parent, the pair is <nullptr, gk_IODefaultIndex>.
   * @return std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>
   */
  std::vector<std::pair<NodePtr, IOIndex_t>> inputs() const;

  /**
   * @brief Parent and its output Tensor ID linked to the inID-th input Tensor.
   * If the input is not linked to any Parent, the pair is <nullptr, gk_IODefaultIndex>.
   * @param inID
   * @return std::pair<std::shared_ptr<Node>, IOIndex_t>
   */
  inline std::pair<NodePtr, IOIndex_t> input(const IOIndex_t inID) const {
    assert((inID != gk_IODefaultIndex) && (inID < nbInputs()) && "Input index out of bound.");
    return std::pair<NodePtr, IOIndex_t>(mParents[inID], mIdOutParents[inID]);
  }


  /**
   * @brief Get the lowest index in the InputData Parent list equal to the
   * nullptr.
   * Data inputs exclude inputs expecting parameters (weights or bias).
   * @return std::size_t
   */
  inline IOIndex_t getFirstFreeDataInput() const {
    IOIndex_t i = 0;
    for (; (i < nbData()) && (input(i).second != gk_IODefaultIndex); ++i) {}
    // assert((i<nbData()) && "No free data input for Node");
    return (i < nbData()) ? i : gk_IODefaultIndex;
  }


  IOIndex_t getNbFreeDataInputs() const;

  /**
   * @brief List input ids of children linked to outputs of the node. The vector
   * size is garanteed to match the number of outputs of the node. If there is
   * no connection to a given output, the corresponding sub-vector will be empty.
   * @return std::vector<std::vector<std::pair<std::shared_ptr<Node>,
   * IOIndex_t>>>
   */
  std::vector<std::vector<std::pair<NodePtr, IOIndex_t>>> outputs() const;

  /**
   * @brief Children and their input Tensor ID linked to the outId-th output
   * Tensor.
   * @param outId
   * @return std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>>
   */
  std::vector<std::pair<NodePtr, IOIndex_t>>
  output(IOIndex_t outId) const;

  /**
   * @brief Number of inputs, including both data and learnable parameters.
   * @details [data, data, weight, bias] => 4
   * @return IOIndex_t
   */
  inline IOIndex_t nbInputs() const noexcept { return getOperator()->nbInputs(); }

  /**
   * @brief Number of input specifically for data.
   * Data inputs exclude inputs expecting parameters (weights or bias).
   * @details [data, data, weight, bias] => 2
   * @return IOIndex_t
   */
  inline IOIndex_t nbData() const noexcept {
    return getOperator()->nbData();
  }

  /**
   * @brief Number of inputs linked to a Parent's output.
   * @return IOIndex_t
   */
  IOIndex_t nbValidInputs() const;

  /**
   * @brief Getter for the number of Output Tensors of the Node.
   * @return IOIndex_t
   */
  inline IOIndex_t nbOutputs() const noexcept { return getOperator()->nbOutputs(); }

  IOIndex_t nbValidOutputs() const;

  ///////////////////////////////////////////////////////
  //        TOPOLOGY
  ///////////////////////////////////////////////////////

  /**
   * @brief Vector of pointers to each GraphView containing the object
   * @return std::vector<GraphView>
   */
  inline std::set<std::shared_ptr<GraphView>> views() const noexcept {
    std::set<std::shared_ptr<GraphView>> res;
    for (const auto &v : mViews) {
      res.insert(v.lock());
    }
    return res;
  }

  /**
   * @brief Add a GraphView pointer to the list of GraphView containing
   * the current Node. This feature allows transparent GraphViews.
   * @param graphPtr Pointer to GraphView to add to the list.
   */
  inline void addView(const std::shared_ptr<GraphView> &graphPtr) {
    mViews.insert(std::weak_ptr<GraphView>(graphPtr));
  }

  inline void removeView(const std::shared_ptr<GraphView> &graphPtr) {
    mViews.erase(graphPtr);
  }

  /**
   * @brief Link another Node to an output of the current Node.
   * @param otherNode Pointer to the other Node.
   * @param outId ID of the current Node output to connect to the other Node.
   * Default to 0.
   * @param otherInId ID of the other Node input to connect to the current Node.
   * Default to the first avaible data input.
   */
  void addChild(NodePtr otherNode,
                const IOIndex_t outId = IOIndex_t(0),
                IOIndex_t otherInId = gk_IODefaultIndex);

  /**
   * @brief Link a Node from a specific GraphView to the current Node.
   * @param otherView Pointer to the GraphView whose content should be
   * linked to the current Node.
   * @param outId ID of the output Tensor to connect to the other Node.
   * Default to 0.
   * @param otherInId Pair of pointer to Node and Tensor ID for specifying the
   * connection. If the GraphView whose content is linked has only one input
   * Node, then it defaults to the first available data input Tensor of this
   * Node.
   */
  void addChild(std::shared_ptr<GraphView> otherView,
                const IOIndex_t outId = IOIndex_t(0),
                std::pair<NodePtr, IOIndex_t> otherInId =
                std::pair<NodePtr, IOIndex_t>(nullptr, gk_IODefaultIndex));

  /**
   * @brief Get the list of parent Nodes. As an input is linked to a unique Node,
   * if none is linked then the parent is a nullptr.
   * @return std::vector<std::shared_ptr<Node>>
   */
  std::vector<NodePtr> getParents() const;

  /**
   * @brief Get the pointer to parent of the specified input index. This pointer is nullptr if no parent is linked.
   * @param inId Input index.
   * @return std::shared_ptr<Node>&
   */
  inline NodePtr &getParent(const IOIndex_t inId) {
    assert(inId != gk_IODefaultIndex);
    return mParents.at(inId);
  }

  /**
   * @brief Unlink the parent Node at the specified input index and return its pointer.
   * Return a nullptr is no parent was linked.
   * @param inId Input index.
   * @return std::shared_ptr<Node>
   */
  NodePtr popParent(const IOIndex_t inId);

  bool removeParent(const IOIndex_t inId);

  /**
   * @brief Get the set of pointers to children Nodes linked to the current Node.object.
   * @details The returned set does not include any nullptr as an output maybe linked to
   * an undifined number of Nodes. It does not change the computation of its associated Operator.
   * @return std::set<std::shared_ptr<Node>>>
   */
  std::set<NodePtr> getChildren() const;

  std::vector<std::vector<NodePtr>> getOrderedChildren() const;

  /**
   * @brief Get the list of children Nodes linked to the output at specified index.
   * @param outId Output index.
   * @return std::vector<std::shared_ptr<Node>>
   */
  std::vector<NodePtr> getChildren(const IOIndex_t outId) const;

  /**
   * @brief Remove registered child from children list of specified output if possible.
   * If so, also remove current Node from child Node from parent.
   * @param std::shared_ptr<Node> Node to remove.
   * @param outId Output index. Default 0.
   * @return true Child found and removed for given output index.
   * @return false Child not found at given index. Nothing removed.
   */
  bool removeChild(const NodePtr nodePtr, const IOIndex_t outId = 0);

  /**
   * @brief Remove every link of surrounding nodes to it and conversly
   */
  void resetConnections(bool includeLearnableParam = false);

  ///////////////////////////////////////////////////////
  //        CLONE
  ///////////////////////////////////////////////////////

  /**
   * @brief Clone the current Node. The Operator attribute of the new Node is not copied but shared with the current Node. The new node has no connection.
   * @return NodePtr
   */
  NodePtr cloneSharedOperators() const;

  /**
   * @brief Clone the Node. Every attribute is copied, even Operator pointer except for Producers for which it is shared. The new Node has no connection.
   * @return NodePtr
   */
  NodePtr cloneSharedProducers() const;

  /**
   * @brief Clone the Node and its Operator. The new Node has no connection.
   * @return NodePtr
   */
  NodePtr clone() const;

  /**
   * @brief Callback function to clone the Node keeping the same Operator object instance. The new Node has no connection.
   * @param node Node to clone.
   * @return NodePtr
   */
  static NodePtr cloneSharedOperators(NodePtr node) {
    return node->cloneSharedOperators();
  }

  /**
   * @brief Callback function to clone the Node. Every attribute is copied, even Operator pointer except for Producers for which it is shared. The new Node has no connection.
   * @param node Node to clone.
   * @return NodePtr
   */
  static NodePtr cloneSharedProducers(NodePtr node) {
    return node->cloneSharedProducers();
  }

  /**
   * @brief Callback function to clone the Node and its Operator. The new Node has no connection.
   * @param node Node to clone.
   * @return NodePtr
   */
  static NodePtr clone(NodePtr node) {
    return node->clone();
  }


  /**
   * @brief  Get the set of pointers to connected node at a distance of a delta.
   * @details the recution are cut
   * Return a nullptr is nofing found.
   * @param delta Input delta.
   * @return std::shared_ptr<Node>
   */

  std::set<NodePtr> getNodeDelta(int delta,std::set<Aidge::NodePtr> nodeSee);


private:
  ///////////////////////////////////////////////////////
  //        OPERATORS
  ///////////////////////////////////////////////////////

  // cannot change operator for now
  // void setOperator(const std::shared_ptr<Operator> op_ptr);

  ///////////////////////////////////////////////////////
  //        TENSOR MANAGEMENT
  ///////////////////////////////////////////////////////

  /**
   * @brief Set the idInChildren parameter.
   * @param inID
   * @param newNodeOutID
   */
  void setInputId(const IOIndex_t inID, const IOIndex_t newNodeOutID);

  ///////////////////////////////////////////////////////
  //        TOPOLOGY
  ///////////////////////////////////////////////////////

  /**
   * @brief Add the given Node as a child for the current Node.
   * @param otherNode
   * @param outId
   * @param otherInId
   */
  void addChildOp(NodePtr otherNode, const IOIndex_t outId,
                  const IOIndex_t otherInId);

  /**
   * @brief Add the given GraphView's input Node as a child for the current Node
   * @param otherGraph
   * @param outId
   * @param otherInId pointer the GraphView's input Node and its input index. Defaults to the
   * only input Node if the GraphView has got one.
   */
  void addChildView(std::shared_ptr<GraphView> otherGraph,
                    const IOIndex_t outId,
                    std::pair<NodePtr, IOIndex_t> otherInId);

  /**
   * @brief Add a Node to the list of parents.
   * @param otherNode Node to add to parents list.
   * @param inId index for adding the parent.
   */
  void addParent(const NodePtr otherNode, const IOIndex_t inId);

  // OPERATOR FUNCTIONNAL but commented out to avoid iostream inclusion
  // /**
  //  * @brief operator<< overload to ease print & debug of nodes
  //  * @param[inout] ostream to print to 
  //  * @param[in] n node to print
  //  */
  // friend std::ostream& operator << (std::ostream& os, Node& n); 
};

} // namespace Aidge


#endif /* AIDGE_CORE_GRAPH_NODE_H_ */
