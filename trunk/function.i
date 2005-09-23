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

class function;
class symmetry;

class function_options
{
	friend class function;
	friend class fderivative;
public:
	function_options();
	function_options(std::string const & n, std::string const & tn=std::string());
	function_options(std::string const & n, unsigned np);
	~function_options();
	void initialize();

	function_options & dummy() { return *this; }
	function_options & set_name(std::string const & n, std::string const & tn=std::string());
	function_options & latex_name(std::string const & tn);
// the following lines have been generated for max. 14 parameters
    function_options & eval_func(eval_funcp_1 e);
    function_options & eval_func(eval_funcp_2 e);
    function_options & eval_func(eval_funcp_3 e);
    function_options & eval_func(eval_funcp_4 e);
    function_options & eval_func(eval_funcp_5 e);

    function_options & evalf_func(evalf_funcp_1 ef);
    function_options & evalf_func(evalf_funcp_2 ef);
    function_options & evalf_func(evalf_funcp_3 ef);
    function_options & evalf_func(evalf_funcp_4 ef);
    function_options & evalf_func(evalf_funcp_5 ef);

    function_options & conjugate_func(conjugate_funcp_1 d);
    function_options & conjugate_func(conjugate_funcp_2 d);
    function_options & conjugate_func(conjugate_funcp_3 d);
    function_options & conjugate_func(conjugate_funcp_4 d);
    function_options & conjugate_func(conjugate_funcp_5 d);

    function_options & derivative_func(derivative_funcp_1 d);
    function_options & derivative_func(derivative_funcp_2 d);
    function_options & derivative_func(derivative_funcp_3 d);
    function_options & derivative_func(derivative_funcp_4 d);
    function_options & derivative_func(derivative_funcp_5 d);

    function_options & series_func(series_funcp_1 s);
    function_options & series_func(series_funcp_2 s);
    function_options & series_func(series_funcp_3 s);
    function_options & series_func(series_funcp_4 s);
    function_options & series_func(series_funcp_5 s);

    template <class Ctx> function_options & print_func(print_funcp_1 p)
    {
    	test_and_set_nparams(1);
    	set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
    	return *this;
    }
    template <class Ctx> function_options & print_func(print_funcp_2 p)
    {
    	test_and_set_nparams(2);
    	set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
    	return *this;
    }
    template <class Ctx> function_options & print_func(print_funcp_3 p)
    {
    	test_and_set_nparams(3);
    	set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
    	return *this;
    }
    template <class Ctx> function_options & print_func(print_funcp_4 p)
    {
    	test_and_set_nparams(4);
    	set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
    	return *this;
    }
    template <class Ctx> function_options & print_func(print_funcp_5 p)
    {
    	test_and_set_nparams(5);
    	set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
    	return *this;
    }
// end of generated lines
	function_options & eval_func(eval_funcp_exvector e);
	function_options & evalf_func(evalf_funcp_exvector ef);
	function_options & conjugate_func(conjugate_funcp_exvector d);
	function_options & derivative_func(derivative_funcp_exvector d);
	function_options & series_func(series_funcp_exvector s);

	template <class Ctx> function_options & print_func(print_funcp_exvector p)
	{
		print_use_exvector_args = true;
		set_print_func(Ctx::get_class_info_static().options.get_id(), print_funcp(p));
		return *this;
	}

	function_options & set_return_type(unsigned rt, unsigned rtt=0);
	function_options & do_not_evalf_params();
	function_options & remember(unsigned size, unsigned assoc_size=0,
	                            unsigned strategy=remember_strategies::delete_never);
	function_options & overloaded(unsigned o);
	function_options & set_symmetry(const symmetry & s);

	std::string get_name() const { return name; }
	unsigned get_nparams() const { return nparams; }

};


/** Exception class thrown by classes which provide their own series expansion
 *  to signal that ordinary Taylor expansion is safe. */
class do_taylor {};


/** The class function is used to implement builtin functions like sin, cos...
	and user defined functions */
//class function : public exprseq
//class function 
class function : public basic
{
public:
	function(unsigned ser);
	// the following lines have been generated for max. 14 parameters
    function(unsigned ser, const ex & param1);
    function(unsigned ser, const ex & param1, const ex & param2);
    function(unsigned ser, const ex & param1, const ex & param2, const ex & param3);
    function(unsigned ser, const ex & param1, const ex & param2, const ex & param3, const ex & param4);
    function(unsigned ser, const ex & param1, const ex & param2, const ex & param3, const ex & param4, const ex & param5);

	// end of generated lines
	//function(unsigned ser, const exprseq & es);
	//function(unsigned ser, const exvector & v, bool discardable = false);
//	function(unsigned ser, std::auto_ptr<exvector> vp);

	// functions overriding virtual functions from base classes
	unsigned precedence() const {return 70;}
	unsigned calchash() const;
	ex thiscontainer(const exvector & v) const;
//	ex thiscontainer(std::auto_ptr<exvector> vp) const;
	//ex conjugate() const;
	static unsigned register_new(function_options const & opt);
	static unsigned current_serial;
	static unsigned find_function(const std::string &name, unsigned nparams);
	unsigned get_serial() const {return serial;}
	std::string get_name() const;
};

//size_t nops(const ex & thisex);
//ex expand(const ex & thisex, unsigned options = 0);
ex conjugate(const ex & thisex);
bool has(const ex & thisex, const ex & pattern);
bool find(const ex & thisex, const ex & pattern, lst & found);
int degree(const ex & thisex, const ex & s);
int ldegree(const ex & thisex, const ex & s);
ex coeff(const ex & thisex, const ex & s, int n=1);
ex numer(const ex & thisex);
ex denom(const ex & thisex);
ex numer_denom(const ex & thisex);
ex normal(const ex & thisex, int level=0);
ex to_rational(const ex & thisex, lst & repl_lst);
//ex to_rational(const ex & thisex, exmap & repl);
//ex to_polynomial(const ex & thisex, exmap & repl);
ex to_polynomial(const ex & thisex, lst & repl_lst);
ex collect(const ex & thisex, const ex & s, bool distributed = false);
//ex eval(const ex & thisex, int level = 0);
//ex evalf(const ex & thisex, int level = 0);
ex evalm(const ex & thisex);
ex eval_integ(const ex & thisex);
ex diff(const ex & thisex, const symbol & s, unsigned nth = 1);
ex series(const ex & thisex, const ex & r, int order, unsigned options = 0);
bool match(const ex & thisex, const ex & pattern, lst & repl_lst);
//ex simplify_indexed(const ex & thisex, unsigned options = 0);
//ex simplify_indexed(const ex & thisex, const scalar_products & sp, unsigned options = 0);
ex symmetrize(const ex & thisex);
ex symmetrize(const ex & thisex, const lst & l);
ex antisymmetrize(const ex & thisex);
ex antisymmetrize(const ex & thisex, const lst & l);
ex symmetrize_cyclic(const ex & thisex);
ex symmetrize_cyclic(const ex & thisex, const lst & l);
ex op(const ex & thisex, size_t i);
ex lhs(const ex & thisex);
ex rhs(const ex & thisex);
//bool is_zero(const ex & thisex);
void swap(ex & e1, ex & e2);
//ex ex::subs(const exmap & m, unsigned options) const;
//ex subs(const ex & thisex, const exmap & m, unsigned options = 0);
ex subs(const ex & thisex, const lst & ls, const lst & lr, unsigned options = 0);
ex subs(const ex & thisex, const ex & e);
//this doesn't work. why?
//ex subs(const ex & thisex, const ex & e, unsigned options = 0);

ex sqrt(const ex & a);
//ex expand(const ex & thisex, unsigned options = 0);
ex expand(const ex & thisex);

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

// vim:ft=cpp:
