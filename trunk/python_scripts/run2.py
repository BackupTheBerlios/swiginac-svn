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
vars=[x,y]
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
