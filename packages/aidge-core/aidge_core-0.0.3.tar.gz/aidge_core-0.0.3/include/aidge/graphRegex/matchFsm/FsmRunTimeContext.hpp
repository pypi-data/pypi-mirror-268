#ifndef AIDGE_CORE_FSM_RUN_TIME_CONTEXT_H_
#define AIDGE_CORE_FSM_RUN_TIME_CONTEXT_H_

#include <memory>
#include <vector>
#include <set>
#include <algorithm>

#include "aidge/nodeTester/ConditionalInterpreter.hpp"
#include "aidge/graph/Node.hpp"


namespace Aidge{

class FsmNode;

/**
 * @brief a class used to save the execution context of state machines, that is the actual state in the FSM, the actual node in the graph
 * all node that have been Validate,Rejecte or Considered common
*/
class FsmRunTimeContext
{
private:
    /**
     * @brief the list of node rejected for all the context
    */
    static std::vector<std::set<NodePtr>> mRejectedNodes;
    /**
     * @brief the actual state of this Context (where it's in the FSM graph)
    */
    std::shared_ptr<FsmNode> mActState;
    /**
     * @brief the actual node of this Context (where it's in the graph)
    */
    NodePtr mActOpNode;
    /**
     * @brief the map of the node consider as common and the common ID
     * @details we need to store what node it's consider as common because of the end
     * resolution of the matching, all node consider as common need to be the same in all context
    */
    std::map<NodePtr,std::size_t> mCommonNodes;
    /**
     * @brief the map of the node that as been valid in this context , and the test that valide the node
    */
    std::map<std::shared_ptr<ConditionalInterpreter>,std::set<NodePtr>> mValidNodes;
    /**
     * @brief the index in the rejected node of this context
    */
    std::size_t mLocalIdxRejeced;
public:
    /**
     * @brief constructor
     * @param actState the actual state in the FSM
     * @param actOpNode the actual node in the graph
     * @param idxRejeced the idx in the global regected node vector init max() as sentinel value of undefind
    */
    FsmRunTimeContext(std::shared_ptr<FsmNode> actState ,NodePtr actOpNode ,std::size_t idxRejeced =std::numeric_limits<std::size_t>::max() );
    FsmRunTimeContext(std::shared_ptr<FsmRunTimeContext> fsmRunTime);
    FsmRunTimeContext(std::shared_ptr<FsmRunTimeContext> fsmRunTime,std::shared_ptr<FsmNode> actState ,NodePtr actOpNode );

    virtual ~FsmRunTimeContext()=default;

    /**
     * @defgroup FsmRunTimeContextRejected Function for managing rejected nodes
     */

    /**
     * @ingroup FsmRunTimeContextRejected
     * @brief Add a node as rejected in this context
     */
    void addRejectedNode(NodePtr node);

    /**
     * @ingroup FsmRunTimeContextRejected
     * @brief get the rejected nodes of this context
     */
    inline std::set<NodePtr> getRejectedNodes(void) const {
        return mRejectedNodes[mLocalIdxRejeced];
    }


    /**
     * @defgroup FsmRunTimeContextTest Function for test the context
     */

    /**
     * @ingroup FsmRunTimeContextTest
     * @brief test if the actual state is valide
     * @return bool
     */
    bool isOnValidState(void);
    /**
     * @ingroup FsmRunTimeContextTest
     * @brief test if the node is considered as common in this context
     * @param node node to test
     * @return bool
     */
    bool isCommonDefined(NodePtr node);
    /**
     * @ingroup FsmRunTimeContextTest
     * @brief test if has already validated in this context
     * @param node node to test
     * @return bool
     */
    bool isAlreadyValid(NodePtr node);
    /**
     * @ingroup FsmRunTimeContextTest
     * @brief test if this context is compatible with an others
     * @details to say that two contexts are compatible is to check :
     *  that the contexts do not validate the same nodes (other than the common ones)
     *  and that the common ones have the same idx
     * @param fsmContext the others context
     * @return bool
     */
    bool areCompatible(std::shared_ptr<FsmRunTimeContext> fsmContext);
    /**
     * @ingroup FsmRunTimeContextTest
     * @brief test if this context is strictly equal with an others
     * @param fsmContext the others context
     * @return bool
     */
    bool areEqual(std::shared_ptr<FsmRunTimeContext> fsmContext);

    /**
     * @defgroup FsmRunTimeContextSet Function set context
    */


    void setCommon(NodePtr node,std::size_t commonIdx);


    void setValid(NodePtr node,std::shared_ptr<ConditionalInterpreter> tag);

    /**
     * @defgroup FsmRunTimeContextGet Function get context
     */


    /**
     * @ingroup FsmRunTimeContextGet
     * @brief get the sub idx state
     * @return bool
     */
    std::size_t getSubStmId(void);

    NodePtr getCommonNodeFromIdx(std::size_t commonIdx);
    std::size_t getCommonNodeIdx(NodePtr node);
    std::set<NodePtr> getCommonNodes(void);

    std::map<NodePtr,std::size_t> getCommon(void);
    std::set<NodePtr> getValidNodes(void);

    std::set<NodePtr> getValidNodesNoCommon(void);
    std::map<std::shared_ptr<ConditionalInterpreter>,std::set<NodePtr>>& getValid(void);


    NodePtr getActNode(void);
    std::shared_ptr<FsmNode> getActState(void);


    /**
     * @defgroup FsmRunTimeContextMem
     */

    void rst(void);


};
} // namespace Aidge

#endif // AIDGE_CORE_FSM_RUN_TIME_CONTEXT_H_
