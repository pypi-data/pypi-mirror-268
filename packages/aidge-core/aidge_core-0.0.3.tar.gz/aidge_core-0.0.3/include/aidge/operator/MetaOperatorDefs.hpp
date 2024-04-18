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

#ifndef AIDGE_CORE_OPERATOR_METAOPERATORDEFS_H_
#define AIDGE_CORE_OPERATOR_METAOPERATORDEFS_H_

#include "aidge/operator/MetaOperator.hpp"
#include "aidge/operator/AvgPooling.hpp"
#include "aidge/operator/MaxPooling.hpp"
#include "aidge/operator/Conv.hpp"
#include "aidge/operator/ConvDepthWise.hpp"
#include "aidge/operator/Pad.hpp"
#include "aidge/operator/Memorize.hpp"
#include "aidge/operator/Add.hpp"
#include "aidge/operator/Mul.hpp"
#include "aidge/operator/FC.hpp"
#include "aidge/operator/Identity.hpp"
#include "aidge/operator/Concat.hpp"
#include "aidge/operator/Tanh.hpp"
#include "aidge/operator/Sigmoid.hpp"

namespace Aidge {
template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> PaddedConv(DimSize_t in_channels,
                                  DimSize_t out_channels,
                                  const std::array<DimSize_t, DIM> &kernel_dims,
                                  const std::string& name = "",
                                  const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                                  const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
                                  const std::array<DimSize_t, DIM> &dilation_dims = create_array<DimSize_t,DIM>(1),
                                  bool no_bias = false)
{
    // Construct micro-graph
    auto pad = Pad<DIM>(padding_dims, (!name.empty()) ? name + "_pad" : "", PadBorderType::Constant, 0.0);
    auto conv = std::make_shared<Node>(std::make_shared<Conv_Op<static_cast<DimIdx_t>(DIM)>>(in_channels, out_channels, kernel_dims, stride_dims, dilation_dims, no_bias), (!name.empty()) ? name + "_conv" : "");

    auto metaOp = MetaOperator("PaddedConv", Sequential({pad, conv}), name);
    addProducer(metaOp, 1, append(out_channels, append(in_channels, kernel_dims)), "w");
    addProducer(metaOp, 2, {out_channels}, "b");
    return metaOp;
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> PaddedConv(
    DimSize_t in_channels,
    DimSize_t out_channels,
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
    const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
    const std::array<DimSize_t, DIM> &dilation_dims = create_array<DimSize_t,DIM>(1),
    bool no_bias = false)
{
    return PaddedConv(in_channels, out_channels, to_array(kernel_dims), name, stride_dims, padding_dims, dilation_dims, no_bias);
}

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> PaddedConvDepthWise(const DimSize_t nb_channels,
                                  const std::array<DimSize_t, DIM> &kernel_dims,
                                  const std::string& name = "",
                                  const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                                  const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
                                  const std::array<DimSize_t, DIM> &dilation_dims = create_array<DimSize_t,DIM>(1),
                                  bool no_bias = false)
{
    // Construct micro-graph
    auto pad = Pad<DIM>(padding_dims, (!name.empty()) ? name + "_pad" : "", PadBorderType::Constant, 0.0);
    auto conv = std::make_shared<Node>(std::make_shared<ConvDepthWise_Op<static_cast<DimIdx_t>(DIM)>>(nb_channels, kernel_dims, stride_dims, dilation_dims, no_bias), (!name.empty()) ? name + "_conv" : "");

    auto metaOp = MetaOperator("PaddedConvDepthWise", Sequential({pad, conv}), name);
    addProducer(metaOp, 1, append(nb_channels, append(DimSize_t(1), kernel_dims)), "w");
    addProducer(metaOp, 2, {nb_channels}, "b");
    return metaOp;
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> PaddedConvDepthWise(
    const DimSize_t nb_channels,
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
    const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
    const std::array<DimSize_t, DIM> &dilation_dims = create_array<DimSize_t,DIM>(1),
    bool no_bias = false)
{
    return PaddedConvDepthWise(nb_channels, to_array(kernel_dims), name, stride_dims, padding_dims, dilation_dims, no_bias);
}

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> PaddedAvgPooling(const std::array<DimSize_t, DIM> &kernel_dims,
                                  const std::string& name = "",
                                  const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                                  const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0))
{
    auto graph = Sequential({
        Pad<DIM>(padding_dims, (!name.empty()) ? name + "_pad" : ""),
        AvgPooling(kernel_dims, (!name.empty()) ? name + "_avgpooling" : "", stride_dims)
    });

    return MetaOperator("PaddedAvgPooling", graph, name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> PaddedAvgPooling(
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
    const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0))
{
    return PaddedAvgPooling(to_array(kernel_dims), name, stride_dims, padding_dims);
}

template <std::array<DimSize_t, 1>::size_type DIM>
inline std::shared_ptr<Node> PaddedMaxPooling(const std::array<DimSize_t, DIM> &kernel_dims,
                                  const std::string& name = "",
                                  const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
                                  const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
                                  bool ceil_mode = false)
{
    auto graph = Sequential({
        Pad<DIM>(padding_dims, (!name.empty()) ? name + "_pad" : ""),
        MaxPooling(kernel_dims, (!name.empty()) ? name + "_maxpooling" : "", stride_dims, ceil_mode)
    });

    return MetaOperator("PaddedMaxPooling", graph, name);
}

// helper with C-style array instead of std::array for kernel_dims to allow automatic template DIM deduction
template <DimSize_t DIM>
inline std::shared_ptr<Node> PaddedMaxPooling(
    DimSize_t const (&kernel_dims)[DIM],
    const std::string& name = "",
    const std::array<DimSize_t, DIM> &stride_dims = create_array<DimSize_t,DIM>(1),
    const std::array<DimSize_t, 2*DIM> &padding_dims = create_array<DimSize_t,2*DIM>(0),
    bool ceil_mode= false)
{
    return PaddedMaxPooling(to_array(kernel_dims), name, stride_dims, padding_dims, ceil_mode);
}

inline std::shared_ptr<Node> LSTM(DimSize_t in_channels,
                                  DimSize_t hidden_channels,
                                  DimSize_t seq_length,
                                  bool noBias = false,
                                  const std::string& name = "")
{
    // Construct micro-graph
    auto input = Identity((!name.empty()) ? name + "_input" : "");
    auto hiddenState = Memorize(seq_length, (!name.empty()) ? name + "_hidden_state" : "");
    auto cellState = Memorize(seq_length, (!name.empty()) ? name + "_cell_state" : "");
    auto add = Add(2, (!name.empty()) ? name + "_add" : "");

    // Forget gate
    auto forgetGateX = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_forgetGateX" : "");
    input->addChild(forgetGateX, 0, 0);
    auto forgetGateH = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_forgetGateH" : "");
    hiddenState->addChild(forgetGateH, 1, 0);
    auto forgetGate = Add(2, (!name.empty()) ? name + "_forgetGate" : "");
    forgetGateX->addChild(forgetGate, 0, 0);
    forgetGateH->addChild(forgetGate, 0, 1);
    auto forgetGateAct = Sigmoid((!name.empty()) ? name + "_forgetGateAct" : "");
    auto forgetGateMul = Mul((!name.empty()) ? name + "_forgetGateMul" : "");
    forgetGate->addChild(forgetGateAct, 0, 0);
    forgetGateAct->addChild(forgetGateMul, 0, 0);
    forgetGateMul->addChild(add, 0, 0);
    cellState->addChild(forgetGateMul, 1, 1);

    // Input gate
    auto inputGateX = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_inputGateX" : "");
    input->addChild(inputGateX, 0, 0);
    auto inputGateH = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_inputGateH" : "");
    hiddenState->addChild(inputGateH, 1, 0);
    auto inputGate = Add(2, (!name.empty()) ? name + "_inputGate" : "");
    inputGateX->addChild(inputGate, 0, 0);
    inputGateH->addChild(inputGate, 0, 1);
    auto inputGateAct = Sigmoid((!name.empty()) ? name + "_inputGateAct" : "");
    auto inputGateMul = Mul((!name.empty()) ? name + "_inputGateMul" : "");
    inputGate->addChild(inputGateAct, 0, 0);
    inputGateAct->addChild(inputGateMul, 0, 0);
    inputGateMul->addChild(add, 0, 1);

    // Candidate for cell update
    auto cellCandidateX = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_cellCandidateX" : "");
    input->addChild(cellCandidateX, 0, 0);
    auto cellCandidateH = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_cellCandidateH" : "");
    hiddenState->addChild(cellCandidateH, 1, 0);
    auto cellCandidate = Add(2, (!name.empty()) ? name + "_cellCandidate" : "");
    cellCandidateX->addChild(cellCandidate, 0, 0);
    cellCandidateH->addChild(cellCandidate, 0, 1);
    auto cellCandidateAct = Tanh((!name.empty()) ? name + "_cellCandidateAct" : "");
    cellCandidate->addChild(cellCandidateAct, 0, 0);
    cellCandidateAct->addChild(inputGateMul, 0, 1);

    // Output gate
    auto outputGateX = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_outputGateX" : "");
    input->addChild(outputGateX, 0, 0);
    auto outputGateH = std::make_shared<Node>(std::make_shared<FC_Op>(hidden_channels, noBias), (!name.empty()) ? name + "_outputGateH" : "");
    hiddenState->addChild(outputGateH, 1, 0);
    auto outputGate = Add(2, (!name.empty()) ? name + "_outputGate" : "");
    outputGateX->addChild(outputGate, 0, 0);
    outputGateH->addChild(outputGate, 0, 1);
    auto outputGateAct = Sigmoid((!name.empty()) ? name + "_outputGateAct" : "");
    auto outputGateMul = Mul((!name.empty()) ? name + "_outputGateMul" : "");
    outputGate->addChild(outputGateAct, 0, 0);
    outputGateAct->addChild(outputGateMul, 0, 0);

    // Updated cell state to help determine new hidden state
    auto cellUpdatedAct = Tanh((!name.empty()) ? name + "_cellUpdatedAct" : "");
    add->addChild(cellUpdatedAct, 0, 0);
    cellUpdatedAct->addChild(outputGateMul, 0, 1);
    outputGateMul->addChild(hiddenState, 0, 0);
    add->addChild(cellState, 0, 0);

    std::shared_ptr<GraphView> microGraph = std::make_shared<GraphView>();
    microGraph->add(input);
    microGraph->add({hiddenState, cellState, add,
        forgetGateX, forgetGateH, forgetGate, forgetGateAct, forgetGateMul,
        inputGateX, inputGateH, inputGate, inputGateAct, inputGateMul,
        cellCandidateX, cellCandidateH, cellCandidate, cellCandidateAct,
        outputGateX, outputGateH, outputGate, outputGateAct, outputGateMul,
        cellUpdatedAct}, false);

    microGraph->setOrderedInputs({{input, 0},
        {inputGateX, 1}, {outputGateX, 1}, {forgetGateX, 1}, {cellCandidateX, 1},
        {inputGateH, 1}, {outputGateH, 1}, {forgetGateH, 1}, {cellCandidateH, 1},
        {inputGateX, 2}, {outputGateX, 2}, {forgetGateX, 2}, {cellCandidateX, 2},
        {inputGateH, 2}, {outputGateH, 2}, {forgetGateH, 2}, {cellCandidateH, 2},
        {hiddenState, 1}, {cellState, 1}});
    microGraph->setOrderedOutputs({{hiddenState, 0}, {cellState, 0}});

    auto metaOp = MetaOperator("LSTM", microGraph, name);
    addProducer(metaOp, 1, {hidden_channels, in_channels}, "wi");
    addProducer(metaOp, 2, {hidden_channels, in_channels}, "wo");
    addProducer(metaOp, 3, {hidden_channels, in_channels}, "wf");
    addProducer(metaOp, 4, {hidden_channels, in_channels}, "wc");
    addProducer(metaOp, 5, {hidden_channels, hidden_channels}, "ri");
    addProducer(metaOp, 6, {hidden_channels, hidden_channels}, "ro");
    addProducer(metaOp, 7, {hidden_channels, hidden_channels}, "rf");
    addProducer(metaOp, 8, {hidden_channels, hidden_channels}, "rc");
    addProducer(metaOp, 9, {(noBias ? 0 : hidden_channels)}, "wbi");
    addProducer(metaOp, 10, {(noBias ? 0 : hidden_channels)}, "wbo");
    addProducer(metaOp, 11, {(noBias ? 0 : hidden_channels)}, "wbf");
    addProducer(metaOp, 12, {(noBias ? 0 : hidden_channels)}, "wbc");
    addProducer(metaOp, 13, {(noBias ? 0 : hidden_channels)}, "rbi");
    addProducer(metaOp, 14, {(noBias ? 0 : hidden_channels)}, "rbo");
    addProducer(metaOp, 15, {(noBias ? 0 : hidden_channels)}, "rbf");
    addProducer(metaOp, 16, {(noBias ? 0 : hidden_channels)}, "rbc");
    return metaOp;
}
}  // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_METAOPERATORDEFS_H_ */
