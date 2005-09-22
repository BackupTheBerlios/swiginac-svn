%module swiginac
%include "std_string.i"

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
#include "ginac.h"
using namespace GiNaC;
#include <sstream>
%}


%include std_list.i
%include std_vector.i
%include stl.i
%include "ptr.i"


namespace GiNaC {

%{ 
lst* list2lst(PyObject *input);
PyObject* lst2list(lst *input); 

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
        /*
            std::cout << "*";
            ex *tmp = new ex(*input);
            //return SWIG_NewPointerObj((void *)tmp, $descriptor(GiNaC::ex *), 1);
            return SWIG_NewPointerObj((void *)tmp, SWIGTYPE_p_GiNaC__ex, 1);
            */
    }
}

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

%include "typemaps.i"

%include "registrar.i"

%include "basic.i"
%include "symbol.i"
%include "numeric.i"
%include "relational.i"

%include "normal.i"
%include "constant.i"
%include "container.i"

//do we need these 4 lines?
/*
%template(lst) container<std::list>;
%template(exprseq) container<std::vector>;
%include "exprseq.i"
%include "lst.i"
*/

%include "integral.i"
%include "matrix.i"
%include "expairseq.i"
%include "mul.i"
%include "ncmul.i"
%include "power.i"
%include "add.i"
%include "function.i"
%include "tensor.i"
%include "indexed.i"
%include "clifford.i"
%include "wildcard.i"


%define DECLARE_FUNCTION_1P(NAME) 
class NAME##_SERIAL { public: static unsigned serial; }; 
const unsigned NAME##_NPARAMS = 1; 
template<typename T1> const GiNaC::function NAME(const T1 & p1) { 
	return GiNaC::function(NAME##_SERIAL::serial, GiNaC::ex(p1)); 
}
%template(NAME##_ex) NAME<ex>;
%template(NAME##_basic) NAME<basic>;
%template(NAME##_int) NAME<int>;
%template(NAME##_double) NAME<double>;
%pythoncode %{
    def NAME(x):
        if isinstance(x,basic):
            return NAME##_basic(x).eval()
        elif isinstance(x,int):
            return NAME##_int(x).eval()
        elif isinstance(x,float):
            return NAME##_double(x).eval()
        else:
            raise "Unimplented type. Fix in main.i."
%}
%enddef

#define DECLARE_FUNCTION_2P(NAME) \
class NAME##_SERIAL { public: static unsigned serial; }; \
const unsigned NAME##_NPARAMS = 2; \
template<typename T1, typename T2> const GiNaC::function NAME(const T1 & p1, const T2 & p2) { \
	return GiNaC::function(NAME##_SERIAL::serial, GiNaC::ex(p1), GiNaC::ex(p2)); \
}

#define DECLARE_FUNCTION_3P(NAME) \
class NAME##_SERIAL { public: static unsigned serial; }; \
const unsigned NAME##_NPARAMS = 3; \
template<typename T1, typename T2, typename T3> const GiNaC::function NAME(const T1 & p1, const T2 & p2, const T3 & p3) { \
	return GiNaC::function(NAME##_SERIAL::serial, GiNaC::ex(p1), GiNaC::ex(p2), GiNaC::ex(p3)); \
}

DECLARE_FUNCTION_1P(conjugate_function)
DECLARE_FUNCTION_1P(abs)
DECLARE_FUNCTION_1P(csgn)
DECLARE_FUNCTION_2P(eta)
DECLARE_FUNCTION_1P(sin)
DECLARE_FUNCTION_1P(cos)
DECLARE_FUNCTION_1P(tan)
DECLARE_FUNCTION_1P(exp)
DECLARE_FUNCTION_1P(log)
DECLARE_FUNCTION_1P(asin)
DECLARE_FUNCTION_1P(acos)
DECLARE_FUNCTION_1P(atan)
DECLARE_FUNCTION_2P(atan2)
DECLARE_FUNCTION_1P(sinh)
DECLARE_FUNCTION_1P(cosh)
DECLARE_FUNCTION_1P(tanh)
DECLARE_FUNCTION_1P(asinh)
DECLARE_FUNCTION_1P(acosh)
DECLARE_FUNCTION_1P(atanh)
DECLARE_FUNCTION_1P(Li2)
DECLARE_FUNCTION_1P(Li3)
DECLARE_FUNCTION_2P(zetaderiv)
DECLARE_FUNCTION_2P(Li)
DECLARE_FUNCTION_3P(S)
DECLARE_FUNCTION_2P(H)
DECLARE_FUNCTION_1P(lgamma)
DECLARE_FUNCTION_1P(tgamma)
DECLARE_FUNCTION_2P(beta)
DECLARE_FUNCTION_1P(factorial)
DECLARE_FUNCTION_2P(binomial)
DECLARE_FUNCTION_1P(Order)


//do we need these two?
//%include "inifcns.i"
//%include "operators.i"

/*%extend ex {
   double to_double() {
      if (is_a<numeric>(*self)) {
         numeric n = ex_to<numeric>(*self);
         return n.to_double();
      }
      return 0.0;
   }
};*/

ex lsolve(lst&, lst&);
//extern ex collect_common_factors(const ex & e);
//extern ex sqrfree(const ex &a, const lst &l );

class subs_options {
    public:
        enum {
            no_pattern = 0x0001,
            subs_no_pattern = 0x0001,
            algebraic = 0x0002,
            subs_algebraic = 0x0002,
            pattern_is_product = 0x0004,
            pattern_is_not_product = 0x0008
        };
};

class determinant_algo {
public:
	enum {
		automatic,
		gauss,
		divfree,
		laplace,
		bareiss
	};
};

class info_flags {
public:
	enum {
		numeric,
		real,
		rational,
		integer,
		crational,
		cinteger,
		positive,
		negative,
		nonnegative,
		posint,
		negint,
		nonnegint,
		even,
		odd,
		prime,
		relation,
		relation_equal,
		relation_not_equal,
		relation_less,
		relation_less_or_equal,
		relation_greater,
		relation_greater_or_equal,
		symbol,
		list,
		exprseq,
		polynomial,
		integer_polynomial,
		cinteger_polynomial,
		rational_polynomial,
		crational_polynomial,
		rational_function,
		algebraic,
		indexed,  
		has_indices,
		idx
	};
};


};

%inline %{
namespace GiNaC {
    ex parse_string(const std::string &str, lst &ls) {
        return ex(str,ls);
    }
}
%};

// vim:ft=cpp:
