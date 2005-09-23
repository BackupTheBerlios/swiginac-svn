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

%module swiginac

%{
#include "ginac.h"
using namespace GiNaC;
#include <sstream>
%}

%include std_string.i

namespace GiNaC {

%include "ex.i"

%include "ptr.i"
%include "typemaps.i"

%include "registrar.i"

%include "basic.i"
%include "symbol.i"
%include "numeric.i"
%include "relational.i"

%include "normal.i"
%include "constant.i"
%include "container.i"

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
