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

#define EXPAIRSEQ_USE_HASHTAB 0

typedef std::vector<expair> epvector;       ///< expair-vector
typedef epvector::iterator epp;             ///< expair-vector pointer
typedef std::list<epp> epplist;             ///< list of expair-vector pointers
typedef std::vector<epplist> epplistvector; ///< vector of epplist

epvector* conjugateepvector(const epvector&);

class expairseq : public basic
{
public:
	expairseq(const ex & lh, const ex & rh);
	expairseq(const exvector & v);
//	expairseq(const epvector & v, const ex & oc);
//	expairseq(std::auto_ptr<epvector>, const ex & oc);
	unsigned precedence() const {return 10;}
	//bool info(unsigned inf) const;
	//size_t nops() const;
	//ex op(size_t i) const;
	//ex map(map_function & f) const;
	//ex eval(int level=0) const;
	//ex to_rational(exmap & repl) const;
	//ex to_polynomial(exmap & repl) const;
	//bool match(const ex & pattern, lst & repl_lst) const;
	//ex subs(const exmap & m, unsigned options = 0) const;
	//ex conjugate() const;
};

// utility functions

/** Specialization of is_exactly_a<expairseq>(obj) for expairseq objects. */
template<> inline bool is_exactly_a<expairseq>(const basic & obj)
{
	return obj.tinfo()==TINFO_expairseq;
}

// vim:ft=cpp:
