#include "aidge/graphRegex/matchFsm/FsmEdge.hpp"
#include "aidge/graphRegex/matchFsm/FsmNode.hpp"
#include "aidge/graphRegex/matchFsm/FsmRunTimeContext.hpp"

using namespace Aidge; 

std::map<std::string,int> FsmEdgeCommon::mCommonIdxMap;

bool FsmEdge::isCommon(void){
    return false;
}

size_t FsmEdge::getCommonIdx(void){
    return std::numeric_limits<std::size_t>::max();
}
const std::map<size_t,int>& FsmEdge::getRelative(void){
    return mRelativePos;
}
void FsmEdge::updateRelative( const std::map<size_t,int>& relativePos ){
    for (const auto& kvp : relativePos) {
            mRelativePos.insert(kvp);
    }
}
std::shared_ptr<FsmNode> FsmEdge::getSourceNode(void){
    return mNodeSource;
}
void FsmEdge::reSetSourceNode(const std::shared_ptr<FsmNode>& newSource){
    mNodeSource->rmEdge(shared_from_this());
    mNodeSource = newSource;
    mNodeSource->addEdge(shared_from_this());
    propagateRelativePos();

}
std::shared_ptr<FsmNode> FsmEdge::getDestNode(void){
    return mNodeDest;
}
void FsmEdge::reSetDestNode(const std::shared_ptr<FsmNode>& newDest){
        mNodeDest->rmParent(mNodeSource);
        mNodeDest = newDest;
        mNodeDest->addParent(mNodeSource);
        propagateRelativePos();
}
void FsmEdge::propagateRelativePos(void){

    std::set<std::size_t> myRelativeID;
    for (const auto& kvp : mRelativePos) {
        myRelativeID.insert(kvp.first);
    }

    for (const auto& nextWeakEdge : mNodeDest->getEdges()){

        if (auto nextEdge = nextWeakEdge.lock()) {
            
            if(this == nextEdge.get()){
                continue;
            }
            

            std::set<std::size_t> nextRelativeID;
            for (const auto& kvp : nextEdge->getRelative()) {
                nextRelativeID.insert(kvp.first);
            }

            // Find elements in myRelativeID but not in nextRelativeID
            std::set<std::size_t> idxsToPush;
            std::set_difference(myRelativeID.begin(), myRelativeID.end(),
                                nextRelativeID.begin(), nextRelativeID.end(),
                                std::inserter(idxsToPush, idxsToPush.begin()));

            // Find elements in nextRelativeID but not in myRelativeID
            std::set<std::size_t> idxsToGet;
            std::set_difference(nextRelativeID.begin(), nextRelativeID.end(),
                                myRelativeID.begin(), myRelativeID.end(),
                                std::inserter(idxsToGet, idxsToGet.begin()));

            //  test for integrity we look if 2 edge refer to the same
            //  ref and are link the ref dif is one
            //  not working for common node
            //  we can go deeper by find the all pass to a ref and see if the delta is good

            // Find elements present in both myRelativeID and nextRelativeID
            std::set<std::size_t> idxsTotest;
            for (auto idx : nextRelativeID){
                if (myRelativeID.find(idx) != myRelativeID.end()){
                    if (std::abs(getRelative().at(idx) - nextEdge->getRelative().at(idx)) != 1) {
                        throw std::runtime_error("Bad relative");
                    }
                }
            }


            
            // this edge have more relative info than the next
            std::map<size_t,int> tmpRelative;
            // we push this info to the next 
            for(auto idxToPush :idxsToPush ){
                tmpRelative.insert( std::make_pair(idxToPush, getRelative().at(idxToPush) +1));
            }
            if(tmpRelative.size() != 0){
                nextEdge->updateRelative(tmpRelative);
                nextEdge->propagateRelativePos();
            }
            tmpRelative.clear();


            // the next node have more info than me i need to get it
            for(auto idxToGet :idxsToGet ){
                tmpRelative.insert( std::make_pair(idxToGet, nextEdge->getRelative().at(idxToGet) -1));
            }
            if(tmpRelative.size() != 0){
                updateRelative(tmpRelative);
                
                for(auto weakParent : getSourceNode()->getParentNodes()){
                    if (auto parent = weakParent.lock()) {
                        for(auto weakPEdge : parent->getEdges()){
                            if (auto pEdge = weakPEdge.lock()) {
                                pEdge->propagateRelativePos();
                            }else{
                                throw std::runtime_error("propagateRelativePos parent edge weak pointer is expired" );
                            }
                        }
                    }else{
                        throw std::runtime_error("propagateRelativePos parent weak pointer is expired" );
                    }
                }
            }
            tmpRelative.clear();
        }else{
            throw std::runtime_error("propagateRelativePos edge weak pointer is expired" );
        }
    }
}

void FsmEdge::updateWeak(void){
    mNodeSource->addEdge(shared_from_this());
    mNodeDest->addParent(mNodeSource);
}

FsmEdge::FsmEdge(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest)
:mToTest(toTest)
{
    mNodeSource = source;
    mNodeDest   = dest;
    // wen i make the edge I init the nodes
    // mNodeSource->addEdge(shared_from_this());
    // mNodeDest->addParent(mNodeSource);
}


/////surchage

FsmEdgeUnique::FsmEdgeUnique(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest)
:FsmEdge(source,dest,toTest)
{
}
const EdgeTestResult FsmEdgeUnique::test(const std::shared_ptr<FsmRunTimeContext> stmContext){
    auto opNode = stmContext->getActNode();

    if(opNode == nullptr){
        return {false,std::set<NodePtr>()};//none
    }
    
    if(mToTest->test(opNode) && opNode->getChildren().size() <= 1){
        stmContext->setValid(opNode,mToTest);
        return {true,opNode->getChildren()} ;
    }else{
        stmContext->addRejectedNode(opNode);
        return {false,std::set<NodePtr>()};
    }
}
/////////////////////
FsmEdgeCommon::FsmEdgeCommon(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest, const std::string commonKey)
:FsmEdge(source,dest,toTest)
{
    //make a uid for common node 
    if(mCommonIdxMap.find(commonKey) == mCommonIdxMap.end()){
        mCommonIdxMap.insert(std::make_pair(commonKey, mCommonIdxMap.size()));
    }
    mCommonIdx = mCommonIdxMap[commonKey];
    propagateRelativePos();
}


const EdgeTestResult FsmEdgeCommon::test(const std::shared_ptr<FsmRunTimeContext> stmContext){
    
    auto opNode = stmContext->getActNode();

    if(opNode == nullptr){
        return {false,std::set<NodePtr>()};//none
    }
    if(mToTest->test(opNode)){
        stmContext->setCommon(opNode,mCommonIdx);
        stmContext->setValid(opNode,mToTest);
        return {true,opNode->getChildren()} ;
    }else{
        stmContext->addRejectedNode(opNode);
        return {false,std::set<NodePtr>()};
    }
}
bool FsmEdgeCommon::isCommon(void){
    return true;
 }
//////////////////// TODO FsmEdgeEmpty must be size_t
FsmEdgeRef::FsmEdgeRef(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const size_t refCommonIdx,const int deltaCommonIdx)
:FsmEdge(source,dest,nullptr),mRefCommonIdx(refCommonIdx),mdeltaCommonIdx(deltaCommonIdx)
{

}
const EdgeTestResult FsmEdgeRef::test(const std::shared_ptr<FsmRunTimeContext> stmContext){
    
    NodePtr refNode = stmContext->getCommonNodeFromIdx(mRefCommonIdx);
    if (refNode){
        std::set<std::shared_ptr<Node>> see;
        return {true,refNode->getNodeDelta(mdeltaCommonIdx,see)};
    }
    return  {false,std::set<NodePtr>()};
}
////////////////////
FsmEdgeEmpty::FsmEdgeEmpty(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest)
:FsmEdge(source,dest,nullptr)
{}
const EdgeTestResult FsmEdgeEmpty::test(const std::shared_ptr<FsmRunTimeContext> stmContext){
    auto opNode = stmContext->getActNode();
    if(opNode == nullptr){
        return {false,std::set<NodePtr>()};
    }
    return {true,std::set<NodePtr>({opNode})};//none
}
//////////////

FsmEdgeNone::FsmEdgeNone(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest)
:FsmEdge(source,dest,nullptr)
{}
 const EdgeTestResult FsmEdgeNone::test(const std::shared_ptr<FsmRunTimeContext> /*stmContext*/){
    return {false,std::set<NodePtr>()};
 }

/// factory
std::shared_ptr<FsmEdge> FsmEdgeFactory::make(
std::shared_ptr<FsmNode> source, 
std::shared_ptr<FsmNode> dest, FsmEdgeTypes type, 
std::map<std::string, std::shared_ptr<ConditionalInterpreter>> allTest,
const std::string lexeme)
{
        if (type == FsmEdgeTypes::EMPTY) {
            if (lexeme.empty()) {
                return std::make_shared<FsmEdgeEmpty>(source, dest);
            } else {
                throw std::invalid_argument("error lexem EMPTY");
            }
        } else if (type == FsmEdgeTypes::REF) {
            std::smatch m;
            std::regex refRegex("\\s*\\(\\s*(\\d+)\\s*,\\s*(-?\\d+)\\s*\\)\\s*");
            if (std::regex_match(lexeme, m, refRegex)) {
                int refCommonIdx = std::stoi(m[1]);
                int deltaCommonIdx = std::stoi(m[2]);
                return std::make_shared<FsmEdgeRef>(source, dest, refCommonIdx, deltaCommonIdx);
            } else {
                throw std::invalid_argument("error lexem REF " + lexeme);
            }
        } else if (type == FsmEdgeTypes::COMMON) {
            std::smatch m;
            std::regex commonRegex("\\s*(\\w+)#(\\d*)");
            if (std::regex_match(lexeme, m, commonRegex)) {
                std::string edgeType = m[1];
                std::string commonId =  m[2];
                size_t commonIdx = commonId.empty() ? 0 : std::stoi(commonId) + 1;
                std::string commonKey = edgeType + std::to_string(commonIdx);
            
                if(allTest.find(edgeType) == allTest.end()){
                    //if the key is not linked to a condition 
                    //by default, it is initialized by a edge that is always false
                    return std::make_shared<FsmEdgeNone>(source, dest);
                    //throw std::invalid_argument("Bad Node Test " + edgeType );
                }

                return  std::make_shared<FsmEdgeCommon> (source, dest, allTest.at(edgeType), commonKey);
            } else {
                throw std::invalid_argument("error lexem COMMON " + lexeme);
            }
        } else if (type == FsmEdgeTypes::UNIQUE) {
            std::regex uniqueRegex("\\s*(\\w+)");
            std::smatch m;
            if (std::regex_match(lexeme, m, uniqueRegex)) {
                std::string edgeType = m[1];

                if(allTest.find(edgeType) == allTest.end()){

                    //if the key is not linked to a condition 
                    //by default, it is initialized by a edge that is always false
                    return std::make_shared<FsmEdgeNone>(source, dest);
                    //throw std::invalid_argument("Bad Node Test " + edgeType );
                }

                return  std::make_shared<FsmEdgeUnique>(source, dest, allTest.at(edgeType));
            } else {
                throw std::invalid_argument("error lexem UNIQUE \"" + std::string(lexeme) +" eee\"");
            }
        } else {
            throw std::invalid_argument("Bad edge Type");
        }
    }