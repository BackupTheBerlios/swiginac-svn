# Swiginac - Extending Python with Symbolic Mathematics
# =====================================================
# 
# Ola Skavhaug [1]_\ [2]_   Ondrej Certic  [3]_\ [4]_
# 
# .. [1] Simula Research Laboratory
# .. [2] Dept. of Informatics, University of Oslo
# .. [3] Faculty of Mathematics and Physics
# .. [4] Charles University in Prague

# October 19-20 2005, TTI, Chicago
# 
# GiNaC
# -----
# 
# GiNaC__ is not a CAS. 
# GiNaC is a C++ library for applications in need of symbolic manipulation.
# Python__ is such an application.
# 
# Features:
# 
# *    Symbols and expressions with arithmetic operations
# *    Multivariate polynomials and rational functions
# *    Matrices and vectors
# *    Linear systems solver
# *    Tayler series expansions
# *    Differentiation and integration
# *    Output C, Python and LaTeX code
# *    ...
# 
# __ http://www.ginac.de
# __ http://www.python.org
# 
# Swiginac
# --------
# 
# Swiginac__ is a Python interface.
# 
# *   New strategy: Manually convert the GiNaC header files to
#     SWIG__ interface files, and implement a set of typemaps to
#     make a higher-level interface
# *   A lot, but not all, of the GiNaC classes are now exposed to
#     Python
# *   Certain GiNaC structures are converted to Python types in the
#     interface and vice versa
# 
# __ http://swiginac.berlios.de/
# __ http://www.swig.org/
# 
# Symbols
# -------
# Symbols are basic units in Swiginac::

from swiginac import *
a = symbol('a', r'\alpha')
b = symbol('b', r'\beta')
print b
u = b + a
u.set_print_context('tex')
print u

# All expressions in GiNaC are built with symbols. The drawback of
# this approach is that the level of abstraction is limited
# 
# Functions
# ---------
# Lots of functions are available ::

u = sin(exp(b))
v = tgamma(a+sqrt(b))

# >>> print u.printlatex()
# \sin(\exp(\beta))
# >>> print v.printlatex() 
# \Gamma(\alpha+\sqrt{\beta})
# 
# All trigonometric and hyperbolic functions are implemented in
# GiNaC, most of them interfaced in swiginac
# 
# Symbolic differentiation
# ------------------------
# Objects have the method diff for differentiation::

x = symbol('x')
y = symbol('y')

P = x**5 + x**2 + y
P.diff(x, 1)         #-> 5*x**4+2*x
P.diff(x, 2)         #-> 2+20*x**3
u = sin(exp(x))
u.diff(x,2)          #-> -sin(exp(x))*exp(x)**2+exp(x)*cos(exp(x))

# Matrices
# --------
# ::

mat1 = matrix(2,2)   # Two by two matrix
mat1[0,0] = v
mat1[1,1] = u
mat1a = diag_matrix([u,v]) # Alternative definition
mat1 == mat1a              # -> True
mat2 = matrix([[sqrt(a),0],[1.0, cosh(b)]])

# >>> print mat1 
# [[tgamma(a+b**(1/2)),0],[0,sin(exp(x))]]
# >>> print mat1.printlatex()
# \left(\begin{array}{cc}\Gamma(\alpha+\sqrt{\beta})&0\\0&\sin(\exp(x))\end{array}\right)
# >>> print mat2.printc()
# [[pow(a,(1.0/2.0)),0.0],[1.0000000000000000e+00,cosh(b)]]
# 
# Simple integral support
# -----------------------
# We can construct integral objects and integrate either symbolically
# or numerically::

x = symbol('x')
integ = integral(x, 0, 1, x*x)

print integ                #-> [integral object]
print integ.printlatex()   #-> \int_{0}^{1} dx\,x^{2}
print integ.eval_integ()   #-> 1/3
print integ.evalf()        #-> 0.33333333333333333332

# Substitution
# ------------
# Algebraic objects in expressions can be substituted::

u = sin(exp(b))
v = u.subs(exp(b)==sqrt(a)) # v = sin(a**(1/2))
w = v.subs(a==2).evalf()    # Convert sin(2**(1/2)) to numeric
wf = float(w)               # Convert to Python double

# >>> print v, w, wf 
# sin(a**(1/2)) 0.98776594599273552706 0.987765945993
#   
# Sub-expressions do not match::

x = symbol('x'); y = symbol('y'); z = symbol('z')
u = sin(x+y+z)
v = u.subs(x+y==4)             # v = sin(x+y+z)
w = u.subs([x==1, y==2, z==3]) # Same as u.subs(x+y+z==6)

# >>> print u, v, w
# sin(y+x+z) sin(y+x+z) sin(6)
#   
# Solving linear systems
# ----------------------
# ``lsolve`` solves linear systems::

x = symbol('x')
y = symbol('y')

solution = lsolve([3*x + 5*y == 2, 5*x+y == -3], [x,y])

# >>> print solution
# [x==-17/22, y==19/22]
# 
# Taylor series expansion
# -----------------------
# Expressions can expand themselves as a Taylor series::

x =symbol("x")
taylor = sin(x).series(x==0, 8)

# >>> print taylor  
# 1*x+(-1/6)*x**3+1/120*x**5+(-1/5040)*x**7+Order(x**8)
# 
