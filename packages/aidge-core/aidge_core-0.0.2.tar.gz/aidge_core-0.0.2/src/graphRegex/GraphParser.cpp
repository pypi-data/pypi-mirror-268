#include <memory>
#include <string>
#include <vector>

#include "aidge/graphRegex/GraphParser.hpp"

Aidge::GraphParser::GraphParser(const std::string gRegexExpressions):
mLexer(gRegexExpressions)
{
    mCurrentToken = mLexer.getNextToken();
}

Aidge::GraphParser::~GraphParser() noexcept = default;


const std::string Aidge::GraphParser::getQuery(){
    return mLexer.getQuery();
}

std::shared_ptr<Aidge::AstNode<Aidge::gRegexTokenTypes>> Aidge::GraphParser::parse(void){

    std::shared_ptr<AstNode<gRegexTokenTypes>> astTree = constructAstAllExpr();
    rstParser();
    return astTree;
}


void Aidge::GraphParser::rstParser(void){
    mLexer.rstPosition();
    mCurrentToken = mLexer.getNextToken();
}


void Aidge::GraphParser::ackToken(gRegexTokenTypes  tokenType){

    if(mCurrentToken->getType() == tokenType ){
        try {
            mCurrentToken = mLexer.getNextToken();
        } catch (const std::runtime_error& e) {
            std::ostringstream errorMessage;
            errorMessage << "Graph Lexer error in Parser :\n"<< e.what() << std::endl;
            throw std::runtime_error(errorMessage.str());
        }
    }else{
        std::ostringstream errorMessage;
        errorMessage << "Bad syntax GraphParser " << static_cast<int>(mCurrentToken->getType())  <<"!="<< static_cast<int>(tokenType) << "\n";
        errorMessage << mLexer.rep();
        throw std::runtime_error(errorMessage.str());
    }
}

/*
exp : KEY(QOM | QZM)?  | CKEY | domain
*/
std::shared_ptr<Aidge::AstNode<Aidge::gRegexTokenTypes>> Aidge::GraphParser::constructAstExp(void)
{

    try{
        std::shared_ptr<ParsingToken<gRegexTokenTypes>> token = mCurrentToken->copy();
        std::shared_ptr<AstNode<gRegexTokenTypes>> node = std::make_shared<AstNode<gRegexTokenTypes>>(token);

        if (mCurrentToken->getType() == gRegexTokenTypes::KEY  ){
            ackToken(gRegexTokenTypes::KEY );
            if (mCurrentToken->getType() == gRegexTokenTypes::QOM  ){
                token = mCurrentToken->copy();
                ackToken(gRegexTokenTypes::QOM );
                std::shared_ptr<AstNode<gRegexTokenTypes>> newNode = std::make_shared<AstNode<gRegexTokenTypes>>(token,
                std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{node});
                return newNode;
            }else if (mCurrentToken->getType() == gRegexTokenTypes::QZM  ){
                token = mCurrentToken->copy();
                ackToken(gRegexTokenTypes::QZM );
                std::shared_ptr<AstNode<gRegexTokenTypes>> newNode = std::make_shared<AstNode<gRegexTokenTypes>>(token,
                std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{node});
                return newNode;
            }
            return node;
        }else if (mCurrentToken->getType() == gRegexTokenTypes::CKEY){
            ackToken(gRegexTokenTypes::CKEY );
            return node;
        }else{
            return constructAstDomain();
        }

    } catch (const std::runtime_error& e) {
        std::ostringstream errorMessage;
        errorMessage << "GraphParser constructAstExp :\n"<< e.what() << std::endl;
        throw std::runtime_error(errorMessage.str());
    }
}

/*
seq :exp (NEXT seq)*
*/
std::shared_ptr<Aidge::AstNode<Aidge::gRegexTokenTypes>> Aidge::GraphParser::constructAstSeq(void)
{

   try{

        std::shared_ptr<AstNode<gRegexTokenTypes>> left = constructAstExp();
        if(mCurrentToken->getType() == gRegexTokenTypes::NEXT )
        {
            std::shared_ptr<ParsingToken<gRegexTokenTypes>> token = mCurrentToken->copy();
            ackToken(gRegexTokenTypes::NEXT);
            std::shared_ptr<AstNode<gRegexTokenTypes>> newNode = std::make_shared<AstNode<gRegexTokenTypes>>(token,
            std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{left,constructAstSeq()});
            left = newNode;
        }
        return left;

    } catch (const std::runtime_error& e) {
        std::ostringstream errorMessage;
        errorMessage << "GraphParser constructAstSeq :\n"<< e.what() << std::endl;
        throw std::runtime_error(errorMessage.str());
    }

}


/*
LPAREN seq RPAREN (QOM | QZM)
*/
std::shared_ptr<Aidge::AstNode<Aidge::gRegexTokenTypes>> Aidge::GraphParser::constructAstDomain(void)
{

   try{
        std::shared_ptr<ParsingToken<gRegexTokenTypes>> token ;
        std::shared_ptr<AstNode<gRegexTokenTypes>> node ;

        token = mCurrentToken->copy();
        ackToken(gRegexTokenTypes::LPAREN);
        node = std::make_shared<AstNode<gRegexTokenTypes>>(token,
        std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{constructAstSeq()});
        ackToken(gRegexTokenTypes::RPAREN);
        //(QOM | QZM)

        token = mCurrentToken->copy();
        if (mCurrentToken->getType() == gRegexTokenTypes::QOM){
            ackToken(gRegexTokenTypes::QOM);
            node = std::make_shared<AstNode<gRegexTokenTypes>>(token,
            std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{node});
        }else if (mCurrentToken->getType() == gRegexTokenTypes::QZM){
            ackToken(gRegexTokenTypes::QZM);
            node = std::make_shared<AstNode<gRegexTokenTypes>>(token,
            std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{node});
        }else{
            std::ostringstream errorMessage;
            errorMessage << "Bad syntax constructAstDomain must have quantifier \n";
            throw std::runtime_error(errorMessage.str());
        }

        return node;

    } catch (const std::runtime_error& e) {
        std::ostringstream errorMessage;
        errorMessage << "GraphParser constructAstDomain :\n"<< e.what() << std::endl;
        throw std::runtime_error(errorMessage.str());
    }
}

/*
        allExpr: seq (SEP allExpr)* | STOP
*/
std::shared_ptr<Aidge::AstNode<Aidge::gRegexTokenTypes>> Aidge::GraphParser::constructAstAllExpr(void)
{

    try{
        std::shared_ptr<AstNode<gRegexTokenTypes>> left = constructAstSeq();
        if(mCurrentToken->getType() == gRegexTokenTypes::SEP )
        {
            std::shared_ptr<ParsingToken<gRegexTokenTypes>> token = mCurrentToken->copy();
            ackToken(gRegexTokenTypes::SEP);

            if(mCurrentToken->getType() == gRegexTokenTypes::STOP )
            {
                 return left;
            }
            std::shared_ptr<AstNode<gRegexTokenTypes>> newNode = std::make_shared<AstNode<gRegexTokenTypes>>(token,
            std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>>{left,constructAstAllExpr()});
            left = newNode;
        }
        return left;

    } catch (const std::runtime_error& e) {
        std::ostringstream errorMessage;
        errorMessage << "GraphParser constructAstDomain :\n"<< e.what() << std::endl;
        throw std::runtime_error(errorMessage.str());
    }
}
