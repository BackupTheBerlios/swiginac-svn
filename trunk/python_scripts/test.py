#!/usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

def E(x):
	one=g.numeric("0")
	return x+one
def integ(a,b,c,d):
	return E(g.integral(E(a),E(b),E(c),E(d)))

#pi=2*g.asin(1)

def Hermite(x,n):
	HKer=g.exp(-pow(x,2))
	return (pow(-1,n)*HKer.diff(x,n)/HKer).normal()

def Legendre(x,n):
#	return ((x**2-1)**n).diff(x,n)/(2**n * g.factorial(n)).normal()
	return ((x**2-1)**n).diff(x,n).normal()
def Li(x,n):
#	return ((x**2-1)**n).diff(x,n)/(2**n * g.factorial(n)).normal()
	return ((x**2-1)**n).diff(x,n-1).normal()

def P(n,x):
	return Legendre(x,n)

def factorial(n):
    if n==0:
        return 1.0
    else:
        return n*factorial(n-1)

def f(n):
	a= factorial(n)*g.numeric(2)**n
	for i in range(1,n+1):
		if i-i/2*2>0.1:
			a*=i
		else:
			a/=-i
	return a

a=g.symbol("a")
b=g.symbol("b")
x=g.symbol("x")
for i in range(10): print "H_%d(z) = %s"%(i,Legendre(a,i))
#for i in range(20): print "H_%d(z) = %s %s"%(i,Legendre(a,i).tcoeff(E(a)),f(i))
print "\n"
#e=g.log(a+1)
#print e.series(a*1,20)
#i=integ(x,0,a/2,x*x)
#n=9
#pn=P(n,x)
#print integ(x,0,1,pn).eval_integ()
#print -Li(x,n).tcoeff(E(x))
#print -Li(x,n)
