#include "aidge/graphRegex/GraphFsmInterpreter.hpp"

using namespace Aidge; 


GraphFsmInterpreter::GraphFsmInterpreter(const std::string graphMatchExpr,std::vector<std::shared_ptr<ConditionalInterpreter>>&nodesCondition):mParser(graphMatchExpr){
    mActGroupe = 0;

    for (const auto &obj : nodesCondition) {
        if(mNodesCondition.find(obj->getKey()) ==mNodesCondition.end()){
             mNodesCondition[obj->getKey()] = obj;
        }else{
            throw std::logic_error("GraphFsmInterpreter Bad Key" );
        }
    }
}
std::shared_ptr<FsmGraph>  GraphFsmInterpreter::interpret(void){
    mActGroupe = 0;
    std::shared_ptr<AstNode<gRegexTokenTypes>> tree = mParser.parse();
    std::shared_ptr<FsmGraph> out = visit(tree);
    return out;
}

std::shared_ptr<FsmGraph> GraphFsmInterpreter::visit(std::shared_ptr<AstNode<gRegexTokenTypes>> AstTree){

    std::vector<std::shared_ptr<AstNode<gRegexTokenTypes>>> nextAstNodes = AstTree->getChilds();

    if(AstTree->getType() == gRegexTokenTypes::SEP){
        return sepF(visit(nextAstNodes[0]),visit(nextAstNodes[1]));
    }else if(AstTree->getType() == gRegexTokenTypes::NEXT){
        return nextF(visit(nextAstNodes[0]),visit(nextAstNodes[1]));
    }else if(AstTree->getType() == gRegexTokenTypes::QOM){
        return qomF(visit(nextAstNodes[0]));
    }else if(AstTree->getType() == gRegexTokenTypes::QZM){
        return qzmF(visit(nextAstNodes[0]));
    }else if(AstTree->getType() == gRegexTokenTypes::KEY || AstTree->getType() == gRegexTokenTypes::CKEY){
        return keyF(AstTree);
    }else if(AstTree->getType() == gRegexTokenTypes::LPAREN){
        mActGroupe += 1;
        std::shared_ptr<FsmGraph> out = visit(nextAstNodes[0]);
        mActGroupe -= 1;
        return out;
    }else{
        throw std::logic_error("visit Bad token type" );
    }
}




std::shared_ptr<FsmGraph> GraphFsmInterpreter::keyF(std::shared_ptr<AstNode<gRegexTokenTypes>> AstNode){
    

    std::shared_ptr<FsmNode>  start = std::make_shared<FsmNode>(false,true);
    std::shared_ptr<FsmNode>  valid = std::make_shared<FsmNode>(true,false);
    std::shared_ptr<FsmGraph> graph = std::make_shared<FsmGraph>(mParser.getQuery());
    std::shared_ptr<FsmEdge> edge;
    

    if(AstNode->getType() == gRegexTokenTypes::CKEY){
        edge = FsmEdgeFactory::make(start,valid,FsmEdgeTypes::COMMON,mNodesCondition,AstNode->getValue());
    }else if (AstNode->getType() == gRegexTokenTypes::KEY)
    {
        edge = FsmEdgeFactory::make(start,valid,FsmEdgeTypes::UNIQUE,mNodesCondition,AstNode->getValue());
    }else{

        throw std::logic_error("keyF Bad in AST" );
    }
    
    graph->addEdge(edge);
    graph->setGroupe(mActGroupe);
    return graph;
}

std::shared_ptr<FsmGraph> GraphFsmInterpreter::sepF(std::shared_ptr<FsmGraph> leftFsm,std::shared_ptr<FsmGraph> rigthFsm){

    size_t idxLeft = leftFsm->getNbSubFsm();
    rigthFsm->incOriginAllNodeBy(idxLeft);
    leftFsm->unionG(rigthFsm);
    //the rigthFsm is no longer usfull
    return leftFsm;
}

std::shared_ptr<FsmGraph> GraphFsmInterpreter::nextF(std::shared_ptr<FsmGraph> leftFsm,std::shared_ptr<FsmGraph> rigthFsm){
    /*
        combine the 2 Graph
        all valid node of A are  merge with Start B, Start B is un Start
        update the relative reference  

           A          B
        SA -> VA + SB -> VB
           A    B
        SA -> q -> VB
    */
    leftFsm->mergeOneStartOneValid(rigthFsm);
    //the rigthFsm is no longer usfull
    return leftFsm;
}

std::shared_ptr<FsmGraph> GraphFsmInterpreter::qomF(std::shared_ptr<FsmGraph> fsm){
    /*
        +
        valid node is connect to the child of Start with the same edge condition
            A
        S -> V

            A
        S -> V
          (E|R)
        V -> S
    */

    std::vector<std::shared_ptr<FsmNode>> allStart =  fsm->getStartNodes();
    std::set<std::shared_ptr<FsmNode>> allValid = fsm->getValidNodes();
    std::shared_ptr<FsmEdge> edge;

    if(allStart.size() != 1){
         throw std::logic_error("qomF Bad in AST" );
    }

    for(auto start : allStart ){
        for(auto edgeStart :start->getEdges() ){
            if (auto sharedEdge = edgeStart.lock()) {

                const std::map<size_t, int> commonRef = sharedEdge->getRelative();
                bool haveCommon = !commonRef.empty();

                for(auto valid : allValid){
                    if(haveCommon){
                        /*
                        the // quantify case 
                        get the go back and make a lexeme id(number)
                        we need to go back to the ref delta min #TODO
                        */
                        bool hasMinRef = false;
                        std::pair<size_t, int> minRef;
                        for (const auto& entry : commonRef) {
                            if (!hasMinRef || std::abs(minRef.second) > std::abs(entry.second)) {
                                hasMinRef = true;
                                minRef = entry;
                            }
                        }
                        std::stringstream lexem;
                        lexem << "(" << minRef.first << ", " << minRef.second << ")";
                        edge = FsmEdgeFactory::make(valid,start,FsmEdgeTypes::REF,mNodesCondition, lexem.str());
                    }else{
                        /*
                        the sequencial quantify case 
                        no reference to common 
                        */
                        edge = FsmEdgeFactory::make(valid,start,FsmEdgeTypes::EMPTY,mNodesCondition,"");

                    }
                    fsm->addEdge(edge);
                }
            }else{
                throw std::runtime_error("edgeStart weak pointer is expired" );
            }
        }
     
    }
    return fsm;

}

std::shared_ptr<FsmGraph> GraphFsmInterpreter::qzmF(std::shared_ptr<FsmGraph> fsm){
        /*
        qomf and a bypass empty start to valide 
        */
    fsm = qomF(fsm);

    std::vector<std::shared_ptr<FsmNode>> allStart =  fsm->getStartNodes();
    std::set<std::shared_ptr<FsmNode>> allValid = fsm->getValidNodes();
    std::shared_ptr<FsmEdge> edge;

    if(allStart.size() != 1){
         throw std::logic_error("qzmF Bad in AST" );
    }

    for(auto start : allStart ){
       
        for(auto valid : allValid){
            edge = FsmEdgeFactory::make(start,valid,FsmEdgeTypes::EMPTY,mNodesCondition,"");
            fsm->addEdge(edge);
        }
    }
        
    return fsm;


}