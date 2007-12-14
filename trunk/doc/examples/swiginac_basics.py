# Symbolic Computation with Python
# ================================
# Basic examples for the use of swiginac
# --------------------------------------
# 
# .. contents:: 
# 
# This script will give a basic overview of what is possible combining
# symbolic computation by `GiNac` with the flexibility and richness of Python
# 
# Objects defined in this script can be imported with
# 
# >>> from swiginac_basics import *
# 
# The swiginac module wraps functions, data and classes defined in the ginac
# C++ library in a python module::

import swiginac
from swiginac import *

# >>> len(dir(swiginac))
# 617
# 
# introspection is possible with e.g. ::

# # pprint(dir(swiginac))
# # pprint(vars(swiginac))
# 
# 
# Symbols
# -------
# Symbols are basic units in Swiginac::

a = symbol('a')

# >>> a
# a
# 
# What's a symbol? 
# 
# The datatype is:
# 
# >>> type(a)
# <class 'swiginac.symbol'>
# 
# It defines two methods but inherits more than 100 others:
# 
# >>> len(dir(a))
# 105
# 
# If you want to list them all, try  ``pprint(dir(a))``
# 
# In most Computer Algebra Systems (CAS), any unbound variable can be used as
# a symbol. In Python, you must define a variable as symbol before you can use
# it in expressions.  
# 
# >>> y = 3*x_1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: name 'x_1' is not defined
# 
# >>> x = symbol('x')
# >>> y = 3*x
# 
# `y` is now an expression:
# 
# >>> y
# 3*x
# 
# In order to use `y` as a symbol again, an ordinary CAS would require you
# to *delete* it. In Python, you overwrite its current binding with a new assignment:
# 
# >>> y = symbol('y')
# >>> y
# y
# 
# Symbol Factory
# ~~~~~~~~~~~~~~
# 
# If you want to define a set of symbols, having to give the name twice (as
# identifier and as name argument) is boring, hence, a function to facilitate
# symbol generaton is nice. ::
    
import sys
def new_symbol(*names, **kwargs):
    """Create symbolic variables for all names in the argument list
    
    and bind them in the namespace of the `__main__` module.
    
    kwargs['obj'] -- an object where the new symbols should be bound, 
                     All other `kwarg`s are ignored.

    Example: create symbols in the calling modules namespace even if it is 
    not `__main__`.

        >>> new_symbol('x', 'y', obj=sys.modules[__name__])
        >>> x, type(x)
        (x, <class 'swiginac.symbol'>)

    """
    obj=kwargs.get('obj', sys.modules['__main__'])
    for name in names:
        setattr(obj, name, symbol(name))


# Define some greek symbols:
# 
# >>> new_symbol("alpha", "beta", "gamma")
# 
# Define a-z as Symbols in the main module::

import string
new_symbol(*[name for name in string.lowercase])

# Define a-z as Symbols in the main module in the current module::

new_symbol(obj=sys.modules[__name__], *[name for name in string.lowercase])

# Test
# 
# >>> [sym for sym in [a,b,c,d,e,f,g,h,i,j,k,l,m,n] if type(sym) != swiginac.symbol]
# []
# 
# Expressions
# -----------
# All expressions in GiNaC are built with symbols. 
# 
# 
# They are converted to a "canonical" representation and have a class that
# depends on the expression::

ab1 = a/2 + b
ab2 = (a+b)/2
ab3 = (a+b)/c 


# >>> ab1, type(ab1)
# (b+1/2*a, <class 'swiginac.add'>)
# >>> ab2, type(ab2)
# (1/2*b+1/2*a, <class 'swiginac.add'>)
# >>> ab3, type(ab3)
# (c**(-1)*(b+a), <class 'swiginac.mul'>)
#   
# In the `Symbolic` package, there is the common class `Symbolic.Expr`.
# 
# 
# Output styles
# ~~~~~~~~~~~~~
# 
# Symbols can be defined with additional TeX string representation
# Greek letter names will be converted to commands in Tex output::

a_pix = symbol('a_pix', 'a_\mathrm{pix}')
beta = symbol('beta')
ab = a_pix + beta/2

# Expressions have methods returning string representations in several styles:
# 
# >>> [method for method in dir(ab) if method.find('print') == 0]
# ['print_dispatch', 'printc', 'printlatex', 'printpython']
#  
# >>> ab.printpython()
# '1/2*beta+a_pix'
# >>> ab.printc()
# 'beta/2.0+a_pix'
# >>> ab.printlatex()
# '\\frac{1}{2} \\beta+a_\\mathrm{pix}'
# 
# More print related methods 
# 
# >>> [method for method in dir(u) if method.find('print') > 0]
# ['dbgprint', 'dbgprinttree', 'set_print_context']
# 
# A default output style (print context) can be set for an object
# 
# >>> print ab
# 1/2*beta+a_pix
# >>> ab.set_print_context('tex')
# >>> print ab
# \frac{1}{2} \beta+a_\mathrm{pix}
#   
# Unfortunately, this cannot be done on a per-module or per-application scale
# currently.
# 
# 
# Numbers
# -------
# 
# The ``numeric`` class can manipulate arbitrary precision integers in a very
# fast way. 
# 
# Rational numbers are automatically converted to fractions of coprime
# integers. 
# 
# >>> numeric('4/12')
# 1/3
# 
# The expression given to `numeric` is evaluated using Pythons "standard"
# arithmetic, which is probabely not what we want when specifying rational
# numbers:
# 
# >>> numeric(1/3)
# 0
# >>> numeric(1./3)
# 0.33333333333333331483
# 
# To prevent evaluation the "normal" Python way, rational numbers can
# be input as string value or as (numerator, denominator) tuple:
#  
# >>> numeric("1/3")
# 1/3
# >>> numeric(1, 3)
# 1/3
# 
# Often, it is sufficient to specify one number in an expression as `numeric`:
# 
# >>> numeric(1)/3
# 1/3
# 
# Converting numbers
# ~~~~~~~~~~~~~~~~~~
# 
# The `evalf` method converts any number in GiNaC's expressions
# into floating point numbers:
#  
# >>> numeric('1/7').evalf()
# 0.14285714285714285714
#   
# The return value of `evalf` is still a `numeric` value:
# 
# >>> type(numeric('1/7').evalf())
# <class 'swiginac.numeric'>
#   
# You can convert it to a Python datatype using the `to_double`, `to_int`, or
# `to_long` methods:
#  
# >>> type(numeric('1/7').to_double())
# <type 'float'>
# 
# There are other converting methods, like `numeric.evalm` or `numeric.to_cl_N`
# but what do they do?
# 
#   
# Complex Numbers
# ~~~~~~~~~~~~~~~
# 
# Complex numbers are represented as expressions with the imaginary unit `I`
# 
# >>> I, I**2
# (I, -1)
# 
# But their type is `numeric`:
# 
# >>> type(I), type(2 + 3*I)
# (<class 'swiginac.numeric'>, <class 'swiginac.numeric'>)
# 
# Python's `complex` numbers can currently not be converted to `numeric` objects::

z_p = 2+3j

# ``z_g = numeric(z_p)`` raises the exception
# 
# NotImplementedError: Wrong number of arguments for overloaded function 'new_numeric'.
#   ...
# 
# A workaround is to use an expression::
 
z_g = z_p.real + z_p.imag*I

# which will be simplified to a number:
# 
# >>> type(z_g)
# <class 'swiginac.numeric'>
# 
# How do complex expression evaluate? 
# 
# `evalf` converts real and imaginary part to floating point numbers
# 
# >>> z_g.evalf()
# 2.0+3.0*I
# 
# `to_double()` returns the real part as `double` instance
# 
# >>> z_g.to_double()
# 2.0
# 
# While Phyton's `complex` class stores real and imaginary part as attributes,
# `numeric` provides methods to retrieve them (as `numeric` instances):
# 
# >>> z_p.real, z_g.real
# (2.0, <bound method numeric.real of 2.0+3.0*I>)
# 
# >>> z_g.real(), z_g.imag()
# (2.0, 3.0)
# 
#   
# Functions
# ---------
# 
# About 40 mathematical functions are available in `swiginac`.  All
# trigonometric and hyperbolic functions are implemented. For a full list of
# available functions see the file `doc/examples/functions.py`.
# 
# Some functions are simplified if this is mathemetically sound and non-ambiguous.
# 
# >>> sin(x), sin(0), sin(Pi/2)
# (sin(x), 0, 1)
# >>> cos(x), cos(0), cos(Pi/2)
# (cos(x), 1, 0)
# >>> tan(x), tan(0), tan(Pi/2)
# Traceback (most recent call last):
#   ...
# StandardError: tan_eval(): simple pole
# 
# But not all simplifications are implemented
# 
# >>> sin(x)**2 + cos(x)**2
# sin(x)**2+cos(x)**2
# 
# ::

z_s = cos(x) + I*sin(x)
z_e = exp(I*x)

# >>> z_s/z_e
# exp(I*x)**(-1)*(I*sin(x)+cos(x))
# 
# Is there a way get more simplifications?
# 
# 
# Symbolic differentiation
# ------------------------
# 
# Objects have the method `diff` for differentiation which is also called by
# the `diff` function:
# 
# >>> P = x**5 + x**2 + x
# 
# 
# >>> P.diff(x) == diff(P, x)
# 1+5*x**4+2*x==1+5*x**4+2*x
# 
# >>> P.diff(x, 2) == diff(P, x, 2)
# 2+20*x**3==2+20*x**3
# 
# >>> diff(sin(exp(x)), x) == sin(exp(x)).diff(x)
# cos(exp(x))*exp(x)==cos(exp(x))*exp(x)
# 
# 
# Matrices
# --------
# 
# Marices can be defined giving the number of rows and columns::

M1 = matrix(2,2)

# Elements will be initialized with 0 and can be set individually::

M1[0,0] = x
M1[1,1] = y

# >>> M1
# [[x,0],[0,y]]
# >>> M1.printc()
# '[[x,0.0],[0.0,y]]'
# >>> M1.printlatex()
# '\\left(\\begin{array}{cc}x&0\\\\0&y\\end{array}\\right)'
# 
# Alternatively, they can be initialized by a list of lists::

M2 = matrix([[x,0],[0, y]])

# Diagonal matrices can be created with a special constructor::

M3 = diag_matrix([x, y])

# >>> bool(M1 == M2 == M3)
# True
#   
# Vectors are (1,n) or (n,1) matrices::

A = matrix([range(4)])
B = matrix([[a], [b], [c]])
C = matrix([[0], [1], [2]])

# But why is the matrix product not working?
# 
# >>> print A*B
# [[0,1,2,3]]*[[a],[b],[c]]
# >>> C = matrix([[0], [1], [2]])
# >>> print A*C
# [[0,1,2,3]]*[[0],[1],[2]]
#   
# Functions are not broadcast to the matrix elements as in NumPy
#   
# >>> sin(A)
# sin([[0,1,2,3]])
# 
# How about substitution?
# 
# >>> sin(x).subs(x == A)
# sin([[0,1,2,3]])
# 
# 
# Simple integral support
# -----------------------
# 
# We can construct integral objects and integrate either symbolically
# or numerically::

x = symbol('x')
integ = integral(x, 0, 1, x*x)

# >>> integ
# [integral object]
# >>> print integ.printlatex()
# \int_{0}^{1} dx\,x^{2}
# >>> integ.eval_integ()
# 1/3
# >>> integ.evalf()
# 0.33333333333333333332
# 
# 
# Substitution
# ------------
# 
# Algebraic objects in expressions can be substituted::

s0 = sin(exp(x))
s1 = s0.subs(exp(x)==sqrt(y))
s2 = s1.subs(y==2)

# >>> s1
# sin(y**(1/2))
# >>> s2.evalf()
# 0.98776594599273552706
# >>> float(s2.evalf())
# 0.98776594599273548
# 
#   
# Sub-expressions do not match::

s3 = sin(x+y+z)

# >>> s3.subs(x+y==4)
# sin(x+z+y)
# 
# However, these should match and substitute but currently fail the doctest:
# 
# >>> s3.subs([x==1, y==2, z==3]) 
# sin(6)
# >>> s3.subs(x+y+z==6)
# sin(6)
# 
# 
# Solving linear systems
# ----------------------
# 
# The function `lsolve` solves linear systems::

lgs = [3*x + 5*y == 2, 5*x+y == -3]

ev = lsolve(lgs, [x,y])

# >>> ev
# [x==-17/22, y==19/22]
# >>> lgs[0].subs(ev)
# 2==2
# >>> lgs[1].subs(ev)
# -3==-3
# 
# Taylor series expansion
# -----------------------
# 
# Expressions can expand themselves as a Taylor series::

x =symbol("x")
taylor = sin(x).series(x==0, 8)

# >>> taylor  
# 1*x+(-1/6)*x**3+1/120*x**5+(-1/5040)*x**7+Order(x**8)
# 
# 
# Interaction with Python
# -----------------------
# 
# Series and sums
# ~~~~~~~~~~~~~~~
# 
# A series could be defined as a Python sequence, e.g.
# 
# >>> [x/n for n in range(1, 10)]
# [x, 1/2*x, 1/3*x, 1/4*x, 1/5*x, 1/6*x, 1/7*x, 1/8*x, 1/9*x]
# 
# >>> sinc5 = [sin(phi)/phi for phi in range(1,5)]; sinc5
# [sin(1), 1/2*sin(2), 1/3*sin(3), 1/4*sin(4)]
# 
# Attention, the loop index is no longer a symbol but an integer now
# 
# >>> n, phi
# (9, 4)
# 
# 
# As the standard function sum is overloaded for swiginac classes, it can be
# used on sequences of symbols or expressions:
# 
# >>> sum((x, y, z))
# y+z+x
# 
# >>> sum([x/n for n in range(1, 10)])
# 7129/2520*x
# 
# >>> sum(sinc5)
# 1/4*sin(4)+1/3*sin(3)+1/2*sin(2)+sin(1)
# 
# 
