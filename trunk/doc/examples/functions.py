#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# ===============================================================
# functions.py: mathematical functions in swiGiNaC
# ===============================================================
# 
# :Date:      $Date$
# :Version:   SVN-Revision $Revision$
# :URL:       $URL: svn+ssh://svn.berlios.de/svnroot/repos/pylit/trunk/src/pylit.py $
# :Copyright: 2005, 2007 Guenter Milde.
#             Released under the terms of the GNU General Public License 
#             (v. 2 or later)





from swiginac import *

a = symbol("a")
k = symbol("k")
m = symbol("m")
n = symbol("n")
p = symbol("p")
s = symbol("s")
x = symbol("x")
y = symbol("y")

# GiNaC contains the following predefined mathematical functions:
# 
# Functions that are not mapped to swiginac, are commented out.

# Name                        Function
abs(x)                        # absolute value
# step(x)                       # step function
csgn(x)                       # complex sign
conjugate(x)                  # complex conjugation
# real_part(x)                  # real part
# imag_part(x)                  # imaginary part
sqrt(x)                       # square root (alias for pow(x, numeric(1, 2)))
sin(x)                        # sine
cos(x)                        # cosine
tan(x)                        # tangent
asin(x)                       # inverse sine
acos(x)                       # inverse cosine
atan(x)                       # inverse tangent
atan2(y, x)                   # inverse tangent with two arguments
sinh(x)                       # hyperbolic sine
cosh(x)                       # hyperbolic cosine
tanh(x)                       # hyperbolic tangent
asinh(x)                      # inverse hyperbolic sine
acosh(x)                      # inverse hyperbolic cosine
atanh(x)                      # inverse hyperbolic tangent
exp(x)                        # exponential function
log(x)                        # natural logarithm
Li2(x)                        # dilogarithm
Li(m, x)                      # classical polylogarithm as well as multiple polylogarithm
G(a, y)                       # multiple polylogarithm
G(a, s, y)                    # multiple polylogarithm with explicit signs for the imaginary parts
S(n, p, x)                    # Nielsen's generalized polylogarithm
H(m, x)                       # harmonic polylogarithm
zeta(m)                       # Riemann's zeta function as well as multiple zeta value
zeta(m, s)                    # alternating Euler sum
zetaderiv(n, x)               # derivatives of Riemann's zeta function
tgamma(x)                     # gamma function
lgamma(x)                     # logarithm of gamma function
beta(x, y)                    # beta function (tgamma(x)*tgamma(y)/tgamma(x+y))
psi(x)                        # psi (digamma) function
psi(n, x)                     # derivatives of psi function (polygamma functions)
factorial(n)                  # factorial function n!
binomial(n, k)                # binomial coefficients
Order(x)                      # order term function in truncated power series

                                                                                                   
# For functions that have a branch cut in the complex plane GiNaC follows the conventions for
# C++ as defined in the ANSI standard as far as possible. In particular: the natural logarithm
# (log) and the square root (sqrt) both have their branch cuts running along the negative real
