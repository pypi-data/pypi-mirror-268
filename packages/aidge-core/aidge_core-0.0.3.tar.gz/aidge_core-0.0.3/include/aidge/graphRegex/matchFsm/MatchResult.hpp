#ifndef AIDGE_CORE_MATCH_RESULT_H_
#define AIDGE_CORE_MATCH_RESULT_H_

#include <cstddef>
#include <map>
#include <memory>
#include <string>
#include <set>
#include <vector>

#include "aidge/graphRegex/matchFsm/FsmRunTimeContext.hpp"
#include "aidge/graph/Node.hpp"

namespace Aidge{

/**
 * @brief contained the result of one match and the associate key , the query and the start node
*/

class MatchSolution{
private:
    std::map<std::string, std::set<NodePtr>> mSolution;
    const std::string mQueryFrom;
    const std::vector<NodePtr> mStartNode;

public:
    MatchSolution() = delete;
    MatchSolution(std::vector<std::shared_ptr<FsmRunTimeContext>>& precedence,const std::string query,const std::vector<NodePtr> startNode);

    inline const std::set<NodePtr>& at(const std::string& key) {
        return mSolution[key];
    }
    const std::set<NodePtr> getAll();
    bool areCompatible(std::shared_ptr<MatchSolution> solution);

    inline const std::string& getQuery() const noexcept { return mQueryFrom; }
    inline const std::vector<NodePtr>& getStartNode() const noexcept { return mStartNode; }
};


/**
 * @brief class that old the result of a matching
 * give access to all node and there tag in the expression
*/
class MatchResult
{
private:
    /* data */
    std::vector<std::shared_ptr<FsmRunTimeContext>> mAllValid;

    /*
    the Run time of each sub FSM , to have a valid match we need a set of one run time per FSM compatible
    the id must be continue
    */
    std::vector<std::vector<std::shared_ptr<FsmRunTimeContext>>> mIdToRunTime;

    std::vector<std::shared_ptr<MatchSolution>> mSolve;

    std::size_t mNbSubStm;



public:
    MatchResult() = delete;
    MatchResult(std::vector<std::shared_ptr<FsmRunTimeContext>> allValid,
                std::size_t nbSubStm,
                const std::string& query,const std::vector<NodePtr>& startNodes);

    /**
     * @brief get the set of the node match for une expression
     * @return the set of node of the graph that corresponding to an expression
    */
    inline std::shared_ptr<MatchSolution> getBiggerSolution(void) const noexcept {
        return mSolve.empty() ? nullptr : mSolve[0];
    }

    inline std::vector<std::shared_ptr<MatchSolution>> getSolutions(void) const noexcept {
        return mSolve;
    }

private:

/**
 * @brief recurrent function use to init mSolve in the constructor
 *
 **/
void _generateCombination( std::size_t idxSubStm, std::vector<std::shared_ptr<FsmRunTimeContext>>& precedence,const std::string& query,const std::vector<NodePtr>& startNodes);

};


}


#endif //AIDGE_CORE_MATCH_RESULT_H_
