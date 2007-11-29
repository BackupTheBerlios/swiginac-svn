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

class clifford : public indexed
{
public:
    clifford(const ex & b, unsigned char rl = 0);
    clifford(const ex & b, const ex & mu,  const ex & metr, unsigned char rl = 0, int comm_sign=-1);
    unsigned precedence() const;
    unsigned char get_representation_label() const;
    ex get_metric() const;
    ex get_metric(const ex & i, const ex & j, bool symmetrised=false) const;
    bool same_metric(const ex & other) const;
    int get_commutator_sign() const;
    size_t nops() const;
    ex op(size_t i) const;
    ex & let_op(size_t i);
    ex subs(const exmap & m, unsigned options = 0) const;
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


class diracgamma5 : public tensor {
    ex conjugate() const;
};


class diracgammaL : public tensor {
    ex conjugate() const;
};


class diracgammaR : public tensor {
    ex conjugate() const;
};


bool is_clifford_tinfo(tinfo_t ti);

ex dirac_ONE(unsigned char rl = 0);
ex clifford_unit(const ex & mu, const ex & metr, unsigned char rl = 0);
ex dirac_gamma(const ex & mu, unsigned char rl = 0);
ex dirac_gamma5(unsigned char rl = 0);
ex dirac_gammaL(unsigned char rl = 0);
ex dirac_gammaR(unsigned char rl = 0);
ex dirac_slash(const ex & e, const ex & dim, unsigned char rl = 0);
ex dirac_trace(const ex & e, const std::set<unsigned char> & rls, const ex & trONE = 4);
ex dirac_trace(const ex & e, const lst & rll, const ex & trONE = 4);
ex dirac_trace(const ex & e, unsigned char rl = 0, const ex & trONE = 4);
ex canonicalize_clifford(const ex & e);
ex clifford_prime(const ex & e);
ex clifford_bar(const ex & e);
ex clifford_star(const ex & e);
ex remove_dirac_ONE(const ex & e, unsigned char rl = 0, unsigned options = 0);
char clifford_max_label(const ex & e, bool ignore_ONE = false);
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
