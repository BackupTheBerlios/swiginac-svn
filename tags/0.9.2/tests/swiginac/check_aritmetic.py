# (c) Copyright 2003, 2004, 2005
#     Authors: Ola Skavhaug and Ondrej Certik
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
import swiginac as g

class test_aritmetic(unittest.TestCase):

    def dotest(self,s):
        def t(a,b):
            s(a,b)
            s(b,a)
        a=g.numeric(2)
        b=g.numeric("1.3")
        c=g.symbol("x")
        d=g.symbol("y")
        e=pow(c,d)*d
        f=5
        h=5.5

        t(a,a)
        t(a,b)
        t(a,c)
        t(a,d)
        t(a,e)
        t(a,f)
        t(a,h)

        t(b,b)
        t(b,c)
        t(b,d)
        t(b,e)
        t(b,f)
        t(b,h)

        t(c,c)
        t(c,d)
        t(c,e)
        t(c,f)
        t(c,h)

        t(d,d)
        t(d,e)
        t(d,f)
        t(d,h)

        t(e,e)
        t(e,f)
        t(e,h)

        t(f,f)
        t(f,h)

        t(h,h)

    def testbasic(self):
        def s(a,b):
            x= a
            x= +a
            x= -a
            x= a+b
            x= a-b
            x= a*b
            x= a/b
            x= a**b
        self.dotest(s)

    def testibasic(self):
        def s(a,b):
            x= a
            x+=b
            x= a
            x-= b
            x= a
            x*=b
            x= a
            x/= b
        self.dotest(s)

if __name__ == "__main__":
    unittest.main()
