%module inifcns

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "function.h"
#include "ex.h"
%}

namespace GiNaC {

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

class zeta1_SERIAL { public: static unsigned serial; };
template<typename T1>
inline function zeta(const T1 & p1) {
	return function(zeta1_SERIAL::serial, ex(p1));
}
class zeta2_SERIAL { public: static unsigned serial; };
template<typename T1, typename T2>
inline function zeta(const T1 & p1, const T2 & p2) {
	return function(zeta2_SERIAL::serial, ex(p1), ex(p2));
}
class zeta_SERIAL;
template<> inline bool is_the_function<class zeta_SERIAL>(const ex & x)
{
	return is_the_function<zeta1_SERIAL>(x) || is_the_function<zeta2_SERIAL>(x);
}

DECLARE_FUNCTION_1P(lgamma)
DECLARE_FUNCTION_1P(tgamma)
DECLARE_FUNCTION_2P(beta)

class psi1_SERIAL { public: static unsigned serial; };
template<typename T1>
inline function psi(const T1 & p1) {
	return function(psi1_SERIAL::serial, ex(p1));
}
class psi2_SERIAL { public: static unsigned serial; };
template<typename T1, typename T2>
inline function psi(const T1 & p1, const T2 & p2) {
	return function(psi2_SERIAL::serial, ex(p1), ex(p2));
}
class psi_SERIAL;
template<> inline bool is_the_function<class psi_SERIAL>(const ex & x)
{
	return is_the_function<psi1_SERIAL>(x) || is_the_function<psi2_SERIAL>(x);
}
	
DECLARE_FUNCTION_1P(factorial)
DECLARE_FUNCTION_2P(binomial)
DECLARE_FUNCTION_1P(Order)

} // namespace GiNaC

