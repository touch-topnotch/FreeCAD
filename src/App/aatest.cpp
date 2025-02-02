//
// Created by Dmitry Tetkin on 01.02.2025.
//

#include "aatest.h"
#include "Application.h"

#include "ProgramOptionsUtilities.h"
#include "Property.h"
#include "PropertyContainer.h"
#include "PropertyExpressionEngine.h"
#include "PropertyFile.h"
#include "PropertyLinks.h"
#include "PropertyPythonObject.h"

PyMODINIT_FUNC
init_freecad_base_module(void)
{
    static struct PyModuleDef BaseModuleDef = {
        PyModuleDef_HEAD_INIT,
        "__FreeCADBase__", Base_doc, -1,
        nullptr, nullptr, nullptr, nullptr, nullptr
    };
    return PyModule_Create(&BaseModuleDef);
}

// Set in inside Application
static PyMethodDef* ApplicationMethods = nullptr;

PyMODINIT_FUNC
init_freecad_module(void)
{
    static struct PyModuleDef FreeCADModuleDef = {
        PyModuleDef_HEAD_INIT,
        "FreeCAD", FreeCAD_doc, -1,
        ApplicationMethods,
        nullptr, nullptr, nullptr, nullptr
    };
    return PyModule_Create(&FreeCADModuleDef);
}

PyMODINIT_FUNC
init_image_module()
{
    static struct PyModuleDef ImageModuleDef = {
        PyModuleDef_HEAD_INIT,
        "Image", "", -1,
        nullptr,
        nullptr, nullptr, nullptr, nullptr
    };
    return PyModule_Create(&ImageModuleDef);
}