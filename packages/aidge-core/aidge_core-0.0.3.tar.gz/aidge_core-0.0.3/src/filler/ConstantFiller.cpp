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

#include "aidge/filler/Filler.hpp"

#include <cstddef>  // std::size_t
#include <memory>
#include <string>

#include "aidge/data/Tensor.hpp"
#include "aidge/utils/ErrorHandling.hpp"


template<typename T>
void Aidge::constantFiller(std::shared_ptr<Aidge::Tensor> tensor, T constantValue) {
    AIDGE_ASSERT(tensor->getImpl(),
                 "Tensor got no implementation, cannot fill it.");
    AIDGE_ASSERT(NativeType<T>::type == tensor->dataType(), "Wrong data type");

    std::shared_ptr<Aidge::Tensor> cpyTensor;
    // Create cpy only if tensor not on CPU
    Aidge::Tensor& tensorWithValues =
        tensor->refCastFrom(cpyTensor, tensor->dataType(), "cpu");

    // Setting values
    for (std::size_t idx = 0; idx < tensorWithValues.size(); ++idx) {
        tensorWithValues.set<T>(idx, constantValue);
    }

    // Copy values back to the original tensors (actual copy only if needed)
    tensor->copyCastFrom(tensorWithValues);
}


template void Aidge::constantFiller<float>(std::shared_ptr<Aidge::Tensor>, float);
template void Aidge::constantFiller<double>(std::shared_ptr<Aidge::Tensor>, double);
