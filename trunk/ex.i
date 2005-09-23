/*
 (c) Copyright 2003, 2004, 2005
     Author: Ola Skavhaug and Ondrej Certik
     
     This file is part of swiginac.

     swiginac is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

     swiginac is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with swiginac; if not, write to the Free Software
     Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

%{ 
lst* list2lst(PyObject *input);
PyObject* lst2list(lst *input); 

//GETDESC1 and GETDESC2 are equivalent - GETDESC1 is the official way how to do
//it, but it's slower than the undocumented way GETDESC2.

#define GETDESC1(NAME) \
static swig_type_info *NAME##descr=0;\
if (!NAME##descr){\
    NAME##descr=SWIG_TypeQuery("GiNaC::"#NAME" *");\
    if (!NAME##descr) {\
        PyErr_SetString(PyExc_ValueError,"Cannot get a "#NAME" descriptor. Fix in ex.i");\
        return NULL;\
    }\
}

#define GETDESC2(NAME) \
static swig_type_info *NAME##descr=SWIGTYPE_p_GiNaC__##NAME

#define GETDESC(NAME) GETDESC2(NAME)

//converts any type from python to ex
ex * type2ex(PyObject * input) {
    ex tmp;
    ex *tmp_ptr;
    basic *btmp;
    symbol *stmp;
    numeric *ntmp;
    int itmp;
    double dtmp;

    bool errconv = true;
    GETDESC(ex);
    if (not((SWIG_ConvertPtr(input, (void **) &tmp_ptr, exdescr, 0)) == -1)) {
        errconv = false;
        tmp = *tmp_ptr;
    }
    GETDESC(basic);
    if (errconv) { 
        if (not((SWIG_ConvertPtr(input, (void **) &btmp, basicdescr,0)) == -1)) {
            errconv = false;
            tmp =(*btmp).eval(); 
        }
    }
    GETDESC(symbol);
    if (errconv) { 
        if (not((SWIG_ConvertPtr(input, (void **) &stmp, symboldescr,0)) == -1)) {
            errconv = false;
            tmp =(*stmp).eval(); 
        }
    }
    GETDESC(numeric);
    if (errconv) { 
        if (not((SWIG_ConvertPtr(input, (void **) &ntmp, numericdescr, 0)) == -1)) {
            errconv = false;
            tmp =(*ntmp).eval(); 
        }
    }
    if (errconv) { 
        if (PyInt_Check(input)) {
            errconv = false;
            itmp = PyInt_AsLong(input);
            tmp =numeric(itmp).eval();
        }
    }
    if (errconv) { 
        if (PyFloat_Check(input)) {
            errconv = false;
            dtmp = PyFloat_AsDouble(input);
            tmp =numeric(dtmp).eval(); 
        }
    }
    if (errconv) { 
        if (PyList_Check(input)) {
            errconv = false;
            lst *l=list2lst(input);
            if (l==NULL) {
                return NULL;
            }
            tmp=l->eval();
        }
    }
    if (errconv) 
        return NULL;
    else {
        tmp_ptr = new ex(tmp);
        return tmp_ptr;
    }
} 

bool checktype2ex(PyObject * input) {
    //we assume, that everything can be converted to ex. 
    //if you find some counterexample, write test for it first (which fail)
    //and then implement it here.
    return true;
}

#define EX2(NAME) \
case TINFO_##NAME: {\
    NAME *p = new NAME(ex_to<NAME>(*input));\
    GETDESC(NAME);\
    return SWIG_NewPointerObj((void *)p, NAME##descr, 1);\
}

//unwraps ex and return python object
PyObject * ex2type(const ex * input) {
    switch (ex_to<basic>(*input).tinfo()) {
        EX2(basic)
        EX2(expairseq)
        EX2(add)
        EX2(mul)
        EX2(symbol)
        EX2(constant)
        //EX2(exprseq)
        EX2(function)
        //EX2(fderivative)
        EX2(ncmul)
        case TINFO_lst: {
            lst *l = new lst(ex_to<lst>(*input));
            return lst2list(l);
        }
        EX2(matrix)
        EX2(power)
        EX2(relational)
        //EX2(fail)
        EX2(numeric)
        EX2(pseries)
        EX2(indexed)
        //EX2(color)
        EX2(clifford)
        EX2(idx)
        EX2(varidx)
        EX2(spinidx)
        EX2(tensor)
        EX2(tensdelta)
        EX2(tensmetric)
        EX2(minkmetric)
        EX2(spinmetric)
        EX2(tensepsilon)
        //EX2(su3one)
        //EX2(su3t)
        //EX2(su3f)
        //EX2(su3d)
        EX2(diracone)
        EX2(diracgamma)
        EX2(diracgamma5)
        EX2(diracgammaL)
        EX2(diracgammaR)
        EX2(wildcard)
        EX2(symmetry)
        EX2(integral)
        EX2(cliffordunit)
        default:
            throw (std::logic_error("Cannot unwrap ex. Fix in ex.i"));
    }
}

//converts ginac lst to python list (unwrapping all exs)
PyObject *lst2list(lst *input) {
    lst::const_iterator i = input->begin();
    lst::const_iterator i_end = input->end();
    PyObject *pylist = PyList_New(0);
    while (i!=i_end) {
        PyObject *item = ex2type(&(*i));
        PyList_Append(pylist, item);
        //is this necessary?
        Py_INCREF(item);
        i++;
    }
    return (pylist);
}

/*
PyObject *lst2list(lst *input) {
    lst *l = input;
    int n = l->nops(); 
    PyObject *pylist = PyList_New(n);
    PyObject *item;
    for (int i=0;i<n;i++) {
        item = ex2type(&(l->let_op(i)));
        PyList_SetItem(pylist, i, item);
        Py_INCREF(item);
    }
    return (pylist);
}*/

//convert any python list to ginac lst
lst* list2lst(PyObject * input)
{
    lst *out=new lst();
    if PyList_Check(input) {
        int n = PyList_Size(input);
        PyObject *item;
        ex *tmp;
        for (int i = 0; i<n;i++) {
            item = PyList_GetItem(input, i);
            tmp = type2ex(item);
            if (tmp) {
                out->append(*tmp);
            } else {
                PyErr_SetString(PyExc_ValueError,"Cannot convert type to ex.");
                return NULL;
            }
        }
        return out;
    }
    else {
        PyErr_SetString(PyExc_ValueError,"List expected.");
        delete out;
        return NULL;
    }
}

//converts ginac exvector to python list (unwrapping all exs)
PyObject *exvector2list(exvector *input) {
    exvector::const_iterator i = input->begin();
    exvector::const_iterator i_end = input->end();
    PyObject *pylist = PyList_New(0);
    while (i!=i_end) {
        PyObject *item = ex2type(&(*i));
        PyList_Append(pylist, item);
        //is this necessary?
        Py_INCREF(item);
        i++;
    }
    return (pylist);
}

%}

// vim:ft=cpp:
