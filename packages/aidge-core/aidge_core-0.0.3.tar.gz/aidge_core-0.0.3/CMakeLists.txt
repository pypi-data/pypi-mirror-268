cmake_minimum_required(VERSION 3.15)

file(READ "${CMAKE_SOURCE_DIR}/version.txt" version)
file(READ "${CMAKE_SOURCE_DIR}/project_name.txt" project)

message(STATUS "Project name: ${project}")
message(STATUS "Project version: ${version}")

# Note : project name is {project} and python module name is also {project}
set(module_name _${project}) # target name


project(${project})
set(CXX_STANDARD 14)

##############################################
# Define options
option(PYBIND "python binding" ON)
option(WERROR "Warning as error" OFF)
option(TEST "Enable tests" ON)
option(COVERAGE "Enable coverage" OFF)
option(ENABLE_ASAN "Enable ASan (AddressSanitizer) for runtime analysis of memory use (over/underflow, memory leak, ...)" OFF)

find_package(Python REQUIRED)
if (${Python_VERSION_MAJOR} LESS 3)
    MESSAGE(FATAL_ERROR "Unsupported Python version. Python 3.0.0+ is required")
endif()


##############################################
# Import utils CMakeLists
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")
include(PybindModuleCreation)

if(CMAKE_COMPILER_IS_GNUCXX AND COVERAGE)
    Include(CodeCoverage)
endif()

##############################################
# Find system dependencies
Include(FetchContent)

FetchContent_Declare(
    fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG        10.2.1 # or a later release
)

set(FMT_SYSTEM_HEADERS ON)
FetchContent_MakeAvailable(fmt)
set_property(TARGET fmt PROPERTY POSITION_INDEPENDENT_CODE ON)

find_package(Threads REQUIRED)

##############################################
# Create target and set properties

file(GLOB_RECURSE src_files "src/*.cpp")
file(GLOB_RECURSE inc_files "include/*.hpp")

add_library(${module_name} ${src_files} ${inc_files})

#Set target properties
set_property(TARGET ${module_name} PROPERTY POSITION_INDEPENDENT_CODE ON)
target_include_directories(${module_name}
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

if( ${ENABLE_ASAN} )
    message("Building ${module_name} with ASAN.")
    set(SANITIZE_FLAGS -fsanitize=address -fno-omit-frame-pointer)
    target_link_libraries(${module_name}
        PUBLIC
            -fsanitize=address
    )
    target_compile_options(${module_name}
        PRIVATE
            ${SANITIZE_FLAGS}
    )
endif()

# PYTHON BINDING
if (PYBIND)
    generate_python_binding(${project} ${module_name})

    # Handles Python + pybind11 headers dependencies
    target_link_libraries(${module_name}
        PUBLIC
            pybind11::pybind11
        # PRIVATE
        #     Python::Python
        )
endif()

target_link_libraries(${module_name} PUBLIC Threads::Threads fmt::fmt)
target_compile_features(${module_name} PRIVATE cxx_std_14)

if (DOSANITIZE STREQUAL "ON")
set(SANITIZE_FLAGS -fsanitize=address,leak,undefined,float-divide-by-zero -fno-omit-frame-pointer)
#TODO sanitizer seems buggy in some situations with msvc, leading to linker errors, temporarily inactivating it
#set(SANITIZE_MSVC_FLAGS)
set(SANITIZE_MSVC_FLAGS /fsanitize=address)
target_compile_definitions(${module_name} PUBLIC _DISABLE_VECTOR_ANNOTATION)
else()
set(SANITIZE_FLAGS)
set(SANITIZE_MSVC_FLAGS)
endif()

set(STRICT_ALIASING_FLAGS -fstrict-aliasing -Wstrict-aliasing=2)

# -fvisibility=hidden required by pybind11
target_compile_options(${module_name} PUBLIC
    $<$<OR:$<CXX_COMPILER_ID:Clang>,$<CXX_COMPILER_ID:AppleClang>,$<CXX_COMPILER_ID:GNU>>:
    -fvisibility=hidden>)
target_compile_options(${module_name} PRIVATE
$<$<OR:$<CXX_COMPILER_ID:Clang>,$<CXX_COMPILER_ID:AppleClang>,$<CXX_COMPILER_ID:GNU>>:
-Wall -Wextra -Wold-style-cast -Winline -pedantic -Werror=narrowing -Wshadow $<$<BOOL:${WERROR}>:-Werror> ${SANITIZE_FLAGS}>)
target_compile_options(${module_name} PRIVATE
$<$<CXX_COMPILER_ID:GNU>:${STRICT_ALIASING_FLAGS}>)
target_compile_options(${module_name} PRIVATE
$<$<CXX_COMPILER_ID:MSVC>:
/W4 /wd4477 /DWIN32 /D_WINDOWS /GR /EHsc /MP /Zc:__cplusplus /Zc:preprocessor /permissive- ${SANITIZE_MSVC_FLAGS}>)
if (DOSANITIZE STREQUAL "ON")
    target_compile_options(${module_name} PRIVATE $<$<CXX_COMPILER_ID:MSVC>:/MDd>)
endif()
# TODO FIXME: I'm not sure it's a good idea to propagate this option but, at this point, it was the only way that worked to silence C4477
target_compile_options(${module_name} PUBLIC $<$<CXX_COMPILER_ID:MSVC>: /wd4477>)

target_link_options(${module_name} PUBLIC $<$<OR:$<CXX_COMPILER_ID:Clang>,$<CXX_COMPILER_ID:AppleClang>,$<CXX_COMPILER_ID:GNU>>:${SANITIZE_FLAGS}>)
#target_link_options(${module_name} PUBLIC $<$<CXX_COMPILER_ID:MSVC>:${SANITIZE_MSVC_FLAGS}>)

if(CMAKE_COMPILER_IS_GNUCXX AND COVERAGE)
    append_coverage_compiler_flags()
endif()

##############################################
# Installation instructions


# For debug !!!
# set(CMAKE_INSTALL_LIBDIR ${CMAKE_CURRENT_SOURCE_DIR}/libZER)
# # set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")


include(GNUInstallDirs)
set(INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/cmake/${project})

install(TARGETS ${module_name} EXPORT ${project}-targets
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

#Export the targets to a script

install(EXPORT ${project}-targets
 FILE "${project}-targets.cmake"
 DESTINATION ${INSTALL_CONFIGDIR}
#  COMPONENT ${module_name}
)

#Create a ConfigVersion.cmake file
include(CMakePackageConfigHelpers)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/${project}-config-version.cmake"
    VERSION ${version}
    COMPATIBILITY AnyNewerVersion
)

configure_package_config_file("${project}-config.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${project}-config.cmake"
    INSTALL_DESTINATION ${INSTALL_CONFIGDIR}
)

#Install the config, configversion and custom find modules
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${project}-config.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/${project}-config-version.cmake"
    DESTINATION ${INSTALL_CONFIGDIR}
)

##############################################
## Exporting from the build tree
export(EXPORT ${project}-targets
    FILE "${CMAKE_CURRENT_BINARY_DIR}/${project}-targets.cmake")


##############################################
## Add test
if(TEST)
    enable_testing()
    add_subdirectory(unit_tests)
endif()
