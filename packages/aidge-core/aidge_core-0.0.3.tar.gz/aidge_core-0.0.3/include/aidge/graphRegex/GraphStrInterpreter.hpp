#ifndef AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_
#define AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_

#include <sstream>
#include <memory>
#include <algorithm>

#include "aidge/utilsParsing/AstNode.hpp"
#include "aidge/graphRegex/GraphRegexTypes.hpp"
#include "aidge/graphRegex/GraphParser.hpp"
#include "aidge/graphRegex/matchFsm/FsmGraph.hpp"

namespace Aidge {

    class GraphStrInterpreter
    {
    private:
        /* data */
        GraphParser mParser;
        std::string mToTest;
    public:
        GraphStrInterpreter(const std::string graphMatchExpr);
        virtual ~GraphStrInterpreter() =default;


        std::string interpret(void);

        private:


         std::string visit(std::shared_ptr<AstNode<gRegexTokenTypes>> AstTree);
    };



}


#endif //AIDGE_CORE_GRAPH_FSM_INTERPRETER_H_
