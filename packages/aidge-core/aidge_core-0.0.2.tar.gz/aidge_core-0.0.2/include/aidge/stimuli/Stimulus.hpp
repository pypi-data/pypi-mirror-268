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

#ifndef AIDGE_CORE_STIMULI_STIMULUS_H_
#define AIDGE_CORE_STIMULI_STIMULUS_H_

#include <string>
#include <memory>
#include <tuple>

#include "aidge/backend/StimulusImpl.hpp"
#include "aidge/data/Tensor.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/ErrorHandling.hpp"

namespace Aidge {
/**
 * @brief Stimulus. A class wrapping a data sample. Stimulus has two functioning modes. The first mode enables to load data samples from a dataPath and optionnaly store the data in-memory. The second mode enables to store a data sample that was already loaded in memory.
 * @details When Stimulus is used in the first mode, the loading function is determined automaticaly based on the backend and the file extension.
 */
class Stimulus : public Registrable<Stimulus, std::tuple<std::string, std::string>, std::unique_ptr<StimulusImpl>(const std::string&)> {
private:
    /// Stimulus data path
    const std::string mDataPath;
    const std::string mFileExtension;
    bool mLoadDataInMemory;

    /// Stimulus data ptr
    std::shared_ptr<Tensor> mData;

    // Implementation of the Stimulus
    std::unique_ptr<StimulusImpl> mImpl;

public:
    Stimulus() = delete;

    /**
     * @brief Construct a new Stimulus object based on a tensor that is already loaded in memory.
     *
     * @param data the data tensor.
     */
    Stimulus(const std::shared_ptr<Tensor> data)
    : mLoadDataInMemory(true),
      mData(data)
    {
        // ctor
    }

    /**
     * @brief Construct a new Stimulus object based on a dataPath to load the data.
     *
     * @param dataPath path to the data to be loaded.
     * @param loadDataInMemory when true, keep the data in memory once loaded
     */
    Stimulus(const std::string& dataPath, bool loadDataInMemory = false)
    : mDataPath(dataPath),
      mFileExtension(dataPath.substr(dataPath.find_last_of(".") + 1)),
      mLoadDataInMemory(loadDataInMemory)
    {
        AIDGE_ASSERT((dataPath.find_last_of(".") !=  std::string::npos), "Cannot find extension");
    }

    /**
     * @brief Construct a new Stimulus object copied from another one.
     * @param otherStimulus
     */
    Stimulus(const Stimulus& otherStimulus)
        : mDataPath(otherStimulus.mDataPath),
          mFileExtension(otherStimulus.mFileExtension),
          mLoadDataInMemory(otherStimulus.mLoadDataInMemory),
          mData(otherStimulus.mData)
    {
        if (otherStimulus.mImpl) {
            mImpl = Registrar<Stimulus>::create({"opencv", mFileExtension})(mDataPath);
        }
    }

    virtual ~Stimulus();

public:
    /**
     * @brief Set the backend of the stimuli associated load implementation
     * @details Create and initialize an implementation.
     * @param name name of the backend.
     */
    inline void setBackend(const std::string &name) {
        mImpl = Registrar<Stimulus>::create({name, mFileExtension})(mDataPath);
    }

    /**
     * @brief Get the data tensor associated to the stimuli. The data is either loaded from a datapath or passed from an in-memory tensor.
     *
     * @return std::shared_ptr<Tensor> the data tensor.
     */
    virtual std::shared_ptr<Tensor> load();
};
} // namespace Aidge

#endif // AIDGE_CORE_STIMULI_STIMULUS_H_
