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

#ifndef AIDGE_RECIPES_LABELGRAPH_H_
#define AIDGE_RECIPES_LABELGRAPH_H_

#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"

namespace Aidge {
NodePtr nodeLabel(NodePtr node);

/**
 * @brief Generate the graph for the pixel-wise labels corresponding to a data graph, taking into account the scaling changes (padding, stride, pooling...).
 * @details Right now, the behavior is to replace the following operators:
 * - Conv: MaxPooling
 * - ConvDepthWie: MaxPooling
 * - AvgPooling: MaxPooling
 * - MaxPooling: MaxPooling
 * - all others: identity (removed)
 * @param graph Data graph
 * @param return Computing graph for the labels derived from the data graph
 */
std::shared_ptr<GraphView> labelGraph(std::shared_ptr<GraphView> graph);
} // namespace Aidge

#endif /* AIDGE_RECIPES_LABELGRAPH_H_ */
