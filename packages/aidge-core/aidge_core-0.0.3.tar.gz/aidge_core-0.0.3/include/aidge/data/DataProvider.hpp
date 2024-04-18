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

#ifndef AIDGE_CORE_DATA_DATAPROVIDER_H_
#define AIDGE_CORE_DATA_DATAPROVIDER_H_

#include <cstddef>  // std::size_t
#include <memory>   // std::shared_ptr
#include <string>
#include <vector>   // std::vector

#include "aidge/data/Database.hpp"
#include "aidge/data/Data.hpp"

namespace Aidge {

/**
 * @brief Data Provider. Takes in a database and compose batches by fetching data from the given database.
 * @todo Implement Drop last batch option. Currently returns the last batch with less elements in the batch.
 * @todo Implement readRandomBatch to compose batches from the database with a random sampling startegy. Necessary for training.
 */
class DataProvider {
private:
    // Dataset providing the data to the dataProvider
    const Database& mDatabase;
    
    // Desired size of the produced batches
    const std::size_t mBatchSize;

    // Enable random shuffling for learning
    const bool mShuffle;

    // Drops the last non-full batch
    const bool mDropLast;

    // Number of modality in one item
    const std::size_t mNumberModality;

    // mNbItems contains the number of items in the database
    std::size_t mNbItems;
    // mBatches contains the call order of each database item
    std::vector<unsigned int> mBatches; 
    // mIndex browsing the number of batch
    std::size_t mIndexBatch;

    // mNbBatch contains the number of batch
    std::size_t mNbBatch;
    // Size of the Last batch
    std::size_t mLastBatchSize;

    // Store each modality dimensions, backend and type
    std::vector<std::vector<std::size_t>> mDataDims;
    std::vector<std::string> mDataBackends;
    std::vector<DataType> mDataTypes; 

public:
    /**
     * @brief Constructor of Data Provider.
     * @param database database from which to load the data.
     * @param batchSize number of data samples per batch.
     */
    DataProvider(const Database& database, const std::size_t batchSize, const bool shuffle = false, const bool dropLast = false);

public:
    /**
     * @brief Create a batch for each data modality in the database.
     * @return a vector of tensors. Each tensor is a batch corresponding to one modality.
     */
    std::vector<std::shared_ptr<Tensor>> readBatch() const;

    /**
     * @brief Get the Number of Batch.
     * 
     * @return std::size_t 
     */
    inline std::size_t getNbBatch(){
        return mNbBatch;
    };

    /**
     * @brief Get the current Index Batch.
     * 
     * @return std::size_t 
     */
    inline std::size_t getIndexBatch(){
        return mIndexBatch;
    };

    /**
     * @brief Reset the internal index batch that browses the data of the database to zero.
     */
    inline void resetIndexBatch(){
        mIndexBatch = 0;
    };

    /**
     * @brief Increment the internal index batch that browses the data of the database.
     */
    inline void incrementIndexBatch(){
        ++mIndexBatch;
    };

    /**
     * @brief Setup the batches for one pass on the database.
     */
    void setBatches();

    /**
     * @brief End condition of dataProvider for one pass on the database.
     * 
     * @return true when all batch were fetched, False otherwise
     */
    inline bool done(){
        return (mIndexBatch == mNbBatch);
    };


    // Functions for python iterator iter and next (definition in pybind.cpp)
    /**
     * @brief __iter__ method for iterator protocol
     * 
     * @return DataProvider* 
     */
    DataProvider* iter();

    /**
     * @brief __next__ method for iterator protocol
     * 
     * @return std::vector<std::shared_ptr<Aidge::Tensor>> 
     */
    std::vector<std::shared_ptr<Aidge::Tensor>> next();
};

} // namespace Aidge

#endif /* AIDGE_CORE_DATA_DATAPROVIDER_H_ */
