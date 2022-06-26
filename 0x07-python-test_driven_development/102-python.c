#define PYSSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Print Python strings
 * @p: Pyobject
 *
 */
void print_python_string(PyObject *p)
{
	PyTypeObject *temp;
	char *data;
	Py_ssize_t len;

	puts("[.] string object info");
	if (!PyUnicode_Check(p))
	{
		puts("  [ERROR] Invalid String Object");
		return;
	}
	len = PyUnicode_GET_SIZE(p);
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		puts("  type: compact ascii");
		printf("  length: %lu\n", len);
		p = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
		data = PyBytes_AS_STRING(p);
		printf("  value: %s\n", data);
	}
	else if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
	{
		puts("  type: compact unicode object");
		printf("  length: %lu\n", len);
		p = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
		data = PyBytes_AS_STRING(p);
		printf("  value: %s\n", data);
	}
}
