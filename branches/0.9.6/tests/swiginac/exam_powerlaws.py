# (c) Copyright 2005, 2006
#     Authors: Matti Peltomaki
#     based on regression tests for PyGiNaC,
#       Copyright (C) 2004, 2005, 2006 Jonathan Brandmeyer, Matti Peltomaki
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
from swiginac import *

class test_powerlaws(unittest.TestCase):

    def test_powerlaws1(self):
        result = 0

        a = symbol('a')
        b = symbol('b')
        x = symbol('x')

        e1 = power(power(x, a), b)
        if not(isinstance(e1,power) and
               isinstance(e1.op(0), power) and
               isinstance(e1.op(0).op(0), symbol) and
               isinstance(e1.op(0).op(1), symbol) and
               isinstance(e1.op(1), symbol) and
               e1 == power(power(x, a), b)):
            print "(x^a)^b with a,b,x symbolic wrong"
            print "returned: ", e1
            result += 1

        e2 = e1.subs(a==1)
        if not(isinstance(e2, power) and
               isinstance(e2.op(0), symbol) and
               isinstance(e2.op(1), symbol) and
               e2 == power(x, b)):
            print "(x^a)^b, x,b symbolic, a==1 wrong"
            print "returned: ", e2
            result += 1

        e3 = e1.subs(a==-1)
        if not(isinstance(e3, power) and
               isinstance(e3.op(0), power)  and
               isinstance(e3.op(0).op(0), symbol) and
               isinstance(e3.op(0).op(1), numeric) and
               isinstance(e3.op(1), symbol)  and
               e3 == power(power(x, -1), b)):
            print "(x^a)^b, x,b, symbolic, a==-1 wrong"
            print "returned: ", e3
            result +=1

        e4 = e1.subs([a==-1, b==2.5])
        if not(isinstance(e4, power) and
               isinstance(e4.op(0), power) and
               isinstance(e4.op(0).op(0), symbol)  and
               isinstance(e4.op(0).op(1), numeric) and
               isinstance(e4.op(1), numeric) and
               e4 == power(power(x, -1), 2.5)):
            print "(x^a)^b, x symbolic, a==-1, b==2.5 wrong"
            print "returned: ", e4
            result += 1

        e5 = e1.subs([a==-0.9, b==2.5])
        if not(isinstance(e5, power) and
               isinstance(e5.op(0), symbol) and
               isinstance(e5.op(1), numeric) and
               e5 == power(x, numeric(-0.9)*numeric(2.5))):
            print "(x^a)^b x symbolic, a==-0.9, b==2.5 wrong"
            print "returned: ", e5
            result += 1            

        e6 = e1.subs([a==numeric(3)+numeric(5.3)*I, b==-5])
        if not(isinstance(e6, power) and
               isinstance(e6.op(0), symbol) and
               isinstance(e6.op(1), numeric) and
               e6 == power(x, numeric(-15) + numeric(5.3)*numeric(-5)*I)):
            print "(x^a)^b, x symbolic, a==3+5.3*I, b==-5 wrong"
            print "returned: ", e6
            result += 1

        self.assertEqual(result,0)
    
    def test_powerlaws2(self):
        result = 0

        x = symbol('x')
        a = symbol('a')
        b = symbol('b')

        e1 = power(a*x, b)
        if not(isinstance(e1, power) and
               isinstance(e1.op(0), mul) and
               e1.op(0).nops() == 2 and
               isinstance(e1.op(0).op(0), symbol) and
               isinstance(e1.op(0).op(1), symbol) and
               isinstance(e1.op(1), symbol) and
               e1 == power(a*x, b)):
            print "(a*x)^b, a,x,b symbolic wrong"
            print "returned: ", e1
            result += 1            

        e2 = e1.subs(a==3)
        if not(isinstance(e2, power) and
               isinstance(e2.op(0), mul) and
               e2.op(0).nops() == 2 and
               isinstance(e2.op(0).op(0), symbol) and
               isinstance(e2.op(0).op(1), numeric) and
               isinstance(e2.op(1), symbol) and
               e2 == power(3*x, b)):
            print "(a*x)^b, x,b symbolic, a==3 wrong"
            print "returned: ", e2
            result += 1

        e3 = e1.subs(b==-3)
        if not(isinstance(e3, mul) and
               e3.nops() == 2 and
               isinstance(e3.op(0), power) and
               isinstance(e3.op(1), power) and
               e3 == power(a, -3) * power(x, -3)):
            print "(a*x)^b, a,x symbolic, b==-3 wrong"
            print "returned: ", e3
            result += 1            

        e4 = e1.subs(b==4.5)
        if not(isinstance(e4, power) and
               e4.op(0).nops() == 2 and
               isinstance(e4.op(0).op(0), symbol) and
               isinstance(e4.op(0).op(1), symbol) and
               isinstance(e4.op(1), numeric) and
               e4 == power(a*x, 4.5)):
            print "(a*x)^b, a,x symbolic, b==4.5 wrong"
            print "returned: ", e4
            result += 1            
        
        e5 = e1.subs([a==3.2, b==3+numeric(5)*I])
        if not(isinstance(e5, mul) and
               e5.nops() == 2 and
               isinstance(e5.op(0), power) and
               isinstance(e5.op(1), numeric) and
               e5 == power(x,3+numeric(5)*I) * power(numeric(3.2),3+numeric(5)*I)):
            print "(a*x)^b, x symbolic, a==3.2, b==3+5I wrong"
            print "returned: ", e5
            result += 1            

        e6 = e1.subs([a==-3.2, b==3+numeric(5)*I])
        if not(isinstance(e6, mul) and
               e6.nops() == 2 and
               isinstance(e6.op(0), power) and
               isinstance(e6.op(1), numeric) and
               e6 == power(-x,3+numeric(5)*I) * power(numeric(3.2),3+numeric(5)*I)):
            print "(a*x)^b, x symbolic, a==-3.2, b==3+5I wrong"
            print "returned: ", e6
            result += 1            

        e7 = e1.subs([a==3+numeric(5)*I, b==3.2])
        if not(isinstance(e7, power) and
               isinstance(e7.op(0), mul) and
               e7.op(0).nops() == 2 and
               isinstance(e7.op(0).op(0), symbol) and
               isinstance(e7.op(0).op(1), numeric) and
               isinstance(e7.op(1), numeric) and
               e7 == power((3+numeric(5)*I)*x,3.2)):
            print "(a*x)^b, x symbolic, a=3+5I, b=3.2 wrong"
            print "returned: ", e7
            result += 1            

        self.assertEqual(result, 0)
    
    def test_powerlaws3(self):
        """Numeric evaluation."""
        result = 0

        e1 = pow(numeric(4), numeric(1,2))
        if e1 != 2:
            print "4^(1/2) erroneously returned ", e1
            result += 1

        e2 = pow(numeric(27), numeric(2,3))
        if e2 != 9:
            print "27^(2/3) erroneously returned ", e2
            result += 1

        e3 = pow(numeric(5), numeric(1,2))
        if not(isinstance(e3, power) and
               e3.op(0) == numeric(5) and
               e3.op(1) == numeric(1,2)):
            print "5^(1/2) erroneously returned ", e3
            result += 1            

        e4 = pow(numeric(5), numeric(1,2).evalf())
        if not isinstance(e4, numeric):
            print "5^(0.5) erroneously returned ", e4
            result += 1
        
        e5 = pow(numeric(5).evalf(), numeric(1,2))
        if not isinstance(e5, numeric):
            print "5.0^(1/2) erroneously returned ", e5
            result += 1

        self.assertEqual(result, 0)

    def test_powerlaws4(self):
        """Test for mul.eval()""" 
        a = symbol('a')
        b = symbol('b')
        c = symbol('c')

        f1 = power(a*b, numeric(1,2))
        f2 = power(a*b, numeric(3,2))
        f3 = c

        result = 0
        e1 = mul(f1,f2,f3)
        if e1 != a*a*b*b*c:
            print "(a*b)^(1/2) * (a*b)^(3/2) * c erroneously returned ", e1
            result += 1

        self.assertEqual(result, 0)

    def test_powerlaws5(self):
        """Cabinet of slightly pathological cases"""
        result = 0

        a = symbol('a')

        e1 = pow(1,a)
        if e1 != 1:
            print "1^a erroneously returned ", e1
            result += 1

        e2 = pow(0,a)
        if not isinstance(e2, power):
            print "0^a was evaluated to ", e2
            print "even though nothing is known about a"
            result += 1

        self.assertEqual(result, 0)

if __name__ == "__main__":  
    unittest.main()
