%module matrix

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


#ifndef __GINAC_MATRIX_H__
#define __GINAC_MATRIX_H__


/** Symbolic matrices. */
class matrix : public basic
{
//	GINAC_DECLARE_REGISTERED_CLASS(matrix, basic)
	
	// other constructors
public:
	matrix(unsigned r, unsigned c);
	//matrix(unsigned r, unsigned c, const exvector & m2);
	matrix(unsigned r, unsigned c, const lst & l);
	//matrix(const lst & l);
	//size_t nops() const;
	//ex op(size_t i) const;
	//ex & let_op(size_t i);
	//ex eval(int level=0) const;
	//ex evalm() const {return *this;}
//	ex subs(const exmap & m, unsigned options = 0) const;
	ex eval_indexed(const basic & i) const;
	ex add_indexed(const ex & self, const ex & other) const;
	ex scalar_mul_indexed(const ex & self, const numeric & other) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
	//ex conjugate() const;
	unsigned rows() const;
	unsigned cols() const;
	matrix add(const matrix & other) const;
	matrix sub(const matrix & other) const;
	matrix mul(const matrix & other) const;
	matrix mul(const numeric & other) const;
	matrix mul_scalar(const ex & other) const;
	matrix pow(const ex & expn) const;
	const ex & operator() (unsigned ro, unsigned co) const;
	ex & operator() (unsigned ro, unsigned co);
	matrix & set(unsigned ro, unsigned co, const ex & value) { (*this)(ro, co) = value; return *this; }
	matrix transpose() const;
	ex determinant(unsigned algo = determinant_algo::automatic) const;
	ex trace() const;
	ex charpoly(const ex & lambda) const;
	matrix inverse() const throw(std::runtime_error);
	matrix solve(const matrix & vars, const matrix & rhs, unsigned algo = solve_algo::automatic) const;
	unsigned rank() const;

%extend {
    std::string __repr__() {
        std::ostringstream out;
        out << *self;
        return out.str();
    }
	/*matrix(const lst & l) {
    }
    */
    /*void __setitem__(int idx0, int idx1, basic &e) {
        (*self)(idx0, idx1) = e;
    }*/
    void __setitem__(int idx0, int idx1, ex &e) {
        (*self)(idx0, idx1) = e;
    }

    ex __getitem__(int idx0, int idx1) {
        return (*self)(idx0, idx1);
    }
}

};

%pythoncode %{
    def matrix2(x):
        return lst_to_matrix(x)
%}

inline size_t nops(const matrix & m);
//inline ex expand(const matrix & m, unsigned options = 0);
inline ex eval(const matrix & m, int level = 0);
inline ex evalf(const matrix & m, int level = 0);
inline unsigned rows(const matrix & m);
inline unsigned cols(const matrix & m);
inline matrix transpose(const matrix & m);
inline ex determinant(const matrix & m, unsigned options = determinant_algo::automatic);
inline ex trace(const matrix & m);
inline ex charpoly(const matrix & m, const ex & lambda);
inline matrix inverse(const matrix & m);
inline unsigned rank(const matrix & m);


/** Specialization of is_exactly_a<matrix>(obj) for matrix objects. */
template<> inline bool is_exactly_a<matrix>(const basic & obj);
extern ex lst_to_matrix(const lst & l);
extern ex diag_matrix(const lst & l);
extern ex unit_matrix(unsigned r, unsigned c);
inline ex unit_matrix(unsigned x);
extern ex symbolic_matrix(unsigned r, unsigned c, const std::string & base_name, const std::string & tex_base_name);
inline ex symbolic_matrix(unsigned r, unsigned c, const std::string & base_name);


#endif // ndef __GINAC_MATRIX_H__

// vim:ft=cpp:
