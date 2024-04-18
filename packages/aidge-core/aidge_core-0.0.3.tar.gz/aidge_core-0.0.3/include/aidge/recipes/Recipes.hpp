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

#ifndef AIDGE_CORE_UTILS_RECIPES_H_
#define AIDGE_CORE_UTILS_RECIPES_H_

#include <memory>
#include <set>

#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graphRegex/matchFsm/MatchResult.hpp"


namespace Aidge {

void constantFolding(std::shared_ptr<GraphView> graph);

// FUSE MATMUL + ADD -> FC

/**
 * @brief Merge ``MatMul`` and :cpp:function:`Aidge::Add` Node into a :cpp:function:`Aidge::FC` Node.
 *
 * @param nodes Strict set of Node to merge.
 */
//void fuseMulAdd(std::set<std::shared_ptr<Node>> nodes);

void fuseMulAdd(std::shared_ptr<MatchSolution> solution);

void fuseMulAdd(std::shared_ptr<Node> matmul,std::shared_ptr<Node> add);

/**
 * @brief Merge ``MatMul`` and :cpp:function:`Aidge::Add` Node into a :cpp:function:`Aidge::FC` Node.
 *
 * @param graphView Graph view to use graph matching on, in order to apply transformations.
 */
void fuseMulAdd(std::shared_ptr<GraphView> graphView);

// REMOVE Dropout

/**
 * @brief Remove ``Dropout`` Node.
 *
 * @param nodes Node to remove.
 */
void removeDropout(std::shared_ptr<Node> dropout);


void removeDropout(std::shared_ptr<MatchSolution> solution);

/**
 * @brief Remove ``Dropout`` Node.
 *
 * @param graphView Graph view to use graph matching on, in order to apply transfomrations.
 */
void removeDropout(std::shared_ptr<GraphView> graphView);

// REMOVE FLATTEN + FC -> FC

/**
 * @brief Remove ``Flatten`` before :cpp:function:`Aidge::FC` Node.
 *
 * @param nodes Strict set of Node to merge.
 */
void removeFlatten(std::shared_ptr<Node> flatten);


void removeFlatten(std::shared_ptr<MatchSolution> solution);

/**
 * @brief Remove ``Flatten`` before :cpp:function:`Aidge::FC` Node.
 *
 * @param graphView Graph view to use graph matching on, in order to apply transformations.
 */
void removeFlatten(std::shared_ptr<GraphView> graphView);

// FUSE BN + FC || CONV -> FC || CONV

/**
 * @brief Fuse :cpp:function:`Aidge::BatchNorm` with :cpp:function:`Aidge::Conv` or :cpp:function:`Aidge::FC` Nodes.
 * Ref: https://nenadmarkus.com/p/fusing-batchnorm-and-conv/
 *
 * @param nodes Strict set of Node to merge.
 */
void fuseBatchNorm(std::shared_ptr<Node> conv,std::shared_ptr<Node> batchnorm);



void fuseBatchNorm(std::shared_ptr<MatchSolution> solution);

/**
 * @brief Fuse :cpp:function:`Aidge::BatchNorm` with :cpp:function:`Aidge::Conv` or :cpp:function:`Aidge::FC` Nodes.
 * Ref: https://nenadmarkus.com/p/fusing-batchnorm-and-conv/
 *
 * @param graphView Graph view to use graph matching on, in order to apply transformations.
 */
void fuseBatchNorm(std::shared_ptr<GraphView> graphView);

std::set<std::shared_ptr<Node>> getConvHorizontalTiling(const std::shared_ptr<Node>& node, const DimIdx_t axis, const std::size_t nbSlices);
// void horizontalTiling(std::shared_ptr<Node> node, DimIdx_t dim, std::size_t nbSlices);
// std::set<std::shared_ptr<Node>> getHorizontalTiling(std::set<std::shared_ptr<Node>> setOfNodes, DimIdx_t dim, std::size_t nbSlices);
// void horizontalTiling(std::set<std::shared_ptr<Node>> setOfNodes, DimIdx_t dim, std::size_t nbSlices);


/**
 * Add Convert operators where needed to ensure no conversion needs to be done
 * at the Operator level.
*/
void explicitCastMove(std::shared_ptr<GraphView> graphView);

/**
 * Flatten the graph by replacing the meta operators by their micro graph.
 * @param recursive If true, recursively replace meta operators until there is
 * no more meta operator in the graph.
*/
void expandMetaOps(std::shared_ptr<GraphView> graph, bool recursive = false);

} // namespace Aidge

#endif /* AIDGE_CORE_UTILS_RECIPES_H_ */
