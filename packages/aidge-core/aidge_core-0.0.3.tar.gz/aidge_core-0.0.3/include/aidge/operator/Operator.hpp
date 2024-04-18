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

#ifndef AIDGE_CORE_OPERATOR_OPERATOR_H_
#define AIDGE_CORE_OPERATOR_OPERATOR_H_

#include <memory>
#include <string>
#include <vector>
#include <utility>
#include <cstddef>

#include "aidge/backend/OperatorImpl.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/utils/Types.h"
#include "aidge/hook/Hook.hpp"

namespace Aidge {

enum class OperatorType {
    Data,
    Tensor
};

class Operator : public std::enable_shared_from_this<Operator> {
protected:
    std::shared_ptr<OperatorImpl> mImpl; // implementation of the operator
    std::map<std::string, std::shared_ptr<Hook>> mHooks;

private:
    std::string mType;
    const OperatorType mOperatorType;
    const IOIndex_t mNbData;
    const IOIndex_t mNbParam;
    const IOIndex_t mNbOut;

public:
    Operator() = delete;
    Operator(const std::string& type, const IOIndex_t nbData, const IOIndex_t nbParam, const IOIndex_t nbOut, const OperatorType operatorType = OperatorType::Data)
    : mType(type),
      mOperatorType(operatorType),
      mNbData(nbData),
      mNbParam(nbParam),
      mNbOut(nbOut)
    {
        // ctor
    }

    Operator(const Operator& op):
        std::enable_shared_from_this<Operator>(),
        mOperatorType(op.mOperatorType),
        mNbData(op.mNbData),
        mNbParam(op.mNbParam),
        mNbOut(op.mNbOut)
    {
        mType = op.mType;
        mImpl = nullptr;
        // Implementation is never cloned. It is up to the non-abstract Operator copy-constructor to create a new implementation matching the copied Operator implementation.
        // See https://gitlab.eclipse.org/eclipse/aidge/aidge_core/-/merge_requests/8#note_1214050 for the discussion.
        // Hooks are not copied.
    }

    virtual ~Operator() noexcept;

public:
    virtual std::shared_ptr<Operator> clone() const = 0;

    /**
     * @brief Set the specified input with a shallow copy.
     * @param inputIdx Index of the input to set.
     * @param data Data to copy.
     */
    virtual void associateInput(const IOIndex_t inputIdx, const std::shared_ptr<Data>& data) = 0;

    /**
     * @brief Set the specified input value by performing a deep copy of the given data.
     * The pointer itself is not changed, thus keeping the current connections.
     * @param inputIdx Index of the input to set.
     * @param data Data to copy.
     */
    virtual void setInput(const IOIndex_t inputIdx, const std::shared_ptr<Data>& data) = 0;
    virtual void setInput(const IOIndex_t inputIdx, std::shared_ptr<Data>&& data) = 0;
    virtual std::shared_ptr<Data> getRawInput(const IOIndex_t inputIdx) const = 0;
        /**
     * @brief Set the specified output value by performing a deep copy of the given data.
     * The pointer itself is not changed, thus keeping the current connections.
     * @param inputIdx Index of the input to set.
     */
    virtual void setOutput(const IOIndex_t outputIdx, const std::shared_ptr<Data>& data) = 0;
    virtual void setOutput(const IOIndex_t outputIdx, std::shared_ptr<Data>&& data) = 0;
    virtual std::shared_ptr<Data> getRawOutput(const IOIndex_t outputIdx) const = 0;

    std::shared_ptr<Hook> getHook(const std::string& hookName) {
        return mHooks[hookName];
    }
    void addHook(const std::string& hookName) {
        mHooks.insert(std::pair<std::string, std::shared_ptr<Hook>>(hookName,Registrar<Hook>::create({hookName})(shared_from_this())));
    }

    void runHooks() const;

///////////////////////////////////////////////////////
//        IMPLEMENTATION
///////////////////////////////////////////////////////
    std::string backend() const noexcept {
        return mImpl ? mImpl->backend() : "";
    }

    virtual void setBackend(const std::string& name, DeviceIdx_t device = 0) = 0;
    virtual void setDataType(const DataType& dataType) const = 0;

    /**
     * @brief Set a new OperatorImpl to the Operator
     *
     */
    inline void setImpl(std::shared_ptr<OperatorImpl> impl) { mImpl = impl; }

    /**
     * @brief Get the OperatorImpl of the Operator
     *
     */
    inline std::shared_ptr<OperatorImpl> getImpl() const noexcept {
        return mImpl;
    }

    /**
     * @brief Minimum amount of data from a specific input for one computation pass.
     * @param inputIdx Index of the input analysed.
     * @return Elts_t
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
     * @return Elts_t
     */
    virtual Elts_t getNbConsumedData(const IOIndex_t inputIdx) const;

    /**
     * @brief Total amount of produced data ready to be used on a specific output.
     *
     * @param outputIdx Index of the output analysed.
     * @return Elts_t
     */
    virtual Elts_t getNbProducedData(const IOIndex_t outputIdx) const;

    virtual void updateConsummerProducer();

    virtual void resetConsummerProducer();

    virtual void forward();

    virtual void backward();

///////////////////////////////////////////////////////
//        INNER
///////////////////////////////////////////////////////

    inline std::string type() const noexcept {
        return mType;
    }

    inline OperatorType operatorType() const noexcept{
        return mOperatorType;
    }

    virtual inline bool isAtomic() const noexcept { return true; }

    inline IOIndex_t nbInputs() const noexcept { return mNbData+mNbParam; };
    inline IOIndex_t nbData() const noexcept { return mNbData; };
    inline IOIndex_t nbParam() const noexcept { return mNbParam; };
    inline IOIndex_t nbOutputs() const noexcept { return mNbOut; };

    static const std::vector<std::string> getInputsName() {
        return {};
    }
    static const std::vector<std::string> getOutputsName() {
        return {};
    }
};
} // namespace Aidge

#endif /* AIDGE_CORE_OPERATOR_OPERATOR_H_ */
