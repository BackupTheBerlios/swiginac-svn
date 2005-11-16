"""High--level symbolic manipulation, built on top of swiginac."""

__author__      = "Ola Skavhaug (skavhaug@simula.no)"
__date__        = "2003-12-01 -- 2005-11-16"
__copyright__   = "Copyright (c) 2003, 2004, 2005 Ola Skavhaug"
__license__     = "GNU GPL Version 2"

import swiginac as _g
_rel = _g.relational

def curl2d(obj):
    """Create a 2D curl from a scalar Expression"""
    return Vector([-obj.diff(obj.spatial_symbs[1], 1), obj.diff(obj.spatial_symbs[0], 1)], obj.spatial_symbs)

def div(obj):
    """Return the divergence of the argument expression"""
    return obj.div()

def grad(obj):
    """ Return the gradient of the argument expression"""
    return obj.grad()

def laplace(obj):
    """Return the Laplace of the argument expression"""
    return obj.laplace()

class Symbolic(object):
    """ Base class for Symbol, Expr, Vector, and Matrix."""
    # Common variables
    data = None
    string_type = "python"

    # Common methods
    def __str__(self):
        return str(self.data)
 

class Expr(Symbolic):
    """This class works a bit like GiNaC::ex. The actual data is stored in
    self.data, and the rest of this class provides various methods for doing
    symbolic manipulation."""

    def __init__(self, data = _g.numeric(0), symbs = None, time = None): 
        self.data = _toex(data)
        self.spatial_symbs = symbs
        self.time = time
        self._string = None
        self._lhs = []

    def __call__(self):
        return self.data

    def __repr__(self):
        return "Expr("+str(self)+")"

    def initEval(self, symbol_point):
        """In order to evaluate a GiNaC object, we need som additinal data
        structures. This method adds this."""

        self._lhs = map(lambda s: s.data, symbol_point)

    def __add__(self, other):
        return Expr(self.data + _toex(other), symbs=self.spatial_symbs, time=self.time)

    def __sub__(self, other):
        return Expr(self.data - _toex(other), symbs=self.spatial_symbs, time=self.time)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector([self.data*x for x in other.data], symbs=self.spatial_symbs, time=self.time)
        return Expr(self.data * _toex(other), symbs=self.spatial_symbs, time=self.time)

    def __div__(self, other):
        return Expr(self.data / _toex(other), symbs=self.spatial_symbs, time=self.time)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rdiv__(self, other):
        return self.__div__(other)

#    def __iadd__(self, other):
#        self.data += _toex(other)
#        return self

#    def __isub__(self, other):
#        self.data -= _toex(other)
#        return self

#    def __imul__(self, other):
#        self.data *= _toex(other)
#        return self

#    def __idiv__(self, other):
#        self.data /= _toex(other)
#        return self

    def __neg__(self):
        return Expr(-self.data, symbs=self.spatial_symbs, time=self.time)

    def __pos__(self):
        return Expr(+self.data, symbs=self.spatial_symbs, time=self.time)

    def __abs__(self):
        return Expr(_g.abs(self.data), symbs=self.spatial_symbs, time=self.time)

    def __pow__(self, other):
        return Expr(_g.power(self.data, _toex(other)).evalf(), symbs=self.spatial_symbs, time=self.time)

    def __eq__(self, other):
        return self.data == _toex(other)

    def __copy__(self):
        return Expr(self.data.copy(), symbs=self.spatial_symbs, time=self.time)

    def copy(self):
        return self.__copy__()

    def diff(self, symb, count=1):
        return Expr(self.data.diff(symb.data, count), symbs=self.spatial_symbs, time=self.time)

    def expand(self):
        return Expr(self.data.expand(), symbs=self.spatial_symbs, time=self.time)
        

    def pyEval(self, *args):
        """Evaluating using Python. Arguments are Python floats in the same
        order as used in initEval(symbol_point)."""
        for i in range(len(self._lhs)): exec("%s=%f" % (str(self._lhs[i]), args[i])) 
        s = str(self)
        from math import exp, log, sin, cos, tan, asin, atan, tanh
        #from operator import abs
        return eval(s)

    def eval(self, *args):
        """Evaluate Expr using GiNaC. Quite robust, not efficient."""
        return float(self.data.subs(self._lhs, list(args)).evalf())

    def setSymbols(self, symbs, time=None):
        print "Deprecated, use setSpatialSymbs instead"
        self.spatial_symbs = symbs
        self.time = time

    def setSpatialSymbols(self, symbs):
        self.spatial_symbs = symbs

    def setTimeSymbol(self, time):
        self.time = time

    def simplify(self):
        return Expr(_g.collect_common_factors(self.data), symbs=self.spatial_symbs, time=self.time)

    def grad(self):
        v = Vector(symbs=self.spatial_symbs, time=self.time)
        for i in range(len(self.spatial_symbs)): 
            v[i] = self.diff(self.spatial_symbs[i], 1)
        return v

    def laplace(self): 
        return self.grad().div()

    def hessian(self):
        m = self.grad().grad()
        l = len(self.spatial_symbs)
        hl = l*(l+1)/2
        hess = []
        for i in range(l):
            hess.append(m[i, i])
        for p in range(l-1):
            for q in range(p+1, l):
                hess.append(m[p, q])
        return hess

class Matrix(Symbolic):
    """Simple wrapping of GiNaC::Matrix, equipped with high-level
    mathematical operations."""

    """ Consider a new constructor that allows setting a Matrix directly with
    lists"""

    def __init__(self, *args, **kwargs):
        if isinstance(args[0], int):
            self.__init1__(*args, **kwargs)
        elif isinstance(args[0], list) and len(args) == 1:
            self.__init2__(*args, **kwargs)
        elif isinstance(args[0], _g.matrix) and len(args) == 1:
            self.__init3__(*args, **kwargs)
        else:
            raise TypeError, ("Wrong arguements to Matrix.__init__():", str(args))

    def __init1__(self, i, j, symbs=None, time=None):
        self.i = i; self.j = j
        self.data = _g.matrix(i, j)
        self.spatial_symbs = symbs
        self.time = time
        if not symbs:
            self.symbs = range(self.j)
        for i in range(self.i):
            for j in range(self.j):
                self[i, j] = Expr()
        self._lhs = []

    def __init2__(self, l, symbs=None, time=None):
        self.i = len(l)
        self.j = len(l[0])
        l = [[_toex(x) for x in sl] for sl in l] #Convert to nested list of swiginac types
        self.data = _g.matrix(l)
        self.spatial_symbs = symbs
        self.time = time
        if not symbs:
            self.symbs = range(self.j)
        self._lhs = []

    def __init3__(self, m, symbs=None, time=None):
        self.i = m.rows()
        self.j = m.cols()
        self.data = m.copy()
        self.spatial_symbs = symbs
        self.time = time
        if not symbs:
            self.symbs = range(self.j)
        self._lhs = []



    def __setitem__(self, index, value):
        i = index[0]; j = index[1]
        b = _toex(value)
        self.data.set(i, j, b)

    def __getitem__(self, index):
        """This method is under construction. It will be improved soon."""
        #print type(index)
        #print index
        i = None
        j = None
        if isinstance(index, tuple):
            if isinstance(index[0], int): # We know the row
                i = index[0]; 
                if i < 0:
                    i = self.i + i
            if isinstance(index[1], int): # We know the column
                j = index[1]
                if j < 0:
                    j = self.j + j
            if not i==None and not j == None:
                if i < self.i and j < self.j:
                    return Expr(self.data[i, j], symbs=self.spatial_symbs, time=self.time)
                else:
                    raise IndexError, "Index out of range"
            if isinstance(index[1], slice):
                #print "Second arg is slice"
                (start, stop, step) = (index[1].start, index[1].stop, index[1].step)
                if not i == None:
                    if start == stop == step == None:
                        return Vector([self.data[i, j] for j in range(self.j)], symbs=self.spatial_symbs, time=self.time)
                    if start == None: start = 0
                    elif start < 0: start = self.j + start
                    if stop == None: stop = self.i
                    elif stop< 0: stop = self.j + stop
                    if step == None: step = 1
                    return Vector([self.data[i, j] for j in range(start, stop, step)])
        elif isinstance(index, int): # Only one slice
            if index < 0:
                #print "i is less than 0"
                index = self.j + index 
                if index < 0:
                    raise IndexError, "Index out of range"
            return Vector([self.data[index, j] for j in range(self.j)], symbs=self.spatial_symbs, time=self.time)
        else:
            (start, stop, step) = (index.start, index.stop, index.step)
            if start == stop == step == None:
                return self.__copy__()
            if start == None: 
                start = 0
            if stop == None:
                stop = self.i
            if step == None:
                step = 1


            

    def addSymbols(self, list):
        self.symbs.extend(list)

    def __call__(self):
        return self.data()

        return self.string()

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return 'Matrix(' + str(self) + ')'

    def diff(self, symb, count=1):
        e = Expr(self())
        return e.diff(symb, count)

    def __add__(self, other):
        if isinstance(other, Matrix):
            m = Matrix(self.i, self.j, self.spatial_symbs, self.time)
            for i in range(self.i):
                for j in range(self.j):
                    m[i, j] = self[i, j]+other[i, j]
            return m
        else:
            raise TypeError, "Expected a Matrix, got %s" % (type(other))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            m = Matrix(self.i, self.j, self.spatial_symbs, self.time)
            for i in range(self.i):
                for j in range(self.j):
                    m[i, j] = Expr()
                    for k in range(self.i):
                        m[i, j] += self[i, k]*other[k, j]
            return m
        elif isinstance(other, Vector):
            v = Vector(self.symbs)
            for j in range(self.j):
                v[j] = Expr()
                for i in range(self.i):
                    v[j] += self[j, i]*other[i]
            return v
        else:
            b = _toex(other)
            m = Matrix(self.i, self.j, self.spatial_symbs, self.time)
            for i in range(self.i):
                for j in range(self.j):
                    m[i, j] = self[i, j]*b
            return m

    def __eq__(self, other):
        return self.data == _toex(other)

    def __copy__(self):
        return Matrix(self.data.copy(), symbs=self.spatial_symbs, time=self.time)

    def copy(self):
        return self.__copy__()


    def determinant(self):
        return Expr(self.data.determinant(), self.spatial_symbs, time=self.time)

    def initEval(self, symbol_point):
        """In order to evaluate an ex in GiNaC, we need som additinal data
        structures. This method adds this.
        """

        self._lhs = map(lambda s: s.data, symbol_point)

    def eval(self, *args):
        ret_vals = []
        for i in range(self.i):
            ret_vals.append([])
            for j in range(self.j):
                ret_vals[i].append(float(self[i, j].data.subs(self._lhs, list(args)).evalf()))
        return ret_vals

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            m = Matrix(self.i, self.j, self.spatial_symbs, self.time)
            for i in range(self.i):
                for j in range(self.j):
                    m[i, j] = self[i, j] - other[i, j]
            return m

    def transpose(self):
        m = Matrix(self.i, self.j, self.spatial_symbs, self.time)
        for i in range(self.i):
            for j in range(self.j):
                m[i, j] = self[j, i]
        return m

    def div(self):
        v = Vector(symbs=self.spatial_symbs, time=self.time)
        for j in range(self.j):
            v[j] = Expr(symbs=self.spatial_symbs, time=self.time)
            for i in range(self.i):
                v[j] += self[i, j].diff(self.spatial_symbs[i], 1)
        return v

class Vector(Symbolic):
    """Simple Vector consisting of Expr, and equipped with arithmetic and differential
    operators. Make sure that the entries the the list data, always are
    swiginac types!"""

    def __eq__(self, other):
        return self.data == _toex(other)
   
    def __call__(self):
        return self.data.eval()

    def __init__ (self, list=None, symbs=None, time=None):
        self.spatial_symbs = symbs
        self.time = time
        self._string = None
        if list: 
            self.data = map(lambda x: _toex(x), list)
        elif symbs: 
            self.data = map(lambda x: x(), symbs)
        else:
            self.data = []
        self._lhs = []
 
    def setSpatialSymbols(self, symbs):
        self.spatial_symbs = symbs
 
    def __setitem__(self, i, val):
        self.data[i] = _toex(val)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Vector("+str(self)+")"
 
    def __getitem__(self, i):
        return Expr(self.data[i], symbs=self.spatial_symbs, time=self.time)

    def __copy__(self):
        return Vector(self.data[:], symbs=self.spatial_symbs, time=self.time)

    def copy(self):
        return self.__copy__()

 
    def div(self):
        data = self.data
        s = self.spatial_symbs
        e = Expr(symbs=s, time=self.time)
        for i in range(len(self)): 
            e += data[i].diff(s[i].data, 1)
        return Expr(e, symbs=self.spatial_symbs, time=self.time)
 
    def initEval(self, symbol_point):
        """In order to evaluate the vector components in GiNaC, we need som
        additinal data structures. This method adds this.
        """
        self._lhs = map(lambda s: s.data, symbol_point)
 
    def pyEval(self, *args):
        for i in range(len(self._lhs)): exec("%s=%f" % (str(self._lhs[i]), args[i])) 
        s = str(self)
        from math import exp, log, sin, cos, tan, asin, atan
        from operator import abs
        ret_vals = []
        for comp in s: 
            ret_vals.append(eval(comp))
        return ret_vals
 
    def eval(self, *args):
        ret_vals = []
        for i in range(len(self)): 
            ret_vals.append(float(self.data[i].subs(self._lhs, list(args)).evalf()))
        return ret_vals
 
    def __add__(self, other):
        v = Vector(list=range(len(self)), symbs=self.spatial_symbs,  time=self.time)
        for i in range(len(self)):
            v[i] = self[i] + other[i]
        return v
 
    def __sub__(self, other):
        v = Vector(list=range(len(self)), symbs=self.spatial_symbs, time=self.time)
        for i in range(len(self)):
            v[i] = self[i] - other[i]
        return v
 
    def __mul__(self, other):
        if isinstance(other, int) | isinstance(other, float) | isinstance(other, Expr):
            v = Vector(list=range(len(self)), symbs=self.spatial_symbs, time=self.time)
            b = _toex(other)
            for i in range(len(self)):
                v[i] = self[i]*b
            return v
        elif isinstance(other, Matrix): #Vector-Matrix product
            v = Vector(symbs=self.spatial_symbs, time=self.time)
            for j in range(other.j):
                v[j] = Expr()
                for i in range(len(self)):
                    tmp = self[i]*other[i, j]
                    v[j] += tmp
            return v

    def __eq__(self, other):
        return self.data == _toex(other)
  
    def __radd__(self, other):
        return self.__add__(other)
 
    def __rsub(self, other):
        return self.__sub__(other)
 
    def __rmul__(self, other):
        return self.__mul__(other)

  
#    def __iadd__(self, other):
#        for i in range(len(self)):
#            self[i] += other[i]
#        return self
# 
#    def __isub__(self, other):
#        for i in range(len(self)):
#            self[i] -= other[i]
#        return self
# 
#    def __imul__(self, other):
#        if isinstance(other, Vector):
#            for i in range(len(self)):
#                self[i] *= other[i]
#        elif isinstance(other, Matrix):
#            result = Vector(symbs=self.spatial_symbs)
#            for j in range(other.j):
#                result[j] = 0
#                for i in range(len(self)):
#                    result[j] += other[j, i]*self[i]
#            return result
#        else:
#            rh = _toex(other)
#            for i in range(len(self)):
#                self.data.let_op(i, self[i]() * rh)
#        return self
# 
 
    def __neg__(self):
        v = Vector(symbs=self.spatial_symbs, time=self.time)
        for i in range(len(self)):
            v[i] = -self[i]
        return v
 
    def simplify(self):
        v = Vector(symbs=self.spatial_symbs, time=self.time)
        for i in range(len(self)):
            v[i] = self[i].simplify()
        return v
 
    def grad(self):
        n = len(self)
        m = Matrix(n, n, symbs=self.spatial_symbs, time=self.time)
        for i in range(n):
            for j in range(n):
                m[i, j] = self[j].diff(self.spatial_symbs[i], 1)
        return m

class Symbol(Symbolic):
    """Simple swiginac::symbol wrapper class, equipped with arithmetic
    operations."""

    def __init__(self, name = 'x'): 
        self.data = _g.symbol(name)
        self.spatial_symbs = [self.data]
        self.time = None

    def eval(self): 
        return self()

    def __rdiv__(self, other):
        return _toex(other)/self.data

    def __eq__(self, other):
        return self.data == _toex(other)

    def __call__(self): 
        return self.data

    def __add__(self, other):
        s = Expr(self)
        return s.__add__(other)

    def __radd__(self, other):
        e = Expr(self)
        return e.__radd__(other)

    def __sub__(self, other):
        s = Expr(self)
        return s.__sub__(other)

    def __rsub__(self, other):
        s = Expr(self)
        return s.__rsub__(other)

    def __mul__(self, other):
        s = Expr(self)
        return s.__mul__(other)

    def __div__(self, other):
        s = Expr(self)
        return s.__div__(other)


    def __rmul__(self, other):
        s = Expr(self)
        return s.__rmul__(other)

    def __neg__(self):
        neg = _g.numeric('-1')
        return self.__mul__(Expr(neg))

    def __str__(self):
        return str(Expr(self))

    def __repr__(self):
        return "Symbol('"+self.__str__()+"')"

    def __pow__(self, other):
        return Expr(self)**other

    def __rpow__(self, other):
        s = Expr(self)
        return Expr(_toex(other)**self.data)

    def __abs__(self):
        return Expr(_g.abs(self.data))

    def __copy__(self):
        new_symbol = Symbol()
        new_symbol.data = self.data.copy()
        return new_symbol

    def copy(self):
        return self.__copy__()

def _toex(other):
    """Converts other to GiNaC::ex.
    """
    if isinstance(other, (float, int)):
        return _g.numeric(other)
    elif isinstance(other, (Symbol, Expr, Matrix, Vector)):
        return other.data
    elif isinstance(other, (_g.basic)):
        return other
    elif isinstance(other, str):
        print "Can not convert a string to symbolic type"
        return _g.numeric(other)
    elif isinstance(other, list):
        return [_toex(x) for x in other]

Pi = _g.Pi
          
# Wrapping GiNaC::<function>s 
def exp(e):
    return Expr(_g.exp(e()), e.spatial_symbs, time=e.time)
def log(e):
    return Expr(_g.log(e()), e.spatial_symbs, time=e.time)

def sin(e):
    return Expr(_g.sin(e()), e.spatial_symbs, time=e.time)
def cos(e):
    return Expr(_g.cos(e()), e.spatial_symbs, time=e.time)
def tan(e):
    return Expr(_g.tan(e()), e.spatial_symbs, time=e.time)

def asin(e):
    return Expr(_g.asin(e()), e.spatial_symbs, time=e.time)
def acos(e):
    return Expr(_g.acos(e()), e.spatial_symbs, time=e.time)
def atan(e):
    return Expr(_g.atan(e()), e.spatial_symbs, time=e.time)

def sinh(e):
    return Expr(_g.sinh(e()), e.spatial_symbs, time=e.time)
def cosh(e):
    return Expr(_g.cosh(e()), e.spatial_symbs, time=e.time)
def tanh(e):
    return Expr(_g.tanh(e()), e.spatial_symbs, time=e.time)

def asinh(e):
    return Expr(_g.asinh(e()), e.spatial_symbs, time=e.time)
def acosh(e):
    return Expr(_g.acosh(e()), e.spatial_symbs, time=e.time)
def atanh(e):
    return Expr(_g.atanh(e()), e.spatial_symbs, time=e.time)

#def abs(e):
#    return Expr(_g.abs(e()), e.spatial_symbs, time=e.time)

def sqrt(e):
    return e**(0.5)

# Some help variables
_e = Expr()
_s = Symbol()

