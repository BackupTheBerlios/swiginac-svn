#!/usr/bin/env python
# -*- coding: latin-1 -*-

# (c) Copyright 2003, 2004, 2005
#     Authors: Ola Skavhaug, Ondrej Certik, Matti Peltomäki
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

class Test_truncation(unittest.TestCase):

    def testcheck_truncation(self):
        """
        >>> check_truncation()
        Truncation consistency checks passed.
        """

        a = symbol('a')
        b = symbol('b')
        x = symbol('x')
        e = power(power(x,a),b)
        es = e.subs([a==-0.9, b==2.5])
        f = power(x, numeric(-0.9)*numeric(2.5))
        self.assert_(es.is_equal(f))

if __name__ == "__main__":
    unittest.main()
