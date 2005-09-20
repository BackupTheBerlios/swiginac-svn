%module integral

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





class integral : public basic
{
public:
	integral(const ex & x_, const ex & a_, const ex & b_, const ex & f_);
	unsigned precedence() const {return 45;}
	ex eval(int level=0) const;
	ex evalf(int level=0) const;
	int degree(const ex & s) const;
	int ldegree(const ex & s) const;
	ex eval_ncmul(const exvector & v) const;
	size_t nops() const;
	ex op(size_t i) const;
	ex & let_op(size_t i);
	ex expand(unsigned options = 0) const;
	exvector get_free_indices() const;
	unsigned return_type() const;
	unsigned return_type_tinfo() const;
	ex conjugate() const;
	ex eval_integ() const;
	static int max_integration_level;
	static ex relative_integration_error;
};

// utility functions

/** Specialization of is_exactly_a<integral>(obj) for integral objects. */
template<> inline bool is_exactly_a<integral>(const basic & obj);

GiNaC::ex adaptivesimpson(
	const GiNaC::ex &x,
	const GiNaC::ex &a,
	const GiNaC::ex &b,
	const GiNaC::ex &f,
	const GiNaC::ex &error = integral::relative_integration_error
);

// vim:ft=cpp:

