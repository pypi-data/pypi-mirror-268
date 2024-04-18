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

#ifndef AIDGE_CORE_DATA_DATABASE_H_
#define AIDGE_CORE_DATA_DATABASE_H_

#include <cstddef>
#include <memory>
#include <vector>

#include "aidge/data/Tensor.hpp"

namespace Aidge {

/**
 * @brief Abstract class representing a map from a key to data.
 * All databases should inherit from this class. All subclasses should overwrite
 * :cpp:function:`Database::getItem` to fetch data from a given index.
 */
class Database {
public:
    Database() = default;
    virtual ~Database() noexcept = default;

    /**
     * @brief Fetch an item of the database.
     * @param index index of the item.
     * @return vector of data mapped to index.
     */
    virtual std::vector<std::shared_ptr<Tensor>> getItem(const std::size_t index) const = 0;

    /**
     * @brief Get the number of items in the database
     *
     * @return std::size_t
     */
    virtual std::size_t getLen() const noexcept = 0;

    /**
     * @brief Get the number of modalities in one database item
     *
     * @return std::size_t
     */
    virtual std::size_t getNbModalities() const noexcept = 0;

};
} // namespace Aidge

#endif /* AIDGE_CORE_DATA_DATABASE_H_ */
