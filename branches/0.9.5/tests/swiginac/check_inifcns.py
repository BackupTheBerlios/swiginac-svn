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

from swiginac import *
from random import random
import unittest

class Test_inifcns(unittest.TestCase):

    def testinifcns_check_sin(self):
        """
        >>> inifcns_check_sin()
        Passed sine checks.
        """
        error = False
        # sin(n*Pi) == 0?
        for n in range(-10, 10):
            expr = sin(n*Pi)
            if expr != 0 or not expr.is_integer():
                    error = True
                    print "sin(n*Pi) with integer n does not always return exact 0"
        
        # sin((n+1/2)*Pi) == {+|-}1?
        for n in range( -10, 10):
            expr = sin((n+numeric(1,2))*Pi)
            if not (expr == 1 or expr == -1) \
                or not expr.is_integer():
                    error = True
                    print "sin((n+1/2)*Pi) with integer n does not always return exact {+|-}1"
        # compare sin((q*Pi).evalf()) with sin(q*Pi).eval().evalf()
        epsilon = numeric(1.0e-8)
        for n in range( -340, 340):
            arg = n*Pi/60
            if abs( sin(arg).evalf() -  sin( arg)) > epsilon:
                error = True
                print "sin(", arg, ") returns ", sin(arg).evalf()
        self.failIf(error)

    def testinifcns_check_cos(self):
        """
        >>> inifcns_check_cos()
        Passed cosine checks.
        """
        error = False
        for n in range( -10, 10):
            expr = cos((n+numeric(1)/2) * Pi)
            if expr != 0 or not expr.is_integer():
                error = True
                print "cos((n+1/2)*Pi) with integer n does not always return exact 0"
            expr = cos(n*Pi)
            if not (expr == 1 or expr == -1) or not expr.is_integer():
                    error = True
                    print "cos(n*Pi) with integer n does not always return exact {+|-}1"
        
        epsilon = numeric(1.0e-8)
        for n in range( -340, 340):
            arg = n*Pi/60
            if abs(cos(arg).evalf() - cos(arg)) > epsilon:
                error = True
                print "cos(", arg, ") returns", cos(arg).evalf()
        self.failIf(error)

    def testinifcns_check_tan(self):
        """
        >>> inifcns_check_tan()
        Passed tangent checks.
        """
        error = False
        epsilon = numeric(1.0e-8)
        for n in range( -340, 340):
            if not n%30 and n%60: 
                # skip poles
                continue
            arg = n*Pi/60
            if abs(tan(arg).evalf() - tan(arg)) > epsilon:
                error = True
                print "cos(", arg, ") returns", cos(arg).evalf()
        self.failIf(error)

    def testinifcns_check_Li2(self):
        """
        >>> inifcns_check_Li2()
        Passed dilogarithm checks.
        """
        error = False
        # check the relation Li2(z^2) == 2 * (Li2(z) + Li2(-z)) numerically, which
        # should hold in the entire complex plane:
        epsilon = numeric( 1.0e-16)
        for n in range( 200):
            # A number from -10 -> +10 in the complex plane.
            argument = numeric(20.0*random()-10.0) + numeric(20.0*random()-10.0)*I
            if abs(Li2(argument**2)-2*Li2(argument)-2*Li2(-argument)) > epsilon:
                print "Li2(z) at z==", argument, "failed to satisfy Li2(z^2)==2*(Li2(z)+Li2(-z))"
                error = True
        self.failIf(error)

    def testbasic(self):
        self.assertEqual(isinstance(cos(1), function),True)
        self.assertNotEqual(isinstance(cos(1), numeric),True)
        self.assertNotEqual(isinstance(cos(1).evalf(), function),True)
        self.assertEqual(isinstance(cos(1).evalf(), numeric),True)

if __name__ == "__main__":
    unittest.main()
