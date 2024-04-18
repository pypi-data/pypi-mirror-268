#ifndef AIDGE_CORE_GRAPH_LEXER_H_
#define AIDGE_CORE_GRAPH_LEXER_H_

#include <string>
#include <memory>
#include <regex>
#include <stdexcept> //error
#include <sstream>

#include "aidge/utilsParsing/ParsingToken.hpp"
#include "aidge/graphRegex/GraphRegexTypes.hpp"

namespace Aidge {

    class GraphLexer
    {

    public:
    GraphLexer( const std::string gRegexExpressions );

    /**
     * @brief Get the next token on the gRegexExpressions
     * @return ConditionalToken
     */
    std::shared_ptr<ParsingToken<gRegexTokenTypes>> getNextToken(void);
    /**
     * @brief Restart at the start of the gRegexExpressions
     *
     */
    void rstPosition(void);

    /**
     * @brief Test if the string is completely read
     * @return bool
     */
    bool isEnd(void);


    const std::string getQuery();


    /**
     * @brief Get the representation of the class
     * @return string
     */
    const std::string rep();

    private:

    /**
     * @brief Constructs an error message to display the character not understood by the lexer
     * @return error message
     */
    std::runtime_error badTokenError(const std::string& currentChars,std::size_t position);

    /**
     * @brief The expression of the test to be performed on the nodes
     */
    const std::string mRegularExpressions;
    /**
     * @brief The lexer's current position in mConditionalExpressions
     */
    std::size_t mPosition;

    };
}




#endif //AIDGE_CORE_GRAPH_LEXER_H_
