#! /usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

a=g.symbol("a")
b=g.symbol("b")
x=g.symbol("x")
y=g.symbol("y")

e1=a*x+b*y==3
e2=x-y==b

eqns=[e1,e2]
vars=[x,y]

mat = g.lsolve(eqns,vars)
print repr(mat)
print type(mat[0])
print type(e1)
print mat[1]
print eqns
