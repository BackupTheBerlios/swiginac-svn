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
    static swig_type_info *exdescr=0;
    if (!exdescr){
        exdescr=SWIG_TypeQuery("GiNaC::ex *");
        if (!exdescr) {
            PyErr_SetString(PyExc_ValueError,"Cannot get an ex descriptor. swiginac.i");
            return NULL;
        }
    }
    if (not((SWIG_ConvertPtr(input, (void **) &tmp_ptr, exdescr, 0)) == -1)) {
        errconv = false;
        tmp = *tmp_ptr;
    }
    static swig_type_info *basicdescr=0;
    if (!basicdescr){
        basicdescr=SWIG_TypeQuery("GiNaC::basic *");
        if (!basicdescr) {
            PyErr_SetString(PyExc_ValueError,"Cannot get a symbol descriptor. swiginac.i");
            return NULL;
        }
    }
    if (errconv) { 
        if (not((SWIG_ConvertPtr(input, (void **) &btmp, basicdescr,0)) == -1)) {
            errconv = false;
            tmp =(*btmp).eval(); 
        }
    }
    static swig_type_info *symboldescr=0;
    if (!symboldescr){
        symboldescr=SWIG_TypeQuery("GiNaC::symbol *");
        if (!symboldescr) {
            PyErr_SetString(PyExc_ValueError,"Cannot get a symbol descriptor. swiginac.i");
            return NULL;
        }
    }
    if (errconv) { 
        if (not((SWIG_ConvertPtr(input, (void **) &stmp, symboldescr,0)) == -1)) {
            errconv = false;
            tmp =(*stmp).eval(); 
        }
    }
    static swig_type_info *numericdescr=0;
    if (!numericdescr){
        numericdescr=SWIG_TypeQuery("GiNaC::numeric *");
        if (!numericdescr) {
            PyErr_SetString(PyExc_ValueError,"Cannot get a numeric descriptor. swiginac.i");
            return NULL;
        }
    }
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
    if (errconv) {
        return NULL;
    }
    else {
        tmp_ptr = new ex(tmp);
        return tmp_ptr;

    }
} 

bool checktype2ex(PyObject * input) {
    return true;
}

#define EX2(NAME) \
case TINFO_##NAME: {\
    NAME *p = new NAME(ex_to<NAME>(*input));\
    return SWIG_NewPointerObj((void *)p, SWIGTYPE_p_GiNaC__##NAME, 1);\
}

//unwraps ex and return python object
PyObject * ex2type(ex * input) {
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
        //EX2(pseries)
        EX2(indexed)
        //EX2(color)
        EX2(clifford)
        //EX2(idx)
        //EX2(varidx)
        //EX2(spinidx)
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
            throw (std::logic_error("Cannot unwrap ex."));
    }
}

//converts ginac lst to python list (unwrapping all exs)
PyObject *lst2list(lst *input) {
    lst *l = input;
    int n = l->nops(); 
    PyObject *pylist = PyList_New(n);
    PyObject *item;
    ex * tmp;
    static swig_type_info *descr = 0;
    descr = SWIG_TypeQuery("GiNaC::ex *");
    for (int i=0;i<n;i++) {
        // Set item
        tmp = &(l->let_op(i));
        item = ex2type(tmp);
        // add to list
        PyList_SetItem(pylist, i, item);
        Py_INCREF(item);
    }
    return (pylist);
}


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
%}

// vim:ft=cpp:
