
#ifndef AIDGE_CORE_CONDITIONAL_DATA_H_
#define AIDGE_CORE_CONDITIONAL_DATA_H_

#include <vector>
#include <string>
#include <stdexcept> //error
#include <memory>
#include <map>
namespace Aidge{



/////////////////////////
// The data type in AST Intepretation
////////////////////////

class BaseConditionalValue {
public:
    virtual ~BaseConditionalValue() {}
};

template <typename T>
class ConditionalValue : public BaseConditionalValue {
public:
    ConditionalValue(const T& data) : value(data) {}
    T value;
};


struct ConditionalData {
    /**
     * @brief generic type to propagate all the different values in the AST interpretation
    */
    //void* value;
    std::unique_ptr<BaseConditionalValue> value;
    const std::type_info* type =nullptr;

    /////////////////////////////////
    //
    ////////////////////////////////
    /**
     * @brief set a value
    */
    template <typename T>
    void setValue(const T& newValue) {
        //make sure that the old value is free
        deleteValue();
        value = std::make_unique<ConditionalValue<T>>(newValue);
        type = &typeid(T);
    }

    /**
     * @brief get the actual value
     * @details recaste the value to the templaited type and checks that the conversion type is compatible with type
     * @tparam the type of the return value
     * @return the value
    */
    template <typename T>
    T getValue() const {
        if (type && *type == typeid(T)) {
            //const Value<T>* typedValue = dynamic_cast<const Value<T>*>(static_cast<const BaseValue*>(value));
            const ConditionalValue<T>* typedValue = dynamic_cast<const ConditionalValue<T>*>(value.get());
            if (typedValue) {
                return typedValue->value;
            }
        }
        throw std::runtime_error(std::string("DATA ERROR ") + type->name() + " != " + typeid(T).name());
    }
    ///////////////////////////////////
    //
    ///////////////////////////////////
    std::string getType() const {
        return  type ? type->name() : "nullptr";
    }


    template <typename T>
    bool isTypeEqualTo() const {
        return (type && *type == typeid(T));
    }

    void deleteValue() {
        if (type) {
            value.reset();
            type = nullptr;
        }
    }

    ~ConditionalData() { // TODO best can we have a list of type supported ?
       deleteValue();
    }
};

}


#endif //AIDGE_CORE_CONDITIONAL_DATA_H_
