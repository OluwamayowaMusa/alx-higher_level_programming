#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python list
 * @p: Pointer to PyObject list
 *
 */
void print_python_list_info(PyObject *p)
{
	PyObject *temp;
	Py_ssize_t len, index, alloc;
	PyTypeObject *type;

	if (!PyList_Check(p))
		return;
	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);
	for (index = 0; index < len; index++)
	{
		temp = PyList_GetItem(p, index);
		type = Py_TYPE(temp);
		printf("Element %ld: %s\n", index, type->tp_name);
	}
}
