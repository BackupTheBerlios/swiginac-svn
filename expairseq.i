%module expairseq

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "expairseq.h"
%}
%include "basic.i"

#ifndef __GINAC_EXPAIRSEQ_H__
#define __GINAC_EXPAIRSEQ_H__

#include <vector>
#include <list>
#include <memory>
// CINT needs <algorithm> to work properly with <vector> and <list>
#include <algorithm>

#include "expair.h"

namespace GiNaC {

#define EXPAIRSEQ_USE_HASHTAB 0

typedef std::vector<expair> epvector;       ///< expair-vector
typedef epvector::iterator epp;             ///< expair-vector pointer
typedef std::list<epp> epplist;             ///< list of expair-vector pointers
typedef std::vector<epplist> epplistvector; ///< vector of epplist

epvector* conjugateepvector(const epvector&);

class expairseq : public basic
{
//	GINAC_DECLARE_REGISTERED_CLASS(expairseq, basic)

	// other constructors
public:
	expairseq(const ex & lh, const ex & rh);
	expairseq(const exvector & v);
	expairseq(const epvector & v, const ex & oc);
	expairseq(std::auto_ptr<epvector>, const ex & oc);
	
	// functions overriding virtual functions from base classes
public:
	unsigned precedence() const {return 10;}
	bool info(unsigned inf) const;
	size_t nops() const;
	ex op(size_t i) const;
	ex map(map_function & f) const;
	ex eval(int level=0) const;
	ex to_rational(exmap & repl) const;
	ex to_polynomial(exmap & repl) const;
	bool match(const ex & pattern, lst & repl_lst) const;
	ex subs(const exmap & m, unsigned options = 0) const;
	ex conjugate() const;
protected:
	bool is_equal_same_type(const basic & other) const;
	unsigned return_type() const;
	unsigned calchash() const;
	ex expand(unsigned options=0) const;
	
	// new virtual functions which can be overridden by derived classes
protected:
	virtual ex thisexpairseq(const epvector & v, const ex & oc) const;
	virtual ex thisexpairseq(std::auto_ptr<epvector> vp, const ex & oc) const;
	virtual void printseq(const print_context & c, char delim,
	                      unsigned this_precedence,
	                      unsigned upper_precedence) const;
	virtual void printpair(const print_context & c, const expair & p,
	                       unsigned upper_precedence) const;
	virtual expair split_ex_to_pair(const ex & e) const;
	virtual expair combine_ex_with_coeff_to_pair(const ex & e,
												 const ex & c) const;
	virtual expair combine_pair_with_coeff_to_pair(const expair & p,
												   const ex & c) const;
	virtual ex recombine_pair_to_ex(const expair & p) const;
	virtual bool expair_needs_further_processing(epp it);
	virtual ex default_overall_coeff() const;
	virtual void combine_overall_coeff(const ex & c);
	virtual void combine_overall_coeff(const ex & c1, const ex & c2);
	virtual bool can_make_flat(const expair & p) const;
	
	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_tree(const print_tree & c, unsigned level) const;
	void construct_from_2_ex_via_exvector(const ex & lh, const ex & rh);
	void construct_from_2_ex(const ex & lh, const ex & rh);
	void construct_from_2_expairseq(const expairseq & s1,
	                                const expairseq & s2);
	void construct_from_expairseq_ex(const expairseq & s,
	                                 const ex & e);
	void construct_from_exvector(const exvector & v);
	void construct_from_epvector(const epvector & v);
	void make_flat(const exvector & v);
	void make_flat(const epvector & v);
	void canonicalize();
	void combine_same_terms_sorted_seq();
#if EXPAIRSEQ_USE_HASHTAB
	void combine_same_terms();
	unsigned calc_hashtabsize(unsigned sz) const;
	unsigned calc_hashindex(const ex & e) const;
	void shrink_hashtab();
	void remove_hashtab_entry(epvector::const_iterator element);
	void move_hashtab_entry(epvector::const_iterator oldpos,
	                        epvector::iterator newpos);
	void sorted_insert(epplist & eppl, epvector::const_iterator elem);
	void build_hashtab_and_combine(epvector::iterator & first_numeric,
	                               epvector::iterator & last_non_zero,
	                               vector<bool> & touched,
	                               unsigned & number_of_zeroes);
	void drop_coeff_0_terms(epvector::iterator & first_numeric,
	                        epvector::iterator & last_non_zero,
	                        vector<bool> & touched,
	                        unsigned & number_of_zeroes);
	bool has_coeff_0() const;
	void add_numerics_to_hashtab(epvector::iterator first_numeric,
	                             epvector::const_iterator last_non_zero);
#endif // EXPAIRSEQ_USE_HASHTAB
	bool is_canonical() const;
	std::auto_ptr<epvector> expandchildren(unsigned options) const;
	std::auto_ptr<epvector> evalchildren(int level) const;
	std::auto_ptr<epvector> subschildren(const exmap & m, unsigned options = 0) const;
	
// member variables
	
protected:
	epvector seq;
	ex overall_coeff;
#if EXPAIRSEQ_USE_HASHTAB
	epplistvector hashtab;
	unsigned hashtabsize;
	unsigned hashmask;
	static unsigned maxhashtabsize;
	static unsigned minhashtabsize;
	static unsigned hashtabfactor;
#endif // EXPAIRSEQ_USE_HASHTAB
};

// utility functions

/** Specialization of is_exactly_a<expairseq>(obj) for expairseq objects. */
template<> inline bool is_exactly_a<expairseq>(const basic & obj)
{
	return obj.tinfo()==TINFO_expairseq;
}

} // namespace GiNaC

#endif // ndef __GINAC_EXPAIRSEQ_H__
