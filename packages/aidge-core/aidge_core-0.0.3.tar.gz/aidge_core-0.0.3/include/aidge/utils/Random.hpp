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

#ifndef AIDGE_RANDOM_H_
#define AIDGE_RANDOM_H_

#include <algorithm>
#include <random>
#include <vector>
namespace Aidge {

namespace Random {

/**
 * @brief Generator is a class created to handle only one Mersenne Twister
 * pseudo-random number generator for the whole Aidge framework.
 *
 * All of its method are static. You can set a random seed and access the
 * generator.
 * By default, the random seed is set to 0 but selected randomly.
 *
 */
class Generator {
   public:
    /**
     * @brief Set a seed to the pseudo-random number generator.
     *
     * @return std::mt19937&
     */
    static void setSeed(unsigned int seed);
    static unsigned int getSeed() { return seed; };
    /**
     * @brief Return a Mersenne Twister pseudo-random number generator.
     * You can set the seed of this generator using ``setSeed`` method.
     *
     * @return std::mt19937&
     */
    static std::mt19937& get() { return generator; };

   private:
    // Mersenne Twister pseudo-random number generator
    static std::mt19937 generator;
    static unsigned int seed;
};

inline void randShuffle(std::vector<unsigned int>& vec) {
    std::shuffle(vec.begin(), vec.end(), Aidge::Random::Generator::get());
}

}  // namespace Random
}  // namespace Aidge

#endif  // AIDGE_RANDOM_H_
