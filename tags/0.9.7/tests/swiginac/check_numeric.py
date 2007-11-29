# (c) Copyright 2003, 2004, 2005
#     Authors: Ola Skavhaug and Ondrej Certik
#     based on regression tests for PyGiNaC,
#       Copyright (C) 2004, 2005 Jonathan Brandmeyer, Matti Peltomaki
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

from swiginac import *
from random import randrange
import sys
import unittest

class Test_numeric(unittest.TestCase):

    def testcheck_numeric1(self):
        """
        >>> check_numeric1()
        Basic consistency checks passed.
        """
        error = False
        # Check some numerator and denominator calcs
        for rep in range(200):
            re_q = randrange(1, sys.maxint)
            im_q = randrange(1, sys.maxint)
            r = numeric( randrange(-sys.maxint-1, sys.maxint), re_q)
            i = numeric( randrange(-sys.maxint-1, sys.maxint), im_q)
            z = r + I*i
            p = numer(z)
            q = denom(z)
            res = p/q
            if res != z:
                error = True
                print z, "erroneously transformed into ", p, "/", q, \
                    "by numer() and denom()"
                #print z, "erroneously transformed into ", \
                #    "by numer() and denom()"
        self.failIf(error)

    def testcheck_numeric2(self):
        """
        >>> check_numeric2()
        Basic consistency checks passed.
        """
        error = False
        # Check non-nested radicals (n/d)^(m/n) in ex wrapper class
        for i in range(200):
            for j in range( 2, 13):
                # construct an exponent 1/j...
                nm = numeric(1)/j
                nm += randrange( -10, 10)
                # a numerator
                i_num = randrange(1, sys.maxint)
                num = numeric(i_num)
                # and a denominator
                i_den = randrange(1, sys.maxint)
                den = numeric(i_den)
                # construct the radicals
                radical = (num/den)**nm
                if radical.__class__ == numeric:
                    # This should be very unlikely, it is probably a power object.
                    if radical**nm.inverse() == num/den:
                        # These aren't the numbers you're looking for.  Move along.
                        pass
                    else:
                        print "(", num, "/", den, ")**(", nm, \
                            ") erroneously returned:", radical
                        print "when it should have returend a power or product"
                        error = True
                # Note: The remaining parts of this test as found in GiNaC are not repeatable
                # with PyGiNaC's interface - this is intentional.
        self.failIf(error)

    def testcheck_numeric3(self):
        """
        >>> cehck_numeric3()
        Basic type conversion checks passed.
        """
        error = False
        x = symbol('x')
        res = int(x-x) 
        if ((not isinstance(res,int)) and (not res == 0)) :
            error = True
            print "int(x-x) erroneously transformed into ", res
        res = float(x-x)
        if ((not isinstance(res,float)) and (not res == 0.0)) :
            error = True
            print "float(x-x) erroneously transformed into ", res
        self.failIf(error)


if __name__ == "__main__":
    unittest.main()
