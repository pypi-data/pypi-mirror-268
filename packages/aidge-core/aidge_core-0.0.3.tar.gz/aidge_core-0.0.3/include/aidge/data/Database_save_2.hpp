#ifndef Database_H_
#define Database_H_

#include <cstring>

#include "aidge/data/Tensor.hpp"

namespace Aidge{

/**
 * @brief Database. An abstract class representing a database. All databases should inherit from this class. All subclasses should overwrite :cpp:function:`Database::get_item` to fetch data from a given index.
 * @todo Make the dataset generic. Always ground truth.
 */
class Database {

public:

    virtual ~Database() = default; 

    /**
     * @brief Fetch a data sample and its corresponding ground_truth 
     * @param index index of the pair (```data```, ```ground truth```) to fetch from the database
     * @return A pair of pointers to the data (first) and its corresping ground truth (second)
     */
    virtual std::pair<std::shared_ptr<Tensor>,std::shared_ptr<Tensor>> get_item(unsigned int index) = 0;

    /** 
     * @return The number of data samples in the database.
     */
    virtual unsigned int get_len() = 0;

protected:
    
    std::vector<std::shared_ptr<Tensor>> mData;
    std::vector<std::shared_ptr<Tensor>> mLabel;

};

}

#endif /* Database_H_ */