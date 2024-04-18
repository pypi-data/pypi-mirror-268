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

#include "aidge/utils/Random.hpp"

#include <random>  // normal_distribution, uniform_real_distribution

std::mt19937 Aidge::Random::Generator::generator{std::random_device{}()};
unsigned int Aidge::Random::Generator::seed = 0;

void Aidge::Random::Generator::setSeed(unsigned int new_seed) {
    seed = new_seed;
    generator.seed(seed);
}
