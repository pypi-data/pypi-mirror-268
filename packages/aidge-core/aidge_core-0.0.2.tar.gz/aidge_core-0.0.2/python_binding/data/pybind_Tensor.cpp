/********************************************************************************
 * Copyright (c) 2023 CEA-List
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 ********************************************************************************/

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>
#include <pybind11/numpy.h>

#include "aidge/data/Tensor.hpp"
#include "aidge/data/Data.hpp"
#include "aidge/utils/Registrar.hpp"
#include "aidge/utils/Types.h"
#include "aidge/backend/TensorImpl.hpp"

namespace py = pybind11;
namespace Aidge {


template<typename T>
void addCtor(py::class_<Tensor,
                        std::shared_ptr<Tensor>,
                        Data,
                        Registrable<Tensor,
                                    std::tuple<std::string, DataType>,
                                    std::shared_ptr<TensorImpl>(DeviceIdx_t device, std::vector<DimSize_t> dims)>>& mTensor){
    mTensor.def(py::init([](
        py::array_t<T, py::array::c_style | py::array::forcecast> b,
        std::string backend = "cpu") {
        /* Request a buffer descriptor from Python */
        py::buffer_info info = b.request();
        Tensor* newTensor = new Tensor();
        newTensor->setDataType(NativeType<T>::type);
        const std::vector<DimSize_t> dims(info.shape.begin(), info.shape.end());
        newTensor->resize(dims);

        std::set<std::string> availableBackends = Tensor::getAvailableBackends();
        if (availableBackends.find(backend) != availableBackends.end()){
            newTensor->setBackend(backend);
            newTensor->getImpl()->copyFromHost(static_cast<T*>(info.ptr), newTensor->size());
        }else{
            AIDGE_THROW_OR_ABORT(py::value_error, "Could not find backend {}, verify you have `import aidge_backend_{}`.\n", backend, backend);
        }

        return newTensor;
    }), py::arg("array"), py::arg("backend")="cpu")
    .def("__setitem__", (void (Tensor::*)(std::size_t, T)) &Tensor::set)
    .def("__setitem__", (void (Tensor::*)(std::vector<std::size_t>, T)) &Tensor::set)
    ;
}


void init_Tensor(py::module& m){
    py::class_<Registrable<Tensor,
                           std::tuple<std::string, DataType>,
                           std::shared_ptr<TensorImpl>(DeviceIdx_t device, std::vector<DimSize_t> dims)>,
               std::shared_ptr<Registrable<Tensor,
                                           std::tuple<std::string, DataType>,
                                           std::shared_ptr<TensorImpl>(DeviceIdx_t device, std::vector<DimSize_t> dims)>>>(m,"TensorRegistrable");

    py::class_<Tensor, std::shared_ptr<Tensor>,
               Data,
               Registrable<Tensor,
                           std::tuple<std::string, DataType>,
                           std::shared_ptr<TensorImpl>(DeviceIdx_t device, std::vector<DimSize_t> dims)>> pyClassTensor
        (m,"Tensor", py::multiple_inheritance(), py::buffer_protocol());

    pyClassTensor.def(py::init<>())
    .def("set_datatype", &Tensor::setDataType, py::arg("datatype"), py::arg("copyCast") = true)
    .def("set_backend", &Tensor::setBackend, py::arg("name"), py::arg("device") = 0, py::arg("copyFrom") = true)
    .def("dims", (const std::vector<DimSize_t>& (Tensor::*)()const) &Tensor::dims)
    .def("grad", &Tensor::grad)
    .def("dtype", &Tensor::dataType)
    .def("size", &Tensor::size)
    .def("resize", (void (Tensor::*)(const std::vector<DimSize_t>&, std::vector<DimSize_t>)) &Tensor::resize)
    .def("has_impl", &Tensor::hasImpl)
    .def("get_coord", &Tensor::getCoord)
    .def("get_idx", &Tensor::getIdx)
    .def_static("get_available_backends", &Tensor::getAvailableBackends)
    .def("__str__", [](Tensor& b) {
        return b.toString();
    })
    .def("__len__", [](Tensor& b) -> size_t{
        return b.size();
    })
    .def("__getitem__", [](Tensor& b, size_t idx)-> py::object {
        if (idx >= b.size()) throw py::index_error();
        switch(b.dataType()){
            case DataType::Float64:
                return py::cast(b.get<double>(idx));
            case DataType::Float32:
                return py::cast(b.get<float>(idx));
            case DataType::Int8:
                return py::cast(b.get<std::int8_t>(idx));
            case DataType::Int16:
                return py::cast(b.get<std::int16_t>(idx));
            case DataType::Int32:
                return py::cast(b.get<std::int32_t>(idx));
            case DataType::Int64:
                return py::cast(b.get<std::int64_t>(idx));
            case DataType::UInt8:
                return py::cast(b.get<std::uint8_t>(idx));
            case DataType::UInt16:
                return py::cast(b.get<std::uint16_t>(idx));
            default:
                return py::none();
        }
    })
    .def("__getitem__", [](Tensor& b, std::vector<size_t> coordIdx)-> py::object {
        if (b.getIdx(coordIdx) >= b.size()) throw py::index_error();
        switch(b.dataType()){
            case DataType::Float64:
                return py::cast(b.get<double>(coordIdx));
            case DataType::Float32:
                return py::cast(b.get<float>(coordIdx));
            case DataType::Int8:
                return py::cast(b.get<std::int8_t>(coordIdx));
            case DataType::Int16:
                return py::cast(b.get<std::int16_t>(coordIdx));
            case DataType::Int32:
                return py::cast(b.get<std::int32_t>(coordIdx));
            case DataType::Int64:
                return py::cast(b.get<std::int64_t>(coordIdx));
            case DataType::UInt8:
                return py::cast(b.get<std::uint8_t>(coordIdx));
            case DataType::UInt16:
                return py::cast(b.get<std::uint16_t>(coordIdx));
            default:
                return py::none();
        }
    })
    .def_buffer([](Tensor& b) -> py::buffer_info {
        const std::shared_ptr<TensorImpl>& tensorImpl = b.getImpl();

        std::vector<size_t> dims;
        std::vector<size_t> strides;
        size_t stride = tensorImpl->scalarSize();

        for (unsigned int dim = b.nbDims(); dim > 0; dim--) {
            dims.push_back(b.dims()[dim-1]);
            strides.push_back(stride);
            stride *= b.dims()[dim-1];
        }
        std::reverse(dims.begin(), dims.end());
        std::reverse(strides.begin(), strides.end());

        std::string dataFormatDescriptor;
        switch(b.dataType()){
            case DataType::Float64:
                dataFormatDescriptor = py::format_descriptor<double>::format();
                break;
            case DataType::Float32:
                dataFormatDescriptor = py::format_descriptor<float>::format();
                break;;
            case DataType::Int8:
                dataFormatDescriptor = py::format_descriptor<std::int8_t>::format();
                break;
            case DataType::Int16:
                dataFormatDescriptor = py::format_descriptor<std::int16_t>::format();
                break;
            case DataType::Int32:
                dataFormatDescriptor = py::format_descriptor<std::int32_t>::format();
                break;
            case DataType::Int64:
                dataFormatDescriptor = py::format_descriptor<std::int64_t>::format();
                break;
            case DataType::UInt8:
                dataFormatDescriptor = py::format_descriptor<std::uint8_t>::format();
                break;
            case DataType::UInt16:
                dataFormatDescriptor = py::format_descriptor<std::uint16_t>::format();
                break;
            default:
                throw py::value_error("Unsupported data format");
        }

        return py::buffer_info(
            tensorImpl->rawPtr(),       /* Pointer to buffer */
            tensorImpl->scalarSize(),   /* Size of one scalar */
            dataFormatDescriptor,       /* Python struct-style format descriptor */
            b.nbDims(),                 /* Number of dimensions */
            dims,                       /* Buffer dimensions */
            strides                     /* Strides (in bytes) for each index */
        );
    });

    // TODO : If the ctor with the right data type does not exist, pybind will always convert the data to INT !
    // Need to find a way to avoid this !
    addCtor<std::int32_t>(pyClassTensor);
    addCtor<std::int64_t>(pyClassTensor);
    addCtor<float>(pyClassTensor);
// #if SIZE_MAX != 0xFFFFFFFF
    addCtor<double>(pyClassTensor);
// #endif

}
}
