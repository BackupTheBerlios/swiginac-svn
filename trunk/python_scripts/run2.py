#! /usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

a=g.symbol("a")
b=g.symbol("b")
x=g.symbol("x")
y=g.symbol("y")
e1=a*x+b*y==3
#e1.tonum()
e2=x-y==b
eqns=[e1,e2]
vars=[x(),y()]
#l1=g.getlst(e1,e2)
#l2=g.getlst(x.eval(),y.eval())
#print l1
#print l2
#print g.lsolve(l1,l2)
#print g.lsolve(eqns,vars)
print g.lsolve(eqns,vars)
#print g.lsolve2(l1,l2)
e=x+y
print e.subs([x+y],[y+y])

#print g.cos(g.Pi*1)
#n=2
#expr = g.cos((g.numeric(n)+g.numeric(1)/g.numeric(2)) * g.Pi).eval()
#print type(expr)
#print expr


from swiginac import *

def inifcns_check_cos():
    """
    >>> inifcns_check_cos()
    Passed cosine checks.
    """
    error = False
    for n in range( -10, 10):
        expr = cos((numeric(n)+numeric(1)/numeric(2)) * Pi).eval()
        if expr != 0 or not expr.tonum().is_integer():
            error = True
            print "cos((n+1/2)*Pi) with integer n does not always return exact 0"
        expr = cos(n*Pi).eval()
        if not (expr == 1 or expr == -1) \
            or not expr.tonum().is_integer():
                error = True
                print "cos(n*Pi) with integer n does not always return exact {+|-}1"
    
    epsilon = numeric(1.0e-8)
    for n in range( -340, 340):
        arg = n*Pi/60
        if abs(cos(evalf(arg)) - cos(arg).evalf()) > epsilon:
            error = True
            print "cos(", arg, ") returns", cos(arg).evalf()
    if not error:
        print "Passed cosine checks."
    else:
        print "Failed cosine checks."

inifcns_check_cos()
