%module clifford 

class clifford : public indexed
{
public:
	clifford(const ex & b, unsigned char rl = 0);
	clifford(const ex & b, const ex & mu,  const ex & metr, unsigned char rl = 0);
//	clifford(unsigned char rl, const ex & metr, const exvector & v, bool discardable = false);
	unsigned precedence() const { return 65; }
	unsigned char get_representation_label() const { return representation_label; }
	ex get_metric() const { return metric; }
	ex get_metric(const ex & i, const ex & j) const;
	bool same_metric(const ex & other) const;
};


class diracone : public tensor {};

class cliffordunit : public tensor
{
public:
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


/** This class represents the Dirac gamma Lorentz vector. */
class diracgamma : public cliffordunit
{
public:
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class diracgamma5 : public tensor {};


class diracgammaL : public tensor {};


class diracgammaR : public tensor {};



template<> inline bool is_exactly_a<clifford>(const basic & obj);

ex dirac_ONE(unsigned char rl = 0);
ex clifford_unit(const ex & mu, const ex & metr, unsigned char rl = 0);
ex dirac_gamma(const ex & mu, unsigned char rl = 0);
ex dirac_gamma5(unsigned char rl = 0);
ex dirac_gammaL(unsigned char rl = 0);
ex dirac_gammaR(unsigned char rl = 0);
ex dirac_slash(const ex & e, const ex & dim, unsigned char rl = 0);
//ex dirac_trace(const ex & e, const std::set<unsigned char> & rls, const ex & trONE = 4);
ex dirac_trace(const ex & e, const lst & rll, const ex & trONE = 4);
//ex dirac_trace(const ex & e, unsigned char rl = 0, const ex & trONE = 4);
ex canonicalize_clifford(const ex & e);
ex clifford_prime(const ex & e);
inline ex clifford_bar(const ex & e);
inline ex clifford_star(const ex & e);
ex remove_dirac_ONE(const ex & e);
ex remove_dirac_ONE(const ex & e, unsigned char rl);
ex clifford_norm(const ex & e);
ex clifford_inverse(const ex & e);
ex lst_to_clifford(const ex & v, const ex & mu,  const ex & metr, unsigned char rl = 0);
ex lst_to_clifford(const ex & v, const ex & e);
lst clifford_to_lst(const ex & e, const ex & c, bool algebraic=true);
ex clifford_moebius_map(const ex & a, const ex & b, const ex & c, const ex & d, const ex & v, const ex & G, unsigned char rl);
ex clifford_moebius_map(const ex & a, const ex & b, const ex & c, const ex & d, const ex & v, const ex & G);
ex clifford_moebius_map(const ex & M, const ex & v, const ex & G, unsigned char rl);
ex clifford_moebius_map(const ex & M, const ex & v, const ex & G);

// vim:ft=cpp:

