
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

#ifndef AIDGE_CORE_GRAPH_GRAPHVIEW_H_
#define AIDGE_CORE_GRAPH_GRAPHVIEW_H_

#include <map>
#include <memory>
#include <set>
#include <string>
#include <utility>
#include <vector>

#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
enum class DataType;

/**
 * @brief Groupement of Nodes forming a computational graph on which properties and functions
 * can easily and safely be applied or run.
 */
class GraphView : public std::enable_shared_from_this<GraphView> {
private:
    /// @brief Name of the graphview
    std::string mName;

    /// @brief GraphView root node
    NodePtr mRootNode;

    /// @brief Set of nodes included in the GraphView
    std::set<NodePtr> mNodes;

    /// @brief Set of nodes included in the graphview with names
    std::map<std::string, NodePtr> mNodeRegistry;

    /// @brief GraphView inputs IOIndex_t designates the input number
    std::vector<std::pair<NodePtr, IOIndex_t>> mInputNodes;

    /// @brief GraphView outputs IOIndex_t designates the input number
    std::vector<std::pair<NodePtr, IOIndex_t>> mOutputNodes;

public:
    GraphView(const std::string& name="")
        : mName(name)
    {
        // ctor
    }

    bool operator==(const GraphView &gv) const
    {
        return mNodes == gv.mNodes;
    }

    const NodePtr operator[](const std::string& nodeName) const;

///////////////////////////////////////////////////////
//        FUNCTIONAL DESCRIPTION
///////////////////////////////////////////////////////

    Connector operator()(const std::vector<Connector> ctors);

///////////////////////////////////////////////////////
//        INNER
///////////////////////////////////////////////////////
public:
    /**
     * @brief Name of the node.
     * @return std::string
     */
    inline std::string name() const noexcept { return mName; }

    /**
     * @brief Set the node name.
     * @warning Undefined behaviour when several Nodes have the same name.
     * @param name New name for the node.
     */
    inline void setName(const std::string &name) { mName = name; }

    /**
     * @brief Save the GraphView as a Mermaid graph in a .md file at the
     * specified location.
     * @param path
     */
    void save(const std::string& path, bool verbose = false, bool showProducers = true) const;

    void logOutputs(const std::string& dirName) const;

    /**
     * Check that a node is in the current GraphView.
     * @param nodePtr Node to check
     * @return bool True is nodePtr belongs to the GraphView.
    */
    bool inView(const NodePtr& nodePtr) const;

    inline NodePtr rootNode() const noexcept {
        return mRootNode;
    }

    void setRootNode(NodePtr node);

///////////////////////////////////////////////////////
//        TENSOR MANAGEMENT
///////////////////////////////////////////////////////
public:
    /** @brief Get reference to the set of input Nodes. */
    std::set<NodePtr> inputNodes() const;

    /** @brief Get reference to the set of output Nodes. */
    std::set<NodePtr> outputNodes() const;

    /** @brief Assess if the given Node is an input Node of the GraphView object. */
    bool isInputNode(const NodePtr& nodePtr) const;

    /** @brief Assess if the given Node is an output Node of the GraphView object. */
    bool isOutputNode(const NodePtr& nodePtr) const;

    void setOrderedInputs(const std::vector<std::pair<NodePtr, IOIndex_t>>& inputs);
    void setOrderedOutputs(const std::vector<std::pair<NodePtr, IOIndex_t>>& outputs);

    /**
     * @brief Get inputs of the current GraphView with their associated id.
     * The rank of the nodes are their rank in the vector.
     * @return const std::vector<std::pair<NodePtr, IOIndex_t>>&
     */
    inline const std::vector<std::pair<NodePtr, IOIndex_t>>& getOrderedInputs() const noexcept { return mInputNodes; };
    /**
     * @brief Get outputs of the current GraphView with their associated id.
     * The rank of the nodes are their rank in the vector.
     * @return const std::vector<std::pair<NodePtr, IOIndex_t>>&
     */
    inline const std::vector<std::pair<NodePtr, IOIndex_t>>& getOrderedOutputs() const noexcept { return mOutputNodes; };

    /**
     * @brief List outside data input connections of the GraphView.
     * Data inputs exclude inputs expecting parameters (weights or bias).
     * The vector size is garanteed to match the number of outside data inputs of the GraphView. If there is
     * no external connection to a given input, a pair of nullptr and gk_IODefaultIndex is returned.
     * @return std::vector<std::pair<NodePtr, IOIndex_t>>
     */
    std::vector<std::pair<NodePtr, IOIndex_t>> dataInputs() const;

    /**
     * @brief List all dataInput connections (within and outside) of the specified GraphView node named "name".
     * Data inputs exclude inputs expecting parameters (weights or bias).
     * @param name Name of the Node.
     * @return std::vector<std::pair<NodePtr, IOIndex_t>>
     */
    inline auto dataInputs(const std::string name) const { return mNodeRegistry.at(name)->dataInputs(); }

    /**
     * @brief List outside input connections of the GraphView. The vector
     * size is garanteed to match the number of outside inputs of the GraphView. If there is
     * no external connection to a given input, a pair of nullptr and gk_IODefaultIndex is returned.
     * @return std::vector<std::pair<NodePtr, IOIndex_t>>
     */
    std::vector<std::pair<NodePtr, IOIndex_t>> inputs() const;

    /**
     * @brief List all input connections (within and outside) of the specified GraphView node named "name".
     * @return std::vector<std::pair<NodePtr, IOIndex_t>>
     */
    std::vector<std::pair<NodePtr, IOIndex_t>> inputs(const std::string& name) const;

    /**
     * @brief List outside output connections of the GraphView. The vector
     * size is garanteed to match the number of outputs of the GraphView. If there is
     * no connection to a given output, the corresponding sub-vector will be empty.
     * @return std::vector<std::pair<NodePtr, IOIndex_t>>
     */
    std::vector<std::vector<std::pair<NodePtr, IOIndex_t>>> outputs() const;

    /**
     * @brief List all output connections (within and outside) of the specified GraphView node named "name".
     * @param nodeName Name of the Node of which to show the output.
     * @return std::vector<std::vector<std::pair<NodePtr, IOIndex_t>>>
     */
    std::vector<std::vector<std::pair<NodePtr, IOIndex_t>>> outputs(
            const std::string& nodeName) const;

    /**
     * @brief Assert Datatype, Backend, data format and dimensions along the GraphView are coherent.
     * If not, apply the required transformations.
     * @details Sets the GraphView ready for computation in four steps:
     * 1 - Assert input Tensors' datatype is compatible with each Operator's datatype.
     * If not, a conversion Operator is inserted.
     * 2 - Assert input Tensors' backend is compatible with each Operator's backend.
     * If not, add a Transmitter Operator.
     * 3 - Assert data format (NCHW, NHWC, ...) of each Operator's input Tensor is
     * compatible with the selected kernel.
     * If not, add a Transpose Operator.
     * 4 - Propagate Tensor dimensions through the consecutive Operators.
     */
    void compile(const std::string& backend = "cpu",
                 const Aidge::DataType datatype = DataType::Float32,
                 DeviceIdx_t device = 0,
                 const std::vector<std::vector<DimSize_t>> dims = {});

    /**
     * @brief Compute dimensions of input/output Tensors for each Operator of the
     * GraphView object's Nodes.
     */
    void forwardDims(const std::vector<std::vector<DimSize_t>> dims = {});

    /** @brief Set the same backend for each Operator of the GraphView object's Nodes. */
    void setBackend(const std::string& backend, const DeviceIdx_t device = 0) const;
    /** @brief Set the same backend for each Operator of the GraphView object's Nodes. */
    void setDataType(const DataType& datatype) const;

///////////////////////////////////////////////////////
//        TOPOLOGY
///////////////////////////////////////////////////////
public:
    /**
     * @brief Get the parents Nodes of inputNodes.
     * @return std::set<NodePtr>
     */
    std::set<NodePtr> getParents() const;
    /**
     * @brief Get parents Nodes of the specified Node.
     * @param nodeName Name of the Node.
     * @return std::vector<NodePtr>
     */
    std::vector<NodePtr> getParents(const std::string nodeName) const;
    std::vector<std::vector<NodePtr>> getOrderedParents() const;

    /**
     * @brief Get the children Nodes of outputNodes.
     * @return std::set<NodePtr>
     */
    std::set<NodePtr> getChildren() const;
    /**
     * @brief Get children Nodes of the specified Node.
     * @param nodeName Name of the Node.
     * @return std::vector<std::vector<NodePtr>>
     */
    std::vector<std::vector<NodePtr>> getChildren(const std::string nodeName) const;
    std::set<NodePtr> getChildren(
            const NodePtr otherNode) const;  // TODO change it for a vector<vector> ?

    /**
     * @brief Get the Nodes pointed to by the GraphView object.
     * @return std::set<NodePtr>
     */
    inline const std::set<NodePtr>& getNodes() const { return mNodes; }

    /**
     * @brief Get the operator with the corresponding name if it is in the
     * GraphView.
     * @param nodeName Name of the node.
     * @return NodePtr returns a nullptr if the one asked for
     * was not found.
     */
    NodePtr getNode(const std::string& nodeName) const;

    /**
     * Get the ranked list of nodes in the GraphView.
     * Node ranking if performed the following:
     * - The root node is put in the ranked list first (rank 1);
     * - Then, its childs (in order of outputs) are added in the ranked list;
     * - Then, its parents (in order of inputs) are added in the ranked list;
     * - The childs and parents of the next node in the ranked list are then
     *   added to the list, and so on.
     * - Any remaining nodes have no path to the root node and are added in
     *   arbitrary order. In this case, the ranking is not garanteed to be unique.
     *
     * If the ranking cannot be garanteed to be unique, the second item indicates
     * the rank from which unicity cannot be garanteed.
     * @return std::pair<std::vector<NodePtr>, size_t> Pair with the list of ranked
     * nodes and the size of the ranked sub-list where unicity is garanteed.
    */
    std::pair<std::vector<NodePtr>, size_t> getRankedNodes() const;

    /**
     * Get the nodes name according to the GraphView nodes ranking.
     * @param format The formatting string to be used with fmt::format().
     * The usable positional arguments are the following:
     * {0} node name, {1} node type, {2} rank, {3} type rank
     * @param markNonUnicity If true, non unique ranking is prefixed with "?"
     * @return std::map<NodePtr, std::string> A map with the corresponding names
    */
    std::map<NodePtr, std::string> getRankedNodesName(const std::string& format, bool markNonUnicity = true) const;

    /**
     * @brief Remove a Node from the current GraphView scope without affecting its connections.
     * @param nodePtr Node to remove
     * @param includeLearnableParam Whether learnable parameters should also be removed. Default true.
     */
    void remove(NodePtr nodePtr, bool includeLearnableParam = true);

    // Surrounding nodes management

    void setInputId(IOIndex_t inID, IOIndex_t newNodeOutID);

    /**
     * @brief Include a Node to the current GraphView object.
     * @param other_Nde Node to add.
     * @param includeLearnableParam Include non-data inputs, like weights and biases
     * in the GraphView automatically. Default: true.
     */
    void add(NodePtr otherNode, bool includeLearnableParam = true);

    /**
     * @brief Include a set of Nodes to the current GraphView object.
     * @param otherNodes
     * @param includeLearnableParam
     * @return true if graph ordering is unique (meaning inputs/outputs order is well defined).
     */
    bool add(std::set<NodePtr> otherNodes,
             bool includeLearnableParam = true);

    /**
     * @brief Include a set of Nodes to the current GraphView object.
     * The first element of the otherNodes pair is the start node and
     * the second is the remaining nodes to add.
     * @param otherNodes
     * @param includeLearnableParam
     * @return true if graph ordering is unique (meaning inputs/outputs order is well defined).
     */
    bool add(std::pair<NodePtr, std::set<NodePtr>> otherNodes,
             bool includeLearnableParam = true);

    /**
     * @brief Include every Node inside another GraphView to the current
     * GraphView.
     * @param other_graph GraphView containing the Nodes to include.
     * @return true if graph ordering is unique (meaning inputs/outputs order is well defined).
     */
    bool add(std::shared_ptr<GraphView> otherGraph);

    /**
     * @brief Include a Node in the current GraphView and link it to another
     * already contained Node.
     *
     * @param toOtherNode Pointer to the Node to add.
     * @param fromOutNode Pointer to the already included Node the new Node will
     * be linked to (it will become a parent of the new Node). If the GraphView
     * only has one output Node, then default to this Node.
     * @param fromTensor Ouput Tensor ID of the already included Node. Default to
     * 0.
     * @param toTensor Input Tensor ID of the new Node. Default to gk_IODefaultIndex, meaning
     * first available data input for the Node.
     */
    void addChild(NodePtr toOtherNode, NodePtr fromOutNode = nullptr,
                  const IOIndex_t fromTensor = IOIndex_t(0),
                  IOIndex_t toTensor = gk_IODefaultIndex);

    /**
     * @brief Include a Node in the current GraphView and link it to another
     * already contained Node.
     *
     * @param toOtherNode Pointer to the Node to add.
     * @param fromOutNodeName Name of the already included Node the new Node will
     * be linked to (it will become a parent of the new Node). As a name is
     * optional, ensure such Node is in the GraphView or it will send back an
     * error message.
     * @param fromTensor Ouput Tensor ID of the already included Node. Default to
     * 0.
     * @param toTensor Input Tensor ID of the new Node. Default to gk_IODefaultIndex, meaning
     * first available data input for the Node.
     */
    inline void addChild(NodePtr toOtherNode, const std::string& fromOutNodeName,
                         const IOIndex_t fromTensor = IOIndex_t(0),
                         IOIndex_t toTensor = gk_IODefaultIndex) {
        AIDGE_ASSERT(mNodeRegistry.find(fromOutNodeName) != mNodeRegistry.end(), "No node named {} in graph {}.", fromOutNodeName, name());
        addChild(toOtherNode, mNodeRegistry.at(fromOutNodeName), fromTensor, toTensor);
    }

    /**
     * @brief Include a GraphView content in the current GraphView and link
     * the two sets by linking one Node from each GraphView.
     * @param toOtherView Pointer to the GraphView whose content should be added.
     * @param fromOutNode Pair of pointer to Node and Tensor ID for specifying the
     * connection. If the GraphView including the other one has only one output
     * Node, then it defaults to the first output Tensor of this Node.
     * @param toNode Pair of pointer to Node and Tensor ID for specifying the
     * connection. If the GraphView whose content is included has only one input
     * Node, then it defaults to the first available data input Tensor of this
     * Node.
     */
    void addChild(std::shared_ptr<GraphView> toOtherView,
                  std::pair<NodePtr, IOIndex_t> fromOutNode =
                          std::pair<NodePtr, IOIndex_t>(nullptr, IOIndex_t(0)),
                  std::pair<NodePtr, IOIndex_t> toNode =
                          std::pair<NodePtr, IOIndex_t>(nullptr, gk_IODefaultIndex));

    /**
     * @brief Swap two Node instances if possible.
     * @param node
     * @param otherNode
     * @return true
     * @return false
     */
    bool swap(Node &node, Node &otherNode);

    void link(const std::string& name1_inID, const std::string& name2_outID);

    /**
     * @brief Insert a node (newParentNode) as a parent of the passed node (childNode).
     *
     * @param childNode Node that gets a new parent.
     * @param newParentNode Inserted Node.
     * @param childInputTensorIdx Index of the input Tensor for the childNode linked to the inserted Node output.
     * @param newParentInputTensorIdx Index of the input Tensor for the newParentNode linked to the former parent of childNode.
     * @param newParentOutputTensorIdx Index of the output Tensor for the newParentNode linked to the childNode's input Tensor.
     */
    void insertParent(NodePtr childNode,
                        NodePtr newParentNode,
                        IOIndex_t childInputTensorIdx,
                        IOIndex_t newParentInputTensorIdx,
                        IOIndex_t newParentOutputTensorIdx);

    /**
     * @brief Replace a set of Nodes in every available GraphView with a new set of Nodes if possible.
     * Both sets should include all the necessary Producers.
     * @details There are 3 cases of replacement:
     * Case 1: same number of input/output connections for oldNodes and newNodes sets.
     *     - input/output connections are replacated according to their IDs.
     * Case 2: different number of input/output connections for oldNodes and newNodes sets.
     *     - only a single parent/child node for the newNodes set, every input/output is
     *       connected to it.
     *     - several parents/children nodes for newNodes set => impossible to know, return false
     * Case 3: newNodes set is empty
     *     - same number of input/output connections in oldNodes, parents and children are linked according
     *       to these connections IDs
     *     - different number of input/output connections in oldNodes => return false
     * @param oldNodes
     * @param newNodes
     * @return true replacement has been performed
     * @return false no replacement has been performed
     */
    static bool replace(const std::shared_ptr<GraphView>& oldG, const std::shared_ptr<GraphView>& newG);
    static bool replace(const std::set<NodePtr>& oldNodes, const std::set<NodePtr>& newNodes);

    /**
     * @brief Clone the GraphView with shared Operators. It is a new GraphView, with cloned Nodes, but the new Nodes refer to the same Operators as the original ones.
     * @return std::shared_ptr<GraphView>
     */
    inline std::shared_ptr<GraphView> cloneSharedOperators() const {
        return cloneCallback(&Node::cloneSharedOperators);
    }

    /**
     * @brief Clone the GraphView with shared Producers. All the other Operators are copied.
     * @return std::shared_ptr<GraphView>
     */
    inline std::shared_ptr<GraphView> cloneSharedProducers() const {
        return cloneCallback(&Node::cloneSharedProducers);
    }

    /**
     * @brief Clone the GraphView. Everything is cloned: Nodes and Operators.
     * @return std::shared_ptr<GraphView>
     */
    inline std::shared_ptr<GraphView> clone() const {
        return cloneCallback(&Node::clone);
    }

    /**
     * @brief Clone the current GraphView using a callback function for the Node cloning, allowing to specify how each Node should be cloned or replaced by another Node type, or removed (i.e. replaced by identity). When a Node is removed, the clone() method automatically finds the next valid parent in line, going backward in the graph and connects it if that makes sense without ambiguity (effectively treating the removed Node as an identity operation).
     * @param cloneNode Callback function to clone a node
     * @return std::shared_ptr<GraphView>
     */
    std::shared_ptr<GraphView> cloneCallback(NodePtr(*cloneNode)(NodePtr)) const;

    /**
     * @brief Get the sum of the number of free dataInput connection for all inputNodes of the GraphView object.
     * Data inputs exclude inputs expecting parameters (weights or bias).
     * @return IOIndex_t
     */
    IOIndex_t getNbFreeDataInputs() const;

private:
///////////////////////////////////////////////////////
//        TENSOR MANAGEMENT
///////////////////////////////////////////////////////

    /**
     * @brief Get the number of dataInput that are outside the GraphView.
     * Data inputs exclude inputs expecting parameters (weights or bias).
     * This number matches the size of the vector returned by GraphView::dataInputs().
     * @return IOIndex_t
     */
    IOIndex_t getNbDataInputs() const;

    /**
     * @brief Automatically update GraphView inputs/outputs with a new Node, checking if
     * it this Node becomes an input/output for the graph and if previous inputs are still
     * inputs/outputs after adding this node.
     * @param nodePtr
     */
    void updateInputsOutputsNew(NodePtr newNode);

    /**
     * @brief Automatically update GraphView inputs/outputs with a Node removed, checking if
     * it this Node was an input/output for the graph and if this node childs become new inputs/outputs
     * for the graph.
     * @param nodePtr
     */
    void updateInputsOutputsDelete(NodePtr deletedNode);

    ///////////////////////////////////////////////////////
    //        TOPOLOGY
    ///////////////////////////////////////////////////////

};

/**
 * Create a GraphView containing all nodes with a path to given argument.
 * @param node Initial node to construct the graph.
 * @return GraphView GraphView containing all nodes with a path to node.
*/
std::shared_ptr<GraphView> getConnectedGraphView(std::shared_ptr<Node> node);
}  // namespace Aidge

#endif /* AIDGE_CORE_GRAPH_GRAPHVIEW_H_ */
