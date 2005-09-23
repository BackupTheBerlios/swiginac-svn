#! /usr/bin/python

import sys
sys.path.append("..")
import swiginac as g

mu=g.varidx(g.symbol("mu"),4)
nu=g.varidx(g.symbol("nu"),4)
A=g.symbol("A")

e= g.indexed(A,mu,nu)*g.metric_tensor(mu,nu)

#e.set_print_context("tex")
print e
