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

class test_lst(unittest.TestCase):

    def testlsolve(self):
        a=g.symbol("a")
        b=g.symbol("b")
        x=g.symbol("x")
        y=g.symbol("y")
        e1=a*x+b*y==3
        e2=x-y==b
        eqns=[e1,e2]
        vars=[x,y]
        #print g.lsolve(eqns,vars)
        self.assertEqual(g.lsolve(eqns,vars),[x==(b+a)**(-1)*(3+b**2),y==(3-b*a)*(b+a)**(-1)])
        self.assertNotEqual(g.lsolve(eqns,vars),[x==(b)**(-1)*(3+b**2),y==(3-b*a)*(b+a)**(-1)])

    def testsubs(self):
        x=g.symbol("x")
        y=g.symbol("y")
        e=x+y
        self.assertEqual(e.subs([x,y],[y,y]),2*y)
        self.assertNotEqual(e.subs([x,y],[y,y]),2*y+1)
        self.assertEqual(e.subs([x,y],[1, 2]),g.numeric(3))
        self.assertNotEqual(e.subs([x,y],[1, 2]),g.numeric(5))

    def testlists(self):
        x=g.symbol("x")
        y=g.symbol("y")
        e=x+y
        self.assertEqual(repr(g.diag_matrix([x,y])),"[[x,0],[0,y]]")
        #self.assertEqual(g.diag_matrix([x,y]),[[x,0],[0,y]])
        self.assertNotEqual(repr(g.diag_matrix([x,y])),"[[x,x],[0,y]]")
        self.assertEqual(repr(g.diag_matrix([x,1.0])),"[[x,0],[0,1.0]]")
        self.assertEqual(repr(g.diag_matrix([2.0,1])),"[[2.0,0],[0,1]]")
        self.assertEqual(repr(g.diag_matrix([x,g.numeric(1)])),"[[x,0],[0,1]]")
        self.assertEqual(repr(g.diag_matrix([x,g.numeric(1,2)])),"[[x,0],[0,1/2]]")
        self.assertEqual(repr(g.diag_matrix([x,e])),"[[x,0],[0,x+y]]")
        self.assertEqual(repr(g.lst_to_matrix([[x,0],[0,e]])),"[[x,0],[0,x+y]]")
        self.assertEqual(repr(g.lst_to_matrix([[1,2],[3,4]])),"[[1,2],[3,4]]")
        self.assertRaises(ValueError,g.diag_matrix,"ha")
        self.assertRaises(ValueError,g.diag_matrix,[x,"ha"])
        self.assertRaises(ValueError,g.diag_matrix,[[x,0],[y,"ha"]])
        self.assertRaises(ValueError,g.diag_matrix,[[x,0],["ha"]])

    def testrepr(self):
        x=g.symbol("x")
        y=g.symbol("y")
        self.assertEqual(repr([x,y]),"[x, y]")
        self.assertEqual(repr([x,y+1-1]),"[x, y]")
        self.assertEqual(repr([g.numeric(1,2)*x*2,y+1-1]),"[x, y]")
        self.assertNotEqual(repr([x,y]),"[x, y+1]")
        self.assertNotEqual(repr([x,y+1-1]),"[x, y+1-1]")


if __name__ == "__main__":
    unittest.main()
