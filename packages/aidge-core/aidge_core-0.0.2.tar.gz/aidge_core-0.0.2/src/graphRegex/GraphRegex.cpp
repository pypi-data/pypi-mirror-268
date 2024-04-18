#include "aidge/graphRegex/GraphRegex.hpp"
using namespace Aidge;


void GraphRegex::setKeyFromGraph(std::shared_ptr<GraphView> ref){

    for (const NodePtr& node : ref->getNodes()) {
        std::string type =  node->type();
        bool isIn = false;
        for(const auto &test:mAllTest){
            if(test->getKey() == type){
                isIn = true;
                break;
            }
        }
        if(!isIn){
             mAllTest.push_back(std::make_shared<ConditionalInterpreter>(type,"getType($) =='" + type + "'"));
        }
        // auto it = mAllTest.find(type);
        // if (it == mAllTest.end()) {
        //    mAllTest[type] = std::make_shared<ConditionalInterpreter>(type,"getType($) =='" + type + "'");
        // }
        // //if the key exist it's ok, but not make 2 ConditionalInterpreter
    }
}



// void GraphRegex::addQuery(const std::string query){
//     //TODO one query only but the same string is a same query but
//     //2 different string it's maybe the same query , we need to check the AST
//     mQueryRecipe[query] = nullptr;
// }

void GraphRegex::addQuery(const std::string query,RecipesFunctionType f ){

    mQueryRecipe[query] = f;

}


// Function to generate all combinations of n elements from a set
void GraphRegex::_generateCombinationsStart(const std::set<NodePtr>& elements, std::size_t n, std::size_t index, std::vector<NodePtr>& current, std::set<std::vector<NodePtr>>& combinations) {
    if (n == 0) {
        combinations.insert(current);
        return;
    }
    for (auto it = elements.begin(); it != elements.end(); ++it) {
        current.push_back(*it);
        _generateCombinationsStart(elements, n - 1, index + 1, current, combinations);
        current.pop_back();
    }
}

// factorial(n) tree searched optimized with a stopping condition
void GraphRegex::_findLargestCompatibleSet(
    const std::vector<std::shared_ptr<MatchSolution>>& solutions,
    std::set<std::shared_ptr<MatchSolution>>& currentSet,
    std::set<std::shared_ptr<MatchSolution>>& largestSet,
    size_t currentIndex
) {
    if (currentIndex >= solutions.size()) {
        if (currentSet.size() > largestSet.size()) {
            largestSet = currentSet;
        }
        return;
    }

    for (size_t i = currentIndex; i < solutions.size(); ++i) {
        if (std::all_of(currentSet.begin(), currentSet.end(),
            [&](const std::shared_ptr<MatchSolution>& solution) {
                return solution->areCompatible(solutions[i]);
            }
        )) {
            currentSet.insert(solutions[i]);
            _findLargestCompatibleSet(solutions, currentSet, largestSet, i + 1);
            currentSet.erase(solutions[i]);
            // cut the size of the graph of possibilities
            if ((currentSet.size() + solutions.size() - currentIndex) <= largestSet.size()) {
                return;
            }
        }
    }
}

std::set<std::shared_ptr<MatchSolution>> GraphRegex::_findLargestCompatibleSet(
    const std::vector<std::shared_ptr<MatchSolution>>& solutions
) {
    std::set<std::shared_ptr<MatchSolution>> largestSet;
    std::set<std::shared_ptr<MatchSolution>> currentSet;
    _findLargestCompatibleSet(solutions, currentSet, largestSet, 0);
    return largestSet;
}



std::set<std::shared_ptr<MatchSolution>> GraphRegex::match(std::shared_ptr<GraphView> ref){

    std::vector<std::shared_ptr<MatchSolution>> solutions = {};

    //for (const std::string& query : mQuery) {
    for (auto it = mQueryRecipe.begin(); it != mQueryRecipe.end(); ++it) {
        const std::string query  = it->first;

        std::shared_ptr<GraphFsmInterpreter>  fsmGenerator = std::make_shared<GraphFsmInterpreter>(query,mAllTest);
        std::shared_ptr<FsmGraph> fsm = fsmGenerator->interpret();

        // generate all the start possibility
        std::size_t nb_startSt =  fsm->getNbStart();
        std::set<std::vector<NodePtr>> combinations;
        std::vector<NodePtr> current;
        _generateCombinationsStart(ref->getNodes(), nb_startSt, 0, current, combinations);


        // all start
        for (const auto& combination : combinations) {
            std::vector<std::shared_ptr<MatchSolution>> solution = fsm->test(combination);
            solutions.insert(solutions.end(), solution.begin(), solution.end());
        }


    }
    return _findLargestCompatibleSet(solutions);
}

void GraphRegex::appliedRecipes(std::shared_ptr<GraphView> ref){
    std::set<std::shared_ptr<MatchSolution>> matchRef  = match(ref);
    for (const auto& solution : matchRef) {
        if(mQueryRecipe[solution->getQuery()] != nullptr){
            mQueryRecipe[solution->getQuery()](solution);
        }
    }
}

void GraphRegex::setNodeKey(const std::string key, const std::string conditionalExpressions ){
    mAllTest.push_back(std::make_shared<ConditionalInterpreter>(key,conditionalExpressions));
    _majConditionalInterpreterLambda();
}


void GraphRegex::setNodeKey(const std::string key,std::function<bool(NodePtr)> f){
    //we can applied to all key but it's not efficient
    if(mAllLambda.find(key) != mAllLambda.end()){
        throw std::runtime_error(key + " is define");
    }
    mAllLambda[key] = f;
    
    _majConditionalInterpreterLambda();
    //we add the lambda as key by default 
    setNodeKey(key, key + "($)==true");
}

void GraphRegex::_majConditionalInterpreterLambda(){

    for (const auto& test : mAllTest) {
        for (const auto& pair : mAllLambda) {
            const std::string& key = pair.first;
            const std::function<bool(NodePtr)>& lambda = pair.second;

            if(!test->isLambdaRegister(key)){
                test->insertLambda(key,lambda);
            }

        }
    }
}

