#ifndef AIDGE_CORE_GRAPH_PARSER_H_
#define AIDGE_CORE_GRAPH_PARSER_H_


#include <memory> // for shared_ptr
#include "aidge/graphRegex/GraphLexer.hpp"
#include "aidge/utilsParsing/AstNode.hpp"
#include "aidge/graphRegex/GraphRegexTypes.hpp"

namespace Aidge{

/**
 * @brief this class uses the lexer to create an AST according to a set of gramer rules
 */
class GraphParser {

public:
    /**
     * @brief AST graph creation function
     * @param gRegexExpressions String representing the logical fuction to be performed
     */
    GraphParser(const std::string gRegexExpressions);

    ~GraphParser() noexcept;

    /**
     * @brief AST graph creation function
     * @return The AST tree
     */
    std::shared_ptr<AstNode<gRegexTokenTypes>> parse(void);


    /**
     * @brief get the query that be use in the parsing
     * @return query
     */
    const std::string getQuery();


private:
    /**
     * @brief restart at the start of the ConditionalExpressions for LEXER and restart  mCurrentToken
     */
    void rstParser(void);

    //////////////////

    /**
     * @defgroup ParsingFunctions Function for creating AST
     * @brief Functions for recursive construction of the AST representing grammar rules
     */

    /**
     * @ingroup ParsingFunctions
     * @brief Token reading and verification function
     *
     */
    void ackToken(gRegexTokenTypes  tokenType);

    //TODO TODO
    /**
     * @ingroup ParsingFunctions
     * @brief Function of grammar rules for key :  KEY(QOM | QZM)? | CKEY
     * @return AST node
     */
    std::shared_ptr<AstNode<gRegexTokenTypes>> constructAstExp(void);

    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for sequence :  seq :exp (NEXT seq)*
    * @return AST node
    */
    std::shared_ptr<AstNode<gRegexTokenTypes>> constructAstSeq(void);

    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for domain : (seq NEXT domain)? | LPAREN domain RPAREN (QOM | QZM) (NEXT domain)?
    * @return AST node
    */
    std::shared_ptr<AstNode<gRegexTokenTypes>> constructAstDomain(void);

    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for multiple exepresion : allExpr: domain (SEP allExpr)*
    * @return AST node
    */
    std::shared_ptr<AstNode<gRegexTokenTypes>> constructAstAllExpr(void);


    /**
    * @brief The actual token in the parce
    */
    std::shared_ptr<ParsingToken<gRegexTokenTypes>> mCurrentToken;

    /**
    * @brief The lexem use
    */
    GraphLexer mLexer;

};


}

#endif //AIDGE_CORE_GRAPH_PARSER_H_
