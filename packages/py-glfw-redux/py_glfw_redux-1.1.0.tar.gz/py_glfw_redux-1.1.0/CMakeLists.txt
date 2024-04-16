cmake_minimum_required(VERSION 3.25.2)

project(py-glfw-redux)

set(CMAKE_DEBUG_POSTFIX, "-d")
set(Python3_FIND_REGISTRY NEVER)

if(${MSVC})
    set(PY_COMPONENTS Interpreter Development)
else()
    set(PY_COMPONENTS Interpreter Development.Module)
endif()

find_package(Python3
    COMPONENTS
    REQUIRED
    ${PY_COMPONENTS}
)

add_subdirectory(third-party)

set(srcs
    src/bind-glfw.cpp
    src/callbacks.cpp
    src/constants.cpp
    src/context.cpp
    src/input.cpp
    src/joystick.cpp
    src/monitors.cpp
    src/structs.cpp
    src/windows.cpp
)

Python3_add_library(pyglfw ${srcs})
set_target_properties(pyglfw
    PROPERTIES
    INTERPROCEDURAL_OPTIMIZATION ON
    VISIBILITY_INLINES_HIDDEN ON
    CXX_STANDARD 17
    OUTPUT_NAME "glfw" # rename to glfw like this so we don't conflict target names
)

target_link_libraries(pyglfw
    PRIVATE
    pybind11::headers
    glfw
    glad
)

target_include_directories(pyglfw
    PRIVATE inc
)

target_compile_definitions(pyglfw
    PRIVATE PYBIND11_DETAILED_ERROR_MESSAGES
)

if(${MSVC})
else()
    target_compile_options(pyglfw
        PRIVATE
        -Wno-format-security
        -fvisibility=hidden
    )
endif()
