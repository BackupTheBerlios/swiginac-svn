%module swiginac

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "inifcns.h"
#include "idx.h"
%}

%typemap(out) GiNaC::basic {
 GiNaC::ex* tmp = new GiNaC::ex($1.evalf());
 $result = SWIG_NewPointerObj(tmp,SWIGTYPE_p_GiNaC__ex,0);
}


%include std_list.i
%include stl.i
%include "gprint.i"
%include "ptr.i"
%include "registrar.i"
%include "basic.i"
//%include "ex.i"
%include "normal.i"
%include "constant.i"
%include "container.i"

%extend GiNaC::container {
    void let_op(int i, ex& rh) {
        self->let_op(i) = rh;
    }

    void set_op(int i, ex& n) {
        self->let_op(i) = n;
    }
};


namespace GiNaC {
%template(ex_lst) container<std::list >;
}

typedef container<std::list> lst;

%include "lst.i"
%include "ex.i"
%include "matrix.i"
%include "numeric.i"
%include "power.i"
%include "relational.i"
%include "symbol.i"
%include "expairseq.i"
%include "add.i"
%include "mul.i"
%include "function.i"
%include "exprseq.i"
%include "inifcns.i"
%include "operators.i"

%template(exp_ex) exp<ex>;
%template(log_ex) log<ex>;
%template(sin_ex) sin<ex>;
%template(cos_ex) cos<ex>;
%template(tan_ex) tan<ex>;
%template(asin_ex) asin<ex>;
%template(acos_ex) acos<ex>;
%template(atan_ex) atan<ex>;
%template(sinh_ex) sinh<ex>;
%template(cosh_ex) cosh<ex>;
%template(tanh_ex) tanh<ex>;
%template(asinh_ex) asinh<ex>;
%template(acosh_ex) acosh<ex>;
%template(atanh_ex) atanh<ex>;
%template(Li2_ex) Li2<ex>;
%template(zeta_ex) zeta<ex>;
%template(lgamma_ex) lgamma<ex>;
%template(tgamma_ex) tgamma<ex>;
%template(psi_ex) psi<ex>;
%template(factorial_ex) factorial<ex>;
%template(binomial_ex_ex) binomial<ex,ex>;
%template(abs_ex) abs<ex>;


//%template(lst) GiNaC::container<std::list >;


%extend GiNaC::ex {
   double to_double() {
      if (is_a<numeric>(*self)) {
         numeric n = ex_to<numeric>(*self);
         return n.to_double();
      }
      return 0.0;
   }
}


