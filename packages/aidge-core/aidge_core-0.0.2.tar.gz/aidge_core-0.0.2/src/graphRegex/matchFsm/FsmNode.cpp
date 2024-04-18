#include "aidge/graphRegex/matchFsm/FsmNode.hpp"
#include "aidge/graphRegex/matchFsm/FsmEdge.hpp"
#include "aidge/graphRegex/matchFsm/FsmRunTimeContext.hpp"

using namespace Aidge; 



FsmNode::FsmNode(bool isAValid,bool isAStart ){
    mIsAStart =isAStart;
    mIsAValid =isAValid;

}
const std::vector<std::shared_ptr<FsmRunTimeContext>> FsmNode::test( std::shared_ptr<FsmRunTimeContext> fsmContext){


    std::vector<std::shared_ptr<FsmRunTimeContext>> out;

    for(auto edge : mEdges){
        if (auto sharedEdge = edge.lock()) {

            std::shared_ptr<FsmNode> nextState =  sharedEdge->getDestNode();

            //make copy of the fsmContext
            std::shared_ptr<FsmRunTimeContext> newFsmContext = std::make_shared<FsmRunTimeContext>(fsmContext);

            EdgeTestResult edgeRes = sharedEdge->test(newFsmContext);

            if(edgeRes.success){
                if(edgeRes.node.size() != 0){
                    for(auto nextNode :edgeRes.node ){
                        if(!newFsmContext->isAlreadyValid(nextNode)|| newFsmContext->isCommonDefined(nextNode) ){
                            out.push_back( std::make_shared<FsmRunTimeContext>(newFsmContext,nextState,nextNode));
                           
                        }else{
                            out.push_back( std::make_shared<FsmRunTimeContext>(newFsmContext,nextState,nullptr));
                        }

                    }
                }else{
                    out.push_back( std::make_shared<FsmRunTimeContext>(newFsmContext,nextState,nullptr));
                }
            }
            newFsmContext.reset();

        }else{
            throw std::runtime_error("test FsmNode weak pointer is expired" );
        }

    }
    return out;
}



std::size_t FsmNode::getOrigin(void){
    return mOriginFsm;
}
void FsmNode::incOrigin(std::size_t inc){
    mOriginFsm += inc;
}
void FsmNode::rmEdge(std::shared_ptr<FsmEdge> edge){
    mEdges.erase(edge);
}

void FsmNode::addEdge(std::shared_ptr<FsmEdge> edge){
    std::weak_ptr<FsmEdge> edgeW(edge);
    if (!edgeW.expired()) {
        mEdges.insert(edgeW);
    }else{
        throw std::runtime_error("addEdge FsmNode weak pointer is expired" );
    }
}

// const std::set<std::shared_ptr<FsmNode>> FsmNode::getChildNodes(void){
//     std::set<std::shared_ptr<FsmNode>> children;
//     for(auto edge : mEdges){
//          if (auto sharedEdge = edge.lock()) {
//                 children.insert(sharedEdge->getDestNode());
//          }else{
//             throw std::runtime_error("getChildNodes FsmNode weak pointer is expired" );
//          }
//     }
//     return children;
// }


const std::set<std::weak_ptr<FsmNode>,lex_compare<FsmNode>>& FsmNode::getParentNodes(void){
    return mParents;
}
const std::set<std::weak_ptr<FsmEdge>,lex_compare<FsmEdge>>& FsmNode::getEdges(void){
    return mEdges;
}

void FsmNode::setGroupe(std::size_t groupeIdx){
    mGroupeFsm = groupeIdx;
    
}

bool FsmNode::isValid(void){
    return mIsAValid;
}
bool FsmNode::isStart(void){
    return mIsAStart;
}
void FsmNode::unValid(void){
    mIsAValid =false;
}
void FsmNode::valid(void){
    mIsAValid =true;
}
void FsmNode::unStart(void){
    mIsAStart =false;
}
void FsmNode::start(void){
    mIsAStart =true;
}



void FsmNode::addParent(std::shared_ptr<FsmNode> node){

    std::weak_ptr<FsmNode> nodeW(node);
    if (!nodeW.expired()) {
        mParents.insert(nodeW);
    }else{
        throw std::runtime_error("addParent FsmNode weak pointer is expired" );
    }
}
void FsmNode::rmParent(std::shared_ptr<FsmNode> node){
    mParents.erase(node);
}