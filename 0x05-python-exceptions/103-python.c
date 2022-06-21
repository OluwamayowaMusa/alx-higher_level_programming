#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <floatobject.h>

/* Function Declaration */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print infomation about element of a list
 * @p: PyObject passed
 *
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len, alloc, index;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	len = PyList_GET_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", alloc);
	for (index = 0; index < len; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %lu: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[index]);
	}
	fflush(stdout);
}


/**
 * print_python_bytes - Print information about PyObject p
 * @p: PyObject passed
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, temp, index;
	char *str;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	printf("  size: %lu\n", len);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);
	temp = len;
	if (len > 10)
		temp = 9;
	printf("  first %lu bytes: ", temp + 1);
	for (index = 0; index < temp + 1; index++)
	{
		if (index != temp)
			printf("%.2x ", (unsigned char)str[index]);
		else
			printf("%.2x\n", (unsigned char)str[index]);
	}
	fflush(stdout);
}


/**
 * print_python_float - Print information about PyObject p
 * @p: PyObject passed
 */
void print_python_float(PyObject *p)
{
	double num;
	char *str;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	num = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	fflush(stdout);
}
