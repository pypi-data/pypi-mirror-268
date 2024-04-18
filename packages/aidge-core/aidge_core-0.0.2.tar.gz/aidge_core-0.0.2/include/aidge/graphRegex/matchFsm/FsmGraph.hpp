
#ifndef AIDGE_CORE_FSM_GRAPH_H_
#define AIDGE_CORE_FSM_GRAPH_H_

#include <set>
#include <vector>
#include <memory>
#include <stdexcept> //error

#include "aidge/graphRegex/matchFsm/FsmNode.hpp"
#include "aidge/graphRegex/matchFsm/FsmEdge.hpp"
#include "aidge/graphRegex/matchFsm/MatchResult.hpp"
namespace Aidge{



class FsmGraph
{
private:
    /**
     * @brief all node Origin
    */
    std::set<std::size_t> mAllOrigin;
    std::set<std::shared_ptr<FsmEdge>> mEdges;


    const std::string mQuery;

public:

    FsmGraph(const std::string query);
    virtual ~FsmGraph() = default;

    std::vector<std::shared_ptr<MatchSolution>> test(const std::vector<NodePtr>& StartNodes);



    const std::set<std::shared_ptr<FsmEdge>>& getEdge(void);
    /**
     * @brief add edge in the graph, as FsmEdge know the source and dest FsmNode these nodes are also add to the graph
    */
    void addEdge(std::shared_ptr<FsmEdge>& edge);

    /**
     * @brief get the list of the starting states
     * @details we need to use a vector because the order of the nodes is important for start node initialization \ref test()
    */
    const std::vector<std::shared_ptr<FsmNode>> getStartNodes(void);

    /**
     * @brief get the set of the valid states
     * @return set of valide state
    */
    const std::set<std::shared_ptr<FsmNode>> getValidNodes(void);

    /**
     * @brief get the set of all the node in the graph
     * @return set of all nodes
    */
    const std::set<std::shared_ptr<FsmNode>> getNodes(void);

    /**
     * @brief set a groupe idx for all the nodes in the graph
    */
    void setGroupe(std::size_t groupeIdx);

    /**
     * @brief make the union between this graph and an input graph
     * @param fsmGraph graph to union
    */
    void unionG(const std::shared_ptr<FsmGraph> fsmGraph);


    /**
     * @brief make the union between this graph and an input graph and merge the valid state to the start state
     * @param fsmGraph graph to merge
    */
    void mergeOneStartOneValid(const std::shared_ptr< FsmGraph> fsmGraph);
    /**
     * @brief get the number of sub FSM
     * @return number of sub Fsm
    */
    std::size_t getNbSubFsm(void);

    /**
     * @brief get the number of start state
     * @return number of start state
    */
    std::size_t getNbStart(void);

    /**
     * @brief increment the origin of all nodes in the graph
     * @param incr  value
    */
    void incOriginAllNodeBy(std::size_t incr);

    private:

    /**
     * @brief merge tow node of the graph
     * @param node
    */
    void _mergeNode(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest);

};


}
#endif //AIDGE_CORE_FSM_GRAPH_H_
