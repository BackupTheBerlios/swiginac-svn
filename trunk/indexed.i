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

class scalar_products;
class symmetry;

class indexed// : public exprseq
{
	friend ex simplify_indexed(const ex & e, exvector & free_indices, exvector & dummy_indices, const scalar_products & sp);
	friend ex simplify_indexed_product(const ex & e, exvector & free_indices, exvector & dummy_indices, const scalar_products & sp);
	friend bool reposition_dummy_indices(ex & e, exvector & variant_dummy_indices, exvector & moved_indices);

public:
	indexed(const ex & b);
	indexed(const ex & b, const ex & i1);
	indexed(const ex & b, const ex & i1, const ex & i2);
	indexed(const ex & b, const ex & i1, const ex & i2, const ex & i3);
	indexed(const ex & b, const ex & i1, const ex & i2, const ex & i3, const ex & i4);
//	indexed(const ex & b, const symmetry & symm, const ex & i1, const ex & i2);
//	indexed(const ex & b, const symmetry & symm, const ex & i1, const ex & i2, const ex & i3);
//	indexed(const ex & b, const symmetry & symm, const ex & i1, const ex & i2, const ex & i3, const ex & i4);
//	indexed(const ex & b, const exvector & iv);
//	indexed(const ex & b, const symmetry & symm, const exvector & iv);
//	indexed(const symmetry & symm, const exprseq & es);
//	indexed(const symmetry & symm, const exvector & v, bool discardable = false);
	exvector get_free_indices() const;
	bool all_index_values_are(unsigned inf) const;
	exvector get_indices() const;
	exvector get_dummy_indices() const;
	exvector get_dummy_indices(const indexed & other) const;
	bool has_dummy_index_for(const ex & i) const;
	ex get_symmetry() const {return symtree;}
};


class spmapkey {
public:
	spmapkey() : dim(wild()) {}
	spmapkey(const ex & v1, const ex & v2, const ex & dim = wild());
	bool operator==(const spmapkey &other) const;
	bool operator<(const spmapkey &other) const;
	void debugprint() const;
};

typedef std::map<spmapkey, ex> spmap;

class scalar_products {
public:
	void add(const ex & v1, const ex & v2, const ex & sp);
	void add(const ex & v1, const ex & v2, const ex & dim, const ex & sp);
	void add_vectors(const lst & l, const ex & dim = wild());
	void clear();
	bool is_defined(const ex & v1, const ex & v2, const ex & dim) const;
	ex evaluate(const ex & v1, const ex & v2, const ex & dim) const;
	void debugprint() const;
};


template<> inline bool is_exactly_a<indexed>(const basic & obj);
exvector get_all_dummy_indices(const ex & e);
ex rename_dummy_indices_uniquely(const ex & a, const ex & b);
ex expand_dummy_sum(const ex & e, bool subs_idx = false);

// vim:ft=cpp:
