
#include "aidge/graphRegex/GraphLexer.hpp"

using namespace Aidge; 


GraphLexer::GraphLexer( const std::string gRegexExpressions ):
mRegularExpressions(gRegexExpressions){
    mPosition = 0;
}

std::shared_ptr<ParsingToken<gRegexTokenTypes>> GraphLexer::getNextToken(void){
    std::string currentChars = "";
    while (mPosition < mRegularExpressions.length())
    {
        //erase all space 
        if (mRegularExpressions[mPosition] != ' ')
        {
            currentChars += mRegularExpressions[mPosition];
        }
        else
        {
            mPosition++;
            continue;
        }

        /////
        // const lent token
        /////

        if (std::regex_match(currentChars,std::regex("\\->")))// the next TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::NEXT,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\*")))// the * TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::QZM,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\+")))// the + TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::QOM,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\(")))// the LPAREN TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::LPAREN,"");
        }
        else if (std::regex_match(currentChars,std::regex("\\)")))// the RPAREN TOKEN 
        {
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::RPAREN,"");
        }

        //
        else if (std::regex_match(currentChars,std::regex(";")))// the SEP TOKEN 
        {
            //test if the last sep
            //std::string subStr = mRegularExpressions.substr(mPosition);
            mPosition++;
            return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::SEP,"");
        }

        /////
        //unconst lent token
        /////

        else if (std::regex_match(currentChars,std::regex("[A-Za-z_0-9]")))// the KEY or CKEY
        {   
            
            //read all the key 
            bool isCKey = false;
            std::regex keyRegex("[A-Za-z_0-9]+");
            std::regex cKeyRegex("[A-Za-z_0-9]+\\#[0-9]*");

            while ( mPosition < mRegularExpressions.length()) {

                if(!std::regex_match(currentChars,keyRegex) && !std::regex_match(currentChars,cKeyRegex))
                {
                    currentChars.pop_back(); //the last char is the problemes
                    break;
                }
                else if (std::regex_match(currentChars,cKeyRegex)){
                    isCKey = true;
                }
                mPosition++;
                if (mPosition < mRegularExpressions.length()) currentChars += mRegularExpressions[mPosition];
                
            }
            //we end the match 2 posibility 
            //we are at the end of the mConditionalExpressions and we need to ensure the match
            //we are not we can continu
            if (mPosition == mRegularExpressions.length()-1)
            {
                if (!std::regex_match(currentChars,keyRegex) && !std::regex_match(currentChars,cKeyRegex))
                {
                    throw badTokenError(currentChars,mPosition);
                }
            }


            if (isCKey){
                return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::CKEY,currentChars);
            } else{
                return std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::KEY,currentChars);
            }
        }

        mPosition++;
    }


    //no more to find no one match the currentChars 
    if (currentChars.empty()) {
        return  std::make_shared<ParsingToken<gRegexTokenTypes>>(gRegexTokenTypes::STOP,"");  // Null shared pointer ;
    }else{
        throw badTokenError(currentChars,mPosition);
    }

}

void GraphLexer::rstPosition(void){
    if (isEnd()){
        mPosition = 0;
    }else{
        throw badTokenError("end rst",mPosition);
    }
}

bool GraphLexer::isEnd(void){
    return mPosition >= mRegularExpressions.length();
}


const std::string GraphLexer::getQuery(){
    return mRegularExpressions;
}

std::runtime_error GraphLexer::badTokenError(const std::string& currentChars,std::size_t position){
    std::ostringstream errorMessage;
    errorMessage << "\nBad syntax " << currentChars << " :\n" << mRegularExpressions << "\n";
    for (std::size_t i = 0; i < position; i++) {
        errorMessage << ' ';
    }
    errorMessage << "^\n";

    return std::runtime_error(errorMessage.str());
}

  const std::string GraphLexer::rep(){
    std::string out = mRegularExpressions;
    out += "\n";
    for (std::size_t i = 0; i < mPosition; i++) {
        out += ' ';
    }
    out +=  "^\n";
    return out ;
    }