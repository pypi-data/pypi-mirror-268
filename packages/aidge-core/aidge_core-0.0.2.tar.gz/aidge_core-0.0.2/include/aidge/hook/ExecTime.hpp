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
 * \author mn271187, ik243221
 * \copyright
 *  Copyright (c) 2023 CEA, LIST, Embedded Artificial Intelligence Laboratory. All
 *  rights reserved.
 */

#ifndef execTime_H_
#define execTime_H_

#include "aidge/operator/Operator.hpp"
#include "aidge/hook/Hook.hpp"
#include <memory>
#include <chrono>
#include <vector>

namespace Aidge {

class ExecTime : public Hook {
private:
    std::vector<std::chrono::high_resolution_clock::time_point> registeredTimes = std::vector<std::chrono::high_resolution_clock::time_point>();
public:
    ExecTime(const std::shared_ptr<Operator> op) : Hook(op) {}
    ~ExecTime() = default;

    void call() override final {
        registeredTimes.push_back(std::chrono::high_resolution_clock::now());
    }

    static std::shared_ptr<ExecTime> create(const std::shared_ptr<Operator> op)
    {
        return std::make_shared<ExecTime>(op);
    }

    std::vector<std::chrono::high_resolution_clock::time_point> getTimes() {
        return  registeredTimes;
    }

    std::chrono::high_resolution_clock::time_point getTime(size_t idx) {
        return registeredTimes[idx];
    }

};

namespace {
    static Registrar<Hook> registrarHook_ExecTime({"execution_time"}, Aidge::ExecTime::create);
}
}

#endif /* execTime_H_ */