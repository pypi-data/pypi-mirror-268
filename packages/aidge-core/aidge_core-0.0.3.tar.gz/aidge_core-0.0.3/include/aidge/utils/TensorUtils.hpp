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

#ifndef AIDGE_CORE_UTILS_TENSOR_UTILS_H_
#define AIDGE_CORE_UTILS_TENSOR_UTILS_H_
#include <cmath>  // std::abs
#include "aidge/data/Tensor.hpp"

namespace Aidge {
/**
 * @brief Compare two :cpp:class:`Aidge::Tensor` value wise. The comparison function is:
 *
 * |t1-t2| <= absolute + relative * |t2|
 *
 * If a tensor value is different from the other tensor return False
 * If the tensor does not have the same size, return False
 * If the datatype is not the same between each tensor return False
 * If the templated type does not correspond to the datatype of each tensor, raise an assertion error
 *
 * @tparam T should correspond to the type of the tensor, define the type of the absolute and relative error
 * @param t1  first :cpp:class:`Aidge::Tensor` to test
 * @param t2  second :cpp:class:`Aidge::Tensor` to test
 * @param relative relative difference allowed (should be betwen 0 and 1)
 * @param absolute absolute error allowed (shoulmd be positive)
 * @return true if both tensor are approximately equal and have the datatype, shape. Else return false
 */
template <typename T1, typename T2 = T1>
bool approxEq(const Tensor& t1, const Tensor& t2, float relative = 1e-5f, float absolute = 1e-8f){
    assert(t1.dataType() == NativeType<T1>::type);
    assert(t2.dataType() == NativeType<T2>::type);
    assert(relative >= 0);
    assert(absolute >= 0 && absolute<=1);

    if (t1.size() != t2.size()){
        return false;
    }
    for(size_t i = 0; i < t1.size(); ++i){
        if (static_cast<float>(std::abs(t1.get<T1>(i) - t2.get<T2>(i))) > (absolute + (relative * static_cast<float>(std::abs(t2.get<T2>(i)))))){
            return false;
        }
    }
    return true;
}
}

#endif /* AIDGE_CORE_UTILS_TENSOR_UTILS_H_s */
