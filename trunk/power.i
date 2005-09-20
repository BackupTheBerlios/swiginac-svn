%module power

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

#ifndef __GINAC_POWER_H__
#define __GINAC_POWER_H__

class numeric;
class add;

class power : public basic
{
	friend class mul;
public:
	power(const ex & lh, const ex & rh) : inherited(TINFO_power), basis(lh), exponent(rh) {}
	template<typename T> power(const ex & lh, const T & rh) : inherited(TINFO_power), basis(lh), exponent(rh) {}
	unsigned precedence() const {return 60;}
	bool info(unsigned inf) const;
	size_t nops() const;
	ex op(size_t i) const;
	ex map(map_function & f) const;
	int degree(const ex & s) const;
	int ldegree(const ex & s) const;
	ex coeff(const ex & s, int n = 1) const;
	ex eval(int level=0) const;
	ex evalf(int level=0) const;
	ex evalm() const;
	ex series(const relational & s, int order, unsigned options = 0) const;
//	ex subs(const exmap & m, unsigned options = 0) const;
//	ex normal(exmap & repl, exmap & rev_lookup, int level = 0) const;
	ex to_rational(exmap & repl) const;
	ex to_polynomial(exmap & repl) const;
	exvector get_free_indices() const;
	ex conjugate() const;
};

#endif // ndef __GINAC_POWER_H__
// vim:ft=cpp:
