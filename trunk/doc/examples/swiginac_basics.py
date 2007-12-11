# Basic examples
# ==============
# for the use of swiginac for symbolic computation with Python
# ------------------------------------------------------------

import swiginac
from swiginac import *
from pprint import pprint

# Symbols
# -------
# Symbols are basic units in Swiginac::

a = symbol('a')
print a
# a

# What's a symbol? ::

type(a)
pprint(vars(a))

# In Python, you must define a variable as symbol before you can use it in
# expressions.  
#
# Repeating the name (as identifier and as name argument) is boring, hence, a
# function to facilitate symbol generaton is nice.

# Symbol Factory
# ~~~~~~~~~~~~~~
# ::
    
import sys
def new_symbol(*names, **kwargs):
    """Create symbolic variables for all names in the argument list
    
    and bind them in the namespace of the `__main__` module.
    
    A keyword argument `parent` is interpreted as an object where the new
    symbols should be bound, e.g. 
    ``new_symbol('name1', 'name2', ..., parent=sys.modules[__name__])``
    binds the symbols in the calling modules namespace even if it is 
    not `__main__`.
    
    All other `kwarg`s are ignored.
    """
    obj=kwargs.get('obj', sys.modules['__main__'])
    for name in names:
        setattr(obj, name, symbol(name))


# Define some angle symbols::

new_symbol("alpha", "beta", "gamma")

print alpha, alpha.printlatex()
# alpha \alpha           # greek letters are preceded with '\' in tex output

# Define a-z as Symbols::

import string
new_symbol(*[name for name in string.lowercase])

print (a, type(a)), (z, type(z))
# (a, <class 'swiginac.symbol'>) (z, <class 'swiginac.symbol'>)


# Expressions
# -----------
# All expressions in GiNaC are built with symbols. 

a = symbol('a'); b = symbol('b'); c = symbol('c')

# They are converted to a "canonical" representation and have a class that
# depends on the "main" expression::

u = b + a/2; print u, type(u)
# b+1/2*a <class 'swiginac.add'>

v = (a+b)/2; print v, type(v)
# 1/2*b+1/2*a <class 'swiginac.add'>

w = (a+b)/c; print w, type(w)
# (b+a)*c**(-1) <class 'swiginac.mul'>

# In the `Symbolic` package, there is the common class `Symbolic.Expr`.


# Numbers
# -------
# The ``numeric`` class can manipulate arbitrary precision integers in a very
# fast way. Rational numbers are automatically converted to fractions of
# coprime integers. 
# 
# When specifying rational numbers, the expression that is the argument
# to `numeric` is evaluated using Pythons "standard" arithmetic, which is
# probabely not what we want:
# 
print numeric(1/3)
# 0
print numeric(1./3)
# 0.33333333333333331483
# 
# To prevent evaluation by the "normal" Python operators, rational numbers can
# be input as string value or as (numerator, denominator) tuple::
 
print numeric("1/3")
# 1/3
print numeric(1, 3), numeric(3, 9)
# 1/3 1/3

# Often, it is sufficient to specify one number in an expression as `numeric`::

print numeric(1)/3
# 1/3

# The ``evalf()`` method converts any number in GiNaC's expressions
# into floating point numbers::
 
numeric('1/7').evalf()
#  0.14285714285714285714

# The return value of ``evalf()`` is still a ``numeric`` value::

type(numeric('1/7').evalf())
# <class 'swiginac.numeric'>

# What does `evalm` do??
numeric('1/7').evalm()
# or `to_cl_N` ??
numeric('1/7').to_cl_N()

# You can convert it to a Python datatype by the usual Python means or 
# using the ``to_double()``, ``to_int()``, or ``to_long()`` methods::
 
type(numeric('1/7').to_double())
#   <type 'float'>


# Complex Numbers
# ---------------

# Python's complex numbers can currently not be converted to `numeric` objects::

numeric(1j)
# NotImplementedError: ...

# But there is the symbol ``I`` for the Imaginary Unit::

print I**2, 1j**2, I.printlatex()
# -1 (-1+0j) i

(2*I+3).real(), (2*I+3).imag()
# (3, 2)
# How do complex expression evaluate? ::

(2*I+3).evalf()
# 3.0+2.0*I

(2*I+3).to_double()
# 3.0
(2*I+3).real().to_double(), (2*I+3).imag().to_double()
# (3.0, 2.0)

# Functions
# ---------
# Lots of functions are available 
# (of course, not all objects defined in `swiginac` are functions, but the
# listing gives an idea)::

pprint(dir(swiginac))
pprint(vars(swiginac))


u = sin(exp(b))
v = tgamma(a+sqrt(b))

print u, v
# sin(exp(beta)) tgamma(beta**(1/2)+a)
# 
# All trigonometric and hyperbolic functions are implemented in
# GiNaC, most of them interfaced in swiginac

sc = cos(x) + I*sin(x)
ee = exp(I*x)
sc / ee


# Output styles
# -------------

# Symbol with additional TeX string representation
a = symbol('a', r'\alpha')
# greek letter names will be converted to commands in Tex output
b = symbol('beta')

u = a + b/2

# Return string expression according to style:
print repr(u)
# 1/2*beta+a
print u.printlatex()
# \alpha+\frac{1}{2} \beta
print u.printc()
# beta/2.0+a
print u.printpython()
# 1/2*beta+a

# Print string repr. (for debugging)::

u.dbgprint() 
# 1/2*beta+a
u.dbgprinttree()
# add @0x8157410, hash=0x73, flags=0x2, nops=2
#     beta (symbol) @0x81558d8, serial=11, hash=0x90cf60a2, flags=0xf, domain=0
#     1/2 (numeric) @0x8156e88, hash=0xc6ef3740, flags=0xf
#     -----
#     a (symbol) @0x8157490, serial=10, hash=0xdfeb1d7f, flags=0xf, domain=0
#     1 (numeric) @0x81a6140, hash=0x160af41d, flags=0xf
#     =====

# Set default output style for an object::

u.set_print_context('tex')
print u
# \alpha+\frac{1}{2} \beta

# Unfortunately, the print contex can be set only for individual objects, not
# on a per-module or per-application scale

# Symbolic differentiation
# ------------------------
# Objects have the method `diff` for differentiation::

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

print mat1 
# [[tgamma(a+b**(1/2)),0],[0,sin(exp(x))]]
print mat1.printlatex()
# \left(\begin{array}{cc}\Gamma(\alpha+\sqrt{\beta})&0\\0&\sin(\exp(x))\end{array}\right)
print mat2.printc()
# [[pow(a,(1.0/2.0)),0.0],[1.0000000000000000e+00,cosh(b)]]

A = matrix([[1,2,3,4]])
sin(A).evalf()


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
float(w)                    # Convert to Python double

print v, w, float(w) 
# sin(a**(1/2)) 0.98776594599273552706 0.987765945993
#   
# Sub-expressions do not match::

x = symbol('x'); y = symbol('y'); z = symbol('z')
u = sin(x+y+z)
v = u.subs(x+y==4)             # v = sin(x+y+z)
w = u.subs([x==1, y==2, z==3]) # Same as u.subs(x+y+z==6)

print u, v, w
# sin(y+x+z) sin(y+x+z) sin(6)

# Solving linear systems
# ----------------------
# ``lsolve`` solves linear systems::

x = symbol('x')
y = symbol('y')

solution = lsolve([3*x + 5*y == 2, 5*x+y == -3], [x,y])

print solution
# [x==-17/22, y==19/22]
# 
# Taylor series expansion
# -----------------------
# Expressions can expand themselves as a Taylor series::

x =symbol("x")
taylor = sin(x).series(x==0, 8)

print taylor  
# 1*x+(-1/6)*x**3+1/120*x**5+(-1/5040)*x**7+Order(x**8)


