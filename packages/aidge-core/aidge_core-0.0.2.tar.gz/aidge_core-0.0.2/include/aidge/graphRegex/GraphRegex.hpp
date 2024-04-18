#ifndef AIDGE_CORE_GRAPH_REGEX_H_
#define AIDGE_CORE_GRAPH_REGEX_H_

#include <string>

#include "aidge/graphRegex/matchFsm/MatchResult.hpp"
#include "aidge/graphRegex/matchFsm/FsmGraph.hpp"
#include "aidge/graphRegex/GraphFsmInterpreter.hpp"
#include "aidge/graph/GraphView.hpp"
#include "aidge/graph/Node.hpp"

namespace Aidge{

/**
 * type for recipes function use in query and resolve  
*/
using RecipesFunctionType = std::function<void(std::shared_ptr<MatchSolution>)>;

/**
 * @brief class which is the hight level interface for graph matching, used to simplify match definition  
 * 
 */
class GraphRegex{

    private:

    //std::vector<std::string> mQuery;
    std::vector<std::shared_ptr<ConditionalInterpreter>> mAllTest;
    std::map<std::string, std::function<bool(NodePtr)>> mAllLambda;
    std::map<std::string,RecipesFunctionType> mQueryRecipe;

    public:
    GraphRegex(){};
    virtual ~GraphRegex() = default;

    /**
     * @brief add a topology query to the match 
     * @param query the topology query to find 
    **/
    //void addQuery(const std::string query);

    /**
     * @brief add a topology query to the match and a function for recipe 
     * @param query the topology query to find 
     * @param f the funct 
    **/
    void addQuery(const std::string query,RecipesFunctionType f = nullptr);
   
   
   /**
     * @brief get all the types of a graph and set it as type key in the query 
     * @param Reference graph use to get all the node types 
    **/
    void setKeyFromGraph(std::shared_ptr<GraphView> ref);

   /**
     * @brief set a node test manually 
     * @param key the ref of this test used in the query
     * @param ConditionalExpressions expression to test the node 
    **/
    void setNodeKey(const std::string key, const std::string conditionalExpressions );

    /**
     * @brief set a specific lambda that can be used in setQueryKey
     * @param key ref to the lambda to use in the 
     * @param f expression to test the node ConditionalExpressions
    **/
    void setNodeKey(const std::string key,std::function<bool(NodePtr)> f);

    /**
     *  @brief brief match the queries in the graph 
     *  @param ref the graph were the querys in search 
     *  @return the result  
    */
    std::set<std::shared_ptr<MatchSolution>> match(std::shared_ptr<GraphView> ref);

    /***
     *  @brief  match the queries in the graph and applied the recipes fuction  
     *  @param ref the graph were the querys in search 
    */
    void appliedRecipes(std::shared_ptr<GraphView> ref);

    private:

    void _generateCombinationsStart(const std::set<NodePtr>& elements, std::size_t n, std::size_t index, 
    std::vector<NodePtr>& current, std::set<std::vector<NodePtr>>& combinations);
 


  void _findLargestCompatibleSet(
      const std::vector<std::shared_ptr<MatchSolution>>& solutions,
      std::set<std::shared_ptr<MatchSolution>>& currentSet,
      std::set<std::shared_ptr<MatchSolution>>& largestSet,
      size_t currentIndex
  );

  std::set<std::shared_ptr<MatchSolution>> _findLargestCompatibleSet(
      const std::vector<std::shared_ptr<MatchSolution>>& solutions
  );

  void _majConditionalInterpreterLambda();

};
}


#endif //AIDGE_CORE_GRAPH_REGEX_H_