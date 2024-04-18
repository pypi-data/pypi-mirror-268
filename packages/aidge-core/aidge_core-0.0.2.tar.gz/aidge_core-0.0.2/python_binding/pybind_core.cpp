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

#include <pybind11/pybind11.h>

#include "aidge/backend/cpu/data/TensorImpl.hpp"  // This include add Tensor

namespace py = pybind11;

namespace Aidge {
void init_Random(py::module&);
void init_Data(py::module&);
void init_Database(py::module&);
void init_DataProvider(py::module&);
void init_Tensor(py::module&);
void init_OperatorImpl(py::module&);
void init_Attributes(py::module&);
void init_Log(py::module&);
void init_Operator(py::module&);
void init_OperatorTensor(py::module&);

void init_Add(py::module&);
void init_AvgPooling(py::module&);
void init_BatchNorm(py::module&);
void init_Concat(py::module&);
void init_Conv(py::module&);
void init_ConvDepthWise(py::module&);
void init_Div(py::module&);
void init_Erf(py::module&);
void init_FC(py::module&);
void init_Gather(py::module&);
void init_GenericOperator(py::module&);
void init_GlobalAveragePooling(py::module&);
void init_LeakyReLU(py::module&);
void init_MatMul(py::module&);
void init_MaxPooling(py::module&);
void init_MetaOperatorDefs(py::module&);
void init_Mul(py::module&);
void init_Producer(py::module&);
void init_Pad(py::module&);
void init_Pop(py::module&);
void init_Pow(py::module&);
void init_ReduceMean(py::module&);
void init_ReLU(py::module&);
void init_Reshape(py::module&);
void init_Sigmoid(py::module&);
void init_Slice(py::module&);
void init_Softmax(py::module&);
void init_Sqrt(py::module&);
void init_Sub(py::module&);
void init_Tanh(py::module&);
void init_Transpose(py::module&);
void init_Identity(py::module&);

void init_Node(py::module&);
void init_GraphView(py::module&);
void init_OpArgs(py::module&);
void init_Connector(py::module&);

void init_GraphRegex(py::module&);
void init_MatchSolution(py::module&);

void init_Recipes(py::module&);
void init_GraphViewHelper(py::module&);

void init_Scheduler(py::module&);
void init_TensorUtils(py::module&);
void init_Filler(py::module&);

void init_Aidge(py::module& m) {
    init_Random(m);

    init_Data(m);
    init_Database(m);
    init_DataProvider(m);
    init_Tensor(m);

    init_Node(m);
    init_GraphView(m);
    init_OpArgs(m);
    init_Connector(m);

    init_OperatorImpl(m);
    init_Attributes(m);
    init_Log(m);
    init_Operator(m);
    init_OperatorTensor(m);
    init_Add(m);
    init_AvgPooling(m);
    init_BatchNorm(m);
    init_Concat(m);
    init_Conv(m);
    init_ConvDepthWise(m);
    init_Div(m);
    init_Erf(m);
    init_FC(m);
    init_Gather(m);
    init_GenericOperator(m);
    init_GlobalAveragePooling(m);
    init_LeakyReLU(m);
    init_MatMul(m);
    init_MaxPooling(m);
    init_MetaOperatorDefs(m);
    init_Mul(m);
    init_Pad(m);

    init_Pop(m);
    init_Pow(m);
    init_ReduceMean(m);
    init_ReLU(m);
    init_Reshape(m);
    init_Sigmoid(m);
    init_Slice(m);
    init_Softmax(m);
    init_Sqrt(m);
    init_Sub(m);
    init_Tanh(m);
    init_Transpose(m);
    init_Identity(m);

    init_Producer(m);

    init_GraphRegex(m);
    init_MatchSolution(m);

    init_Recipes(m);
    init_GraphViewHelper(m);
    init_Scheduler(m);
    init_TensorUtils(m);
    init_Filler(m);
}

PYBIND11_MODULE(aidge_core, m) { init_Aidge(m); }
}  // namespace Aidge
