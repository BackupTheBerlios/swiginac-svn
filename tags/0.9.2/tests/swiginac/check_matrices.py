# (c) Copyright 2003, 2004, 2005
#     Authors: Ola Skavhaug and Ondrej Certik
#     based on regression tests for PyGiNaC,
#       Copyright (C) 2004, 2005 Jonathan Brandmeyer, Matti Peltomaki
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
from swiginac import *
from genex import dense_univariate_poly, sparse_tree
from random import randrange

class test_matrix(unittest.TestCase):

    def testcreation(self):
        a=g.symbol("a")
        b=g.symbol("b")
        x=g.symbol("x")
        y=g.symbol("y")
        m=g.matrix(2,2,[a,0,0,b])
        self.assertEqual(repr(m),"[[a,0],[0,b]]")
        self.assertNotEqual(repr(m),"[[a,1],[0,b]]")
        m=g.matrix(2,2)
        self.assertEqual(repr(m),"[[0,0],[0,0]]")
        m[0,0]=a
        self.assertEqual(repr(m),"[[a,0],[0,0]]")
        m[1,1]=b
        self.assertEqual(repr(m),"[[a,0],[0,b]]")
        self.assertNotEqual(repr(m),"[[a,0],[b,0]]")
        self.assertEqual(m[0,0],a)
        self.assertNotEqual(m[0,0],b)
        self.assertEqual(m[0,1],0)
        self.assertNotEqual(m[0,1],b)
        self.assertEqual(m[1,1],b)
        self.assertNotEqual(m[1,1],0)

        M=g.lst_to_matrix
        m[0,1]=a
        self.assertEqual(m,M([[a,a],[0,b]]))
        m[0,1]=b
        self.assertEqual(m,M([[a,b],[0,b]]))
        m[0,1]=b*a
        self.assertEqual(m,M([[a,a*b],[0,b]]))

    def testcreation2(self):
        a=g.symbol("a")
        b=g.symbol("b")
        x=g.symbol("x")
        y=g.symbol("y")
        m=g.matrix([[a,0],[0,b]])
        self.assertEqual(repr(m),"[[a,0],[0,b]]")
        self.assertNotEqual(repr(m),"[[a,1],[0,b]]")
        m=g.matrix([[0,0],[0,0]])
        self.assertEqual(repr(m),"[[0,0],[0,0]]")
        m[0,0]=a
        self.assertEqual(repr(m),"[[a,0],[0,0]]")
        m[1,1]=b
        self.assertEqual(repr(m),"[[a,0],[0,b]]")
        self.assertNotEqual(repr(m),"[[a,0],[b,0]]")
        self.assertEqual(m[0,0],a)
        self.assertNotEqual(m[0,0],b)
        self.assertEqual(m[0,1],0)
        self.assertNotEqual(m[0,1],b)
        self.assertEqual(m[1,1],b)
        self.assertNotEqual(m[1,1],0)

        M=g.matrix
        m[0,1]=a
        self.assertEqual(m,M([[a,a],[0,b]]))
        m[0,1]=b
        self.assertEqual(m,M([[a,b],[0,b]]))
        m[0,1]=b*a
        self.assertEqual(m,M([[a,a*b],[0,b]]))


    def testops(self):
        m=g.lst_to_matrix
        A=m([[1,2],[3,4]])
        B=m([[-1,0],[2,1]])
        C=m([[8,4],[2,1]])

        self.assertEqual(repr((A*B-(C*2)).evalm()),"[[-13,-6],[1,2]]")
        self.assertEqual((A*B-(C*2)).evalm(),m([[-13.0,-6.0],[1.0,2.0]]))
        self.assertEqual((A*B-(C*2)).evalm(),m([[-13,-6],[1,2]]))

    # determinants of some sparse symbolic matrices with coefficients in
    # an integral domain.
    def test_integdom_matrix_determinants(self):
        """
        >>> integdom_matrix_determinants()
        Matrix determinant test passed.
        """
        error = False
        a = symbol('a')
        # Feel like you have CPU time to burn?  
        # Raise the value of the upper bounds here...
        for size in range(3, 22):
            A = matrix( size, size)
            # Populate one element in each row
            for r in range( size-1):
                A[r, randrange(0,size)] = dense_univariate_poly(a, 5)
            # Set the last row to a linear combination of two others to
            # guarantee that the determinant should be zero
            for c in range(size):
                A[size-1, c] = A[0,c] - A[size-2,c]
            if A.determinant() != 0:
                error = True
                print "Determinant of", size, "x", size, "matrix", A
                print "was not found to vanish!"
        self.assertEqual(error,0)

    # determinants of some sparse symbolic matrices with coefficients in
    # the rational domain.
    def test_rational_matrix_determinants(self):
        """
        >>> rational_matrix_determinants()
        Rational matrix determinants test passed.
        """
        error = False
        a = symbol('a')
        b = symbol('b')
        c = symbol('c')
        for size in range( 3, 9):
            A = matrix(size, size)
            for r in range(size-1):
                # Populate one or two elements in each row:
                for ec in range(2):
                    numer = sparse_tree( a, b, c, randrange(1, 4), 
                        False, False, False)
                    denom = numeric(0)
                    while denom == 0:
                        denom = sparse_tree( a, b, c, randrange(2), 
                            False, False, False)
                    A[r, randrange(size)] = numer/denom
            # set the last row to a linear combination of two other lines
            # to guarantee that the determinant is zero:        
            for co in range(size):
                A[size-1, co] = A[0,co] - A[size-2,co]
            if A.determinant() != 0:
                error = True
                print "Determinant of", size, "x", size," matrix ", A
                print "was not found to vanish!"
        self.assertEqual(error,0)

    # Throw some trigonimetric functions in the mix...
    def test_funny_matrix_determinants(self):
        """
        >>> funny_matrix_determinants()
        'Funny' matrix determinant test passed.
        """
        error = False
        a = symbol('a')
        b = symbol('b')
        c = symbol('c')
        for size in range(3, 8):
            A = matrix(size, size)
            for co in range(size-1):
                # Populate one or two elements in each row
                for ec in range(0, 2):
                    numer = sparse_tree(a, b, c, randrange(1, 4), True, True, False)
                    denom = numeric(0)
                    while denom == 0:
                        denom = sparse_tree(a, b, c, randrange(2), False, True, False)
                    A[randrange(size), co] = numer/denom
                # Set the last column to a linear combination of two other columns to
                # guarantee that the determinant is zero
                for ro in range(size):
                    A[ro, size-1] = A[ro, 0] - A[ro,size-2]
                if A.determinant() != 0:
                    error = True
                    print "Determinant of", size, "x", size, "matrix", A
                    print "was not found to vanish!"
        self.assertEqual(error,0)

    # Compare results from different determinant algorithms
    def test_compare_matrix_determinants(self):
        """
        >>> compare_matrix_determinants()
        Matrix determinant comparison test passed.
        """
        error = False
        a = symbol('a')
        for size in range(2, 8):
            A = matrix(size, size)
            for co in range(size):
                for ro in range(size):
                    if randrange(size/2) == 0:
                        A[ro, co] = sparse_tree(a, a, a, randrange(3), 
                            False, True, False)
            det_gauss = A.determinant( determinant_algo.gauss)
            det_laplace = A.determinant( determinant_algo.laplace)
            det_divfree = A.determinant( determinant_algo.divfree)
            det_bareiss = A.determinant( determinant_algo.bareiss)
            if not (det_gauss - det_laplace).normal().is_zero() \
                or not (det_bareiss - det_laplace).normal().is_zero() \
                or not (det_divfree - det_laplace).normal().is_zero():
                    error = True
                    print "Determinant of", size, "x", size, "matrix", A
                    print "is inconsistent between different algorithms:"
                    print "Gauss elimination:   ", det_gauss
                    print "Minor elimination:   ", det_laplace
                    print "Division-free elim.: ", det_divfree
                    print "Fraction-free elim.: ", det_bareiss
        self.assertEqual(error,0)

    # Check the matrix inversion algorithm.
    def test_symbolic_matrix_inverse(self):
        """
        >>> symbolic_matrix_inverse()
        Symbolic matrix inverse test passed.
        """
        error = False
        a = symbol('a')
        b = symbol('b')
        c = symbol('c')
        for size in range(2, 6):
            A = matrix(size, size)
            while A.determinant() == 0:
                for co in range(size):
                    for ro in range(size):
                        if randrange(size/2) == 0:
                            A[ro, co] = sparse_tree(a, b, c, randrange(2), 
                                False, True, False)
            B = A.inverse()
            C = (A * B).evalm().normal()
            ok = True
            for ro in range(size):
                for co in range(size):
                    elem = C[ro, co]
                    if ro == co and elem != 1:
                        print "non-unity", "(", ro, ",", co, ")", elem
                        ok = False
                    if ro != co and elem != 0:
                        print "nonzero", "(", ro, ",", co, ")", elem
                        ok = False
            if not ok:
                print "Inverse of ", size, "x", size, "matrix", A
                print "errooneously returned:", B
                print "Its determinant is: ", A.determinant()
                error = True

        self.assertEqual(error,0)

if __name__ == "__main__":
    unittest.main()
