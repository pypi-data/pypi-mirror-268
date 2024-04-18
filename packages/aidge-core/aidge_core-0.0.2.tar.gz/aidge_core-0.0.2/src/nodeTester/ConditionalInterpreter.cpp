
#include "aidge/nodeTester/ConditionalInterpreter.hpp"

using namespace Aidge;


///////////////////////////////
//ConditionalRegisterFunction
///////////////////////////////

     std::shared_ptr<ConditionalData> ConditionalRegisterFunction::run(const std::string key,std::vector< std::shared_ptr<ConditionalData>> & datas){

        auto lambdaIt = mWlambda.find(key);
        if (lambdaIt != mWlambda.end()) {
            return lambdaIt->second(datas);
        }else {
            throw std::runtime_error("can not run Lambda due to invalid key: " + key);
        }
    }


//////////////////////
//ConditionalInterpreter
///////////////////////
    ConditionalInterpreter::ConditionalInterpreter(const std::string key,const std::string ConditionalExpressions)
    :mLambdaRegister(),mKey(key)
    {

        ConditionalParser conditionalParser = ConditionalParser(ConditionalExpressions);
        mTree = conditionalParser.parse();
        
        ///lambda by default
        mLambdaRegister.insert("getType",+[](NodePtr NodeOp){return NodeOp->type();});

    }
    
    bool ConditionalInterpreter::isLambdaRegister(const std::string &key){
        return mLambdaRegister.isLambdaRegister(key);
    }
    
    const std::string& ConditionalInterpreter::getKey(){
        return mKey;
    }


    bool ConditionalInterpreter::test( const NodePtr nodeOp)
    {
        mResolution.clear();
        try{
            std::vector< std::shared_ptr<ConditionalData>> r =  visit({mTree},nodeOp);
   
            if (mResolution.size() != 1){
                throw std::runtime_error("Multi output interpretation output");
            }else{
                if (!mResolution[0]->isTypeEqualTo<bool>()){
                    throw std::runtime_error("TEST OUT MUST BE A BOOL ");
                }else{
                    return mResolution[0]->getValue<bool>();
                }
            }

        }catch(const std::exception& e){
            std::ostringstream errorMessage;
            errorMessage << "Error in test " << "\n\t" << e.what()  << "\n";
            throw std::runtime_error(errorMessage.str());
        }
    }

    void ConditionalInterpreter::insertLambda(const std::string key,std::function<bool(Aidge::NodePtr)> f){
        mLambdaRegister.insert<std::function<bool(Aidge::NodePtr)> >(key, f);
    }

    /////
    std::vector< std::shared_ptr<ConditionalData>> ConditionalInterpreter::visit(const ASTNodeCh& nodes, const NodePtr nodeOp ){
            std::vector< std::shared_ptr<ConditionalData>> dataVector;

            for ( std::shared_ptr<AstNode<ConditionalTokenTypes>> node : nodes) {
                try{
                    switch (node->getType()){
                        ///////////////////////////////////
                        //OPERATOR
                        ///////////////////////////////////
                        case ConditionalTokenTypes::NOT:
                            {
                            visit(node->getChilds(),nodeOp);
                            fNot();
                            }
                            break;
                        case ConditionalTokenTypes::AND:
                            {
                            visit(node->getChilds(),nodeOp);
                            fAnd();
                            }
                            break;
                        case ConditionalTokenTypes::OR:
                            {
                            visit(node->getChilds(),nodeOp);
                            fOr();
                            }
                            break;
                        case ConditionalTokenTypes::EQ:
                            {
                            visit(node->getChilds(),nodeOp);
                            fEq();
                            //dataVector.insert(dataVector.end(), tmp.begin(), tmp.end());
                            }
                            break;
                        case ConditionalTokenTypes::NEQ:
                            {
                            visit(node->getChilds(),nodeOp);
                            fNeq();
                            }
                            break;

                        ///////////////////////////////////
                        //VALUE
                        ///////////////////////////////////

                        case ConditionalTokenTypes::KEY:

                            break;
                        case ConditionalTokenTypes::INTEGER:
                            {
                                fStrToInteger(node);
                            }
                            break;
                        case ConditionalTokenTypes::FLOAT:
                            {
                                fStrToFloat(node);

                            }
                            break;
                        case ConditionalTokenTypes::STRING:
                            {
                                fStrToStr(node);
                            }
                            break;

                        case ConditionalTokenTypes::NODE: //TODO
                            {

                                std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
                                data->setValue<NodePtr>(nodeOp);
                                mResolution.push_back(data);

                            }
                            break;

                        case ConditionalTokenTypes::LAMBDA:
                            {
                                visit(node->getChilds(),nodeOp);
                                fLambda(node);

                            }
                            break;

                        case ConditionalTokenTypes::BOOL: //TODO
                            {
                             std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();

                            if(node->getValue() == "true"){
                                data->setValue<bool>(true);
                            }else{
                                data->setValue<bool>(false);
                            }

                            mResolution.push_back(data);

                            }
                            break;

                        case ConditionalTokenTypes::ARGSEP:
                        case ConditionalTokenTypes::LPAREN:
                        case ConditionalTokenTypes::RPAREN:
                        case ConditionalTokenTypes::STOP:
                        default:
                            throw std::runtime_error("NODE TYPE NOT SUPORTED IN ConditionalInterpreter");
                    }
                }catch(const std::exception& e){
                    std::ostringstream errorMessage;
                    errorMessage << "Error in visiting AST for node "<< nodeOp->name() << "\n\t" << e.what()  << "\n";
                    throw std::runtime_error(errorMessage.str()); 
                }
            }

            return dataVector;
    }


    //////////////////////
    //value convertor
    /////////////////////


    void ConditionalInterpreter::fStrToInteger(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node)
    {
         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();

        data->setValue<int>(std::stoi(node->getValue()));
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fStrToFloat(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node)
    {

         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
        data->setValue<float>(std::stof(node->getValue()));
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fStrToStr(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node)
    {
         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
        data->setValue<std::string>(node->getValue());
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fLambda(const std::shared_ptr<AstNode<ConditionalTokenTypes>>& node)
    {
        //if the lambda have input
         std::shared_ptr<ConditionalData> data;
        try {
            data = mLambdaRegister.run(node->getValue(),mResolution);
        } catch (const std::exception& e) {
            std::ostringstream errorMessage;
            errorMessage << "Error in conditional interpretation when run the "<<  node->getValue() <<" Lambda\n\t" << e.what()  << "\n";
            throw std::runtime_error(errorMessage.str());
        }

        //clearRes();
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fEq(void)
    {
        if (mResolution.size() < 2){
            throw std::runtime_error("EQ need 2 arg and get :" + std::to_string(mResolution.size()));
        }
        auto a = mResolution.back(); 
        mResolution.pop_back();
        auto b = mResolution.back(); 
 	    mResolution.pop_back();
     

        if (a->getType() != b->getType()){
            throw std::runtime_error("EQ Unsupported between type :" + a->getType() +" "+ b->getType());
        }



         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();

        if (a->isTypeEqualTo<int>()) {
           data->setValue<bool>( a->getValue<int>() == b->getValue<int>());
        }else if (a->isTypeEqualTo<float>()){
           data->setValue<bool>( a->getValue<float>() == b->getValue<float>());
        }else if (a->isTypeEqualTo<std::string>()){
           data->setValue<bool>( a->getValue<std::string>() == b->getValue<std::string>());
        }else if (a->isTypeEqualTo<bool>()){
           data->setValue<bool>( a->getValue<bool>() == b->getValue<bool>());
        }else{
           throw std::runtime_error("EQ Unknown type encountered :" + a->getType() );
        }

        
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fNeq(void)
    {
        if (mResolution.size() < 2){
             throw std::runtime_error("NEQ need 2 arg and get :" + std::to_string(mResolution.size()));
        }
        auto a = mResolution.back(); 
 	    mResolution.pop_back();
        auto b = mResolution.back(); 
 	    mResolution.pop_back();

        if (a->getType() != b->getType()){
            throw std::runtime_error("NEQ Unsupported between type :" + a->getType() +" "+ b->getType());
        }

         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();

        if (a->isTypeEqualTo<int>()) {
           data->setValue<bool>( a->getValue<int>() != b->getValue<int>());
        }else if (a->isTypeEqualTo<float>()){
           data->setValue<bool>( a->getValue<float>() != b->getValue<float>());
        }else if (a->isTypeEqualTo<std::string>()){
           data->setValue<bool>( a->getValue<std::string>() != b->getValue<std::string>());
        }else
        {
           throw std::runtime_error("NEQ Unknown type encountered :" + a->getType() );
        }

        
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fAnd(void)
    {
        if (mResolution.size() < 2){
           throw std::runtime_error("AND need 2 arg and get :" + std::to_string(mResolution.size()));
        }
        auto a = mResolution.back(); 
 	    mResolution.pop_back();
        auto b = mResolution.back(); 
 	    mResolution.pop_back();


        if (a->getType() != typeid(bool).name() || b->getType() != typeid(bool).name()){
            throw std::runtime_error("AND Unknown type encountered need bool get :" + a->getType() );
        }

         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
        data->setValue<bool>( a->getValue<bool>() && b->getValue<bool>());


        
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fOr(void)
    {
        if (mResolution.size() < 2){
             throw std::runtime_error("OR need 2 arg and get :" + std::to_string(mResolution.size()));
        }
        auto a = mResolution.back(); 
 	    mResolution.pop_back();
        auto b = mResolution.back(); 
 	    mResolution.pop_back();


        if (a->getType() != typeid(bool).name() || b->getType() != typeid(bool).name()){
             throw std::runtime_error("OR Unknown type encountered need bool get :" + a->getType() );
        }

         std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
        data->setValue<bool>( a->getValue<bool>() || b->getValue<bool>());


        
        mResolution.push_back(data);
    }

    void ConditionalInterpreter::fNot()
        {
            if (mResolution.size() < 1){
                throw std::runtime_error("NOT need 1 arg and get :" + std::to_string(mResolution.size()));
            }
            auto a = mResolution.back(); 
 	        mResolution.pop_back();

            if (a->getType() != typeid(bool).name()){
                throw std::runtime_error("NOT Unknown type encountered need bool get :" + a->getType() );
            }

             std::shared_ptr<ConditionalData> data = std::make_shared<ConditionalData>();
            data->setValue<bool>( !a->getValue<bool>() );

            
            mResolution.push_back(data);

        }
