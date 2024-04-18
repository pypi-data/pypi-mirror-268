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

#include "aidge/operator/ReduceMean.hpp"

#include <algorithm>  // std::for_each, std::sort
#include <cstddef>    // std::size_t
#include <cstdint>    // std::int32_t
#include <memory>
#include <stdexcept>  // std::runtime_error
#include <string>
#include <vector>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

const std::string Aidge::ReduceMean_Op::Type = "ReduceMean";

void Aidge::ReduceMean_Op::computeOutputDims() {
        if (!getInput(0)) {
            AIDGE_THROW_OR_ABORT(std::runtime_error, "Every input should be associated with a Tensor");
        }
        if (!getInput(0)->empty()) {
            // make Axes attribute positive
            std::vector<std::int32_t>& axes = this->template getAttr<ReduceMeanAttr::Axes>();
            std::for_each(axes.begin(), axes.end(), [&] (std::int32_t& val) {
                if (val < 0)
                    val+=static_cast<std::int32_t>(getInput(0)->nbDims());
            });
            std::sort(axes.begin(), axes.end());

            // build output dimensions
            std::vector<DimSize_t> outDims = getInput(0)->dims();
            if (this->template getAttr<ReduceMeanAttr::KeepDims>()) {
                std::for_each(axes.cbegin(), axes.cend(), [&outDims] (const std::int32_t& val) { outDims[val] = 1; });
            }
            else {
                for (auto it = axes.crbegin(); it != axes.crend(); ++it)
                    outDims.erase(outDims.begin() + static_cast<std::size_t>(*it));
            }

            // TODO: change {1} for {} when scalar Tensors are better handled.
            mOutputs[0]->resize((outDims.size()>0) ? outDims : std::vector<DimSize_t>({1}));

        }
    }

void Aidge::ReduceMean_Op::setBackend(const std::string& name, Aidge::DeviceIdx_t device) {
    SET_IMPL_MACRO(ReduceMean_Op, *this, name);
    mOutputs[0]->setBackend(name, device);
}