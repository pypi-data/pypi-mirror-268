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
#include <cassert>
#include <memory>
#include <set>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/BatchNorm.hpp"
#include "aidge/operator/Conv.hpp"
#include "aidge/operator/ConvDepthWise.hpp"
#include "aidge/operator/FC.hpp"
#include "aidge/operator/MetaOperator.hpp"
#include "aidge/recipes/Recipes.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

// Graph Regex
#include "aidge/graphRegex/GraphRegex.hpp"

void Aidge::fuseBatchNorm(std::shared_ptr<Aidge::Node> convNode,
                          std::shared_ptr<Aidge::Node> batchnormNode) {
    // Case: convNode is a MetaOperator ending with a Convolution
    // eg. PaddedConv
    if (!(convNode -> getOperator() -> isAtomic())) {
        const std::shared_ptr<MetaOperator_Op> metaNode = std::static_pointer_cast<MetaOperator_Op>(convNode -> getOperator());
        const std::shared_ptr<GraphView>  metanodeGraph = metaNode -> getMicroGraph();
        const std::vector<std::pair<std::shared_ptr<Node>, IOIndex_t>> outputNodes = metanodeGraph -> getOrderedOutputs();
        if (outputNodes.size() != 1) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Bad MetaOperator argument for fuseBatchNorm recipie.");
        }
        convNode = outputNodes[0].first;
    }

    AIDGE_ASSERT(((convNode->type() == Conv_Op<2>::Type) || (convNode->type() == ConvDepthWise_Op<2>::Type)), "Wrong type");
    AIDGE_ASSERT(batchnormNode->type() == BatchNorm_Op<2>::Type, "Wrong type for batchnorm node.");

    // TODO: Find a way to remove the template
    // A feature map with 2 dimensions is assumed
    const std::shared_ptr<BatchNorm_Op<2>> batchOp =
            std::static_pointer_cast<BatchNorm_Op<2>>(batchnormNode->getOperator());

    DimSize_t convNbOutChannels = 1;
    DimSize_t channelsSize = 1;
    std::array<DimSize_t, 2> kernelDims = {1,1};
    AIDGE_ASSERT(convNode->getOperator()->operatorType() == OperatorType::Tensor, "Operator must be of Tensor type.");
    std::shared_ptr<OperatorTensor> convOp = std::static_pointer_cast<OperatorTensor>(convNode->getOperator());
    if (convNode->type() == Conv_Op<2>::Type) {
        const std::shared_ptr<Conv_Op<2>> convOpPtr =
            std::static_pointer_cast<Conv_Op<2>>(convNode->getOperator());
        convNbOutChannels = convOpPtr->getAttr<DimSize_t>("OutChannels");
        channelsSize = convOpPtr->getAttr<DimSize_t>("InChannels");
        kernelDims = convOpPtr->getAttr<std::array<DimSize_t, 2>>("KernelDims");
    }
    else if (convNode->type() == ConvDepthWise_Op<2>::Type) {
        const std::shared_ptr<ConvDepthWise_Op<2>> convOpPtr =
            std::static_pointer_cast<ConvDepthWise_Op<2>>(convNode->getOperator());
        convNbOutChannels = convOpPtr->getAttr<DimSize_t>("Channels");
        kernelDims = convOpPtr->getAttr<std::array<DimSize_t, 2>>("KernelDims");
    }

    std::shared_ptr<Tensor> scaleBuf, shiftBuf, b_meanBuf, b_varBuf;
    const Tensor& scale = batchOp->getInput(1)->refCastFrom(scaleBuf, DataType::Float32, "cpu");
    const Tensor& shift = batchOp->getInput(2)->refCastFrom(shiftBuf, DataType::Float32, "cpu");
    const Tensor& b_mean = batchOp->getInput(3)->refCastFrom(b_meanBuf, DataType::Float32, "cpu");
    const Tensor& b_var = batchOp->getInput(4)->refCastFrom(b_varBuf, DataType::Float32, "cpu");

    const float epsilon = batchOp->getAttr<float>("Epsilon");


    assert(epsilon > 0.0);
    // TODO : no no_bias attribute ?

    float meanVariance = 0.0;
    unsigned int count = 0;

    for (std::size_t outChId = 0; outChId < convNbOutChannels; ++outChId) {
        if (b_var.get<float>(outChId) > 1.0e-12) {
            meanVariance += b_var.get<float>(outChId);
            ++count;
        } else {
            fmt::print("Zero-variance: {} [{}]\n", convNode->name(), outChId);
        }
    }
    if (count > 0)
        meanVariance /= count;
    else {
        fmt::print("Warning: variance < 1e-12 for all outputs! Is the network correctly trained?\n");
    }

    std::shared_ptr<Tensor> weightBuf, biasBuf;
    Tensor& weight = convOp->getInput(1)->refCastFrom(weightBuf, DataType::Float32, "cpu");
    Tensor& bias = convOp->getInput(2)->refCastFrom(biasBuf, DataType::Float32, "cpu");

    for (std::size_t outChId = 0; outChId < convNbOutChannels; ++outChId) {
        // Corrected for zero-variance issue:
        // "A Quantization-Friendly Separable Convolution for MobileNets"
        // https://arxiv.org/pdf/1803.08607.pdf
        // to help post-training quantization
        const float factor = scale.get<float>(outChId)
            / std::sqrt(epsilon + ((b_var.get<float>(outChId) > 1.0e-12 || count == 0)
                        ? b_var.get<float>(outChId) : meanVariance));
        // Weights adjustments
        for (std::size_t channel = 0; channel < channelsSize; ++channel) {
            // TODO : Suppose kerneldims = 2
            for (std::size_t k0 = 0; k0 < kernelDims[0]; ++k0) {
                for (std::size_t k1 = 0; k1 < kernelDims[1]; ++k1) {
                    std::vector<DimSize_t> currentIdx = {outChId, channel, k0, k1};
                    float weightValue = weight.get<float>(currentIdx);
                    weight.set<float>(currentIdx, weightValue*factor); // Update check it update Conv weights
                }
            }
        }

        // TODO : check if noBias==true is set, then set biasValue to 0
        float biasValue = bias.get<float>(outChId);

        biasValue = shift.get<float>(outChId) + (biasValue - b_mean.get<float>(outChId)) * factor;

        bias.set<float>(outChId, biasValue);

    }

    // Copy values back to the original tensors (actual copy only if needed)
    convOp->getInput(1)->copyCastFrom(weight);
    convOp->getInput(2)->copyCastFrom(bias);

    GraphView::replace(std::set<std::shared_ptr<Node>>({
        batchnormNode,
        batchnormNode->input(1).first,
        batchnormNode->input(2).first,
        batchnormNode->input(3).first,
        batchnormNode->input(4).first
        }), {});

}

void Aidge::fuseBatchNorm(std::shared_ptr<Aidge::MatchSolution> solution) {
    assert(solution->at("BatchNorm").size() == 1 && "Wrong number of nodes BatchNorm to replace\n");
    assert(solution->at("OP").size() == 1 && "Wrong number of nodes OP to replace\n");

    for (const auto& op : solution->at("OP")) {
        if (op->getOperator()->isAtomic()) {
            for (const auto& batchNorm : solution->at("BatchNorm")) {
                fuseBatchNorm(op, batchNorm);
            }
        } else {  // op is a MetaOperator
            auto metaOp = std::dynamic_pointer_cast<MetaOperator_Op>(op->getOperator());
            if ((metaOp->getMicroGraph()->getOrderedOutputs().size() == 1) &&
                ((metaOp->getMicroGraph()->getOrderedOutputs()[0].first->type() ==
                  Conv_Op<2>::Type) ||
                 (metaOp->getMicroGraph()->getOrderedOutputs()[0].first->type() ==
                  ConvDepthWise_Op<2>::Type))) {
                for (const auto& batchNorm : solution->at("BatchNorm")) {
                    fuseBatchNorm(op, batchNorm);
                }
            }
        }
    }
}

void Aidge::fuseBatchNorm(std::shared_ptr<Aidge::GraphView> graphView) {
    std::shared_ptr<GraphRegex> regex = std::make_shared<GraphRegex>();
    regex->setNodeKey("BatchNorm", "getType($) =='BatchNorm'");
    fmt::print("\n============================\nSearching for solutions\n==============================\n");
    regex->setNodeKey(
            "OP",
            "getType($) =='Conv' || getType($) =='ConvDepthWise' || getType($) =='PaddedConv' || getType($) =='PaddedConvDepthWise'");
            //  || getType($) =='FC' ");

    regex->addQuery("OP -> BatchNorm");

    for (const auto& solution : regex->match(graphView)) {

        fuseBatchNorm(solution);

    }
}