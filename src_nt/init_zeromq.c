#include <Python.h>

/* Provide the init_zeromq() function that Visual Studio will be told to
   look for when we compile libzmq by pretending it is a Python extension. */

static PyMethodDef Methods[] = {
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
init_zeromq(void)
{
    (void) Py_InitModule("spam", Methods);
}
