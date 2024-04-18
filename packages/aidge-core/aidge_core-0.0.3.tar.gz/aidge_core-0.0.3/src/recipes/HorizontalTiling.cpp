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

#include <set>
#include <memory>
#include <numeric>   // std::iota
#include <vector>
#include <utility>

#include "aidge/recipes/Recipes.hpp"

#include "aidge/graph/Node.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/utils/Types.h"

#include "aidge/operator/Add.hpp"
#include "aidge/operator/Concat.hpp"
#include "aidge/operator/Slice.hpp"

// TODO: assert Operator uses Tensors when implemented
std::set<std::shared_ptr<Aidge::Node>> Aidge::getConvHorizontalTiling(const std::shared_ptr<Aidge::Node>& node,
                                                            const Aidge::DimIdx_t axis,
                                                            const std::size_t nbSlices)
{
    if (node->getOperator()->type() != "Conv") {
        AIDGE_INTERNAL_ASSERT("Operator should be a Convolution.");
    }
    AIDGE_ASSERT(node->getOperator()->operatorType() == OperatorType::Tensor, "Operator must be of Tensor type.");
    const auto& op = std::static_pointer_cast<OperatorTensor>(node->getOperator());
    if (op->nbOutputs() != 1 || op->nbData() > 1) {
        AIDGE_INTERNAL_ASSERT("Only slice Operators with one output and at most one input for now.");
    }
    if (!op->outputDimsForwarded()) {
        AIDGE_INTERNAL_ASSERT("Dimensions must be forwarded before any tiling");
    }
    // start by doing a tiling with strict dimensions division
    const auto& outTensor = op->getOutput(0);
    if (op->getOutput(0)->dims()[axis] % nbSlices != 0) {
        AIDGE_INTERNAL_ASSERT("axis should be a multiple of nbSlices");
    }

    // dimensions of a Slice
    std::vector<DimSize_t> outputDims = outTensor->dims();
    outputDims[axis] /= nbSlices;

    std::vector<DimSize_t> currentFirstDims = std::vector<DimSize_t>(outTensor->nbDims(), 0);

    std::set<std::shared_ptr<Aidge::Node>> res;
    auto concat = Concat(nbSlices, axis);
    res.insert(concat);

    // check slice sizes
    // const auto inputDims = op->computeReceptiveField(currentFirstDims[axis], outputDims, 0);
    // std::vector<bool> shareTensor(node->nbInputs(), false);
    // for (DimSize_t inputID = 0; inputID < node->nbInputs(); ++inputID) {
    //     const auto inTensor = std::dynamic_pointer_cast<Tensor>(node->getOperator()->getRawInput(inputID));
    //     if (inTensor->dims() == inputDims[inputID].second)
    //         shareTensor[inputID] = true;
    // }

    std::vector<std::shared_ptr<Node>> clonedInputs = std::vector<std::shared_ptr<Node>>(node->nbInputs(), nullptr);
    for (std::size_t i = node->nbData(); i < node ->nbInputs(); ++i) {
        clonedInputs[i] = node -> getParent(i) -> cloneSharedOperators();
        clonedInputs[i] -> setName(node -> name() + "_0");
        res.insert(clonedInputs[i]);
    }

    for (IOIndex_t i = 0; currentFirstDims[axis] < outTensor->dims()[axis]; currentFirstDims[axis] += outputDims[axis], ++i) {
        const auto inputDims = op->computeReceptiveField(currentFirstDims, outputDims, 0);
        auto newNode = node -> clone(); // no input associated to clones
        newNode -> setName(node->name() + "_" + std::to_string(currentFirstDims[axis]));
        clonedInputs[1] -> addChild(newNode, 0, 1);
        clonedInputs[2] -> addChild(newNode, 0, 2);
        // Slice for input and each parameter
        std::vector<std::int64_t> inputDimsEnd(inputDims[0].first.size());
        for (std::size_t dim = 0; dim < inputDimsEnd.size(); ++dim) {
            inputDimsEnd[dim] = static_cast<std::int64_t>(inputDims[0].first[dim] + inputDims[0].second[dim]) - 1;
        }
        std::vector<std::int64_t> inputDimsStart(inputDims[0].first.size());
        for (std::size_t dim = 0; dim < inputDimsStart.size(); ++dim) {
            inputDimsStart[dim] = static_cast<std::int64_t>(inputDims[0].first[dim]);
        }
        std::vector<std::int64_t> usedDims(inputDimsEnd.size());
        std::iota(usedDims.begin(), usedDims.end(), static_cast<std::int64_t>(0));
        auto slice = Slice(inputDimsStart, inputDimsEnd, usedDims, "Slice_" + std::to_string(currentFirstDims[axis]));
        slice -> addChild(newNode, 0, 0);
        newNode -> addChild(concat, 0, i);

        res.insert(slice);
        res.insert(newNode);
    }

    return res;
}