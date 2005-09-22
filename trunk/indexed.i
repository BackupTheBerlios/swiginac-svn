%module indexed

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
	unsigned precedence() const {return 55;}
	bool info(unsigned inf) const;
	ex eval(int level = 0) const;
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