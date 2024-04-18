/**
 * @file
 * @brief
 * @version file 1.0.0
 * @author vl241552
 * @copyright
 *  Copyright (c) 2023 CEA, LIST, Embedded Artificial Intelligence Laboratory. All
 *  rights reserved.
 */



#ifndef AIDGE_CORE_CONDITIONAL_LEXER_H_
#define AIDGE_CORE_CONDITIONAL_LEXER_H_

#include <string>
#include <regex>
#include <memory> // for shared_ptr


#include <stdexcept> //error
#include <sstream>

#include "aidge/nodeTester/ConditionalTypes.hpp"
#include "aidge/utilsParsing/ParsingToken.hpp"


namespace Aidge{



class ConditionalLexer
{

public:
ConditionalLexer( const std::string ConditionalExpressions );

/**
 * @brief Get the next token on the ConditionalExpressions
 * @return ParsingToken<ConditionalTokenTypes>
 */
std::shared_ptr<ParsingToken<ConditionalTokenTypes>> getNextToken(void);
/**
 * @brief Restart at the start of the ConditionalExpressions
 *
 */
void rstPosition(void);

/**
 * @brief Test if the string is completely read
 * @return bool
 */
bool isEnd(void);


/**
 * @brief Get the representation of the class
 * @return string
 */
const std::string rep(){
   return mConditionalExpressions;
}

private:

/**
 * @brief Constructs an error message to display the character not understood by the lexer
 * @return error mesage
 */
std::runtime_error badTokenError(const std::string& currentChars,std::size_t position);

/**
 * @brief The expression of the test to be performed on the nodes
 */
const std::string mConditionalExpressions;
/**
 * @brief The lexer's current position in mConditionalExpressions
 */
std::size_t mPosition;

};

/////////////////////////////////////


}

#endif //AIDGE_CORE_CONDITIONAL_LEXER_H_
