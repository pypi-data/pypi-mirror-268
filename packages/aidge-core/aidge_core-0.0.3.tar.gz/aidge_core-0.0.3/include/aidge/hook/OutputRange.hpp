/**
 * \file execTime.hpp
 * \brief execTime structure
 * \version file 1.0.0
 * \date Creation 27 June 2023
 * \date 27 June 2023
 * \par ChangeLog
 * \par
 *  v1.0.0, 27 June 2023<br>
 *  - Initial version.
 * \author ik243221
 * \copyright
 *  Copyright (c) 2023 CEA, LIST, Embedded Artificial Intelligence Laboratory. All
 *  rights reserved.
 */

#ifndef AIDGE_CORE_HOOK_OUTPUTRANGE_H_
#define AIDGE_CORE_HOOK_OUTPUTRANGE_H_

#include "aidge/operator/Operator.hpp"
#include "aidge/hook/Hook.hpp"
#include <memory>
#include <chrono>
#include <vector>
#include <cmath>
namespace Aidge {

class OutputRange : public Hook {
private:
    std::vector<float> registeredOutputs = std::vector<float>();
public:
    OutputRange(const std::shared_ptr<Operator> op) : Hook(op) {}
    ~OutputRange() = default;

    void call() override final {
        //std::cout << "call() outputRange hook " << std::endl;
        //this assumes there is only 1 output possible
        std::shared_ptr<Tensor> tensor = mOperator->getOutput(0);
        //tensor->print();
        //std::cout << "call() outputRange hook : tensor printed" << std::endl;
        float max_value = 0.;
        float * casted_tensor = static_cast<float *>(tensor->getImpl()->rawPtr());
        //find the absolute max value in the tensor, save it to registered outputs
        for(std::size_t i = 0; i < tensor->size(); ++i) {
            //std::cout << "call() outputRange hook : casted_tensor[i] = " << casted_tensor[i] << std::endl;
            if(std::abs(casted_tensor[i]) > max_value){
                max_value = std::abs(casted_tensor[i]);
            }
        }
        //std::cout << "call() outputRange hook : max_value = " << max_value << std::endl;
        registeredOutputs.push_back(max_value);
    }

    static std::shared_ptr<OutputRange> create(const std::shared_ptr<Operator> op)
    {
        return std::make_shared<OutputRange>(op);
    }

    std::vector<float> getOutputs() {
        return  registeredOutputs;
    }

    float getOutput(size_t idx) {
        return registeredOutputs[idx];
    }

};

namespace {
    static Registrar<Hook> registrarHook_OutputRange({"output_range"}, Aidge::OutputRange::create);
}
}

#endif /* outputRange_H_ */