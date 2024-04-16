#define PY_SSIZE_T_CLEAN
#include <Python.h>

#if PY_MAJOR_VERSION >= 3
#define PY3K
#endif

#include "1bpp.h"
#include "2bpp.h"
#include "4bpp.h"
#include <stdio.h>

#define W 1600
#define H 1200
#define STEP 3

PyObject* convert_1bpp(PyObject* self, PyObject *args, PyObject *keywds)
{
    unsigned char *image;
    Py_ssize_t imagesize;

    uint8_t *out_img;

    PyObject* result;

    out_img = malloc( (H*W>>3)+32 );
    memset(out_img, 0, (H*W>>3)+32);

    static char *kwlist[] = {"data", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "s#", kwlist, &image, &imagesize)) return NULL;


    //FIXME check image size!
    kaleido_convert_1bpp(image, out_img, W, H);


    #if PY_MAJOR_VERSION >= 3
    result = Py_BuildValue("y#", out_img, (H*W>>3)+32);
    #else
    result = Py_BuildValue("s#", out_img, (H*W>>3)+32);
    #endif

    free( out_img );

    return result;

}

PyObject* convert_2bpp(PyObject* self, PyObject *args, PyObject *keywds)
{
    unsigned char *image;
    Py_ssize_t imagesize;

    uint8_t *out_img;

    PyObject* result;

    out_img = malloc( (H*W>>3)*2+32 );
    memset(out_img, 0, (H*W>>3)*2+32 );

    static char *kwlist[] = {"data", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "s#", kwlist, &image, &imagesize)) return NULL;


    //FIXME check image size!
    kaleido_convert_2bpp(image, out_img, W, H);


    #if PY_MAJOR_VERSION >= 3
    result = Py_BuildValue("y#", out_img, (H*W>>3)*2+32);
    #else
    result = Py_BuildValue("s#", out_img, (H*W>>3)*2+32);
    #endif

    free( out_img );

    return result;

}

PyObject* convert_4bpp(PyObject* self, PyObject *args, PyObject *keywds)
{
    unsigned char *image;
    Py_ssize_t imagesize;

    uint8_t *out_img;

    PyObject* result;

    out_img = malloc( (H*W>>3)*4+32 );
    memset(out_img, 0, (H*W>>3)*4+32 );

    static char *kwlist[] = {"data", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "s#", kwlist, &image, &imagesize)) return NULL;


    //FIXME check image size!
    kaleido_convert_4bpp(image, out_img, W, H);


    #if PY_MAJOR_VERSION >= 3
    result = Py_BuildValue("y#", out_img, (H*W>>3)*4+32);
    #else
    result = Py_BuildValue("s#", out_img, (H*W>>3)*4+32);
    #endif

    free( out_img );

    return result;

}

static PyMethodDef module_methods[] = {
   {"convert_1bpp", (PyCFunction)convert_1bpp, METH_VARARGS | METH_KEYWORDS, "Conversion of RGB"},
   {"convert_2bpp", (PyCFunction)convert_2bpp, METH_VARARGS | METH_KEYWORDS, "Conversion of RGB"},
   {"convert_4bpp", (PyCFunction)convert_4bpp, METH_VARARGS | METH_KEYWORDS, "Conversion of RGB"},
   {NULL}
};

#ifdef PY3K
// module definition structure for python3
static struct PyModuleDef convert_mod =
{
    PyModuleDef_HEAD_INIT,
    "c_kaleido", /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,   /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};

PyMODINIT_FUNC PyInit_kaleido(void)
{
    return PyModule_Create(&convert_mod);
}
#else
// module initializer for python2 - this is not tested!!!
PyMODINIT_FUNC initc_kaleido(void)
{
    Py_InitModule("c_kaleido", module_methods);
}
#endif