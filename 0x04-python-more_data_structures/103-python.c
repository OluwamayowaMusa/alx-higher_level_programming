#include <Python.h>


/* Function Declarations */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print basic info about Python Lists
 * @p: Pointer to PyObject to python list
 *
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len, index, alloc;
	PyObject *temp;

	if (!PyList_Check(p))
		return;
	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);
	for (index = 0; index < len; index++)
	{
		temp = PyList_GET_ITEM(p, index);
		if (PyBytes_Check(temp))
		{
			printf("Element %ld: %s\n", index, "bytes");
			print_python_bytes(temp);
		}
		else if (PyLong_Check(temp))
			printf("Element %ld: %s\n", index, "int");
		else if (PyFloat_Check(temp))
			printf("Element %ld: %s\n", index, "float");
		else if (PyTuple_Check(temp))
			printf("Element %ld: %s\n", index, "tuple");
		else if (PyList_Check(temp))
			printf("Element %ld: %s\n", index, "list");
		else if (PyUnicode_Check(temp))
			printf("Element %ld: %s\n", index, "str");
	}
}

/**
 * print_python_bytes - Print Basic info about Python bytes
 * @p: Pointer to PyObjetc to python bytes
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, temp, index;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", str);
	temp = len;
	if (len > 10)
		temp = 9;
	printf("  first %ld bytes: ", temp + 1);
	for (index = 0; index <= temp; index++)
	{
		if (index != temp)
			printf("%02x ", (unsigned char)*(str + index));
		else
			printf("%02x\n", *(str + index));
	}
}
