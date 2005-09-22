%module function

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

#ifndef __GINAC_FUNCTION_H__
#define __GINAC_FUNCTION_H__



#define REGISTER_FUNCTION(NAME,OPT) \
unsigned NAME##_SERIAL::serial = \
	GiNaC::function::register_new(GiNaC::function_options(#NAME, NAME##_NPARAMS).OPT);


class function;
class symmetry;

typedef ex (* eval_funcp)();
typedef ex (* evalf_funcp)();
typedef ex (* conjugate_funcp)();
typedef ex (* derivative_funcp)();
typedef ex (* series_funcp)();
typedef void (* print_funcp)();

// the following lines have been generated for max. 14 parameters
typedef ex (* eval_funcp_1)(const ex &);
typedef ex (* eval_funcp_2)(const ex &, const ex &);
typedef ex (* eval_funcp_3)(const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_4)(const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_6)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_7)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_8)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_9)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_10)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_11)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_12)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_13)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* eval_funcp_14)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);

typedef ex (* evalf_funcp_1)(const ex &);
typedef ex (* evalf_funcp_2)(const ex &, const ex &);
typedef ex (* evalf_funcp_3)(const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_4)(const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_6)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_7)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_8)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_9)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_10)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_11)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_12)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_13)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);
typedef ex (* evalf_funcp_14)(const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &, const ex &);

typedef ex (* conjugate_funcp_1)(const ex &);
typedef ex (* conjugate_funcp_2)(const ex &, const ex &);
typedef ex (* conjugate_funcp_3)(const ex &, const ex &, const ex &);
typedef ex (* conjugate_funcp_4)(const ex &, const ex &, const ex &, const ex &);
typedef ex (* conjugate_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &);

typedef ex (* derivative_funcp_1)(const ex &, unsigned);
typedef ex (* derivative_funcp_2)(const ex &, const ex &, unsigned);
typedef ex (* derivative_funcp_3)(const ex &, const ex &, const ex &, unsigned);
typedef ex (* derivative_funcp_4)(const ex &, const ex &, const ex &, const ex &, unsigned);
typedef ex (* derivative_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &, unsigned);

typedef ex (* series_funcp_1)(const ex &, const relational &, int, unsigned);
typedef ex (* series_funcp_2)(const ex &, const ex &, const relational &, int, unsigned);
typedef ex (* series_funcp_3)(const ex &, const ex &, const ex &, const relational &, int, unsigned);
typedef ex (* series_funcp_4)(const ex &, const ex &, const ex &, const ex &, const relational &, int, unsigned);
typedef ex (* series_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &, const relational &, int, unsigned);

typedef void (* print_funcp_1)(const ex &, const print_context &);
typedef void (* print_funcp_2)(const ex &, const ex &, const print_context &);
typedef void (* print_funcp_3)(const ex &, const ex &, const ex &, const print_context &);
typedef void (* print_funcp_4)(const ex &, const ex &, const ex &, const ex &, const print_context &);
typedef void (* print_funcp_5)(const ex &, const ex &, const ex &, const ex &, const ex &, const print_context &);


// Alternatively, an exvector may be passed into the static function, instead
// of individual ex objects.  Then, the number of arguments is not limited.
typedef ex (* eval_funcp_exvector)(const exvector &);
typedef ex (* evalf_funcp_exvector)(const exvector &);
typedef ex (* conjugate_funcp_exvector)(const exvector &);
typedef ex (* derivative_funcp_exvector)(const exvector &, unsigned);
typedef ex (* series_funcp_exvector)(const exvector &, const relational &, int, unsigned);
typedef void (* print_funcp_exvector)(const exvector &, const print_context &);


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

protected:
	bool has_derivative() const { return derivative_f != NULL; }
	void test_and_set_nparams(unsigned n);
	void set_print_func(unsigned id, print_funcp f);

	std::string name;
	std::string TeX_name;

	unsigned nparams;

	eval_funcp eval_f;
	evalf_funcp evalf_f;
	conjugate_funcp conjugate_f;
	derivative_funcp derivative_f;
	series_funcp series_f;
	std::vector<print_funcp> print_dispatch_table;

	bool evalf_params_first;

	bool use_return_type;
	unsigned return_type;
	unsigned return_type_tinfo;

	bool use_remember;
	unsigned remember_size;
	unsigned remember_assoc_size;
	unsigned remember_strategy;

	bool eval_use_exvector_args;
	bool evalf_use_exvector_args;
	bool conjugate_use_exvector_args;
	bool derivative_use_exvector_args;
	bool series_use_exvector_args;
	bool print_use_exvector_args;

	unsigned functions_with_same_name;

	ex symtree;
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

	// CINT has a linking problem
#ifndef __MAKECINT__
//	friend void ginsh_get_ginac_functions();
#endif // def __MAKECINT__

	friend class remember_table_entry;
	// friend class remember_table_list;
	// friend class remember_table;

// member functions

	// other constructors
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
public:
	unsigned precedence() const {return 70;}
	ex expand(unsigned options=0) const;
	ex eval(int level=0) const;
	ex evalf(int level=0) const;
	unsigned calchash() const;
	ex series(const relational & r, int order, unsigned options = 0) const;
	ex thiscontainer(const exvector & v) const;
//	ex thiscontainer(std::auto_ptr<exvector> vp) const;
	ex conjugate() const;
protected:
	ex derivative(const symbol & s) const;
	bool is_equal_same_type(const basic & other) const;
	bool match_same_type(const basic & other) const;
	unsigned return_type() const;
	unsigned return_type_tinfo() const;
	
	// new virtual functions which can be overridden by derived classes
	// none
	
	// non-virtual functions in this class
protected:
	ex pderivative(unsigned diff_param) const; // partial differentiation
	static std::vector<function_options> & registered_functions();
	bool lookup_remember_table(ex & result) const;
	void store_remember_table(ex const & result) const;
public:
	static unsigned register_new(function_options const & opt);
	static unsigned current_serial;
	static unsigned find_function(const std::string &name, unsigned nparams);
	unsigned get_serial() const {return serial;}
	std::string get_name() const;

// member variables

protected:
	unsigned serial;
};

// utility functions/macros

/** Specialization of is_exactly_a<function>(obj) for objects of type function. */
template<> inline bool is_exactly_a<function>(const basic & obj)
{
	return obj.tinfo()==TINFO_function;
}

template <typename T>
inline bool is_the_function(const ex & x)
{
	return is_exactly_a<function>(x)
	    && ex_to<function>(x).get_serial() == T::serial;
}

// Check whether OBJ is the specified symbolic function.
#define is_ex_the_function(OBJ, FUNCNAME) (GiNaC::is_the_function<FUNCNAME##_SERIAL>(OBJ))

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

#endif // ndef __GINAC_FUNCTION_H__

// vim:ft=cpp: