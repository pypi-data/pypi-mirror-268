#include <pybind11/pybind11.h>
#include "aidge/utils/Log.hpp"

namespace py = pybind11;
namespace Aidge {
void init_Log(py::module& m){
    py::enum_<Log::Level>(m, "Level")
        .value("Debug", Log::Debug)
        .value("Info", Log::Info)
        .value("Notice", Log::Notice)
        .value("Warn", Log::Warn)
        .value("Error", Log::Error)
        .value("Fatal", Log::Fatal);

    py::class_<Log>(m, "Log")
    .def_static("debug", [](const std::string& msg) { Log::debug(msg); }, py::arg("msg"),
          R"mydelimiter(
          Detailed messages for debugging purposes, providing information helpful
          for developers to trace and identify issues.
          Detailed insights of what is appening in an operation, not useful for the
          end-user. The operation is performed nominally.
          Note: This level is disabled at compile time for Release, therefore
          inducing no runtime overhead for Release.

          :param msg: Debug message.
          :type msg: str
          )mydelimiter")
    .def_static("info", [](const std::string& msg) { Log::info(msg); }, py::arg("msg"),
          R"mydelimiter(
          Messages that provide a record of the normal operation, about
          the application's state, progress, or important events.
          Reports normal start, end and key steps in an operation. The operation is
          performed nominally.

          :param msg: Info message.
          :type msg: str
          )mydelimiter")
    .def_static("notice", [](const std::string& msg) { Log::notice(msg); }, py::arg("msg"),
          R"mydelimiter(
          Applies to normal but significant conditions that may require monitoring,
          like unusual or normal fallback events.
          Reports specific paths in an operation. The operation can still be
          performed normally.

          :param msg: Notice message.
          :type msg: str
          )mydelimiter")
    .def_static("warn", [](const std::string& msg) { Log::warn(msg); }, py::arg("msg"),
          R"mydelimiter(
          Indicates potential issues or situations that may lead to errors but do
          not necessarily cause immediate problems.
          Some specific steps of the operation could not be performed, but it can
          still provide an exploitable result.

          :param msg: Warning message.
          :type msg: str
          )mydelimiter")
    .def_static("error",[](const std::string& msg) { Log::error(msg); }, py::arg("msg"),
          R"mydelimiter(
          Signifies a problem or unexpected condition that the application can
          recover from, but attention is needed to prevent further issues.
          The operation could not be performed, but it does not prevent potential
          further operations.

          :param msg: Error message.
          :type msg: str
          )mydelimiter")
    .def_static("fatal", [](const std::string& msg) { Log::fatal(msg); }, py::arg("msg"),
          R"mydelimiter(
          Represents a critical error or condition that leads to the termination of
          the application, indicating a severe and unrecoverable problem.
          The operation could not be performed and any further operation is
          impossible.

          :param msg: Fatal message.
          :type msg: str
          )mydelimiter")
    .def_static("set_console_level", &Log::setConsoleLevel, py::arg("level"),
          R"mydelimiter(
          Set the minimum log level displayed in the console.

          :param level: Log level.
          :type level: Level
          )mydelimiter")
    .def_static("set_file_level", &Log::setFileLevel, py::arg("level"),
          R"mydelimiter(
          Set the minimum log level saved in the log file.

          :param level: Log level.
          :type level: Level
          )mydelimiter")
    .def_static("set_file_name", &Log::setFileName, py::arg("fileName"),
          R"mydelimiter(
          Set the log file name.
          Close the current log file and open the one with the new file name.
          If empty, stop logging into a file.

          :param fileName: Log file name.
          :type fileName: str
          )mydelimiter");
}

}
