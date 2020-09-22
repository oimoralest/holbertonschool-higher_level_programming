#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_bytes - print info about bytes object
 * @p: PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *aux = NULL;
	long int i = 0, bytes = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		bytes = ((PyVarObject *)p)->ob_size;
		printf("  syze: %li\n", bytes);
		aux = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", aux);
		if (bytes < 10 && bytes >= 0)
			printf("  first %li bytes: ", bytes + 1);
		else if (bytes > 10)
			printf("  first 10 bytes: ");
		while (i < bytes && i < 10)
		{
			if (i == 9)
				printf("%02hhx", aux[i]);
			else
				printf("%02hhx ", aux[i]);
			i++;
		}
		if (i < 10)
			printf("00");
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
/**
 * print_python_float - print info about float object
 * @p: PyObject
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *buffer;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		buffer = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
			'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buffer);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}
/**
 * print_python_list - print info about list object
 * @p: PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int bytes = 0, i = 0;
	PyObject *aux = NULL;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		bytes = ((PyVarObject *)p)->ob_size;
		printf("[*] Size of the Python List = %li\n", bytes);
		printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
		while (i < bytes)
		{
			aux = ((PyListObject *)p)->ob_item[i];
			printf("Element %li: %s\n", i, aux->ob_type->tp_name);
			if (PyBytes_Check(aux))
				print_python_bytes(aux);
			else if (PyFloat_Check(aux))
				print_python_float(aux);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
