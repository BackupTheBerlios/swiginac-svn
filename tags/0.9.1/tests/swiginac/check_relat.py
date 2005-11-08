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

class test_relat(unittest.TestCase):

    def testrelat1(self):
        r=g.cos(0)
        self.assertEqual(r,1)
        self.assertNotEqual(r,1.1)
        r=g.cos(g.Pi)
        self.assertEqual(r,-1)
        self.assertNotEqual(r,-2)
        r=g.cos(2*g.Pi)
        self.assertEqual(r,1)
        self.assertNotEqual(r,1.1)

    def testrelat2(self):
        x=g.symbol("x")
        y=g.symbol("y")
        r1=x+y
        r2=2*(x+y)
        r2/=2
        self.assertEqual(r1,r2)
        self.assertNotEqual(r1,r2+1)
        r3=r1-r2
        self.assertEqual(r3,0)
        self.assertNotEqual(r3,1)

    def testrelat3(self):
        x=g.symbol("x")
        y=g.symbol("y")
        r1=x/y
        r2=2*(x/y)
        r2/=2
        self.assertEqual(r1,r2)
        self.assertNotEqual(r1,r2+1)
        r3=r1-r2
        self.assertEqual(r3,0)
        self.assertNotEqual(r3,1)

    def testrelat4(self):
        numeric=g.numeric
        relational=g.relational
        self.assertEqual(isinstance(numeric(0) == numeric(0), relational),True)
        self.assertEqual(isinstance(numeric(0) <= numeric(0), relational),True)
        self.assertEqual(isinstance(numeric(0) != numeric(0), relational),True)
        self.assertEqual(isinstance(numeric(0) >= numeric(0), relational),True)
        self.assertEqual(isinstance(numeric(0) < numeric(0), relational),True)
        self.assertEqual(isinstance(numeric(0) > numeric(0), relational),True)

if __name__ == "__main__":
    unittest.main()
