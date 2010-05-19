
ex * type2ex(PyObject * input);
numeric * type2numeric(PyObject * input);
PyObject * ex2type(const ex* input);
bool checktype2ex(PyObject * input);
lst* list2lst(PyObject *input);
PyObject *lst2list(const lst *input);
PyObject *exvector2list(exvector *input);
