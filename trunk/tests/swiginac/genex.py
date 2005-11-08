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
from random import random, randrange
import sys

# Helper functions for the testsuite.  These generate different kinds of
# expressions.

# Returns a univariate polynomial in symbol, through degree "degree"
def dense_univariate_poly( symbol, degree):
    unipoly = numeric(0)
    for i in range(degree):
        unipoly += numeric(randrange(-sys.maxint-1, sys.maxint)) * symbol**i
    return unipoly

# Returns a dense polynomial in x1 and x2, through degree "degree"
def dense_bivariate_poly( x1, x2, degree):
    ret = numeric(0)
    for i in range(degree):
        for j in range( degree-i):
            ret += numeric(randrange(-sys.maxint-1, sys.maxint)) * x1**i * x2**j
    return ret

# Randomly picks a symbol from x, y, or z, or a rational or complex number.
def random_symbol( x, y, z, rational=True, complex=False):
    i = randrange( 0, 4)
    if i == 0:
        return x
    elif i == 1:
        return y
    elif i == 2:
        return z
    else:
        c1 = randrange(-10, 10)
        c2 = None
        if rational:
            c2 = randrange(-10, 10)
            if c2 == 0:
                c2 = 1
        else:
            c2 = 1
        ret = numeric(c1)/c2
        if complex and randrange(5) == 0:
            ret *= I
        return ret

def sparse_tree( x, y, z, level, trig = False, # true includes trigonomatric functions
    rational = True, # false excludes coefficients in Q
    complex = True): # true includes complex numbers
    if level == 0:
        # Break recursion
        return random_symbol( x, y, z, rational, complex)
    i = randrange(10)
    if i < 4:
        return sparse_tree(x, y, z, level-1, trig, rational, complex) \
            + sparse_tree( x, y, z, level-1, trig, rational, complex)
    elif i < 7:
        return sparse_tree(x, y, z, level-1, trig, rational, complex) \
            * sparse_tree( x, y, z, level-1, trig, rational, complex)
    elif i < 9:
        powbase = sparse_tree( x, y, z, level-1, trig, rational, complex)
        while powbase == 0:
            powbase = sparse_tree( x, y, z, level-1, trig, rational, complex)
        return powbase**randrange(4)
    else:
        if trig:
            i = randrange(4)
            if i == 0:
                return sin( sparse_tree(x, y, z, level-1, trig, rational))
            elif i == 1:
                return cos( sparse_tree(x, y, z, level-1, trig, rational))
            elif i == 2:
                return exp( sparse_tree(x, y, z, level-1, trig, rational))
            else:
                logex = numeric(0)
                while logex == 0:
                    logarg = numeric(0)
                    while logarg == 0:
                        logarg = sparse_tree( x, y, z, level-1, trig, rational)
                    if not complex and logarg.info( info_flags.negative):
                        logarg = -logarg
                    logex = log(logarg)
                return logex
        else:
            return random_symbol( x, y, z, rational, complex)
            

