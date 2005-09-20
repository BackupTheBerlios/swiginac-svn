%module mul

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

#ifndef __GINAC_MUL_H__
#define __GINAC_MUL_H__

/** Product of expressions. */
class mul : public expairseq
{
	friend class add;
	friend class ncmul;
	friend class power;
	
public:
	mul(const ex & lh, const ex & rh);
	mul(const exvector & v);
	mul(const epvector & v);
//	mul(const epvector & v, const ex & oc);
//	mul(std::auto_ptr<epvector> vp, const ex & oc);
	mul(const ex & lh, const ex & mh, const ex & rh);
	unsigned precedence() const {return 50;}
	bool info(unsigned inf) const;
	int degree(const ex & s) const;
	int ldegree(const ex & s) const;
	ex coeff(const ex & s, int n = 1) const;
	ex eval(int level=0) const;
	ex evalf(int level=0) const;
	ex evalm() const;
	ex series(const relational & s, int order, unsigned options = 0) const;
//	ex normal(exmap & repl, exmap & rev_lookup, int level = 0) const;
	numeric integer_content() const;
	ex smod(const numeric &xi) const;
	numeric max_coefficient() const;
	exvector get_free_indices() const;
	ex algebraic_subs_mul(const exmap & m, unsigned options) const;
};

/** Specialization of is_exactly_a<mul>(obj) for mul objects. */
template<> inline bool is_exactly_a<mul>(const basic & obj)
{
	return obj.tinfo()==TINFO_mul;
}


#endif // ndef __GINAC_MUL_H__
// vim:ft=cpp:
