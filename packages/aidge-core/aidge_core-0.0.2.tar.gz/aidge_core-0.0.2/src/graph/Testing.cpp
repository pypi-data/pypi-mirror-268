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

#include <algorithm> // std::shuffle, std::transform
#include <cstddef>
#include <memory>
#include <numeric>   // std::iota
#include <random>    // std::binomial_distribution, std::mt19937, std::discrete_distribution
#include <string>
#include <utility>   // std::pair
#include <vector>

#include "aidge/graph/Testing.hpp"
#include "aidge/operator/GenericOperator.hpp"
#include "aidge/utils/Types.h"

std::pair<Aidge::NodePtr, std::set<Aidge::NodePtr>> Aidge::RandomGraph::gen(std::mt19937::result_type seed, std::size_t nbNodes) const {
    std::mt19937 gen(seed);
    std::binomial_distribution<> dIn(maxIn - 1, avgIn/maxIn);
    std::binomial_distribution<> dOut(maxOut - 1, avgOut/maxOut);
    std::binomial_distribution<> dLink(1, density);
    std::discrete_distribution<> dType(typesWeights.begin(), typesWeights.end());

    std::vector<std::pair<IOIndex_t, IOIndex_t>> nbIOs;
    std::vector<std::string> nodesType;
    for (std::size_t i = 0; i < nbNodes; ++i) {
        const auto nbIn = 1 + dIn(gen);
        nbIOs.push_back(std::make_pair(nbIn, 1 + dOut(gen)));
        nodesType.push_back(types[dType(gen)]);
    }

    std::vector<std::size_t> nodesSeq(nbNodes);
    std::iota(nodesSeq.begin(), nodesSeq.end(), static_cast<std::size_t>(0));
    // Don't use gen or seed here, must be different each time!
    std::shuffle(nodesSeq.begin(), nodesSeq.end(), std::default_random_engine(std::random_device{}()));

    std::vector<NodePtr> nodes(nbNodes, nullptr);
    for (auto idx : nodesSeq) {
        const std::string name = nodesType[idx] + std::to_string(idx);
        nodes[idx] = GenericOperator(nodesType[idx], nbIOs[idx].first, 0, nbIOs[idx].second, name);
    }

    for (std::size_t i = 0; i < nbNodes; ++i) {
        for (std::size_t j = (acyclic) ? i + 1 : 0; j < nbNodes; ++j) {
            if (i == j) {
                // Do not connected node to itself in case of cyclic graph!
                continue;
            }

            for (std::size_t outId = 0; outId < nodes[i]->nbOutputs(); ++outId) {
                for (std::size_t inId = 0; inId < nodes[j]->nbInputs(); ++inId) {
                    if (dLink(gen)) {
                        // Warning: connections can be set multiple time for the
                        // same node input! In this case, the previous connection
                        // is overwritten. This is the expected behavior.
                        nodes[i]->addChild(nodes[j], outId, inId);
                        if (nodes[i]->type() == omitType || nodes[j]->type() == omitType) {
                            // Let nodes[i]->addChild() overwrite the previous connection.
                            // Now we remove the new one!
                            nodes[i]->removeChild(nodes[j], outId);
                            nodes[j]->removeParent(inId);
                        }
/*
                        // Alternative: only add child if no node is omitted
                        // and remove the potential previous connection, like this:
                        if (nodes[i]->type() != omitType && nodes[j]->type() != omitType) {
                            nodes[i]->addChild(nodes[j], outId, inId);
                        }
                        else {
                            const auto prevIn = nodes[j]->input(inId);

                            if (prevIn.first != nullptr) {
                                prevIn.first->removeChild(nodes[j], prevIn.second);
                                nodes[j]->removeParent(inId);
                            }
                        }
*/
                        break;
                    }
                }
            }
        }
    }

    NodePtr rootNode = nullptr;
    std::set<NodePtr> nodesSet;
    for (std::size_t i = 0; i < nbNodes; ++i) {
        if (nodes[i]->type() != omitType) {
            if (rootNode == nullptr) {
                rootNode = nodes[i];
            }
            nodesSet.insert(nodes[i]);
        }
    }

    return std::make_pair(rootNode, nodesSet);
}

std::string Aidge::nodePtrToType(NodePtr node) {
    return node->type();
}

std::string Aidge::nodePtrToName(NodePtr node) {
    return node->name();
}

std::set<std::string> Aidge::nodePtrTo(const std::set<NodePtr>& nodes,
    std::string(*nodeTo)(NodePtr))
{
    std::set<std::string> nodesStr;
    std::transform(nodes.begin(), nodes.end(), std::inserter(nodesStr, nodesStr.begin()), nodeTo);
    return nodesStr;
}

std::vector<std::pair<std::string, Aidge::IOIndex_t>> Aidge::nodePtrTo(
    const std::vector<std::pair<NodePtr, IOIndex_t>>& nodes,
    std::string(*nodeTo)(NodePtr))
{
    std::vector<std::pair<std::string, IOIndex_t>> nodesStr;
    std::transform(nodes.begin(), nodes.end(), std::back_inserter(nodesStr),
        [nodeTo](const std::pair<NodePtr, IOIndex_t>& node) {
            return std::make_pair(nodeTo(node.first), node.second);
        });
    return nodesStr;
}
