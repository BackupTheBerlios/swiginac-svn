%module add

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "add.h"
%}
%include "expairseq.i"


#ifndef __GINAC_ADD_H__
#define __GINAC_ADD_H__

#include "expairseq.h"

namespace GiNaC {

/** Sum of expressions. */
class add : public expairseq
{
	GINAC_DECLARE_REGISTERED_CLASS(add, expairseq)
	
	friend class mul;
	friend class power;
	
	// other constructors
public:
	add(const ex & lh, const ex & rh);
	add(const exvector & v);
	add(const epvector & v);
	add(const epvector & v, const ex & oc);
	add(std::auto_ptr<epvector> vp, const ex & oc);
	
	// functions overriding virtual functions from base classes
public:
	unsigned precedence() const {return 40;}
	bool info(unsigned inf) const;
	int degree(const ex & s) const;
	int ldegree(const ex & s) const;
	ex coeff(const ex & s, int n=1) const;
	ex eval(int level=0) const;
	ex evalm() const;
	ex series(const relational & r, int order, unsigned options = 0) const;
	ex normal(exmap & repl, exmap & rev_lookup, int level=0) const;
	numeric integer_content() const;
	ex smod(const numeric &xi) const;
	numeric max_coefficient() const;
	ex conjugate() const;
	exvector get_free_indices() const;
	ex eval_ncmul(const exvector & v) const;
protected:
	ex derivative(const symbol & s) const;
	unsigned return_type() const;
	unsigned return_type_tinfo() const;
	ex thisexpairseq(const epvector & v, const ex & oc) const;
	ex thisexpairseq(std::auto_ptr<epvector> vp, const ex & oc) const;
	expair split_ex_to_pair(const ex & e) const;
	expair combine_ex_with_coeff_to_pair(const ex & e,
	                                     const ex & c) const;
	expair combine_pair_with_coeff_to_pair(const expair & p,
	                                       const ex & c) const;
	ex recombine_pair_to_ex(const expair & p) const;
	ex expand(unsigned options=0) const;

	// non-virtual functions in this class
protected:
	void print_add(const print_context & c, const char *openbrace, const char *closebrace, const char *mul_sym, unsigned level) const;
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
	void do_print_csrc(const print_csrc & c, unsigned level) const;
	void do_print_python_repr(const print_python_repr & c, unsigned level) const;
};

// utility functions

/** Specialization of is_exactly_a<add>(obj) for add objects. */
template<> inline bool is_exactly_a<add>(const basic & obj)
{
	return obj.tinfo()==TINFO_add;
}

} // namespace GiNaC

#endif // ndef __GINAC_ADD_H__
