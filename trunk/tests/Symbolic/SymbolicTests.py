from Symbolic import *
import unittest
import math

class SymbolTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = Symbol('x')

    def testSymbAdd(self): 
        assert str(2*self.symbol) == '2*x'
        x = Symbol('x')
        x_symb = x
        x += 1
        assert x == 1 + x_symb

    def testSymbSub(self): 
        assert self.symbol - self.symbol == 0
        x = Symbol('x')
        x_symb = x
        x -= 1
        assert x == x_symb-1

    def testSymbMult(self): 
        assert str(self.symbol * self.symbol) == 'x**2'
        assert str(2 * self.symbol) == '2*x'
        x = Symbol('x')
        x_symb = x
        x *=3
        assert x == 3*x_symb

    def testSymbDiv(self): 
        assert str(self.symbol / self.symbol) == '1'
        assert str(self.symbol / (2*self.symbol)) == '1/2'
        assert str(1.0 / (self.symbol)) == 'x**(-1)'

    def testSymbPow(self):
        x = self.symbol
        assert x**3 == x*x*x
        assert str(3**x) == '3**x'

    def testSymbMisc(self):
        x = self.symbol
        assert str(-x) == '-x'
        assert str(--x) == 'x'
        assert str(abs(x)) == 'abs(x)'

class ExprTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = Symbol('x')
        self.expr = exp(self.symbol)

    def testExprAdd(self): 
        assert str(self.expr + self.expr) == '2*exp(x)'
        assert str(2+self.expr) == str(self.expr+2)
        e = self.symbol + 1
        e += 1
        assert e == self.symbol + 2

    def testExprEq(self):
        a = 1 + self.expr
        b = self.expr + 1
        assert a == b

    def testExprSub(self): 
        assert str(self.expr - self.expr) == '0'

    def testExprMult(self): 
        assert str(self.expr * self.expr) == 'exp(x)**2'
        assert str(2 * self.expr) == '2*exp(x)'
        # Expr*Vector multiplies each entry in Vector by Expr
        x = self.symbol
        y = Symbol('y')
        v = Vector([x,y])
        self.assertEqual(self.expr*v, Vector([exp(x)*x, exp(x)*y]))

    def testExprDiv(self): 
        assert str(self.expr / self.expr) == '1'
        assert str(self.expr / 2) == '1/2*exp(x)'

    def testExprEval(self):
        x = Symbol('x')
        y = Symbol('y')
        f = exp(x)*sin(y)
        f.initEval([x, y])
        assert f.eval(10, 5) == math.exp(10.0)*math.sin(5.0)

    def testExprPyEval(self):
        x = Symbol('x')
        y = Symbol('y')
        f = abs(exp(x)*sin(y))
        f.initEval([x, y])
        assert f.pyEval(10, 5) == f.eval(10, 5)


    def testExprExpand(self):
        x = Symbol('x')
        f = (x-1)*(x+1)
        self.assertEqual(f.expand(), x**2 - 1)

    def testExprDiff(self):
        x = Symbol('x')
        f = sin(x)
        self.assertEqual(f.diff(x), cos(x))
        self.assertEqual(f.diff(x,2), -sin(x))

class VectorTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = Symbol('x')
        self.symbol2 = Symbol('y')
        self.expr = exp(self.symbol)
        self.vec = Vector([self.expr,1+self.symbol2])

    def testVecAdd(self): 
        sum = self.vec + self.vec
        assert str(sum) == "[2*exp(x), 2+2*y]"
        sum += self.vec
        assert str(sum) == "[3*exp(x), 3+3*y]"

    def testVecEval(self):
        x = self.symbol
        y = self.symbol2
        self.vec.initEval([x,y])
        assert self.vec.eval(10,5) == [math.exp(10), 6.0]

    def testVecDiv(self):
        self.vec.setSpatialSymbols([self.symbol, self.symbol2])
        self.vec.div()

class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.mat = Matrix(2,2)
        self.symbol = Symbol('x')
        self.symbol2 = Symbol('y')
        self.expr = exp(self.symbol2)

        self.mat[0,0] = self.symbol
        self.mat[0,1] = self.expr
        self.mat[1,0] = 2*self.symbol
        self.mat[1,1] = 1+self.expr

    def testMatInit(self):
        m1 = Matrix([[0,0],[0,0]])
        assert str(m1)  == "[[0,0],[0,0]]"
        m1 = Matrix(2,2)
        assert str(m1)  == "[[0,0],[0,0]]"
        self.assertRaises(TypeError, Matrix, [[0,0],[0,0]], 2, 2)

    def testMatSubAdd(self):
        x = self.symbol
        y = self.symbol2
        m1 = Matrix([[sin(x),1],[cos(x+y),2]])
        m2 = Matrix([[sin(x),2],[cos(x+y),2]])
        self.assertEqual(str(m2-m1),'[[0,1],[0,0]]')
        self.assertEqual((m2-m1)+m1,m2)
        

    def testMatMul(self):
        tmpmat = self.mat*2
        assert str(tmpmat[0,0]) == '2*x'
        tmpmat *= 2
        assert str(tmpmat[0,0]) == '4*x'
        m1 = Matrix([[2,0],[0,1]])
        v = Vector([1, 2])
        self.assertEqual(str(m1*v), '[2, 2]')

    def testMatEval(self):
            x = self.symbol
            y = self.symbol2
            self.mat.initEval([x, y])
            assert self.mat.eval(10, 1) == [[10.0, math.exp(1.0)], [20.0, 1.0+math.exp(1.0)]]

class OperTestCase(unittest.TestCase):
    def setUp(self):
        self.x = Symbol('x')
        self.y = Symbol('y')

    def testDivergence(self):
        x = self.x
        y = self.y
        f = Vector([x * y, 1 + y], symbs=[x, y])
        self.assertEqual(div(f), 1+y)

    def testGradient(self):
        x = self.x
        y = self.y
        f = sin(x)*cos(y)
        f.setSpatialSymbols([x,y])
        assert grad(f) == [cos(y)*cos(x), -sin(x)*sin(y)]

    def testLaplace(self):
        x = self.x
        y = self.y
        f = sin(x)*cos(y)
        f.setSpatialSymbols([x,y])
        assert laplace(f) == div(grad(f)) == -2*cos(y)*sin(x) 


class MiscTestCase(unittest.TestCase):
    def testCopy(self):
        x = Symbol('x')
        self.assertEqual(x, x.copy())
        f = sin(x)
        self.assertEqual(f, f.copy())
        v = Vector([f,f+1])
        self.assertEqual(v, v.copy())
        m = Matrix([v,[exp(x), 0]])
        self.assertEqual(m, m.copy())
        self.assertEqual(f.diff(x,1), f.diff(x.copy(),1))

suite1 = unittest.makeSuite(SymbolTestCase)
suite2 = unittest.makeSuite(ExprTestCase)
suite3 = unittest.makeSuite(VectorTestCase)
suite4 = unittest.makeSuite(MatrixTestCase)
suite5 = unittest.makeSuite(OperTestCase)
suite6 = unittest.makeSuite(MiscTestCase)
allsuites = unittest.TestSuite((suite1, suite2, suite3, suite4, suite5, suite6))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(allsuites)
