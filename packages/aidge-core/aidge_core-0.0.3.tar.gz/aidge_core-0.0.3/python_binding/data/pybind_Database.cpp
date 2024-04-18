#include <pybind11/pybind11.h>
#include "aidge/data/Database.hpp"

namespace py = pybind11;
namespace Aidge {

void init_Database(py::module& m){

    py::class_<Database, std::shared_ptr<Database>>(m,"Database");

    
}
}
