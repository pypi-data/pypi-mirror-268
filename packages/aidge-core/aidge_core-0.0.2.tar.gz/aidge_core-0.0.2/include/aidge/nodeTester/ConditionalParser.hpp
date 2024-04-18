


#ifndef AIDGE_CORE_CONDITIONAL_PARSER_H_
#define AIDGE_CORE_CONDITIONAL_PARSER_H_


#include <memory> // for shared_ptr
#include <map>
#include <vector>

#include "aidge/nodeTester/ConditionalLexer.hpp"
#include "aidge/nodeTester/ConditionalTypes.hpp"
#include "aidge/utilsParsing/ParsingToken.hpp"
#include "aidge/utilsParsing/AstNode.hpp"

namespace Aidge{

const std::map<ConditionalTokenTypes, std::size_t> ConditionalPrec{
    {ConditionalTokenTypes::AND,2},
    {ConditionalTokenTypes::OR,1}
};




using ASTNodeCh = std::vector<std::shared_ptr<AstNode<ConditionalTokenTypes>>>;

/**
 * @brief this class uses the lexer to create an AST according to a set of gramer rules
 */
class ConditionalParser {

    public:
    /**
     * @brief AST graph creation function
     * @param ConditionalExpressions String representing the logical fuction to be performed
     */
    ConditionalParser(const std::string ConditionalExpressions);

    ~ConditionalParser() noexcept;

    /**
     * @brief AST graph creation function
     * @return The AST tree
     */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> parse(void);


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
    void ackToken(ConditionalTokenTypes  tokenType);

    /**
     * @ingroup ParsingFunctions
     * @brief Function of grammar rules for values : (KEY|INTEGER|FOAT|STRING|LAMBDA lambda)
     * @return AST node
     */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> constructAstVal(void);
    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for comparison : val (EQ|NEQ) val | LPAREN expr RPAREN
    * @return AST node
    */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> constructAstCmpr(void);
    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for arguments of a lambda : LAMBDA val (ARGSEP val)* RPAREN
    * @return AST node
    */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> constructAstLambda(void);
    /**
    * @ingroup ParsingFunctions
    * @brief Function of grammar rules for a expresion : cmpr ((AND | OR) cmpr)*
    * @return AST node
    */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> constructAstExpr(std::size_t precLimit = 0);


    /**
    * @brief The actual token in the parce
    */
    std::shared_ptr<ParsingToken<ConditionalTokenTypes>> mCurrentToken;
    /**
    * @brief The lexem use
    */
    ConditionalLexer mLexer;

};


}

#endif //AIDGE_CORE_CONDITIONAL_PARSER_H_
