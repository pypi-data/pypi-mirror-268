// #include <pybind11/pybind11.h>
// #include <pybind11/stl.h>
// #include "aidge/data/DataProvider.hpp"
// #include "aidge/data/Database.hpp"

// namespace py = pybind11;

// namespace Aidge {

// // __iter__ method for iterator protocol
// DataProvider* DataProvider::iter(){
//     resetIndexBatch();
//     setBatches();
//     return this;
// }

// // __next__ method for iterator protocol
// std::vector<std::shared_ptr<Aidge::Tensor>> DataProvider::next() {
//     if (!done()){
//         incrementIndexBatch();
//         return readBatch();
//     } else {
//         throw py::stop_iteration();
//     }
// }

// void init_DataProvider(py::module& m){

//     py::class_<DataProvider, std::shared_ptr<DataProvider>>(m, "DataProvider")
//         .def(py::init<Database&, std::size_t, bool, bool>(), py::arg("database"), py::arg("batch_size"), py::arg("shuffle"), py::arg("drop_last"))
//         .def("__iter__", &DataProvider::iter)
//         .def("__next__", &DataProvider::next)
//         .def("__len__", &DataProvider::getNbBatch);
    
// }
// }
