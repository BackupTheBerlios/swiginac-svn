class ex;

%typemap(in) lst & {
    $1=list2lst($input);
    if (!$1) return NULL;
}

%typemap(typecheck) lst & {
    $1 = (PyList_Check($input)) ? 1 : 0;
}

%typemap(out) lst & {
    $result = lst2list($1);
}

%typemap(in) (int idx0, int idx1) {
    $1 = PyInt_AsLong(PyTuple_GetItem($input,0));
    $2 = PyInt_AsLong(PyTuple_GetItem($input,1));
}

%typemap(in) ex & {
    $1 = type2ex($input);
    if (!$1) return NULL;
}

%typemap(typecheck) ex & {
    $1 = (checktype2ex($input)) ? 1 : 0;
}

%typemap(out) ex &{
    $result = ex2type($1);
}

%typemap(out) ex {
    $result = ex2type(&($1));
}

// vim:ft=cpp:
