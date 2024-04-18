

#ifndef AIDGE_CORE_CONDITIONAL_TYPES_H_
#define AIDGE_CORE_CONDITIONAL_TYPES_H_
namespace Aidge{
    /**
     * @brief enum for all types of token use in the parsing
     * 7-5 type
     * 4-0 id
    */
    enum class ConditionalTokenTypes
    {
        STOP,

        NOT,     /**< ! */
        AND,     /**< && */
        OR,      /**< || */

        EQ,      /**< == */
        NEQ,     /**< != */

        KEY,     /**< [A-Za-z][A-Za-z0-9_]* */
        INTEGER, /**< [0-9]+ */
        FLOAT,   /**< [0-9]+\.[0-9]* */
        STRING , /**< \'.*\' */
        BOOL,    /**< true|false */
        NODE,    /**< \$ */
        LAMBDA , /**< [A-Za-z][A-Za-z0-9_]*\( */

        ARGSEP,  /**< , */
        LPAREN,  /**< \( */
        RPAREN,  /**< \) */

    };
}
#endif // AIDGE_CORE_CONDITIONAL_TYPES_H_
