#! /usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

a=g.symbol("a")
#print a
b=g.symbol("b")
x=g.symbol("x")
y=g.symbol("y")
e1=a*x+b*y==3
print e1
e2=x-y==b
eqns=[e1,e2]
vars=[x,y]
print "ano"
mat = g.lsolve(eqns,vars)
print mat[0]
print mat[1]
mat= g.lst_to_matrix([[x,0],[0,y]])
#mat= g.matrix(2,2,[[x,0],[0,y]])
mat= g.matrix(2,2,[x,0,0,y])
mat[0,1]=x.eval()
mat=g.matrix(2,2)
print type(mat)
print mat
