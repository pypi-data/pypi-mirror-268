#include <memory>
#include <vector>

#include "aidge/nodeTester/ConditionalParser.hpp"


//////////////////////////////
//ConditionalParser
//////////////////////////////

Aidge::ConditionalParser::ConditionalParser(const std::string ConditionalExpressions)
    : mLexer(ConditionalExpressions)
{
    mCurrentToken = mLexer.getNextToken();
}

Aidge::ConditionalParser::~ConditionalParser() noexcept = default;

void Aidge::ConditionalParser::rstParser(void){
    mLexer.rstPosition();
    mCurrentToken = mLexer.getNextToken();
}

void Aidge::ConditionalParser::ackToken(ConditionalTokenTypes  tokenType){
    if(mCurrentToken->getType() == tokenType ){

        try {
            mCurrentToken = mLexer.getNextToken();
        } catch (const std::runtime_error& e) {
            std::ostringstream errorMessage;
            errorMessage << "Conditional Lexer error in Parser :\n"<< e.what() << std::endl;
            throw std::runtime_error(errorMessage.str());
        }
    }else{

        std::ostringstream errorMessage;
        errorMessage << "Bad syntax ConditionalParser " << static_cast<int>(mCurrentToken->getType())  <<"!="<< static_cast<int>(tokenType) << "\n";
        errorMessage << mLexer.rep();
        throw std::runtime_error(errorMessage.str());
    }
}



std::shared_ptr<Aidge::AstNode<Aidge::ConditionalTokenTypes>> Aidge::ConditionalParser::constructAstVal(void){
    /*
    val : (KEY|INTEGER|FOAT|STRING|LAMBDA)
    */
    std::shared_ptr<ParsingToken<ConditionalTokenTypes>> token = mCurrentToken->copy();

    if (token->getType() == ConditionalTokenTypes::KEY){
        ackToken(ConditionalTokenTypes::KEY);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);
    }
    else if(token->getType() == ConditionalTokenTypes::INTEGER){
        ackToken(ConditionalTokenTypes::INTEGER);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);
    }
    else if(token->getType() == ConditionalTokenTypes::FLOAT){
        ackToken(ConditionalTokenTypes::FLOAT);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);
    }
    else if(token->getType() == ConditionalTokenTypes::BOOL){
        ackToken(ConditionalTokenTypes::BOOL);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);
    }
    else if(token->getType() == ConditionalTokenTypes::STRING){
        ackToken(ConditionalTokenTypes::STRING);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);

    }else if(token->getType() == ConditionalTokenTypes::NODE){
        ackToken(ConditionalTokenTypes::NODE);
        return std::make_shared<AstNode<ConditionalTokenTypes>>(token);

    }else if(token->getType() == ConditionalTokenTypes::LAMBDA){
        return constructAstLambda();
    }

   throw std::runtime_error("ConditionalParser unknow val type "+ token->rep().str() + "\n" + mLexer.rep());

}

std::shared_ptr<Aidge::AstNode<Aidge::ConditionalTokenTypes>> Aidge::ConditionalParser::constructAstLambda(void){
    /*
    AstLambda :  LAMBDA val (ARGSEP val)* RPAREN
    */
    std::shared_ptr<ParsingToken<ConditionalTokenTypes>> tokenLdb = mCurrentToken->copy();
    ackToken(ConditionalTokenTypes::LAMBDA);
    ASTNodeCh paramLambda;
    //AT LEAST ONE VALUE AS INPUT OF A LAMBDA
    paramLambda.push_back(constructAstVal());
    while (mCurrentToken->getType() != ConditionalTokenTypes::RPAREN)
    {
        ackToken(ConditionalTokenTypes::ARGSEP);
        paramLambda.push_back(constructAstVal());
    }
    ackToken(ConditionalTokenTypes::RPAREN);
    return std::make_shared<AstNode<ConditionalTokenTypes>>(tokenLdb,paramLambda);
}

std::shared_ptr<Aidge::AstNode<Aidge::ConditionalTokenTypes>> Aidge::ConditionalParser::constructAstCmpr(void){
      /*
        cmpr   : val (EQ|NEQ) val | LPAREN expr RPAREN
        NOT ir ?
      */
     std::shared_ptr<ParsingToken<ConditionalTokenTypes>> token = mCurrentToken->copy();
     //we can check the type relation ir  key (EQ|NEQ) val | val (EQ|NEQ) key , but val (EQ|NEQ) val is valid ?
     if (token->getType() == ConditionalTokenTypes::LPAREN)
     {
        ackToken(ConditionalTokenTypes::LPAREN);
        std::shared_ptr<AstNode<ConditionalTokenTypes>> node = constructAstExpr();
        ackToken(ConditionalTokenTypes::RPAREN);
        return node;
     }else{

        std::shared_ptr<AstNode<ConditionalTokenTypes>> node = constructAstVal();
        token = mCurrentToken->copy();
        if (token->getType() == ConditionalTokenTypes::EQ){
            ackToken(ConditionalTokenTypes::EQ);
            return std::make_shared<AstNode<ConditionalTokenTypes>>(token,ASTNodeCh{node,constructAstVal()});
        }else if(token->getType() == ConditionalTokenTypes::NEQ){
            ackToken(ConditionalTokenTypes::NEQ);
            return std::make_shared<AstNode<ConditionalTokenTypes>>(token,ASTNodeCh{node,constructAstVal()});
        }else{

            throw std::runtime_error("constructAstCmpr "+ token->rep().str() + "\n" + mLexer.rep());
        }

     }
}

std::shared_ptr<Aidge::AstNode<Aidge::ConditionalTokenTypes>> Aidge::ConditionalParser::constructAstExpr(std::size_t precLimit /*= 0*/){
    /*
        expr   : cmpr ((AND | OR) cmpr)*
        the NOT is not binary OP can be use in pratt
        precedence H to L: TODO
        AND
        OR
    */

   //the not
    std::shared_ptr<AstNode<ConditionalTokenTypes>> left;
    std::shared_ptr<ParsingToken<ConditionalTokenTypes>> token = mCurrentToken->copy();

    if (mCurrentToken->getType() == ConditionalTokenTypes::NOT  ){
        ackToken(ConditionalTokenTypes::NOT );
        left= std::make_shared<AstNode<ConditionalTokenTypes>>(token,ASTNodeCh{constructAstCmpr()});
    }else{
        left= constructAstCmpr();
    }

    //pratt
    while (mCurrentToken->getType() != ConditionalTokenTypes::STOP ) //security
    {
        token = mCurrentToken->copy();
        //if the token is not in the map is not a operator so we consider a prec of 0
        if (ConditionalPrec.find(token->getType()) ==ConditionalPrec.end() ){
            return left;
        }

        //if my actual operator have a prec <= of the last operator
        std::size_t prec = ConditionalPrec.at(token->getType());
        if (prec <= precLimit){
            return left;
        }

        //Act all AND and OR
        ackToken(token->getType());

        std::shared_ptr<AstNode<ConditionalTokenTypes>> right = constructAstExpr(prec);

        //i'm not sur what append to newNode
        //std::shared_ptr<AstNode<ConditionalTokenTypes>> newNode = std::make_shared<AstNode<ConditionalTokenTypes>>(token,ASTNodeCh{left,constructAstCmpr()});
        std::shared_ptr<AstNode<ConditionalTokenTypes>> newNode = std::make_shared<AstNode<ConditionalTokenTypes>>(token,ASTNodeCh{left,right});
        left = newNode;
    }
    return left;
}


std::shared_ptr<Aidge::AstNode<Aidge::ConditionalTokenTypes>> Aidge::ConditionalParser::parse(void){
    /*
        expr   : cmpr ((AND | OR) cmpr)*
        cmpr   : val (EQ|NEQ) val | LPAREN expr RPAREN | BOOL | LAMBDA
        val    : (KEY|INTEGER|FOAT|STRING|LAMBDA)
        lambda :  LAMBDA val (ARGSEP val)* RPAREN
    */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> astTree = constructAstExpr();

    rstParser();
    return astTree;
}