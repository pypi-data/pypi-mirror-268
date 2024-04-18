

#ifndef AIDGE_CORE_CONDITIONAL_INTERPRETER_H_
#define AIDGE_CORE_CONDITIONAL_INTERPRETER_H_

#include "aidge/nodeTester/ConditionalParser.hpp"
#include "aidge/nodeTester/ConditionalData.hpp"

#include <memory> // for shared_ptr
#include <unordered_map>
#include <functional>
#include "aidge/graph/Node.hpp"
#include <sstream>


namespace Aidge{



//////////////////////////////
//
/////////////////////////////
/**
 * @brief class used to register any lambda function without context,
 * it encapsulates the source lambda in a lambda which takes as argument  std::shared_ptr<ConditionalData> which are any type.
 * @see ConditionalData
 */
class ConditionalRegisterFunction {
    //////////////////////////
    //Safe recaste
    //////////////////////////

    /**
     * @brief recast the  std::shared_ptr<ConditionalData> to the argument type of the lambda
     * @tparam T type of the lambda argument
     * @see ConditionalData
     */
    template <typename T>
    T safeCastInput( std::shared_ptr<ConditionalData> data) {
        //cnvertion and type cheking
        if (data->isTypeEqualTo<T>()){
            return data->getValue<T>();
        }else{
            throw std::invalid_argument( "incompatible input type " + data->getType() +" "+ typeid(T).name() );
        }

    }


    /**
     * @brief recaste the output of the lambda to a   std::shared_ptr<ConditionalData>
     * @tparam T type of the lambda return
     * @see ConditionalData
     */
    template <typename T>
     std::shared_ptr<ConditionalData> safeCastOutput(T data) {

        std::shared_ptr<ConditionalData> out = std::make_shared<ConditionalData>();
        out->setValue<T>(data);

        return out;
    }




    //////////////////////
    // get all the type of the function
    //////////////////////

    /**
     * @brief Retrieves information about a function's return type and argument types.
     * @tparam T The function type.
     */
    template <typename T>
    struct function_traits;


    /**
     * @brief Specialization of function_traits for function pointers.
     * @tparam R The return type of the function.
     * @tparam Args The argument types of the function.
     */
    template <typename R, typename... Args>
    struct function_traits<R (*)(Args...)> {
        using return_type = R;
        static constexpr std::size_t arity = sizeof...(Args);

        template <std::size_t N>
        struct argument {
            static_assert(N < arity, "Index out of range.");
            using type = typename std::tuple_element<N, std::tuple<Args...>>::type;
        };
    };

    /**
     * @brief Specialization of function_traits for std::function types.
     * @tparam R The return type of the function.
     * @tparam Args The argument types of the function.
     */
    template <typename R, typename... Args>
    struct function_traits<std::function<R(Args...)>> {
        using return_type = R;
        static constexpr std::size_t arity = sizeof...(Args);

        template <std::size_t N>
        struct argument {
            static_assert(N < arity, "Index out of range.");
            using type = typename std::tuple_element<N, std::tuple<Args...>>::type;
        };
    };

    /////////////////////
    //change the function to  std::shared_ptr<ConditionalData>(std::vector< std::shared_ptr<ConditionalData>>)
    /////////////////////

    /**
     * @brief Converts a function to a  std::shared_ptr<ConditionalData>(std::vector< std::shared_ptr<ConditionalData>>).
     * @tparam F The type of the function to convert.
     * @tparam ParamsIdx The indices of the function parameters.
     * @param f The function to convert.
     * @return The pointer to the converted function.
     */
    template <class F, std::size_t... ParamsIdx>
    auto funcPointer(F f, std::index_sequence<ParamsIdx...>) {
        //wrapp the lambda in a new one that as ConditionalData as inputs and output
    	return [this,f](std::vector< std::shared_ptr<ConditionalData>>  &args) {
            if (args.size() < sizeof...(ParamsIdx)){
                std::ostringstream errorMessage;
                errorMessage << "bad Number of argument: get " << args.size() << " need " << sizeof...(ParamsIdx) << "\n";
                throw std::runtime_error(errorMessage.str());
            }
    		//we used std::vector< std::shared_ptr<ConditionalData>> as a fifo 
            std::size_t offset = args.size()-sizeof...(ParamsIdx);

    		using FuncTraits = function_traits<decltype(f)>;
    		using outType = typename FuncTraits::return_type;

    		outType result = f(safeCastInput<typename FuncTraits::template argument<ParamsIdx>::type>(args[offset+ParamsIdx])...);

            //suppress what we used
            for (size_t i = 0; i < sizeof...(ParamsIdx); ++i) {
                args.pop_back();
            }
    		//typename
    		return safeCastOutput<outType>(result);
    	};
    }

    /**
     * @brief Converts a function pointer to a  std::shared_ptr<ConditionalData>(std::vector< std::shared_ptr<ConditionalData>>).
     * @tparam R The return type of the function.
     * @tparam Params The parameter types of the function.
     * @param f The function pointer to convert.
     * @return The pointer to the converted function.
     */
    template <class R,class... Params>
    auto funcPointer(R (*f)(Params...)) {
    	return funcPointer(f, std::index_sequence_for<Params...>{});
    }

    /**
     * @brief Converts a std::function to a  std::shared_ptr<ConditionalData>(std::vector< std::shared_ptr<ConditionalData>>).
     * @tparam R The return type of the function.
     * @tparam Params The parameter types of the function.
     * @param f The function pointer to convert.
     * @return The pointer to the converted function.
     */
    template <class R,class... Params>
    auto funcPointer(std::function<R(Params...)> f) {
    	return funcPointer(f, std::index_sequence_for<Params...>{});
    }


    ///////////////////
    // interface
    ///////////////////

    public:

     /**
     * @brief Default constructor
     */
    ConditionalRegisterFunction(){}


     /**
     * @brief Inserts a function into the map with the provided key.
     * @tparam T The function type.
     * @param key The key to associate with the function.
     * @param f The function to insert.
     */
    template <class T>
    void insert(const std::string key,T f){
        mWlambda.insert({ key, funcPointer(f)});
    }


     /**
     * @brief Runs the function associated with the given key, using the provided vector of input data.
     * @param key The key of the function to run.
     * @param datas The vector of input data.
     * @return A pointer to the output ConditionalData object.
     */
     std::shared_ptr<ConditionalData> run(const std::string key,std::vector< std::shared_ptr<ConditionalData>> & datas);

    bool isLambdaRegister(const std::string &key) {
        if(mWlambda.find(key) != mWlambda.end()){
            return true;
        }
        return false;
    }

    private:
    /// @brief map of name and the converted function.
    std::map<const std::string, std::function< std::shared_ptr<ConditionalData>(std::vector< std::shared_ptr<ConditionalData>>  &)>> mWlambda;
};

///////////////////
//AST tree node
// ////////////////
/**
 * @brief this class interprets AST to generate a test on a graph node. For each AST node,
 * it generates an interpretation and registers lambda functions that can be used in the test expression.
 * there are two lambda control mechanisms:
 * - A cpp mechanism which allows any lambda to be inserted into the constructor that use templaite
 * - A user mechanism limited to lambda bool(NodePtr)
 * @see ConditionalParser use to get the AST
 */
class ConditionalInterpreter
{
    private:

    /**
     * @brief the AST generate by the Parser
     * @see ConditionalParser
     */
    std::shared_ptr<AstNode<ConditionalTokenTypes>> mTree;
    /**
     * @brief the registery for the lambda fuction
     * @see ConditionalRegisterFunction
    */
    ConditionalRegisterFunction mLambdaRegister;


    std::vector< std::shared_ptr<ConditionalData>> mResolution ;

    // void clearRes(){

    //     for (std::size_t i = 0; i < mResolution.size(); ++i) {
    //         delete mResolution[i];
    //     }
    //     mResolution.clear();
    // }

    public:

    const std::string mKey;

    /**
     * @brief Constructor
     * @param ConditionalExpressions The expression of the test to be performed on the nodes
     */

    ConditionalInterpreter(const std::string key,const std::string ConditionalExpressions);

    ~ConditionalInterpreter(){}

     /**
     * @brief get the condition key
     * @return the key
    */

    const std::string& getKey();

    /**
     * @brief Test a node depending of the ConditionalExpressions
     * @details the AST is visit using \ref visit() whith the $ init whit the nodeOp
     * @return bool the match node has the initialized expresion
     * @see visit() This function uses the visit() function to perform the evaluation.
     */
    bool test( const NodePtr nodeOp);

    /**
     * @brief Interface for inserting custom lambda bool(NodePtr) functions in AST interpretation,
     *         it will be available in the ConditionalExpressions expretion as : key($)
     * @param key The key that will be used to call the function in the expression
     * @param f The pointer to function
     */
    void insertLambda(const std::string key,std::function<bool(Aidge::NodePtr)> f);

    bool isLambdaRegister(const std::string &key);
    /////

    private:
    /**
     * @brief Recursive AST traversal function, using the for interpreting AST nodes function,
     * using \ref ASTnodeInterpreterF fuctions
     * @param NodeOp The node currently being tested
     * @param nodes The AST given by the parsing process
     */
    std::vector< std::shared_ptr<ConditionalData>> visit(const ASTNodeCh& nodes, const NodePtr NodeOp );

    /**
     * @defgroup ASTnodeInterpreterF Functions for interpreting AST nodes
     * @brief For each node type in the AST, function defines the processing to be performed
     *          they return a  std::vector< std::shared_ptr<ConditionalData>> which corresponds to the value(s) obtained
     */

    /**
     * @ingroup ASTnodeInterpreterF
     * @brief Function that does something.
     */
    void fLambda(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node);
    /**
     * @ingroup ASTnodeInterpreterF
     * @brief Converted the lexeme to a int and to  std::shared_ptr<ConditionalData>
     */
    void fStrToInteger(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node);
    /**
     * @ingroup ASTnodeInterpreterF
     * @brief Converted the lexeme to a float and to  std::shared_ptr<ConditionalData>
     */
    void fStrToFloat(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node);
    /**
     * @ingroup ASTnodeInterpreterF
     * @brief Converted the lexeme to a str and to  std::shared_ptr<ConditionalData>
     */
    void fStrToStr(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node);

    /**
     * @ingroup ASTnodeInterpreterF
     * @brief makes the == operation between two previously converted  std::shared_ptr<ConditionalData>
     */
    void fEq(void);
       /**
     * @ingroup ASTnodeInterpreterF
     * @brief makes the != operation between two previously converted  std::shared_ptr<ConditionalData>
     */
    void fNeq(void);
    /**
     * @ingroup ASTnodeInterpreterF
     * @brief makes the && operation between two previously converted  std::shared_ptr<ConditionalData> in bool
     */
    void fAnd(void);
        /**
     * @ingroup ASTnodeInterpreterF
     * @brief makes the || operation between two previously converted  std::shared_ptr<ConditionalData> in bool
     */
    void fOr(void);

    /**
     * @ingroup ASTnodeInterpreterF
     * @brief makes the ! operation
     */
    void fNot(void);
};


}

#endif //AIDGE_CORE_CONDITIONAL_INTERPRETER_H_
