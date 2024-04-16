#include <modules.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(glfw, m)
{
    m.doc() = "GLFW Windowing System";

    //init_internal(m);
    init_constants(m);
    init_structs(m);
    init_context(m);
    init_monitors(m);
    init_windows(m);
    init_input(m);
    init_joystick(m);
    init_callbacks(m);
}