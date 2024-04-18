function(generate_python_binding name target_to_bind)
    add_definitions(-DPYBIND)
    Include(FetchContent)

    FetchContent_Declare(
    PyBind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.10.4 # or a later release
    )

    # Use the New FindPython mode, recommanded. Requires CMake 3.15+
    find_package(Python COMPONENTS Interpreter Development)
    FetchContent_MakeAvailable(PyBind11)

    message(STATUS "Creating binding for module ${name}")
    file(GLOB_RECURSE pybind_src_files "python_binding/*.cpp")

    pybind11_add_module(${name} MODULE ${pybind_src_files} "NO_EXTRAS") # NO EXTRA recquired for pip install
    target_include_directories(${name} PUBLIC "python_binding")
    target_link_libraries(${name} PUBLIC ${target_to_bind})
endfunction()
