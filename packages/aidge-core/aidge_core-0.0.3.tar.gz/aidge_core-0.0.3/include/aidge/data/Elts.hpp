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

#ifndef AIDGE_ELTS_H_
#define AIDGE_ELTS_H_

#include "aidge/utils/ErrorHandling.hpp"
#include "aidge/utils/Types.h"

namespace Aidge {
/**
 * Base object for Aidge consumer-producer model (C-P model).
 * It is a hybrid model: operator implementations can specify their C-P model
 * with precise data (bytes) or with tokens.
*/
struct Elts_t {
    enum EltType {
        Data,
        Token,
        Undef
    };

    NbElts_t data;
    NbElts_t token;
    EltType type;

    // Addition operator
    inline Elts_t operator+(const Elts_t& other) const {
        AIDGE_ASSERT(type == other.type || other.type == Undef || type == Undef,
            "Incompatible C-P model types: {} + {}. Data and Token cannot be mixed.", type, other.type);
        return Elts_t(data + other.data, token + other.token, (other.type == Undef) ? type : other.type);
    }

    // Addition assignment operator
    inline Elts_t& operator+=(const Elts_t& other) {
        AIDGE_ASSERT(type == other.type || other.type == Undef || type == Undef,
            "Incompatible C-P model types: {} += {}. Data and Token cannot be mixed.", type, other.type);
        data += other.data;
        token += other.token;
        type = (other.type == Undef) ? type : other.type;
        return *this;
    }

    // Comparison operators
    inline bool operator<(const Elts_t& other) const {
        if (type == Elts_t::Undef || type == Elts_t::Token) {
            // Nothing, or only a token is required: don't care about how much data has been produced for the token
            return (token < other.token);
        }
        else if (type == Elts_t::Data && other.type != Elts_t::Token) {
            // A precise amount of data is required, so the amount of produced data must be specified, a token is not enough
            return (data < other.data);
        }
        else {
            AIDGE_THROW_OR_ABORT(std::runtime_error,
                "Incompatible C-P model types: {} < {}. Data is expected for right-hand side.", type, other.type);
        }
    }

    inline bool operator>(const Elts_t& other) const {
        if (type == Elts_t::Undef || type == Elts_t::Token) {
            // Nothing, or only a token is required: don't care about how much data has been produced for the token
            return (token > other.token);
        }
        else if (type == Elts_t::Data && other.type != Elts_t::Token) {
            // A precise amount of data is required, so the amount of produced data must be specified, a token is not enough
            return (data > other.data);
        }
        else {
            AIDGE_THROW_OR_ABORT(std::runtime_error,
                "Incompatible C-P model types: {} > {}. Data is expected for right-hand side.", type, other.type);
        }
    }

    inline static Elts_t NoneElts() {
        return Elts_t(0, 0, Elts_t::Undef);
    }

    inline static Elts_t DataElts(NbElts_t data, NbElts_t token = 1) {
        return Elts_t(data, token, Elts_t::Data);
    }

    inline static Elts_t TokenElts(NbElts_t token) {
        return Elts_t(0, token, Elts_t::Token);
    }

private:
    inline Elts_t(NbElts_t data_, NbElts_t token_, EltType type_):
        data(data_), token(token_), type(type_) {}
};
} // end namespace Aidge

template<>
struct fmt::formatter<Aidge::Elts_t> {
    template<typename ParseContext>
    inline constexpr auto parse(ParseContext& ctx) {
        return ctx.begin();
    }

    template<typename FormatContext>
    inline auto format(Aidge::Elts_t const& elt, FormatContext& ctx) {
        return fmt::format_to(ctx.out(), "{}:{}", elt.data, elt.token);
    }
};

namespace {
template <>
const char* const EnumStrings<Aidge::Elts_t::EltType>::data[]
    = {"Data", "Token", "Undef"};
}

namespace Aidge {
inline auto format_as(Elts_t::EltType elt) { return EnumStrings<Aidge::Elts_t::EltType>::data[static_cast<int>(elt)]; }
}

#endif /* AIDGE_ELTS_H_ */
