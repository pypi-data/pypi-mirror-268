#ifndef AIDGE_CORE_FSM_NODE_H_
#define AIDGE_CORE_FSM_NODE_H_

#include <set>
#include <vector>
#include <memory>

//#include "graphRegex/matchFsm/FsmEdge.hpp"
//#include "graphRegex/matchFsm/FsmRunTimeContext.hpp"

namespace Aidge{
    // Forward declaration of the class defined in graphRegex/matchFsm/FsmEdge.hpp
    class FsmEdge;
    struct EdgeTestResult;
    class FsmRunTimeContext;


    //------------------------------------------------------------------------------

    // MAY BE IN UTILE
    template <typename T>
    struct lex_compare {
        bool operator() (const std::weak_ptr<T> &lhs, const std::weak_ptr<T> &rhs)const {
            auto lptr = lhs.lock(), rptr = rhs.lock();
            if (!rptr) return false; // nothing after expired pointer
            if (!lptr) return true;
            return lptr < rptr;
        }
    };

    /**
     * @brief is a node in the FSM graph, it's a state in the FSM
     * @details a state can be and/or :
     * - a valide state, the match is valide if it stop on this edge
     * - a start state , the match start on this state
     * The state is also define by this Origin (is the unique id of it's expretion )
     * and it's groupe (for inner expression TODO)
    */
    class FsmNode : public std::enable_shared_from_this<FsmNode>
    {
    private:
        /**
         * @brief the edge of the node
         * @details the edge have a shared ref to the node so we use weak ref
        */
        std::set<std::weak_ptr<FsmEdge>,lex_compare<FsmEdge>> mEdges;
        /**
         * @brief the parent of the node
        */
        std::set<std::weak_ptr<FsmNode>,lex_compare<FsmNode>> mParents;

        std::size_t mOriginFsm = 0;
        std::size_t mGroupeFsm = 0;

        bool mIsAValid;
        bool mIsAStart;

    public:
        FsmNode(bool isAValid,bool isAStart );
        virtual ~FsmNode() = default;
        /**
         * @brief use to MAG the actual context , and return all the possible new context
         * @details one input context can generate a multitude of contexts because a graph node
         *  can have more than one child, and each traversal possibility is a new context.
         * @param actContext the actual context
         * @return A vector of all the new context
        */
        const std::vector<std::shared_ptr<FsmRunTimeContext>> test( std::shared_ptr<FsmRunTimeContext>);


        std::size_t getOrigin(void);
        void incOrigin(std::size_t inc);


        void rmEdge(std::shared_ptr<FsmEdge>);
        void addEdge(std::shared_ptr<FsmEdge>);

        //const std::set<std::shared_ptr<FsmNode>> getChildNodes(void);

        const std::set<std::weak_ptr<FsmNode>,lex_compare<FsmNode>>& getParentNodes(void);
        const std::set<std::weak_ptr<FsmEdge>,lex_compare<FsmEdge>>& getEdges(void);

        void setGroupe(std::size_t groupeIdx);

        bool isValid(void);
        bool isStart(void);
        void unValid(void);
        void valid(void);
        void unStart(void);
        void start(void);



        void addParent(std::shared_ptr<FsmNode>);
        void rmParent(std::shared_ptr<FsmNode>);
    };

}
#endif //AIDGE_CORE_FSM_NODE_H_
