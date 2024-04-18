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

#ifndef AIDGE_BACKEND_OPERATORIMPL_H_
#define AIDGE_BACKEND_OPERATORIMPL_H_

#include <string>
#include <vector>

#include "aidge/utils/Types.h"
#include "aidge/data/Elts.hpp"

namespace Aidge {
class Operator;

class OperatorImpl {
public:
    OperatorImpl(const Operator& op, const std::string& backend);
    virtual void forward();
    virtual void backward();

    const std::string& backend() const noexcept {
        return mBackend;
    }
    /**
     * @brief Minimum amount of data from a specific input required by the
     * implementation to be run.
     *
     * @param inputIdx Index of the input analysed.
     * @return std::size_t
     */
    virtual Elts_t getNbRequiredData(const IOIndex_t inputIdx) const;

    // Amount of input data that cannot be overwritten during the execution.
    virtual Elts_t getNbRequiredProtected(const IOIndex_t inputIdx) const;

    // Memory required at an output for a given input size.
    virtual Elts_t getRequiredMemory(const IOIndex_t outputIdx, const std::vector<DimSize_t> &inputsSize) const;

    /**
     * @brief Total amount of consumed data from a specific input.
     *
     * @param inputIdx Index of the input analysed.
     * @return DimSize_t
     */
    virtual Elts_t getNbConsumedData(const IOIndex_t inputIdx) const;

    /**
     * @brief Total amount of produced data ready to be used on a specific output.
     *
     * @param outputIdx Index of the output analysed.
     * @return DimSize_t
     */
    virtual Elts_t getNbProducedData(const IOIndex_t outputIdx) const;

    /**
     * @brief Update the Consummer Producer system by simulating the consumption and production of i/o
     *
     */
    virtual void updateConsummerProducer();

    /**
     * @brief Reset the Consummer Producer system.
     *
     */
    virtual void resetConsummerProducer();

    virtual ~OperatorImpl() = default;

protected:
    const Operator &mOp;
    const std::string mBackend;
    std::vector<Elts_t> mNbConsumedData;
    std::vector<Elts_t> mNbProducedData;
};
} // namespace Aidge

#endif /* AIDGE_BACKEND_OPERATORIMPL_H_ */
