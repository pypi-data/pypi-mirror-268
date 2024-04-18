#include <algorithm> // set_intersection, std::sort
#include <memory>
#include <set>
#include <string>
#include <vector>

#include "aidge/graphRegex/matchFsm/MatchResult.hpp"

Aidge::MatchSolution::MatchSolution(std::vector<std::shared_ptr<FsmRunTimeContext>>& precedence,const std::string query,const std::vector<NodePtr> startNode):mQueryFrom(query),mStartNode(startNode){
        //reformat the solution
        for (const auto& context : precedence) {
            for (const auto& pair : context->getValid()) {

                if(mSolution.find(pair.first->getKey()) == mSolution.end()){
                    mSolution[pair.first->getKey()] = pair.second;
                }else{
                        mSolution[pair.first->getKey()].insert(pair.second.begin(), pair.second.end());
                }
            }
        }
}

const std::set<Aidge::NodePtr> Aidge::MatchSolution::getAll(){

        // Create a unique set to store all the elements
        std::set<NodePtr> uniqueSet;

        // Iterate through the map and insert elements from each set into the unique set
        for (const auto& pair : mSolution) {
            const std::set<NodePtr>& nodeSet = pair.second;

            // Insert elements from the current set into the unique set
            uniqueSet.insert(nodeSet.begin(), nodeSet.end());
        }

        return uniqueSet;
}

bool Aidge::MatchSolution::areCompatible(std::shared_ptr<Aidge::MatchSolution> solution){
    std::set<NodePtr> set1 = solution->getAll();
    std::set<NodePtr> set2 = getAll();
    std::set<NodePtr> intersection ;
    std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), std::inserter(intersection, intersection.begin()));
    return intersection.empty();
}


////////////////////////////////
//
////////////////////////////////
Aidge::MatchResult::MatchResult(std::vector<std::shared_ptr<Aidge::FsmRunTimeContext>> allValid,
                                std::size_t nbSubStm,
                                const std::string& query,
                                const std::vector<Aidge::NodePtr>& startNodes)
        : mIdToRunTime(nbSubStm),
          mNbSubStm(nbSubStm)
{
    mAllValid = allValid;

    //mIdToRunTimm
    for (const auto& contextPtr : allValid) {
        mIdToRunTime[contextPtr->getSubStmId()].push_back(contextPtr);
    }

    std::vector<std::shared_ptr<FsmRunTimeContext>> precedence;
    //make all solution possible
    _generateCombination(0,precedence,query,startNodes);
    //sort by solution number of elements
    std::sort(mSolve.begin(), mSolve.end(), [](std::shared_ptr<MatchSolution>& set1, std::shared_ptr<MatchSolution>& set2) {
        return set1->getAll().size() < set2->getAll().size();
    });
}

void Aidge::MatchResult::_generateCombination( std::size_t idxSubStm,
                                        std::vector<std::shared_ptr<Aidge::FsmRunTimeContext>>& precedence,
                                        const std::string& query,
                                        const std::vector<Aidge::NodePtr>& startNodes)
{
    //it's end , we are below the number of stm
    if (idxSubStm == mNbSubStm)
    {
        //precedence contain a list of FSM compatible, we just need to
        //check if all the nodes have been validated by at least one context

        //1) make the set of all node for the compute graph that are valid in all the  FsmRunTimeContext
        std::set<NodePtr> validNode;
        std::set<NodePtr> rejectNode;
        for (const auto& contextPtr : precedence) {
            std::set<NodePtr> tmpV =  contextPtr->getValidNodes();
            validNode.insert(tmpV.begin(), tmpV.end());
            std::set<NodePtr> tmpR =  contextPtr->getRejectedNodes();
            rejectNode.insert(tmpR.begin(),tmpR.end());
        }
        // 2) all  RejectedNodes need to be valid by an others stm
        // if it's not the case the match is not valid
        if(std::includes(validNode.begin(), validNode.end(), rejectNode.begin(), rejectNode.end())){
            //we can save the solution
            mSolve.push_back(std::make_shared<MatchSolution>(precedence,query,startNodes));
        }
        precedence.pop_back();
        return;
    }


    for (const auto& contextPtrOneFsm : mIdToRunTime[idxSubStm])
    {
        if(idxSubStm == 0){
            precedence.push_back(contextPtrOneFsm);
            _generateCombination(idxSubStm+1,precedence,query,startNodes);

        }else{
            //test if the new context is compatible with all the context in the precedence
            //
            bool compatibleSolutionFsm = true;
            for (const auto& contextPtrOfOtherFsm : precedence) {
                if(!(contextPtrOneFsm->areCompatible(contextPtrOfOtherFsm))){
                    compatibleSolutionFsm = false;
                    break;
                }
            }

            if(compatibleSolutionFsm){
                precedence.push_back(contextPtrOneFsm);
                _generateCombination(idxSubStm+1,precedence,query,startNodes);
            }

        }
    }

    if(idxSubStm != 0){
        precedence.pop_back();
    }
    return;

}