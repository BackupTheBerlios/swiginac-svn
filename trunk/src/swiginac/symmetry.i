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

class symmetry : public basic
{
public:
	typedef enum {
		none,          
		symmetric,     
		antisymmetric, 
		cyclic         
	} symmetry_type;
	symmetry(unsigned i);
	symmetry(symmetry_type t, const symmetry &c1, const symmetry &c2);
	symmetry_type get_type() const {return type;}
	void set_type(symmetry_type t) {type = t;}
	symmetry &add(const symmetry &c);
	symmetry &add(const unsigned &c);
	void validate(unsigned n);
	bool has_symmetry() const {return type != none || !children.empty(); }
};

//set the typemaps only for the functions below and clear it afterwards
%typemap(in) symmetry & {
    $1=type2symmetry($input);
    if (!$1) return NULL;
}

%typemap(typecheck) symmetry & {
    $1 = (checktype2symmetry($input)) ? 1 : 0;
}

symmetry sy_none();
symmetry sy_none(const symmetry &c1, const symmetry &c2);
symmetry sy_none(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_none(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

symmetry sy_symm();
symmetry sy_symm(const symmetry &c1, const symmetry &c2);
symmetry sy_symm(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_symm(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

symmetry sy_anti();
symmetry sy_anti(const symmetry &c1, const symmetry &c2);
symmetry sy_anti(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_anti(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

symmetry sy_cycl();
symmetry sy_cycl(const symmetry &c1, const symmetry &c2);
symmetry sy_cycl(const symmetry &c1, const symmetry &c2, const symmetry &c3);
symmetry sy_cycl(const symmetry &c1, const symmetry &c2, const symmetry &c3, const symmetry &c4);

//clear the typemap
%typemap(in) symmetry &; 
%typemap(typecheck) symmetry &;

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

%{ 

symmetry * type2symmetry(PyObject * input) {
    symmetry *tmp_ptr;
    GETDESC(symmetry);
    if (not((SWIG_ConvertPtr(input, (void **) &tmp_ptr, symmetrydescr, 0)) 
                    == -1)) return tmp_ptr;
    if (PyInt_Check(input)) return new symmetry(PyInt_AsLong(input));
    return NULL;
} 

bool checktype2symmetry(PyObject * input) {
    if (PyInt_Check(input)) return true;
    symmetry *tmp_ptr;
    GETDESC(symmetry);
    return (SWIG_ConvertPtr(input, (void **) &tmp_ptr, symmetrydescr, 0)) != -1;
}

%}

// vim:ft=cpp:
