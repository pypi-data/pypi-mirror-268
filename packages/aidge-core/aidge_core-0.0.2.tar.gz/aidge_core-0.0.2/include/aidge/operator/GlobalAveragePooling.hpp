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

#ifndef AIDGE_CORE_OPERATOR_GLOBAL_AVERAGE_POOLING_H_
#define AIDGE_CORE_OPERATOR_GLOBAL_AVERAGE_POOLING_H_

#include <memory>
#include <string>
#include <vector>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/graph/Node.hpp"
#include "aidge/operator/OperatorTensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {

/**
 * @brief Description for the tensor data structure.
 * @details Sets the properties of the tensor without actually containing any
 * data. Contains a pointer to an actual contiguous implementation of data.
 */
class GlobalAveragePooling_Op
    : public OperatorTensor,
      public Registrable<GlobalAveragePooling_Op, std::string,
                         std::shared_ptr<OperatorImpl>(
                             const GlobalAveragePooling_Op &)> {
public:
  static const std::string Type;

  GlobalAveragePooling_Op() : OperatorTensor(Type, 1, 0, 1) {}

  GlobalAveragePooling_Op(const GlobalAveragePooling_Op &op)
      : OperatorTensor(op) {
        if (op.mImpl) {
            SET_IMPL_MACRO(GlobalAveragePooling_Op, *this, op.backend());
        } else {
            mImpl = nullptr;
        }
  }

  std::shared_ptr<Operator> clone() const override {
    return std::make_shared<GlobalAveragePooling_Op>(*this);
  }

  void computeOutputDims() override final;

  void setBackend(const std::string &name, DeviceIdx_t device = 0) override final;

  static const std::vector<std::string> getInputsName() {
    return {"data_input"};
  }
  static const std::vector<std::string> getOutputsName() {
    return {"data_output"};
  }
};

inline std::shared_ptr<Node>
GlobalAveragePooling(const std::string &name = "") {
  return std::make_shared<Node>(std::make_shared<GlobalAveragePooling_Op>(),
                                name);
}
} // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_GLOBAL_AVERAGE_POOLING_H_ */
