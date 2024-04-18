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

#ifndef AIDGE_IMPORTS_H_
#define AIDGE_IMPORTS_H_

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/backend/TensorImpl.hpp"
#include "aidge/backend/StimulusImpl.hpp"

#include "aidge/backend/cpu/data/TensorImpl.hpp"
#include "aidge/backend/cpu/data/GetCPUPtr.h"

#include "aidge/data/Data.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/data/Database.hpp"
#include "aidge/data/DataProvider.hpp"

#include "aidge/graph/Connector.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/graph/OpArgs.hpp"

#include "aidge/graphRegex/GraphRegex.hpp"

#include "aidge/filler/Filler.hpp"

#include "aidge/nodeTester/ConditionalInterpreter.hpp"

#include "aidge/operator/Add.hpp"
#include "aidge/operator/AvgPooling.hpp"
#include "aidge/operator/BatchNorm.hpp"
#include "aidge/operator/Concat.hpp"
#include "aidge/operator/Conv.hpp"
#include "aidge/operator/ConvDepthWise.hpp"
#include "aidge/operator/Div.hpp"
#include "aidge/operator/Erf.hpp"
#include "aidge/operator/FC.hpp"
#include "aidge/operator/Gather.hpp"
#include "aidge/operator/GenericOperator.hpp"
#include "aidge/operator/GlobalAveragePooling.hpp"
#include "aidge/operator/MatMul.hpp"
#include "aidge/operator/MaxPooling.hpp"
#include "aidge/operator/MetaOperator.hpp"
#include "aidge/operator/MetaOperatorDefs.hpp"
#include "aidge/operator/Mul.hpp"
#include "aidge/operator/Operator.hpp"
#include "aidge/operator/Pad.hpp"
#include "aidge/operator/Producer.hpp"
#include "aidge/operator/Pow.hpp"
#include "aidge/operator/ReduceMean.hpp"
#include "aidge/operator/ReLU.hpp"
#include "aidge/operator/Reshape.hpp"
#include "aidge/operator/Scaling.hpp"
#include "aidge/operator/Slice.hpp"
#include "aidge/operator/Softmax.hpp"
#include "aidge/operator/Sqrt.hpp"
#include "aidge/operator/Sub.hpp"
#include "aidge/operator/Transpose.hpp"
#include "aidge/scheduler/Scheduler.hpp"
#include "aidge/stimuli/Stimulus.hpp"

#include "aidge/recipes/Recipes.hpp"

#include "aidge/utils/Attributes.hpp"
#include "aidge/utils/StaticAttributes.hpp"
#include "aidge/utils/DynamicAttributes.hpp"
#include "aidge/utils/Random.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

#endif /* AIDGE_IMPORTS_H_ */
