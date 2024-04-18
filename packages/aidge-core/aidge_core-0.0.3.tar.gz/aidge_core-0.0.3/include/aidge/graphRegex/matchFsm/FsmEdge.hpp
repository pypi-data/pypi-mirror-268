#ifndef AIDGE_CORE_FSM_EDGE_H_
#define AIDGE_CORE_FSM_EDGE_H_

#include <memory>
#include <set>
#include <string>

#include "aidge/nodeTester/ConditionalInterpreter.hpp"


namespace Aidge{

    class FsmNode;
    class FsmRunTimeContext;

    struct EdgeTestResult {
        bool success;
        std::set<NodePtr> node;
    };

    /**
     * @brief virtual class use test the node  on the node to validate
    */
    class FsmEdge: public std::enable_shared_from_this<FsmEdge>
    {
    private:

        /**
         * @brief the relative position to this test relative to all the const key
         * first is common id, second is the relative position
        */
        std::map<size_t,int> mRelativePos;
        /**
         * @brief the ptr on the source node
        */
        std::shared_ptr<FsmNode> mNodeSource;
        /**
         * @brief the ptr on the dest node
        */
        std::shared_ptr<FsmNode> mNodeDest;
         /**
         * @brief the weak ptr
        */
        std::weak_ptr<FsmEdge> weakPtr;

    public:
        FsmEdge(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest);

        virtual  ~FsmEdge(){};

        FsmEdge() : weakPtr(shared_from_this()) {}


        /**
        *  @brief test is the validation of the node, it must be defined for all types of edge
        * it takes as argument an FSM traversal context and returns a set of next nodes
        *  @return set of next node or nullptr if not next
        */

        virtual const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> stmContext) =0;

        /**
        *  @brief test is the egde test a common node
        *  @return true if is a common
        */
        virtual bool isCommon(void);
        /**
         * @brief get the Common idx of the common test in this edge (if is a common edge)
         * @return idx of the common
        */
        virtual size_t getCommonIdx(void);
        /**
         * @brief get the relative postion to the common node deffine in this edge
         * @return map
        */
        const std::map<size_t,int>& getRelative(void);
        /**
         * @brief add new relative position
        */
        void updateRelative( const std::map<size_t,int>& relativePos );
        /**
         * @brief get source FsmNode
         * @return FsmNode
        */
        std::shared_ptr<FsmNode> getSourceNode(void);
        /**
         * @brief set a new source to the edge
         * @return FsmNode
        */
        void reSetSourceNode(const std::shared_ptr<FsmNode>& newSource);
          /**
         * @brief get dest FsmNode
         * @return FsmNode
        */
        std::shared_ptr<FsmNode> getDestNode(void);
        /**
         * @brief set a new dest to the edge
         * @return FsmNode
        */
        void reSetDestNode(const std::shared_ptr<FsmNode>& newDest);
        /**
         * @brief propagate the edge  mRelativePos to the others Edge and recalcul the relative position
        */
        void propagateRelativePos(void);

         /**
         * @brief test to make on the node to validate
         * @see ConditionalInterpreter
        */
        const std::shared_ptr<ConditionalInterpreter>  mToTest;

         /**
         * @brief update week ptr for the node, TODO best
        */
        void updateWeak(void);
    };

    /**
     * @brief class specialization for not commun node (node that must be match one Unique) transition
    */
    class FsmEdgeUnique:public FsmEdge
    {

        public:
        FsmEdgeUnique(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest);
        const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> stmContext) override;
    };

    /**
     * @brief class specialization for  commun node transition
     * @see FsmEdge
    */
    class FsmEdgeCommon:public FsmEdge
    {

        private:
        /**
         * @brief the map that defind the ralation between the commonKey find by the lexer and a unique id use to refer to the common node
        */
        static std::map<std::string,int> mCommonIdxMap;
        /**
         * @brief the common id test in this transition
        */
        int mCommonIdx;
        public:

        /**
         * @brief constructor  commun node ,
         * @details during construction,
         * the node key found by the lexer is converted to a unique id and the relative positions are updated.
        */
        FsmEdgeCommon(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const std::shared_ptr<ConditionalInterpreter>  toTest, const std::string commonKey);
       // ~FsmEdgeCommon() override {}
        const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> stmContext) override;
        bool isCommon(void) override;

    };



    /**
     * @brief class spesialisation for ref transition
     * @see FsmEdge
    */
    class FsmEdgeRef:public FsmEdge
    {
        private:
        /**
         * @brief the id of one common node that we use as an anchor
        */
        const int mRefCommonIdx;
        /**
         * @brief the delta in terme of child or parent refer to the anchor
        */
        const int mdeltaCommonIdx;
        public:
        FsmEdgeRef(std::shared_ptr<FsmNode>& source,std::shared_ptr<FsmNode>& dest, const size_t refCommonIdx,const int deltaCommonIdx);
        //~FsmEdgeRef() override {}
        const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> stmContext) override;

    };

    /**
     * @brief class specialization for ref empty transition
     * @see FsmEdge
    */
    class FsmEdgeEmpty:public FsmEdge
    {

        public:
        FsmEdgeEmpty(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest);
        //~FsmEdgeEmpty() override {}
        const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> stmContext) override;

    };


    /**
     * @brief class specialization for ref empty transition
     * @see FsmEdge
    */
    class FsmEdgeNone:public FsmEdge
    {

        public:
        FsmEdgeNone(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest);
        const EdgeTestResult test(const std::shared_ptr<FsmRunTimeContext> /*stmContext*/) override;

    };



////////////////////////
// FACTORY
////////////////////////

enum class FsmEdgeTypes {
    EMPTY = 0,
    REF,
    COMMON,
    UNIQUE
};


class FsmEdgeFactory {
    public:
    /**
    * @brief factory for making edge and read the info in the lexeme of the token
    * @param source source node of the edge
    * @param dest Dest node of the edge
    * @param type type of the edge
    * @param lexeme the additional information to build the edge
    * @return s prt of the edge
    */
    static std::shared_ptr<FsmEdge> make(std::shared_ptr<FsmNode> source, std::shared_ptr<FsmNode> dest,
    FsmEdgeTypes type,std::map<std::string, std::shared_ptr<ConditionalInterpreter>> allTest,
    const std::string lexeme = "");
   };

}

#endif //AIDGE_CORE_FSM_EDGE_H_
