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
from swiginac import symbol

class test_degree_and_coefficients(unittest.TestCase):

    def test_multivariate_polynomial_analyze(self):
        x = symbol("x")
        y = symbol("y")
        p_correct = [ y**2+11*y, 5*y**2-2*y, -1, 4*y ]
        PolyInp = 4*pow(x,3)*y + 5*x*pow(y,2) + 3*y - pow(x+y,2) + 2*pow(y+2,2) - 8
        Poly = PolyInp.expand()
        for i in xrange(Poly.ldegree(x),Poly.degree(x)+1):
            self.assertEqual(Poly.coeff(x,i), p_correct[i])
         
        self.assertEqual(Poly.collect(y), -x**2+(5*x+1)*y**2+(-2*x+4*x**3+11)*y)



if __name__ == "__main__":
    unittest.main()

