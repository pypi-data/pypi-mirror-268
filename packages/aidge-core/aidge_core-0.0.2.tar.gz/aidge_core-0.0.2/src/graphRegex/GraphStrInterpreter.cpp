#include "aidge/graphRegex/GraphStrInterpreter.hpp"

using namespace Aidge; 

GraphStrInterpreter::GraphStrInterpreter(const std::string graphMatchExpr):mParser(graphMatchExpr){
    mToTest = graphMatchExpr;
    mToTest.erase(std::remove_if(mToTest.begin(), mToTest.end(), ::isspace), mToTest.end());
}


std::string GraphStrInterpreter::visit(std::shared_ptr<AstNode<gRegexTokenTypes>> AstTree){

    std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>> nextAstNodes = AstTree->getChilds();

    if(AstTree->getType() == gRegexTokenTypes::SEP){
        return visit(nextAstNodes[0])+";"+visit(nextAstNodes[1]);
    }else if(AstTree->getType() == gRegexTokenTypes::NEXT){
        return visit(nextAstNodes[0])+"->"+visit(nextAstNodes[1]);
    }else if(AstTree->getType() == gRegexTokenTypes::QOM){
        return visit(nextAstNodes[0])+"+";
    }else if(AstTree->getType() == gRegexTokenTypes::QZM){
        return visit(nextAstNodes[0])+"*";
    }else if(AstTree->getType() == gRegexTokenTypes::KEY || AstTree->getType() == gRegexTokenTypes::CKEY){
        return AstTree->getValue();
    }else if(AstTree->getType() == gRegexTokenTypes::LPAREN){
        return "("+visit(nextAstNodes[0])+")";
    }else{
        throw std::logic_error("visit Bad token type" );
    }


}


std::string GraphStrInterpreter::interpret(void){
    std::shared_ptr<AstNode<gRegexTokenTypes>> tree = mParser.parse();
    return visit(tree);
}