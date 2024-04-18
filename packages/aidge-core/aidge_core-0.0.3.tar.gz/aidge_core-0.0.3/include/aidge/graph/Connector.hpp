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
#ifndef AIDGE_CORE_GRAPH_CONNECTOR_H_
#define AIDGE_CORE_GRAPH_CONNECTOR_H_

#include <cassert>
#include <memory>
#include <vector>

#include "aidge/utils/Types.h"

namespace Aidge {

class Node;
class GraphView;
/**
 * @brief Object meant for simpler and more instrinctive user API.
 *
 * example:
 *  Connector x();
 *  x = Conv(...)(x);
 *  Connector y = Split(3)(x[0]); // Error! Cannot slice a Connector with one output only
 *  Connector y = Split(3)(x);
 *  CustomLayer cl(...);
 *  Connector z = cl(y) // Error! y has multiple outputs, must specify which one to use
 *  Connector z1 = cl(y[0]);
 *  Connector z2 = cl(y[1]);
 *  Connector z3 = cl(y[2]);
 *  x = Sum(...)(z1, z2, z3);
 *  GraphView g = x.generateGraph();
 */
class Connector {
   private:
    std::shared_ptr<Node> mNode;
    ///\brief output id
    ///\details gk_IODefaultIndex is reserved for?
    ///\bug Is negative value pertinent?
    IOIndex_t mOutputId = gk_IODefaultIndex;

   public:
    Connector() : mNode(nullptr) {
        // ctor
    }
    Connector(std::shared_ptr<Node> node);

    ~Connector() = default;

   public:
    Connector operator[](IOIndex_t index) {
        assert((size() > 1) && "Cannot refer a slice of the output.");
        return Connector(mNode, index);
    }

   public:
    IOIndex_t size() const;

    inline std::shared_ptr<Node> node() const { return mNode; }

    inline IOIndex_t index() const { return mOutputId; }

   private:
    Connector(std::shared_ptr<Node> node, IOIndex_t index) : mNode(node) {
        assert((index != gk_IODefaultIndex) && (index < size()) &&
               "Non-valid output index.\n");
        mOutputId = index;
    }
};

/**
 * @brief Generate a GraphView from a list of output Connectors
 *
 * @param ctors list of output Connector for the graph to generate.
 * @return std::shared_ptr<GraphView>
 */
std::shared_ptr<GraphView> generateGraph(std::vector<Connector> ctors);
}  // namespace Aidge

#endif /* AIDGE_CORE_GRAPH_CONNECTOR_H_ */