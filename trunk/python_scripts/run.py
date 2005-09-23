#! /usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

a=g.symbol("a")
b=g.symbol("b")
x=g.symbol("x")
y=g.symbol("y")

i=g.idx(g.symbol("i"),3)
j=g.idx(g.symbol("j"),3)

A=g.symbol("A")

print g.indexed(A,i,j)
