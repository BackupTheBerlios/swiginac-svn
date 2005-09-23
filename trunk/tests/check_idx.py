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
        #print e
        #print e.get_free_indices()

if __name__ == "__main__":
    unittest.main()
