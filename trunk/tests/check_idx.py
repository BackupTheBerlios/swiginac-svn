# (c) Copyright 2003, 2004, 2005
#     Authors: Ola Skavhaug and Ondrej Certik
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
import swiginac as g

class test_idx(unittest.TestCase):

    def testidx(self):
        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("j"),3)
        A=g.symbol("A")
        self.assertEqual(str(g.indexed(A,i,j)),"A.i.j")

    def testvaridx1(self):
        i=g.varidx(g.symbol("i"),3)
        j=g.varidx(g.symbol("j"),3)
        A=g.symbol("A")
        self.assertEqual(str(g.indexed(A,i,j)),"A~i~j")

    def testvaridx2(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4,True)
        A=g.symbol("A")
        self.assertEqual(str(g.indexed(A,mu,nu)),"A~mu.nu")
        self.assertEqual(str(g.indexed(A,mu,nu.toggle_variance())),"A~mu~nu")
        self.failUnless(mu.is_contravariant())
        self.failIf(mu.is_covariant())
        self.failUnless(nu.is_covariant())

    def testvaridx3(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4)
        A=g.symbol("A")
        self.assertEqual(str(g.indexed(A,mu,nu)),"A~mu~nu")
        self.assertEqual(str(g.indexed(A,mu,nu.toggle_variance())),"A~mu.nu")
        self.assertEqual(str(g.indexed(A,mu.toggle_variance(),nu)),"A.mu~nu")
        self.failUnless(mu.is_contravariant())
        self.failUnless(nu.is_contravariant())

    def testsubs(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4,True)
        A=g.symbol("A")
        e=g.indexed(A,mu)
        self.assertEqual(str(e),"A~mu")
        self.assertEqual(str(e.subs(mu==nu)),"A.nu")
        self.assertEqual(str(e.subs(mu==0)),"A~0")

    def testdummy(self):
        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("j"),3)
        k=g.idx(g.symbol("k"),3)
        l=g.idx(g.symbol("l"),3)
        A=g.symbol("A")
        B=g.symbol("B")
        C=g.symbol("C")

        e=g.indexed(A,i,j)*g.indexed(B,j,k)+g.indexed(C,k,l,i,l)
        #can vary from run to run
        #self.assertEqual(str(e),"C.k.l.i.l+B.j.k*A.i.j")
        f=e.get_free_indices()
        self.failUnless(type(f)==list)
        self.failUnless(f==[i,k] or f==[k,i])
        self.failUnless(str(f)=="[.i, .k]" or str(f)=="[.k, .i]")

        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4)
        rho=g.varidx(g.symbol("rho"),4)
        sigma=g.varidx(g.symbol("sigma"),4)

        e=g.indexed(A,mu,nu)*g.indexed(B,nu.toggle_variance(),rho)+\
            g.indexed(C,mu,sigma,rho,sigma.toggle_variance())
        self.assertEqual(e.get_free_indices(),[mu, rho])

        e=g.indexed(A,mu,mu)
        self.assertEqual(e.get_free_indices(),[mu])
        self.assertNotEqual(e.get_free_indices(),[mu.toggle_variance()])

    def testsimplify(self):
        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("i"),3)
        A=g.symbol("A")
        B=g.symbol("B")
        C=g.symbol("C")
        sp=g.scalar_products()
        sp.add(A,B,0)
        sp.add(A,C,0)
        sp.add(A,A,4)

        e=g.indexed(A+B,i)*g.indexed(A+C,i)
        self.assertEqual(e.expand(g.expand_options.expand_indexed).
            simplify_indexed(sp),4+g.indexed(C,i)*g.indexed(B,i))
        self.assertEqual(g.simplify_indexed(e.expand(g.expand_options.
            expand_indexed),sp),4+g.indexed(C,i)*g.indexed(B,i))
        self.assertNotEqual(g.simplify_indexed(e.expand(g.expand_options.
            expand_indexed)),4+g.indexed(C,i)*g.indexed(B,i))
        self.assertNotEqual(g.simplify_indexed(e.expand(g.expand_options.
            expand_indexed),sp),5+g.indexed(C,i)*g.indexed(B,i))
        self.assertNotEqual(g.simplify_indexed(e.expand(g.expand_options.
            expand_indexed),sp),4+g.indexed(C,i)*g.indexed(B,j))

    def testdelta(self):
        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("j"),3)
        k=g.idx(g.symbol("k"),3)
        l=g.idx(g.symbol("l"),3)
        A=g.symbol("A")
        B=g.symbol("B")

        e=g.indexed(A,i,j)*g.indexed(B,k,l)*g.delta_tensor(i,k)*\
            g.delta_tensor(j,l)
        self.assertEqual((e-g.indexed(A,k,l)*g.indexed(B,k,l)).
            simplify_indexed(),0)
        self.assertEqual((e-g.indexed(B,k,l)*g.indexed(A,k,l)).
            simplify_indexed(),0)
        self.assertEqual((e-g.indexed(A,i,l)*g.indexed(B,i,l)).
            simplify_indexed(),0)
        self.assertEqual((e-g.indexed(A,i,j)*g.indexed(B,i,j)).
            simplify_indexed(),0)
        self.assertNotEqual((e-g.indexed(A,i,i)*g.indexed(B,k,k)).
            simplify_indexed(),0)
        self.assertEqual(g.delta_tensor(i,i),3)
        self.assertNotEqual(g.delta_tensor(i,i),4)

    def testsimplify(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4)
        A=g.symbol("A")

        e1=g.indexed(A,mu,mu.toggle_variance())
        e2=g.indexed(A,nu,nu.toggle_variance())
        self.assertNotEqual(e1,e2)
        self.assertEqual((e1-e2).simplify_indexed(),0)

    def testmetric(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4)
        rho=g.varidx(g.symbol("rho"),4)
        A=g.symbol("A")

        e=g.metric_tensor(mu,nu)*g.indexed(A,nu.toggle_variance(),rho)
        self.assertEqual(e.simplify_indexed(),g.indexed(A,mu,rho))
        self.assertNotEqual(e.simplify_indexed(),g.indexed(A,nu,rho))

        e=g.delta_tensor(mu,nu.toggle_variance())*g.metric_tensor(nu,rho)
        self.assertEqual(e.simplify_indexed(),g.metric_tensor(mu,rho))

        e=g.metric_tensor(mu.toggle_variance(),nu.toggle_variance())*\
            g.metric_tensor(nu,rho)
        self.assertEqual(e.simplify_indexed(),
            g.delta_tensor(mu.toggle_variance(),rho))

        e=g.metric_tensor(nu.toggle_variance(),rho.toggle_variance())*\
            g.metric_tensor(mu,nu)*(g.delta_tensor(mu.toggle_variance(),rho)+\
            g.indexed(A,mu.toggle_variance(),rho))
        self.assertEqual((e-(4+g.indexed(A,rho.toggle_variance(),rho))).
            simplify_indexed(),0)

    def testlorentz(self):
        mu=g.varidx(g.symbol("mu"),4)
        e=g.delta_tensor(g.varidx(0,4),mu.toggle_variance())*\
            g.lorentz_g(mu,g.varidx(0,4))
        self.assertEqual(e.simplify_indexed(),1)

        e=g.delta_tensor(g.varidx(0,4),mu.toggle_variance())*\
            g.lorentz_g(mu,g.varidx(0,4),True)
        self.assertEqual(e.simplify_indexed(),-1)

    def testeps(self):
        mu=g.varidx(g.symbol("mu"),4)
        nu=g.varidx(g.symbol("nu"),4)
        rho=g.varidx(g.symbol("rho"),4)
        sig=g.varidx(g.symbol("sig"),4)
        lam=g.varidx(g.symbol("lam"),4)
        bet=g.varidx(g.symbol("bet"),4)

        e=g.lorentz_eps(mu,nu,rho,sig)*g.lorentz_eps(mu.toggle_variance(),
            nu.toggle_variance(),lam,bet)
        g.simplify_indexed(e)

        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("j"),3)
        k=g.idx(g.symbol("k"),3)
        A=g.symbol("A")
        B=g.symbol("B")
        e=g.epsilon_tensor(i,j,k)*g.indexed(A,j)*g.indexed(B,k)
        self.assertNotEqual(g.simplify_indexed(e),0)
        e=g.epsilon_tensor(i,j,k)*g.indexed(A,j)*g.indexed(A,k)
        self.assertEqual(g.simplify_indexed(e),0)

    def testsymm(self):
        i=g.idx(g.symbol("i"),3)
        j=g.idx(g.symbol("j"),3)
        k=g.idx(g.symbol("k"),3)
        l=g.idx(g.symbol("l"),3)
        A=g.symbol("A")
        e=g.indexed(A,i,j)
        e=g.indexed(A,g.sy_none(), i,j)
        e=g.indexed(A,g.sy_none(0, 1), i,j)
        e=g.indexed(A,g.sy_none(g.symmetry(0), g.symmetry(1)), i,j)

        e=g.indexed(A,g.sy_symm(), i,j,k)
        e=g.indexed(A,g.sy_symm(0,1,2), i,j,k)
        e=g.indexed(A,g.sy_symm(2,0,1), i,j,k)

        e=g.indexed(A,g.sy_symm(0,1), i,j,k)
        #e=g.indexed(A,g.sy_none(g.sy_symm(0,1),2), i,j,k)


if __name__ == "__main__":
    unittest.main()
