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

#ifndef AIDGE_CORE_HOOK_HOOKLIST_H_
#define AIDGE_CORE_HOOK_HOOKLIST_H_

#include <memory>
#include <chrono>
#include <vector>
#include <cmath>

#include "aidge/data/Tensor.hpp"

struct OutputRange {
    std::vector<Tensor> res;
    
    void call(Tensor input) {
        for (std::size_t i = 0; i < mNode->getOperator()->nbOutputs(); ++i){ 
            std::shared_ptr<Tensor> tensor = mNode->getOperator()->getOutput(i);
            float max_value = 0.;
            float * casted_tensor = static_cast<float *>(tensor->getImpl()->rawPtr());
            // find the absolute max value in the tensor, save it to res
            for(std::size_t j = 0; j < tensor->size(); ++j) {
                if(std::abs(casted_tensor[j]) > max_value){
                    max_value = std::abs(casted_tensor[j]);
                }
            }
            auto result = Array1D<float, 1>{{max_value}};
            res.push_back(result);
        }
    }
};



#endif /* AIDGE_CORE_HOOK_HOOKLIST_H_ */


