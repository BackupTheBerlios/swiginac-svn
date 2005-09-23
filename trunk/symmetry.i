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

class sy_is_less;
class sy_swap;

class symmetry : public basic
{
public:
	typedef enum {
		none,          /**< no symmetry properties */
		symmetric,     /**< totally symmetric */
		antisymmetric, /**< totally antisymmetric */
		cyclic         /**< cyclic symmetry */
	} symmetry_type;
	symmetry(unsigned i);
	symmetry(symmetry_type t, const symmetry &c1, const symmetry &c2);
	symmetry_type get_type() const {return type;}
	void set_type(symmetry_type t) {type = t;}
	symmetry &add(const symmetry &c);
	void validate(unsigned n);
	bool has_symmetry() const {return type != none || !children.empty(); }
};

symmetry sy_none();
symmetry sy_none(const symmetry &c1, const symmetry &c2);
symmetry sy_none(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_none(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);
symmetry sy_none(const unsigned &c1, const unsigned &c2);
symmetry sy_none(const unsigned &c1, const unsigned &c2, const unsigned &c2);
symmetry sy_none(const unsigned &c1, const unsigned &c2, const unsigned &c2, const unsigned &c2);

symmetry sy_symm();
symmetry sy_symm(const symmetry &c1, const symmetry &c2);
symmetry sy_symm(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_symm(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);
symmetry sy_symm(const unsigned &c1, const unsigned &c2);
symmetry sy_symm(const unsigned &c1, const unsigned &c2, const unsigned &c2);
symmetry sy_symm(const unsigned &c1, const unsigned &c2, const unsigned &c2, const unsigned &c2);

symmetry sy_anti();
symmetry sy_anti(const symmetry &c1, const symmetry &c2);
symmetry sy_anti(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_anti(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

symmetry sy_cycl();
symmetry sy_cycl(const symmetry &c1, const symmetry &c2);
symmetry sy_cycl(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_cycl(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

const symmetry & not_symmetric();
const symmetry & symmetric2();
const symmetry & symmetric3();
const symmetry & symmetric4();
const symmetry & antisymmetric2();
const symmetry & antisymmetric3();
const symmetry & antisymmetric4();

extern int canonicalize(exvector::iterator v, const symmetry &symm);
ex symmetrize(const ex & e, exvector::const_iterator first, exvector::const_iterator last);
ex symmetrize(const ex & e, const exvector & v);

ex antisymmetrize(const ex & e, exvector::const_iterator first, exvector::const_iterator last);
ex antisymmetrize(const ex & e, const exvector & v);

ex symmetrize_cyclic(const ex & e, exvector::const_iterator first, exvector::const_iterator last);
ex symmetrize_cyclic(const ex & e, const exvector & v);

// vim:ft=cpp:
