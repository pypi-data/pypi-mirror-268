#include "aidge/graphRegex/matchFsm/FsmRunTimeContext.hpp"
#include "aidge/graphRegex/matchFsm/FsmNode.hpp"

using namespace Aidge;

std::vector<std::set<NodePtr>> FsmRunTimeContext::mRejectedNodes;

FsmRunTimeContext::FsmRunTimeContext(std::shared_ptr<FsmNode> actState ,NodePtr actOpNode ,std::size_t idxRejeced  ){
    mActOpNode = actOpNode;
    mActState  = actState;

    //not define case
    if(idxRejeced ==  std::numeric_limits<std::size_t>::max()){
        mLocalIdxRejeced =  mRejectedNodes.size();
        mRejectedNodes.push_back(std::set<NodePtr>());
    }else{
        if(idxRejeced > mRejectedNodes.size()-1 ){
            throw std::runtime_error("FsmRunTimeContext idxRejeced");
        }
        mLocalIdxRejeced =idxRejeced;
    }
}



FsmRunTimeContext::FsmRunTimeContext(std::shared_ptr<FsmRunTimeContext> fsmRunTime){
    mActOpNode        = fsmRunTime->mActOpNode;
    mActState         = fsmRunTime->mActState;
    mCommonNodes      = fsmRunTime->mCommonNodes;
    mValidNodes       = fsmRunTime->mValidNodes;
    mLocalIdxRejeced  = fsmRunTime->mLocalIdxRejeced;
}
FsmRunTimeContext::FsmRunTimeContext(std::shared_ptr<FsmRunTimeContext> fsmRunTime,std::shared_ptr<FsmNode> actState ,NodePtr actOpNode ){
    mActOpNode        = actOpNode;
    mActState         = actState;
    mCommonNodes      = fsmRunTime->mCommonNodes;
    mValidNodes       = fsmRunTime->mValidNodes;
    mLocalIdxRejeced  = fsmRunTime->mLocalIdxRejeced;
}

void FsmRunTimeContext::addRejectedNode(NodePtr node){
    mRejectedNodes[mLocalIdxRejeced].insert(node);
}

bool FsmRunTimeContext::isOnValidState(void){
    return mActState->isValid();
}

bool FsmRunTimeContext::isCommonDefined(NodePtr node){
    //return mCommonNodes.find(node) != mCommonNodes.end();

    std::set<NodePtr> nodes = getCommonNodes();
    for(const auto& nodeC : nodes){
        if(nodeC.get() == node.get()){
            return true;
        }
    }
    return false;
}

bool FsmRunTimeContext::isAlreadyValid(NodePtr node){

    std::set<NodePtr> nodes = getValidNodes();
    for(const auto& nodeV : nodes){
        if(nodeV.get() == node.get()){
            return true;
        }
    }
    return false;

    //return getValidNodes().find(node) != getValidNodes().end();
}

bool FsmRunTimeContext::areCompatible(std::shared_ptr<FsmRunTimeContext> fsmContext){
    /*
    see if 2 context can be merge
    it need to have different  mValidNodes exept for common
    and the same idx for the common
    */

   //common node

   for (const auto& ref : getCommon()) {
        for (const auto& test : fsmContext->getCommon()) {
            //same index
            if(ref.second == test.second){
                if(ref.first != test.first){
                    return false;
                }
            }
        }
   }

   //valid nodes
    std::set<NodePtr> commonElements;
    std::set<NodePtr> A = getValidNodesNoCommon();
    std::set<NodePtr> B = fsmContext->getValidNodesNoCommon();
    std::set_intersection(
        A.begin(),A.end(),
        B.begin(),  B.end(),
        std::inserter(commonElements, commonElements.end())
       );

    return (commonElements.empty()) ? true : false;
}

bool FsmRunTimeContext::areEqual(std::shared_ptr<FsmRunTimeContext> fsmContext){
    if(getActNode() != fsmContext->getActNode()){
        return false;
    }
    if (getActState() != fsmContext->getActState()){
        return false;
    }
    if (getValidNodes() != fsmContext->getValidNodes()){
        return false;
    }
    if (getCommon() != fsmContext->getCommon()){
        return false;
    }


    return true;
}

void FsmRunTimeContext::setCommon(NodePtr node,std::size_t commonIdx){
    if(isCommonDefined(node)){
        if (mCommonNodes.at(node) != commonIdx){
            throw std::runtime_error("conflict idx in the Common node");
        }
    }else{
        mCommonNodes[node] = commonIdx;
    }
}

void FsmRunTimeContext::setValid(NodePtr node,std::shared_ptr<ConditionalInterpreter> tag){
    //we already find a node of this type
    if(mValidNodes.find(tag) != mValidNodes.end()){
        if(isAlreadyValid(node) && !isCommonDefined(node) ){
            throw std::runtime_error("setValid you valid tow time");
        }
        mValidNodes[tag].insert(node);
    }else{
        mValidNodes[tag] = {node};
    }

}

std::size_t FsmRunTimeContext::getSubStmId(void){
    return mActState->getOrigin();
}

NodePtr FsmRunTimeContext::getCommonNodeFromIdx(std::size_t commonIdx){
    for (const auto& pair : mCommonNodes) {
        if (pair.second == commonIdx) {
            return pair.first; // Return the key when the value is found
        }
    }
    throw std::runtime_error("getCommonNodeFromIdx Value not found in the map");
}

std::size_t FsmRunTimeContext::getCommonNodeIdx(NodePtr node){
    if(isCommonDefined(node)){
        return mCommonNodes.at(node);
    }
    throw std::runtime_error("getCommonNodeIdx node not found");
}

std::set<NodePtr> FsmRunTimeContext::getCommonNodes(void){
    std::set<NodePtr> nodes;
    // Iterate over the map and insert values into the set
    for (const auto& pair : mCommonNodes) {
        nodes.insert(pair.first);
    }
    return nodes;
}

std::map<NodePtr,std::size_t> FsmRunTimeContext::getCommon(void){
    return mCommonNodes;
}

std::set<NodePtr> FsmRunTimeContext::getValidNodes(void){

    auto sharedSet = std::make_shared<std::set<NodePtr>>();
    // Create a set to store the values from the map
    std::set<NodePtr> nodes;
    // Iterate over the map and insert values into the set
    for (const auto& pair : mValidNodes) {
        nodes.insert(pair.second.begin(),pair.second.end());
    }
    return nodes;
}

std::set<NodePtr> FsmRunTimeContext::getValidNodesNoCommon(void){
    std::set<NodePtr> differenceSet;
    std::set<NodePtr> valide = getValidNodes();
    std::set<NodePtr> common = getCommonNodes();
    std::set_difference(valide.begin(), valide.end(), common.begin(), common.end(),std::inserter(differenceSet, differenceSet.end()));
    return differenceSet;
}

std::map<std::shared_ptr<ConditionalInterpreter>,std::set<NodePtr>>& FsmRunTimeContext::getValid(void){
    return mValidNodes;
}

NodePtr FsmRunTimeContext::getActNode(void){
    return mActOpNode;
}

std::shared_ptr<FsmNode> FsmRunTimeContext::getActState(){
    return mActState;
}


void FsmRunTimeContext::rst(void){
    mRejectedNodes.clear();
}

