#include "aidge/graphRegex/matchFsm/FsmGraph.hpp"

using namespace Aidge;



FsmGraph::FsmGraph(const std::string query):mQuery(query){

}

//TODO
    std::vector<std::shared_ptr<MatchSolution>> FsmGraph::test(const std::vector<NodePtr>& startNodes){
        
    std::vector<std::shared_ptr<Aidge::FsmNode>> startNodesFsm = getStartNodes();
    if(startNodes.size() != startNodesFsm.size()){
         throw std::runtime_error("bad number of Start nodes");
    }

    std::vector<std::shared_ptr<FsmRunTimeContext>> walks;
    for(std::size_t i = 0; i < startNodes.size(); i++){
        walks.push_back(std::make_shared<FsmRunTimeContext>(startNodesFsm[i],startNodes[i]));
    }
    std::vector<std::shared_ptr<FsmRunTimeContext>> nextWalks;

    std::vector<std::shared_ptr<FsmRunTimeContext>> allValidContext;
    std::vector<std::shared_ptr<FsmRunTimeContext>> allContextSee;




    while (!walks.empty())
    {
        for(auto fsmContext : walks){
            allContextSee.push_back(fsmContext);
            //if we are in a valid st we save it
            //it's one solution of the posible solution of the matching
            if(fsmContext->isOnValidState()){
                //not save 2 time the same end point
                if(!std::any_of(allValidContext.begin(), allValidContext.end(),
                    [&](std::shared_ptr<Aidge::FsmRunTimeContext> oldValid) {
                        return fsmContext->areEqual(oldValid);
                })){
                    allValidContext.push_back(fsmContext);
                }

            }

            //dont test 2 time a fsmContext
            std::vector<std::shared_ptr<FsmRunTimeContext>> tmpNextWalks = fsmContext->getActState()->test(fsmContext);
            for(auto PotentialFsmContext : tmpNextWalks){

                if(!std::any_of(allContextSee.begin(), allContextSee.end(),
                    [&](std::shared_ptr<Aidge::FsmRunTimeContext> oldSee) {
                        return PotentialFsmContext->areEqual(oldSee);
                })){
                    nextWalks.push_back(PotentialFsmContext);
                }
            }

        }
        walks.swap(nextWalks);
        nextWalks.clear();
    }
    
    MatchResult allMatch(allValidContext,getNbSubFsm(),mQuery,startNodes);
    return allMatch.getSolutions();

}


///////////////
// FSM construction
///////////////
const std::set<std::shared_ptr<FsmEdge>>& FsmGraph::getEdge(void){
    return mEdges;
}

void FsmGraph::addEdge(std::shared_ptr<FsmEdge>& edge){
    edge->updateWeak();
    mEdges.insert(edge);
    mAllOrigin.insert(edge->getDestNode()->getOrigin());
    mAllOrigin.insert(edge->getSourceNode()->getOrigin());
}

const std::vector<std::shared_ptr<FsmNode>> FsmGraph::getStartNodes(void){
    std::set<std::shared_ptr<FsmNode>> nodes = getNodes();
    std::vector<std::shared_ptr<FsmNode>> startNodes;
    for(auto node :nodes){
        if(node->isStart()){
            startNodes.push_back(node);
        }
    }
    return startNodes;
}

const std::set<std::shared_ptr<FsmNode>> FsmGraph::getValidNodes(void){
    std::set<std::shared_ptr<FsmNode>> nodes = getNodes();
    std::set<std::shared_ptr<FsmNode>> ValidNodes;
    for(auto node :nodes){
        if(node->isValid()){
            ValidNodes.insert(node);
        }
    }
    //may short
    return ValidNodes;
}

const std::set<std::shared_ptr<FsmNode>> FsmGraph::getNodes(void){
    std::set<std::shared_ptr<FsmNode>> nodes;
    for(auto edge : mEdges){
        nodes.insert(edge->getDestNode());
        nodes.insert(edge->getSourceNode());
    }
    return nodes;
}

void FsmGraph::setGroupe(std::size_t groupeIdx){
    std::set<std::shared_ptr<FsmNode>> nodes = getNodes();
    for(auto node :nodes){
        node->setGroupe(groupeIdx);
    }
}

void FsmGraph::unionG(const std::shared_ptr<FsmGraph> fsmGraph){

    for(auto edge : fsmGraph->getEdge()){
        addEdge(edge);
    }
}

void FsmGraph::mergeOneStartOneValid(const std::shared_ptr<FsmGraph> fsmGraph){
    std::set<std::shared_ptr<FsmNode>> validNodes = getValidNodes();
    std::vector<std::shared_ptr<FsmNode>> startNodes = fsmGraph->getStartNodes();

    if (startNodes.size() != 1 || validNodes.size() != 1){

        std::ostringstream errorMessage;
        errorMessage <<"mergeOneStartOneValid  start size: " << startNodes.size() << " valide size : " << validNodes.size()
        <<" can only merge FSM 1 start 1 valide";
        throw std::runtime_error(errorMessage.str());
    }

    unionG(fsmGraph);
    //for loop useless but for future merge it's coudl be used
    for(auto valid : validNodes){
        valid->unValid();
        for(auto start : startNodes){
            start->unStart();
            _mergeNode(start,valid);
        }
    }
}

std::size_t FsmGraph::getNbSubFsm(void){
    return mAllOrigin.size();
}

std::size_t FsmGraph::getNbStart(void){
    return getStartNodes().size();
}

void FsmGraph::incOriginAllNodeBy(std::size_t incr){
    std::set<std::shared_ptr<FsmNode>> nodes = getNodes();
    for(auto node :nodes){
        node->incOrigin(incr);
    }
    std::set<std::size_t> updatedOrigin;
    for(auto origin : mAllOrigin){
        updatedOrigin.insert(origin + incr);
    }
    mAllOrigin.swap(updatedOrigin);
}

void FsmGraph::_mergeNode(std::shared_ptr<FsmNode> source,std::shared_ptr<FsmNode> dest){
    std::set<std::shared_ptr<FsmNode>> nodes = getNodes();

    if(nodes.find(source) == nodes.end() || nodes.find(dest) == nodes.end()){
        throw std::runtime_error("FsmGraph can not merge node not in the graph");
    }
    nodes.clear();

    //probagate source attribut
    if(source->isValid()){
        dest->valid();
    }
    if(source->isStart()){
        dest->start();
    }

    //merge source to dest by replace source by dest in all EDGE
    for(auto edge : mEdges){
        if(edge->getDestNode() == source ){
            edge->reSetDestNode(dest);
        }else if(edge->getSourceNode() == source ){
            edge->reSetSourceNode(dest);
        }

    }
    //check is source is not in graph
    nodes = getNodes();
    if(nodes.find(source) != nodes.end() ){
        throw std::runtime_error("FsmGraph merge node not effective");
    }
    nodes.clear();

}
