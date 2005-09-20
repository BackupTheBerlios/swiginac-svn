#!/usr/bin/python
import sys
sys.path.append("..")
import swiginac as g
def s(a,b):
	x= a
	x= +a
	x= -a
	x= a+b
	x= a-b
	x= a*b
	x= a/b
	x= a**b
def t(a,b):
	s(a,b)
	s(b,a)
a=g.numeric(2)
b=g.numeric("1.3")
c=g.symbol("x")
d=g.symbol("y")
e=pow(c,d)*d
f=5
g=5.5

t(a,a)
t(a,b)
t(a,c)
t(a,d)
t(a,e)
t(a,f)
t(a,g)

t(b,b)
t(b,c)
t(b,d)
t(b,e)
t(b,f)
t(b,g)

t(c,c)
t(c,d)
t(c,e)
t(c,f)
t(c,g)

t(d,d)
t(d,e)
t(d,f)
t(d,g)

t(e,e)
t(e,f)
t(e,g)

t(f,f)
t(f,g)

t(g,g)
