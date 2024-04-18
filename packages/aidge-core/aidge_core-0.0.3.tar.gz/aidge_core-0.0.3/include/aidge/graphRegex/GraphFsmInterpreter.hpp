#ifndef AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_
#define AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_

#include <string>
#include <memory>

#include "aidge/utilsParsing/AstNode.hpp"
#include "aidge/graphRegex/GraphRegexTypes.hpp"
#include "aidge/graphRegex/GraphParser.hpp"
#include "aidge/graphRegex/matchFsm/FsmGraph.hpp"

namespace Aidge {

    class GraphFsmInterpreter
    {
    private:
        /* data */
        GraphParser mParser;
        std::size_t mActGroupe;
        std::map<std::string,std::shared_ptr<ConditionalInterpreter>> mNodesCondition;

        const std::string mGraphMatchExpr;
    public:
        GraphFsmInterpreter(const std::string graphMatchExpr,std::vector<std::shared_ptr<ConditionalInterpreter>> & nodesCondition);
        virtual ~GraphFsmInterpreter() =default;


        std::shared_ptr<FsmGraph>  interpret(void);

        

        private:


        std::shared_ptr<FsmGraph> visit(std::shared_ptr<AstNode<gRegexTokenTypes>> AstTree);

        /**
         * @defgroup graphFsmInterpreterF Functions for interpreting AST nodes
         * @brief For each node type in the AST, define how build the FsmGraph
         */


        /**
         * @ingroup graphFsmInterpreterF
         * @brief leaf of fsm make the fsm for test one transition
         */
        std::shared_ptr<FsmGraph> keyF(std::shared_ptr<AstNode<gRegexTokenTypes>> AstNode);
        /**
         * @ingroup graphFsmInterpreterF
         * @brief combine two fsm of two expression.
         */
        std::shared_ptr<FsmGraph> sepF(std::shared_ptr<FsmGraph> leftFsm,std::shared_ptr<FsmGraph> rigthFsm);
        /**
         * @ingroup graphFsmInterpreterF
         * @brief combine two to make a new that match leftFsm next rigthFsm
         */
        std::shared_ptr<FsmGraph> nextF(std::shared_ptr<FsmGraph> leftFsm,std::shared_ptr<FsmGraph> rigthFsm);
        /**
         * @ingroup graphFsmInterpreterF
         * @brief make the fsm match +
         */
        std::shared_ptr<FsmGraph> qomF(std::shared_ptr<FsmGraph> fsm);
        /**
         * @ingroup graphFsmInterpreterF
         * @brief  make the fsm match *
         */
        std::shared_ptr<FsmGraph> qzmF(std::shared_ptr<FsmGraph> fsm);

    };



}


#endif // AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_
