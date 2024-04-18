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

#include <cassert>
#include <cstddef>  // std::size_t
#include <memory>
#include <vector>
#include <cmath>


#include "aidge/data/Database.hpp"
#include "aidge/data/DataProvider.hpp"
#include "aidge/data/Tensor.hpp"

#include "aidge/utils/Random.hpp"


Aidge::DataProvider::DataProvider(const Aidge::Database& database, const std::size_t batchSize, const bool shuffle, const bool dropLast)
    : mDatabase(database),
      mBatchSize(batchSize),
      mShuffle(shuffle),
      mDropLast(dropLast),
      mNumberModality(database.getItem(0).size()),
      mNbItems(mDatabase.getLen()),
      mIndexBatch(0)
{
    // Iterating on each data modality in the database
    // Get the tensor dimensions, datatype and backend of each modality to ensure each data have the same
    for (const auto& modality : mDatabase.getItem(0)) {
        mDataDims.push_back(modality->dims());
        // assert(std::strcmp(item[i]->getImpl()->backend(), "cpu") == 0 && "DataProvider currently only supports cpu backend tensors");
        mDataTypes.push_back(modality->dataType());
    }

    // Compute the number of bacthes depending on mDropLast boolean
    mNbBatch = (mDropLast) ?
                static_cast<std::size_t>(std::floor(mNbItems / mBatchSize)) :
                static_cast<std::size_t>(std::ceil(mNbItems / mBatchSize));
}

std::vector<std::shared_ptr<Aidge::Tensor>> Aidge::DataProvider::readBatch() const
{
    AIDGE_ASSERT(mIndexBatch <= mNbBatch, "Cannot fetch more data than available in database");
    std::size_t current_batch_size;
    if (mIndexBatch == mNbBatch) {
        current_batch_size = mLastBatchSize;
    } else {
        current_batch_size = mBatchSize;
    }

    // Create batch tensors (dimensions, backends, datatype) for each modality
    std::vector<std::shared_ptr<Tensor>> batchTensors;
    auto dataBatchDims = mDataDims;
    for (std::size_t i = 0; i < mNumberModality; ++i) {
        dataBatchDims[i].insert(dataBatchDims[i].begin(), current_batch_size);
        auto batchData = std::make_shared<Tensor>();
        batchData->resize(dataBatchDims[i]);
        batchData->setBackend("cpu");
        batchData->setDataType(mDataTypes[i]);
        batchTensors.push_back(batchData);
    }

    // Call each database item and concatenate each data modularity in the batch tensors
    for (std::size_t i = 0; i < current_batch_size; ++i){

        auto dataItem = mDatabase.getItem(mBatches[(mIndexBatch-1)*mBatchSize+i]);
        // auto dataItem = mDatabase.getItem(startIndex+i);
        // assert same number of modalities
        assert(dataItem.size() == mNumberModality && "DataProvider readBatch : item from database have inconsistent number of modality.");

        // Browse each modularity in the database item
        for (std::size_t j = 0; j < mNumberModality; ++j) {
            auto dataSample = dataItem[j];

            // Assert tensor sizes
            assert(dataSample->dims() == mDataDims[j] && "DataProvider readBatch : corrupted Data size");

            // Assert implementation backend
            // assert(dataSample->getImpl()->backend() == mDataBackends[j] && "DataProvider readBatch : corrupted data backend");

            // Assert DataType
            assert(dataSample->dataType() == mDataTypes[j] && "DataProvider readBatch : corrupted data DataType");

            // Concatenate into the batch tensor
            batchTensors[j]->getImpl()->copy(dataSample->getImpl()->rawPtr(), dataSample->size(), i*dataSample->size());
        }
    }
    return batchTensors;
}


void Aidge::DataProvider::setBatches(){

    mBatches.clear();
    mBatches.resize(mNbItems);
    std::iota(mBatches.begin(),
              mBatches.end(),
              0U);

    if (mShuffle){
        Aidge::Random::randShuffle(mBatches);
    }

    if (mNbItems % mBatchSize !=0){ // The last batch is not full
        std::size_t lastBatchSize = static_cast<std::size_t>(mNbItems % mBatchSize);
        if (mDropLast){ // Remove the last non-full batch
            AIDGE_ASSERT(lastBatchSize <= mBatches.size(), "Last batch bigger than the size of database");
            mBatches.erase(mBatches.end() - lastBatchSize, mBatches.end());
            mLastBatchSize = mBatchSize;
        } else { // Keep the last non-full batch
            mLastBatchSize = lastBatchSize;
        }
    } else { // The last batch is full
        mLastBatchSize = mBatchSize;
    }
}
