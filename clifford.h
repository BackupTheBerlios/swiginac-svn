/** @file clifford.h
 *
 *  Interface to GiNaC's clifford algebra (Dirac gamma) objects. */

/*
 *  GiNaC Copyright (C) 1999-2004 Johannes Gutenberg University Mainz, Germany
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#ifndef __GINAC_CLIFFORD_H__
#define __GINAC_CLIFFORD_H__

#include "indexed.h"
#include "tensor.h"

#include <set>

namespace GiNaC {


/** This class holds an object representing an element of the Clifford
 *  algebra (the Dirac gamma matrices). These objects only carry Lorentz
 *  indices. Spinor indices are hidden. A representation label (an unsigned
 *  8-bit integer) is used to distinguish elements from different Clifford
 *  algebras (objects with different labels commutate). */
class clifford : public indexed
{
	GINAC_DECLARE_REGISTERED_CLASS(clifford, indexed)

	// other constructors
public:
	clifford(const ex & b, unsigned char rl = 0);
	clifford(const ex & b, const ex & mu, unsigned char rl = 0);

	// internal constructors
	clifford(unsigned char rl, const exvector & v, bool discardable = false);
	clifford(unsigned char rl, std::auto_ptr<exvector> vp);

	// functions overriding virtual functions from base classes
protected:
	ex eval_ncmul(const exvector & v) const;
	bool match_same_type(const basic & other) const;
	ex thiscontainer(const exvector & v) const;
	ex thiscontainer(std::auto_ptr<exvector> vp) const;
	unsigned return_type() const { return return_types::noncommutative; }
	unsigned return_type_tinfo() const { return TINFO_clifford + representation_label; }

	// non-virtual functions in this class
public:
	unsigned char get_representation_label() const {return representation_label;}

protected:
	void do_print_dflt(const print_dflt & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;

	// member variables
private:
	unsigned char representation_label; /**< Representation label to distinguish independent spin lines */
};


/** This class represents the Clifford algebra unity element. */
class diracone : public tensor
{
	GINAC_DECLARE_REGISTERED_CLASS(diracone, tensor)

	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
};


/** This class represents the Dirac gamma Lorentz vector. */
class diracgamma : public tensor
{
	GINAC_DECLARE_REGISTERED_CLASS(diracgamma, tensor)

	// functions overriding virtual functions from base classes
public:
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;

	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
};


/** This class represents the Dirac gamma5 object which anticommutates with
 *  all other gammas. */
class diracgamma5 : public tensor
{
	GINAC_DECLARE_REGISTERED_CLASS(diracgamma5, tensor)

	// functions overriding virtual functions from base classes
	ex conjugate() const;

	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
};


/** This class represents the Dirac gammaL object which behaves like
 *  1/2 (1-gamma5). */
class diracgammaL : public tensor
{
	GINAC_DECLARE_REGISTERED_CLASS(diracgammaL, tensor)

	// functions overriding virtual functions from base classes
	ex conjugate() const;

	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
};


/** This class represents the Dirac gammaL object which behaves like
 *  1/2 (1+gamma5). */
class diracgammaR : public tensor
{
	GINAC_DECLARE_REGISTERED_CLASS(diracgammaR, tensor)

	// functions overriding virtual functions from base classes
	ex conjugate() const;

	// non-virtual functions in this class
protected:
	void do_print(const print_context & c, unsigned level) const;
	void do_print_latex(const print_latex & c, unsigned level) const;
};


// global functions

/** Specialization of is_exactly_a<clifford>(obj) for clifford objects. */
template<> inline bool is_exactly_a<clifford>(const basic & obj)
{
	return obj.tinfo()==TINFO_clifford;
}

/** Create a Clifford unity object.
 *
 *  @param rl Representation label
 *  @return newly constructed object */
ex dirac_ONE(unsigned char rl = 0);

/** Create a Dirac gamma object.
 *
 *  @param mu Index (must be of class varidx or a derived class)
 *  @param rl Representation label
 *  @return newly constructed gamma object */
ex dirac_gamma(const ex & mu, unsigned char rl = 0);

/** Create a Dirac gamma5 object.
 *
 *  @param rl Representation label
 *  @return newly constructed object */
ex dirac_gamma5(unsigned char rl = 0);

/** Create a Dirac gammaL object.
 *
 *  @param rl Representation label
 *  @return newly constructed object */
ex dirac_gammaL(unsigned char rl = 0);

/** Create a Dirac gammaR object.
 *
 *  @param rl Representation label
 *  @return newly constructed object */
ex dirac_gammaR(unsigned char rl = 0);

/** Create a term of the form e_mu * gamma~mu with a unique index mu.
 *
 *  @param e Original expression
 *  @param dim Dimension of index
 *  @param rl Representation label */
ex dirac_slash(const ex & e, const ex & dim, unsigned char rl = 0);

/** Calculate dirac traces over the specified set of representation labels.
 *  The computed trace is a linear functional that is equal to the usual
 *  trace only in D = 4 dimensions. In particular, the functional is not
 *  always cyclic in D != 4 dimensions when gamma5 is involved.
 *
 *  @param e Expression to take the trace of
 *  @param rls Set of representation labels
 *  @param trONE Expression to be returned as the trace of the unit matrix */
ex dirac_trace(const ex & e, const std::set<unsigned char> & rls, const ex & trONE = 4);

/** Calculate dirac traces over the specified list of representation labels.
 *  The computed trace is a linear functional that is equal to the usual
 *  trace only in D = 4 dimensions. In particular, the functional is not
 *  always cyclic in D != 4 dimensions when gamma5 is involved.
 *
 *  @param e Expression to take the trace of
 *  @param rll List of representation labels
 *  @param trONE Expression to be returned as the trace of the unit matrix */
ex dirac_trace(const ex & e, const lst & rll, const ex & trONE = 4);

/** Calculate the trace of an expression containing gamma objects with
 *  a specified representation label. The computed trace is a linear
 *  functional that is equal to the usual trace only in D = 4 dimensions.
 *  In particular, the functional is not always cyclic in D != 4 dimensions
 *  when gamma5 is involved.
 *
 *  @param e Expression to take the trace of
 *  @param rl Representation label
 *  @param trONE Expression to be returned as the trace of the unit matrix */
ex dirac_trace(const ex & e, unsigned char rl = 0, const ex & trONE = 4);

/** Bring all products of clifford objects in an expression into a canonical
 *  order. This is not necessarily the most simple form but it will allow
 *  to check two expressions for equality. */
ex canonicalize_clifford(const ex & e);

} // namespace GiNaC

#endif // ndef __GINAC_CLIFFORD_H__
