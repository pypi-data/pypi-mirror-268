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

#include <memory>
#include <stdexcept>  // std::runtime_error
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/operator/GlobalAveragePooling.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::GlobalAveragePooling_Op::Type = "GlobalAveragePooling";

void Aidge::GlobalAveragePooling_Op::computeOutputDims() {
  // error checking
  if (!getInput(0)) {
    AIDGE_THROW_OR_ABORT(std::runtime_error,
                         "GlobalAveragePooling : The input was not connected");
  }
  // necessary bc forward dims sometimes passes with an empty vector before
  // doing another pass
  else if (getInput(0)->empty()) {
    return;
  // computation
  } else {
    AIDGE_ASSERT(getInput(0)->dims().size() >= 3,
                 "GlobalAveragePooling :  needs at least a 3 dimensions input, "
                 "number of input dim : {}",
                 getInput(0)->dims().size());
    // Global average pooling takes each filter, averages its values and uses
    // it as an output(Much like a fancier flatten). 1st dim is batch 2nd is
    // number of filter
    const std::vector<DimSize_t> out_dims{getInput(0)->dims().at(0),
                                          getInput(0)->dims().at(1)};
    mOutputs[0]->resize(out_dims);
  }
}

void Aidge::GlobalAveragePooling_Op::setBackend(const std::string &name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(GlobalAveragePooling_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}