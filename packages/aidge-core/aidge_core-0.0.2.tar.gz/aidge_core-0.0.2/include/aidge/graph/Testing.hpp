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

#ifndef AIDGE_CORE_GRAPH_TESTING_H_
#define AIDGE_CORE_GRAPH_TESTING_H_

#include <cstddef>
#include <vector>
#include <set>
#include <random>     // std::mt19937::result_type
#include <utility>    // std::pair

#include "aidge/graph/Node.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
/**
 * Random (directed) graph generator
*/
struct RandomGraph {
    /// @brief If true, the generated graph is a DAG (no cycle)
    bool acyclic = false;
    /// @brief Connection density (between 0 and 1)
    float density = 0.5;
    /// @brief Max number of inputs per node (regardless if they are connected or not)
    std::size_t maxIn = 5;
    /// @brief Average number of inputs per node (regardless if they are connected or not)
    float avgIn = 1.5;
    /// @brief Max number of outputs per node (regardless if they are connected or not)
    std::size_t maxOut = 2;
    /// @brief Average number of outputs per node (regardless if they are connected or not)
    float avgOut = 1.1;
    /// @brief List of node types that should be generated in the graph (as GenericOperator)
    std::vector<std::string> types = {"Fictive"};
    /// @brief Weights of each node type, used to compute the probability of generating this type
    std::vector<float> typesWeights = {1.0};
    /// @brief Type of node that should be omitted from the generated topology
    std::string omitType;

    /**
     * Generate a DAG according to the parameters of the class.
     * @param seed Random seed. For an identical seed, an identical topology is
     * generated, but with a random node ordering in the return set of nodes.
     * @param nbNodes Number of nodes to generate.
    */
    std::pair<NodePtr, std::set<NodePtr>> gen(std::mt19937::result_type seed, std::size_t nbNodes) const;
};

std::string nodePtrToType(NodePtr node);
std::string nodePtrToName(NodePtr node);
std::set<std::string> nodePtrTo(const std::set<NodePtr>& nodes,
    std::string(*nodeTo)(NodePtr) = nodePtrToType);
std::vector<std::pair<std::string, IOIndex_t>> nodePtrTo(
    const std::vector<std::pair<NodePtr, IOIndex_t>>& nodes,
    std::string(*nodeTo)(NodePtr) = nodePtrToType);

} // namespace Aidge

#endif /* AIDGE_CORE_GRAPH_TESTING_H_ */
