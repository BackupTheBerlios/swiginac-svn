# (c) Copyright 2006
#     Authors: Matti Peltomaki
#     based on regression tests for GiNaC,
#       Copyright (C) 1999-2006 Johannes Gutenberg University, Mainz
#     
#     This file is part of swiginac.
#
#     swiginac is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.
#
#     swiginac is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with swiginac; if not, write to the Free Software
#     Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import unittest
from swiginac import *

half = numeric(1,2)

def check_equal(e1, e2):
    e = normal(e1 - e2)
    if not e.is_zero():
        print "(",e1, ") - (", e2, ") erroneously returned (", e, ") instead of 0)"
        return 1
    return 0

def check_equal_simplify(e1, e2):
    e = normal(simplify_indexed(e1) - e2)
    if not e.is_zero():
        print e1, "-", e2, " erroneously returned ", e
        return 1
    return 0

def check_equal_simplify_term(e1, e2, mu):
    e = expand_dummy_sum(normal(simplify_indexed(e1) - e2), True)
    for j in xrange(4):
        esub = e.subs([mu==idx(j, mu.get_dim()), mu.toggle_variance() == idx(j, mu.get_dim())])
        if not canonicalize_clifford(esub).is_zero():
            print "simplify_indexed(", e1, ") - (", e2, ") erroneously returned ",\
            canonicalize_clifford(esub), " instead of 0 for mu=", j 
            return 1;
    return 0

def check_equal_simplify_term2(e1, e2):
    e = expand_dummy_sum(normal(simplify_indexed(e1) - e2), True)
    if not canonicalize_clifford(e).is_zero():
        print "simplify_indexed(", e1, ") - (", e2, ") erroneously returned ",\
        canonicalize_clifford(esub), " instead of 0"
        return 1;
    return 0




class test_clifford(unittest.TestCase):

    def test_clifford1(self):
        """Checks general identities and contractions"""
        result = 0

        dim = symbol('D')
        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)
        rho = varidx(symbol('rho'), dim)
        
        e = dirac_ONE() * dirac_ONE()
        result += check_equal(e, dirac_ONE())

        e = dirac_ONE() * dirac_gamma(mu) * dirac_ONE()
        result += check_equal(e, dirac_gamma(mu))

        e = dirac_gamma(varidx(2, dim)) * dirac_gamma(varidx(1, dim)) * \
            dirac_gamma(varidx(1, dim)) * dirac_gamma(varidx(2, dim))
        result += check_equal(e, dirac_ONE())

        e = dirac_gamma(mu) * dirac_gamma(nu) * \
            dirac_gamma(nu.toggle_variance()) * dirac_gamma(mu.toggle_variance())
        result += check_equal_simplify(e, pow(dim, 2) * dirac_ONE())

        e = dirac_gamma(mu) * dirac_gamma(nu) * \
            dirac_gamma(mu.toggle_variance()) * dirac_gamma(nu.toggle_variance())
        result += check_equal_simplify(e, 2*dim*dirac_ONE()-pow(dim, 2)*dirac_ONE())

        e = dirac_gamma(nu.toggle_variance()) * dirac_gamma(rho.toggle_variance()) * \
            dirac_gamma(mu) * dirac_gamma(rho) * dirac_gamma(nu)
        e = e.simplify_indexed().collect(dirac_gamma(mu))
        result += check_equal(e, pow(2 - dim, 2).expand() * dirac_gamma(mu))

        self.assertEqual(result, 0)

    def test_clifford2(self):
        """Checks identities relating to gamma5"""
        result = 0

        dim = symbol('D')
        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)

        e = dirac_gamma(mu) * dirac_gamma5() + dirac_gamma5() * dirac_gamma(mu)
        result += check_equal(e, 0)

        e = dirac_gamma5() * dirac_gamma(mu) * dirac_gamma5() + dirac_gamma(mu)
        result += check_equal(e, 0)

        self.assertEqual(result, 0)

    def test_clifford3(self):
        """Checks traces"""

        result = 0

        dim = symbol('D')
        m = symbol('m')
        q = symbol('q')
        l = symbol('l')
        ldotq = symbol('ldotq')
        
        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)
        rho = varidx(symbol('rho'), dim)
        sig = varidx(symbol('sig'), dim)
        kap = varidx(symbol('kap'), dim)
        lam = varidx(symbol('lam'), dim)        

        e = dirac_gamma(mu)
        result += check_equal(dirac_trace(e), 0)

        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho)
        result += check_equal(dirac_trace(e), 0)

        e = dirac_gamma5() * dirac_gamma(mu)
        result += check_equal(dirac_trace(e), 0)

        e = dirac_gamma5() * dirac_gamma(mu) * dirac_gamma(nu)
        result += check_equal(dirac_trace(e), 0)

        e = dirac_gamma5() * dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho)
        result += check_equal(dirac_trace(e), 0)

        sp = scalar_products()
        sp.add(q, q, pow(q, 2))
        sp.add(l, l, pow(l, 2))
        sp.add(l, q, ldotq)

        e = pow(m, 2) * dirac_slash(q, dim) * dirac_slash(q, dim)
        e = dirac_trace(e).simplify_indexed(sp)
        result += check_equal(e, 4*pow(m, 2)*pow(q, 2))


        # cyclicity without gamma5
        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * dirac_gamma(sig) \
          - dirac_gamma(nu) * dirac_gamma(rho) * dirac_gamma(sig) * dirac_gamma(mu)
        e = dirac_trace(e)
        result += check_equal(e, 0)

        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(sig) * dirac_gamma(kap) * dirac_gamma(lam) \
            - dirac_gamma(nu) * dirac_gamma(rho) * dirac_gamma(sig) * \
            dirac_gamma(kap) * dirac_gamma(lam) * dirac_gamma(mu)
        e = dirac_trace(e).expand()
        result += check_equal(e, 0)

        # cyclicity of gamma5 * S_4
        e = dirac_gamma5() * dirac_gamma(mu) * dirac_gamma(nu) * \
            dirac_gamma(rho) * dirac_gamma(sig) \
            - dirac_gamma(sig) * dirac_gamma5() * dirac_gamma(mu) * \
            dirac_gamma(nu) * dirac_gamma(rho)
        e = dirac_trace(e)
        result += check_equal(e, 0)

        
        # non-cyclicity of order D-4 of gamma5 * S_6
        e = dirac_gamma5() * dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(sig) * dirac_gamma(kap) * dirac_gamma(mu.toggle_variance()) \
            + dim * dirac_gamma5() * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(sig) * dirac_gamma(kap)
        e = dirac_trace(e).simplify_indexed()
        e = (e / (dim - 4)).normal()
        result += check_equal(e, 8 * I * lorentz_eps(nu.replace_dim(4),
                                                     rho.replace_dim(4),
                                                     sig.replace_dim(4), kap.replace_dim(4)))

        # one-loop vacuum polarization in QED
        e = dirac_gamma(mu) * \
            (dirac_slash(l, dim) + dirac_slash(q, 4) + m * dirac_ONE()) * \
            dirac_gamma(mu.toggle_variance()) * \
            (dirac_slash(l, dim) + m * dirac_ONE())
        e = dirac_trace(e).simplify_indexed(sp)
        result += check_equal(e, 4*((2-dim)*l*l + (2-dim)*ldotq + dim*m*m).expand())

        e = dirac_slash(q, 4) * \
            (dirac_slash(l, dim) + dirac_slash(q, 4) + m * dirac_ONE()) * \
            dirac_slash(q, 4) * \
            (dirac_slash(l, dim) + m * dirac_ONE())
        e = dirac_trace(e).simplify_indexed(sp)
        result += check_equal(e, 4*(2*ldotq*ldotq + q*q*ldotq - q*q*l*l + q*q*m*m).expand())


        # stuff that had problems in the past
        prop = dirac_slash(q, dim) - m * dirac_ONE()
        e = dirac_slash(l, dim) * dirac_gamma5() * dirac_slash(l, dim) * prop
        e = dirac_trace(dirac_slash(q, dim) * e) - dirac_trace(m * e) \
          - dirac_trace(prop * e)
        result += check_equal(e, 0)

        e = dirac_gamma5()*dirac_gamma5() + dirac_ONE()*dirac_gamma5()
        e = dirac_trace(e)
        result += check_equal(e, 4)


        # traces with multiple representation labels
        e = dirac_ONE(0) * dirac_ONE(1) / 16
        result += check_equal(dirac_trace(e, 0), dirac_ONE(1) / 4)
        result += check_equal(dirac_trace(e, 1), dirac_ONE(0) / 4)
        result += check_equal(dirac_trace(e, 2), e)
        result += check_equal(dirac_trace(e, [0,1]), 1)
        e = dirac_gamma(mu, 0) * dirac_gamma(mu.toggle_variance(), 1) * \
            dirac_gamma(nu, 0) * dirac_gamma(nu.toggle_variance(), 1)
        result += check_equal_simplify(dirac_trace(e, 0), 4 * dim * dirac_ONE(1))
        result += check_equal_simplify(dirac_trace(e, 1), 4 * dim * dirac_ONE(0))
        # Fails with new tinfo mechanism because the order of gamme matrices with different rl depends on luck. 
        #result += check_equal_simplify(dirac_trace(e, 2), canonicalize_clifford(e))
        result += check_equal_simplify(dirac_trace(e, [0,1]), 16 * dim)

        self.assertEqual(result, 0)

    def test_clifford4(self):
        """simplify_indexed()/dirac_trace() cross-checks"""

        result = 0

        dim = symbol('D')

        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)
        rho = varidx(symbol('rho'), dim)
        sig = varidx(symbol('sig'), dim)
        lam = varidx(symbol('lam'), dim)

        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(mu.toggle_variance())
        t1 = dirac_trace(e).simplify_indexed()
        t2 = dirac_trace(e.simplify_indexed())
        result += check_equal((t1 - t2).expand(), 0)

        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(sig) * dirac_gamma(mu.toggle_variance()) * dirac_gamma(lam)
        t1 = dirac_trace(e).simplify_indexed()
        t2 = dirac_trace(e.simplify_indexed())
        result += check_equal((t1 - t2).expand(), 0)

        e = dirac_gamma(sig) * dirac_gamma(mu) * dirac_gamma(nu) * \
            dirac_gamma(rho) * dirac_gamma(nu.toggle_variance()) * \
            dirac_gamma(mu.toggle_variance())
        t1 = dirac_trace(e).simplify_indexed()
        t2 = dirac_trace(e.simplify_indexed())
        result += check_equal((t1 - t2).expand(), 0)

        e = dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(rho) * \
            dirac_gamma(mu.toggle_variance()) * dirac_gamma(sig) * \
            dirac_gamma(nu.toggle_variance())
        t1 = dirac_trace(e).simplify_indexed()
        t2 = dirac_trace(e.simplify_indexed())
        result += check_equal((t1 - t2).expand(), 0)

        self.assertEqual(result, 0)

    def test_clifford5(self):
        """canonicalize_clifford() checks"""

        result = 0

        dim = symbol('D')
        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)
        lam = varidx(symbol('lam'), dim)

        e = dirac_gamma(mu) * dirac_gamma(nu) + dirac_gamma(nu) * dirac_gamma(mu)
        result += check_equal(canonicalize_clifford(e), 2*dirac_ONE()*lorentz_g(mu, nu))

        e = (dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(lam) \
           + dirac_gamma(nu) * dirac_gamma(lam) * dirac_gamma(mu) \
           + dirac_gamma(lam) * dirac_gamma(mu) * dirac_gamma(nu) \
           - dirac_gamma(nu) * dirac_gamma(mu) * dirac_gamma(lam) \
           - dirac_gamma(lam) * dirac_gamma(nu) * dirac_gamma(mu) \
           - dirac_gamma(mu) * dirac_gamma(lam) * dirac_gamma(nu)) / 6 \
          + lorentz_g(mu, nu) * dirac_gamma(lam) \
          - lorentz_g(mu, lam) * dirac_gamma(nu) \
          + lorentz_g(nu, lam) * dirac_gamma(mu) \
          - dirac_gamma(mu) * dirac_gamma(nu) * dirac_gamma(lam)
        result += check_equal(canonicalize_clifford(e), 0)

        self.assertEqual(result, 0)

    def test_clifford6(self):
        for A in [matrix([[-1,0,0,0],\
                          [0,1,0,0],\
                          [0,0,1,0],\
                          [0,0,0,1]]),
                  matrix([[-1,0,0,0],\
                          [0,-1,0,0],\
                          [0,0,-1,0],\
                          [0,0,0,-1]]),
                  matrix([[-1,0,0,0],\
                          [0,1,0,0],\
                          [0,0,1,0],\
                          [0,0,0,-1]]),
                  matrix([[-1,0,0,0],\
                          [0,0,0,0],\
                          [0,0,1,0],\
                          [0,0,0,-1]])]:
            self.check_clifford6(A)

    def check_clifford6(self, A):

        v = varidx(symbol('v'), 4)
        nu = varidx(symbol('nu'), 4)
        mu = varidx(symbol('mu'), 4)
        psi = varidx(symbol('psi'), 4)
        lam = varidx(symbol('lam'), 4)
        xi = varidx(symbol('xi'), 4)
        rho = varidx(symbol('rho'), 4)
        G = A
        A2 = A.mul(A)

        A_symm = A.add(A.transpose()).mul(half)

        result = 0

        # checks general identities and contractions for clifford_unit
        e = dirac_ONE(2) * clifford_unit(mu, G, 2) * dirac_ONE(2)
        result += check_equal(e, clifford_unit(mu, G, 2))

        e = clifford_unit(varidx(2, 4), G) * clifford_unit(varidx(1, 4), G) \
            * clifford_unit(varidx(1, 4), G) * clifford_unit(varidx(2, 4), G)
        result += check_equal(e, A[1, 1] * A[2, 2] * dirac_ONE())

        e = clifford_unit(nu, G) * clifford_unit(nu.toggle_variance(), G)
        result += check_equal_simplify(e, A.trace() * dirac_ONE())

        e = clifford_unit(nu, G) * clifford_unit(nu, G)
        result += check_equal_simplify(e, indexed(G, sy_symm(), nu, nu) * dirac_ONE())

        e = clifford_unit(nu, G) * clifford_unit(nu.toggle_variance(), G) * clifford_unit(mu, G)
        result += check_equal_simplify(e, A.trace() * clifford_unit(mu, G))

        e = clifford_unit(nu, G) * clifford_unit(mu, G) * \
            clifford_unit(nu.toggle_variance(), G)
        result += check_equal_simplify_term(e, 2*indexed(A_symm, sy_symm(), nu.toggle_variance(), mu)*\
                                       clifford_unit(nu, G) - A.trace()*clifford_unit(mu, G), mu)

        e = clifford_unit(nu, G) * clifford_unit(nu.toggle_variance(), G) \
            * clifford_unit(mu, G) * clifford_unit(mu.toggle_variance(), G)
        result += check_equal_simplify(e, pow(A.trace(), 2) * dirac_ONE())

        e = clifford_unit(mu, G) * clifford_unit(nu, G) \
            * clifford_unit(nu.toggle_variance(), G) * clifford_unit(mu.toggle_variance(), G)
        result += check_equal_simplify(e, pow(A.trace(), 2)  * dirac_ONE())

        e = clifford_unit(mu, G) * clifford_unit(nu, G) \
            * clifford_unit(mu.toggle_variance(), G) * clifford_unit(nu.toggle_variance(), G)
        result += check_equal_simplify_term2(e, 2*indexed(A_symm, sy_symm(), \
            nu.toggle_variance(), mu.toggle_variance())*clifford_unit(mu, G)*clifford_unit(nu,G) - pow(A.trace(), 2)*dirac_ONE())

        e = clifford_unit(mu.toggle_variance(), G) * clifford_unit(nu, G) \
            * clifford_unit(mu, G) * clifford_unit(nu.toggle_variance(), G)
        result += check_equal_simplify_term2(e, 2*indexed(A_symm, nu, \
            mu)*clifford_unit(mu.toggle_variance(),G)*clifford_unit(nu.toggle_variance(),G)\
            - pow(A.trace(), 2)*dirac_ONE())

        e = clifford_unit(nu.toggle_variance(), G) * clifford_unit(rho.toggle_variance(), G)\
            * clifford_unit(mu, G) * clifford_unit(rho, G) * clifford_unit(nu, G)
        e = e.simplify_indexed().collect(clifford_unit(mu, G))
        result += check_equal_simplify_term(e, 4*indexed(A_symm, sy_symm(), nu.toggle_variance(),  rho)*indexed(A_symm, sy_symm(), rho.toggle_variance(), mu) *clifford_unit(nu, A) \
               - 2*A.trace() * (clifford_unit(rho, A) * indexed(A_symm, sy_symm(), rho.toggle_variance(), mu) \
               + clifford_unit(nu, A) * indexed(A_symm, sy_symm(), nu.toggle_variance(), mu)) + pow(A.trace(),2)* clifford_unit(mu, A), mu)

        e = clifford_unit(nu.toggle_variance(), G) * clifford_unit(rho, G) \
            * clifford_unit(mu, G) * clifford_unit(rho.toggle_variance(), G) * \
            clifford_unit(nu, G);
        e = e.simplify_indexed().collect(clifford_unit(mu, G))
        result += check_equal_simplify_term(e, 4* indexed(A_symm, sy_symm(), nu.toggle_variance(),  rho)*indexed(A_symm, sy_symm(), rho.toggle_variance(), mu) *clifford_unit(nu, A)\
               - 2*A.trace() * (clifford_unit(rho, A) * indexed(A_symm, sy_symm(), rho.toggle_variance(), mu)\
               + clifford_unit(nu, A) * indexed(A_symm, sy_symm(), nu.toggle_variance(), mu)) + pow(A.trace(),2)* clifford_unit(mu, A), mu)

        # canonicalize_clifford() checks
        e = clifford_unit(mu, G) * clifford_unit(nu, G) + clifford_unit(nu, G) * \
            clifford_unit(mu, G)
        result += check_equal(canonicalize_clifford(e),
                              2*dirac_ONE()*indexed(A_symm, sy_symm(), mu, nu))

        e = (clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G) \
           + clifford_unit(nu, G) * clifford_unit(lam, G) * clifford_unit(mu, G) \
           + clifford_unit(lam, G) * clifford_unit(mu, G) * clifford_unit(nu, G) \
           - clifford_unit(nu, G) * clifford_unit(mu, G) * clifford_unit(lam, G) \
           - clifford_unit(lam, G) * clifford_unit(nu, G) * clifford_unit(mu, G) \
           - clifford_unit(mu, G) * clifford_unit(lam, G) * clifford_unit(nu, G)) / 6 \
          + indexed(A_symm, sy_symm(), mu, nu) * clifford_unit(lam, G) \
          - indexed(A_symm, sy_symm(), mu, lam) * clifford_unit(nu, G) \
          + indexed(A_symm, sy_symm(), nu, lam) * clifford_unit(mu, G) \
          - clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G)
        result += check_equal(canonicalize_clifford(e), 0)

        # lst_to_clifford() and clifford_inverse()  check
        s = realsymbol('s')
        t = realsymbol('t')
        x = realsymbol('x')
        y = realsymbol('y')
        z = realsymbol('z')
        
        c = clifford_unit(nu, G, 1)
        e = lst_to_clifford([t,x,y,z], mu, G, 1) * lst_to_clifford([1,2,3,4], c)
        e1 = clifford_inverse(e)
        result += check_equal_simplify_term2((e*e1).simplify_indexed().normal(), dirac_ONE(1))

        self.assertEqual(result, 0)

    def test_clifford7(self):
        """checks general identities and contractions"""

        result = 0

        dim = symbol('D')

        mu = varidx(symbol('mu'), dim)
        nu = varidx(symbol('nu'), dim)
        rho = varidx(symbol('rho'), dim)
        psi = varidx(symbol('psi'), dim)
        lam = varidx(symbol('lam'), dim)
        xi = varidx(symbol('xi'), dim)

        G = minkmetric()

        unit = clifford_unit(mu, G)
        scalar = unit.get_metric(varidx(0, dim), varidx(0, dim))

        e = dirac_ONE() * dirac_ONE()
        result += check_equal(e, dirac_ONE())

        e = dirac_ONE() * clifford_unit(mu, G) * dirac_ONE()
        result += check_equal(e, clifford_unit(mu, G))

        e = clifford_unit(varidx(2, dim), G) * clifford_unit(varidx(1, dim), G) \
            * clifford_unit(varidx(1, dim), G) * clifford_unit(varidx(2, dim), G)
        result += check_equal(e, dirac_ONE()*pow(scalar,2))

        e = clifford_unit(mu, G) * clifford_unit(nu, G) \
            * clifford_unit(nu.toggle_variance(), G) * clifford_unit(mu.toggle_variance(), G)
        result += check_equal_simplify(e, pow(dim*scalar, 2) * dirac_ONE())

        e = clifford_unit(mu, G) * clifford_unit(nu, G) \
            * clifford_unit(mu.toggle_variance(), G) * clifford_unit(nu.toggle_variance(), G)
        result += check_equal_simplify(e, 2*dim*pow(scalar,2)*dirac_ONE() - pow(dim, 2)*pow(scalar,2)*dirac_ONE())

        e = clifford_unit(nu.toggle_variance(), G) * clifford_unit(rho.toggle_variance(), G) \
            * clifford_unit(mu, G) * clifford_unit(rho, G) * clifford_unit(nu, G)
        e = e.simplify_indexed().collect(clifford_unit(mu, G))
        result += check_equal(e, pow(2 - dim, 2).expand() * clifford_unit(mu, G))

        # canonicalize_clifford() checks
        if clifford_unit(mu, G).get_metric().get_symmetry().has_symmetry():
            e = clifford_unit(mu, G) * clifford_unit(nu, G) + clifford_unit(nu, G) * \
                clifford_unit(mu, G)
            result += check_equal(canonicalize_clifford(e),
                              2*dirac_ONE()*unit.get_metric(nu, mu))

            e = (clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G) \
               + clifford_unit(nu, G) * clifford_unit(lam, G) * clifford_unit(mu, G) \
               + clifford_unit(lam, G) * clifford_unit(mu, G) * clifford_unit(nu, G) \
               - clifford_unit(nu, G) * clifford_unit(mu, G) * clifford_unit(lam, G) \
               - clifford_unit(lam, G) * clifford_unit(nu, G) * clifford_unit(mu, G) \
               - clifford_unit(mu, G) * clifford_unit(lam, G) * clifford_unit(nu, G)) / 6 \
              + indexed(G, sy_symm(), mu, nu) * clifford_unit(lam, G) \
              - indexed(G, sy_symm(), mu, lam) * clifford_unit(nu, G) \
              + indexed(G, sy_symm(), nu, lam) * clifford_unit(mu, G) \
              - clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G)
            result += check_equal(canonicalize_clifford(e), 0)
        else:
            e = clifford_unit(mu, G) * clifford_unit(nu, G) + clifford_unit(nu, G) * clifford_unit(mu, G)
            result += check_equal(canonicalize_clifford(e), dirac_ONE()*unit.get_metric(mu, nu) + dirac_ONE()*unit.get_metric(nu, mu))
            e = (clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G)
            + clifford_unit(nu, G) * clifford_unit(lam, G) * clifford_unit(mu, G)
            + clifford_unit(lam, G) * clifford_unit(mu, G) * clifford_unit(nu, G)
            - clifford_unit(nu, G) * clifford_unit(mu, G) * clifford_unit(lam, G)
            - clifford_unit(lam, G) * clifford_unit(nu, G) * clifford_unit(mu, G)
            - clifford_unit(mu, G) * clifford_unit(lam, G) * clifford_unit(nu, G)) / 6
            + half * (unit.get_metric(mu, nu) + unit.get_metric(nu, mu)) * clifford_unit(lam, G)
            - half * (unit.get_metric(mu, lam) + unit.get_metric(lam, mu)) * clifford_unit(nu, G)
            + half * (unit.get_metric(nu, lam) + unit.get_metric(lam, nu)) * clifford_unit(mu, G)
            - clifford_unit(mu, G) * clifford_unit(nu, G) * clifford_unit(lam, G);
            #result += check_equal(canonicalize_clifford(e), 0) #FIXME!!!
 

        self.assertEqual(result, 0)
 


if __name__ == "__main__":
    unittest.main()
