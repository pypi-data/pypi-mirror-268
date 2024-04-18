#include "aidge/nodeTester/ConditionalLexer.hpp"

using namespace Aidge; 

//////////////////
//ConditionalLexer
//////////////////


ConditionalLexer::ConditionalLexer( const std::string ConditionalExpressions):
mConditionalExpressions(ConditionalExpressions)
{
    mPosition = 0;
}

std::shared_ptr<ParsingToken<ConditionalTokenTypes>> ConditionalLexer::getNextToken(void){
    std::string currentChars = "";

    while (mPosition < mConditionalExpressions.length())
    {
        //erase all space 
        if (mConditionalExpressions[mPosition] != ' ')
        {
            currentChars += mConditionalExpressions[mPosition];
        }
        else
        {
            mPosition++;
            continue;
        }
        //performe tokenisation, find a regex and make a new token
        
        if (std::regex_match(currentChars,std::regex("\\&\\&")))// the AND TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::AND,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\|\\|")))// the OR TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::OR,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\!")))// the Not and not equ
        {
            mPosition++;
            if ( mPosition < mConditionalExpressions.length()){
                currentChars += mConditionalExpressions[mPosition];
                if(std::regex_match(currentChars,std::regex("!="))){
                    mPosition++;
                    return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::NEQ,"");
                }else{
                     return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::NOT,"");
                }
            }
            //a not at the end not ok but it's the parseur work
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::NOT,"");
        }
        else if (std::regex_match(currentChars,std::regex("==")))// the EQ TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::EQ,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\(")))// the LPAREN TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::LPAREN,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\)")))// the RPAREN TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::RPAREN,"");
        }
        else if (std::regex_match(currentChars,std::regex(",")))// the RPAREN TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::ARGSEP,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\$")))// the ACTNode TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::NODE,"");
        }


        /////
        //non const lent token
        /////

        //LAMBDA, KEY , bool //the fuction TAG 
        else if (std::regex_match(currentChars,std::regex("[A-Za-z_]")))// the KEY TOKEN (a char next )
        {   
            //read all the key 
            bool isLambda = false;
            std::regex keyRegex("[A-Za-z_0-9]+");
            std::regex LambdaRegex("[A-Za-z_0-9]+\\(");

            while ( mPosition < mConditionalExpressions.length()) {
                if(!std::regex_match(currentChars,keyRegex) && !std::regex_match(currentChars,LambdaRegex))
                {
                    currentChars.pop_back(); //the last char is the problemes
                    break;
                }
                else if (std::regex_match(currentChars,LambdaRegex)){
                    isLambda = true;
                }
                mPosition++;
                if (mPosition < mConditionalExpressions.length()) currentChars += mConditionalExpressions[mPosition];
                //currentChars += mConditionalExpressions[mPosition];
            }
            //we end the match 2 posibility 
            //we are at the end of the mConditionalExpressions and we need to ensure the match
            //we are not we can continu
            if (mPosition == mConditionalExpressions.length()-1)
            {
                if (!std::regex_match(currentChars,keyRegex) && !std::regex_match(currentChars,LambdaRegex))
                {
                    throw badTokenError(currentChars,mPosition);
                }
                //mPosition++; // we stop all by going pos > lengt
            }


            if (std::regex_match(currentChars,std::regex("(true|false|True|False)"))){
                return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::BOOL,currentChars);

            } else if (isLambda){
                currentChars.pop_back();//pop the ( of the lambda
                return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::LAMBDA,currentChars);
            } else{
                return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::KEY,currentChars);
            }
            
        }
        //numeric value 
        else if (std::regex_match(currentChars,std::regex("[0-9]")))// the KEY TOKEN (a char next )
        {   
            //read all the key 
            bool isFloat = false;
            std::regex integerRegex("[0-9]+$");
            std::regex floatRegex("[0-9]+\\.[0-9]*$");

            while ( mPosition < mConditionalExpressions.length()) {

                if(!std::regex_match(currentChars,integerRegex) && !std::regex_match(currentChars,floatRegex))
                {
                    currentChars.pop_back(); // the last char match is not a good one 
                    break;
                }
                else if (std::regex_match(currentChars,floatRegex)){
                    isFloat = true;
                }
                mPosition++;
                if (mPosition < mConditionalExpressions.length()) currentChars += mConditionalExpressions[mPosition];
                //currentChars += mConditionalExpressions[mPosition];
            }
            //we end the match 2 posibility 
            //we are at the end of the mConditionalExpressions and we need to ensure the match
            //we are not we can continu
            if (mPosition == mConditionalExpressions.length()-1)
            {
                if (!std::regex_match(currentChars,integerRegex) && !std::regex_match(currentChars,floatRegex))
                {
                     throw badTokenError(currentChars,mPosition);
                }
            }
            
            if(isFloat){
                return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::FLOAT,currentChars);
            }else{
                return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::INTEGER,currentChars);
            }
            
        }
        //string TODO
        else if (std::regex_match(currentChars,std::regex("\'"))) // TODO ' or \'
        {
            std::regex strRegex("\'[A-Za-z_0-9\\s]*\'$");
            while ( mPosition < mConditionalExpressions.length()) {
                if(std::regex_match(currentChars,strRegex)){
                    break;
                }
                mPosition++;
                if (mPosition < mConditionalExpressions.length()) currentChars += mConditionalExpressions[mPosition];
                //currentChars += mConditionalExpressions[mPosition];
            }

            //test the end condition
            if (mPosition == mConditionalExpressions.length()-1 ){
                if (!std::regex_match(currentChars,strRegex)){
                     throw badTokenError(currentChars,mPosition);
                }
                //mPosition++; // we stop all by going pos > lengt
            }

            mPosition++; // go after the last " 
            //erase the " char
            currentChars.pop_back();
            currentChars.erase(0,1);

            return std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::STRING,currentChars);

        }

        //Array TODO

        mPosition++;
    }

    //no more to find no one match the currentChars 
    if (currentChars.empty()) {
        return  std::make_shared<ParsingToken<ConditionalTokenTypes>>(ConditionalTokenTypes::STOP,"");  // Null shared pointer ;
    }else{
        //std::ostringstream errorMessage;
        //errorMessage << "\nBad syntax " << currentChars << " :\n" << mConditionalExpressions;
        throw badTokenError(currentChars,mPosition);
    }
    
}

void ConditionalLexer::rstPosition(void){
    if (isEnd()){
        mPosition = 0;
    }else{
        throw badTokenError("end rst",mPosition);
    }
    
}

bool ConditionalLexer::isEnd(void){
    return mPosition >= mConditionalExpressions.length();
}

std::runtime_error ConditionalLexer::badTokenError(const std::string& currentChars,std::size_t position){
    std::ostringstream errorMessage;
    errorMessage << "\nBad syntax " << currentChars << " :\n" << mConditionalExpressions << "\n";
     for (std::size_t i = 0; i < position; i++) {
        errorMessage << ' ';
    }
    errorMessage << "^\n";

    return std::runtime_error(errorMessage.str());
}