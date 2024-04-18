/**
 * \file Hook.hpp
 * \brief Hook structure
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

#ifndef Hook_H_
#define Hook_H_

#include "aidge/utils/Attributes.hpp"
#include "aidge/utils/Registrar.hpp"
#include <memory>

namespace Aidge {

class Operator;
class Hook : public Registrable<Hook, std::tuple<std::string>, std::shared_ptr<Hook>(const std::shared_ptr<Operator>)> {
//class Hook : public Registrable<Hook, std::tuple<std::string>, std::shared_ptr<Hook>(const std::shared_ptr<Operator>)>{
protected:
    const std::shared_ptr<Operator> mOperator;

public:
    Hook(std::shared_ptr<Operator> op) : mOperator(op) {}
    virtual ~Hook() = default;

    virtual void call() = 0;

};
}

#endif /* Hook_H_ */
