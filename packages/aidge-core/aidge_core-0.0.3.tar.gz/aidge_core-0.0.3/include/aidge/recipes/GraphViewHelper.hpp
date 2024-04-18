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

#ifndef AIDGE_CORE_UTILS_GRAPHVIEWHELPER_H_
#define AIDGE_CORE_UTILS_GRAPHVIEWHELPER_H_

#include <memory>
#include <set>

#include "aidge/graph/GraphView.hpp"
#include "aidge/data/Tensor.hpp"


namespace Aidge {

/**
 * @brief Getter for every Producer operator in a GraphView.
 * @param graphview GraphView instance where Producers should be searched.
 * @return std::set<std::shared_ptr<Node>>
 */
std::set<std::shared_ptr<Tensor>> producers(std::shared_ptr<GraphView> graphview);


// TODO: change for every Tensor of Operator Producer not constant
/**
 * @brief Getter for every ``Tensor`` owned by an ``Operator`` inside the provided ``GraphView``.
 * @note An ``Operator`` owns its output ``Tensor``s.
 *
 * @param graphview Pointer to the ``GraphView`` from which ``Tensor``s should be extracted.
 * @return std::set<std::shared_ptr<Tensor>> Set of pointers to the ``Tensor``s.
 */
std::set<std::shared_ptr<Tensor>> parameters(std::shared_ptr<GraphView> graphview);

void compile_gradient(std::shared_ptr<Aidge::GraphView> gv);

} // namespace Aidge

#endif /* AIDGE_CORE_UTILS_GRAPHVIEWHELPER_H_ */
