%module numeric

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%typemap(out) GiNaC::numeric {
 GiNaC::ex* tmp = new GiNaC::ex($1.eval());
 $result = SWIG_NewPointerObj(tmp,SWIGTYPE_p_GiNaC__ex,0);
 Py_INCREF($result);
}

%{
#include "numeric.h"
%}
%include "basic.i"
namespace GiNaC {

class numeric : public basic
{
public:
        numeric(int i);
//        numeric(long i);
        numeric(long numer, long denom);
        numeric(double d);
        numeric(const char *);
public:
        void print(const print_context & c, unsigned level = 0) const;
        ex coeff(const ex & s, int n = 1) const;
        ex eval(int level = 0) const;
        ex evalf(int level = 0) const;
public:
        const numeric add(const numeric &other) const;
        const numeric sub(const numeric &other) const;
        const numeric mul(const numeric &other) const;
        const numeric div(const numeric &other) const;
        const numeric power(const numeric &other) const;
//        const numeric & operator=(int i);
//        const numeric & operator=(unsigned int i);
//        const numeric & operator=(long i);
//        const numeric & operator=(unsigned long i);
//        const numeric & operator=(double d);
//        const numeric & operator=(const char *s);
        bool operator==(const numeric &other) const;
        bool operator!=(const numeric &other) const;
        bool operator<(const numeric &other) const;
        bool operator<=(const numeric &other) const;
        bool operator>(const numeric &other) const;
        bool operator>=(const numeric &other) const;
        int to_int(void) const;
        long to_long(void) const;
        double to_double(void) const;
        const numeric real(void) const;
        const numeric imag(void) const;
};


const numeric exp(const numeric &x);
const numeric log(const numeric &x);
const numeric sin(const numeric &x);
const numeric cos(const numeric &x);
const numeric tan(const numeric &x);
const numeric asin(const numeric &x);
const numeric acos(const numeric &x);
const numeric atan(const numeric &x);
const numeric atan(const numeric &y, const numeric &x);
const numeric sinh(const numeric &x);
const numeric cosh(const numeric &x);
const numeric tanh(const numeric &x);
const numeric asinh(const numeric &x);
const numeric acosh(const numeric &x);
const numeric atanh(const numeric &x);
const numeric Li2(const numeric &x);
const numeric zeta(const numeric &x);
const numeric lgamma(const numeric &x);
const numeric tgamma(const numeric &x);
const numeric psi(const numeric &x);
const numeric psi(const numeric &n, const numeric &x);
const numeric factorial(const numeric &n);
const numeric doublefactorial(const numeric &n);
const numeric binomial(const numeric &n, const numeric &k);
const numeric bernoulli(const numeric &n);
const numeric fibonacci(const numeric &n);
const numeric isqrt(const numeric &x);
const numeric sqrt(const numeric &x);
const numeric abs(const numeric &x);
const numeric mod(const numeric &a, const numeric &b);
const numeric smod(const numeric &a, const numeric &b);
const numeric irem(const numeric &a, const numeric &b);
const numeric irem(const numeric &a, const numeric &b, numeric &q);
const numeric iquo(const numeric &a, const numeric &b);
const numeric iquo(const numeric &a, const numeric &b, numeric &r);
const numeric gcd(const numeric &a, const numeric &b);
const numeric lcm(const numeric &a, const numeric &b);

%extend numeric {
numeric __add__(numeric& other) { return *self + other; }
numeric __sub__(numeric& other) { return *self - other; }
numeric __mul__(numeric& other) { return *self * other; }
numeric __div__(numeric& other) { return *self / other; }
numeric & __imul__(numeric& other) {
   *self *= other; return *self;
}
numeric & __isub(numeric& other) {
   *self -= other; return *self;
}
numeric & __iadd__(numeric& other) {
   *self += other; return *self;
}
numeric & __idiv(numeric& other) {
   *self /= other; return *self;
}
numeric __pos__() {
   return +*self;
}
numeric __neg__() {
   return -*self;
}
ex __call__() {
   return self->eval();
}
};


ex PiEvalf(void);
ex EulerEvalf(void);
ex CatalanEvalf(void);
}
