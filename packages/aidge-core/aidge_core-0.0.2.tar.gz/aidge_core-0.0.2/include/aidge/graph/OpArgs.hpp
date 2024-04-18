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

#ifndef AIDGE_CORE_GRAPH_OPARGS_H_
#define AIDGE_CORE_GRAPH_OPARGS_H_

#include <memory>
#include <cassert>

namespace Aidge {
class Node;
class GraphView;

/**
 * @brief Intermediate representation for Structural description.
 */
class OpArgs {
private:
    std::shared_ptr<Node> mNode = nullptr;
    std::shared_ptr<GraphView> mView = nullptr;

public:
    OpArgs(const std::shared_ptr<GraphView>& view_)
     : mView(view_) {assert(mView && "The GraphView provided should not be a nullptr.");}

    OpArgs(const std::shared_ptr<Node>& node_)
     : mNode(node_) {assert(mNode && "The Node provided should not be a nullptr.");}

    inline std::shared_ptr<Node> node() const noexcept {
        return mNode;
    }

    inline std::shared_ptr<GraphView> view() const noexcept {
        return mView;
    }
};


/////////////////////////////
// Sequential

/**
 * @brief Create a GraphView by linking every input with the next
 * one in a sequential way. Nodes linked with the Sequential graph
 * generation instructions must have a single output.
 * Sequential(A, B, C) returns A-->B-->C.
 * @param inputs List of Node and GraphView to link sequentially.
 * @return std::shared_ptr<GraphView> Pointer to the generated view.
 */
std::shared_ptr<GraphView> Sequential(std::vector<OpArgs> inputs);

/////////////////////////////
// Parallel

/**
 * @brief Creates a GraphView with provided Nodes without linking them.
 * @param inputs List of Node and GraphView to link sequentially.
 * @return std::shared_ptr<GraphView> pointer to the generated view.
 */
std::shared_ptr<GraphView> Parallel(std::vector<OpArgs> inputs);

/////////////////////////////
// Residual

/**
 * @brief Create a GraphView by linking every input with the next
 * one in a sequential way. Finally the first element output is used
 * as another input for the last element. Nodes linked with the Recursive graph
 * generation instructions must have a single output.
 * Recursive(A, B, C) returns A-->B-->C , A-->C.
 * @param inputs List of Node and GraphView to link sequentially.
 * @return std::shared_ptr<GraphView> pointer to the generated view.
 */
std::shared_ptr<GraphView> Residual(std::vector<OpArgs> inputs);

}

#endif /* AIDGE_CORE_GRAPH_OPARGS_H_ */
