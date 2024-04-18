
#ifndef AIDGE_CORE_GREGEX_TOKEN_TYPES_H_
#define AIDGE_CORE_GREGEX_TOKEN_TYPES_H_


namespace Aidge {
    /**
     * @brief enum for all types of token use in the of the regex
     * 7-5 type
     * 4-0 id
    */
    enum class gRegexTokenTypes
    {
        STOP,
        NEXT,   /**< -> */

        QOM,    /**< + */
        QZM,    /**< * */

        KEY,    /**< [A-Za-z_0-9]+ */
        CKEY,   /**< [A-Za-z_0-9]+#[0-9]* */

        SEP,    /**< \( */
        LPAREN, /**< \( */
        RPAREN, /**< \) */
    };

}
#endif //AIDGE_CORE_GREGEX_TOKEN_TYPES_H_
