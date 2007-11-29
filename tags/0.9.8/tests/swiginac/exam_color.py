# (c) Copyright 2006
#     Authors: Matti Peltomaki
#     based on regression tests for GiNaC,
#       Copyright (C) 1999-2006 Johannes Gutenberg University, Mainz
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
from swiginac import *

def check_equal(e1, e2):
    e = e1 - e2
    if not e.is_zero():
        print e1, "-", e2, " erroneously returned ", e
        return 1
    return 0

def check_equal_simplify(e1, e2):
    e = simplify_indexed(e1) - e2
    if not e.is_zero():
        print e1, "-", e2, " erroneously returned ", e
        return 1
    return 0

class test_color(unittest.TestCase):

    def test_color1(self):
        """checks general identities and contractions of the structure constants"""

        result = 0

        a = idx(symbol('a'), 8)
        b = idx(symbol('b'), 8)
        c = idx(symbol('c'), 8)
        d = idx(symbol('d'), 8)        
        
        result += check_equal(color_d(a, c, a), 0)
        result += check_equal_simplify(color_d(a, b, c) * color_d(b, d, c),
                                       numeric(5,3) * delta_tensor(a, d))
        result += check_equal_simplify(color_d(idx(5, 8), b, c) * color_d(b, idx(5, 8), c),
                                       numeric(5,3))
        result += check_equal_simplify(color_d(a, b, c) * color_d(b, c, a), numeric(40,3))
        result += check_equal_simplify(color_d(a, b, c) * color_f(b, d, c), 0)
        result += check_equal_simplify(color_d(a, b, c) * color_f(b, c, a), 0)
        result += check_equal_simplify(color_f(a, b, c) * color_f(b, c, a), 24)
        result += check_equal_simplify(color_f(a, b, c) * color_f(b, d, c), -3 \
                                       * delta_tensor(a, d))
        result += check_equal_simplify(color_h(a, b, c) * color_h(a, b, c), numeric(-32,3))
        result += check_equal_simplify(color_h(a, b, c) * color_h(b, a, c), numeric(112,3))

        e = color_h(a, b, c) * color_h(a, b, c)
        summ = 0
        for i in range(1,9):
            for j in range(1,9):
                for k in range(1,9):
                    summ += e.subs([a == i, b == j, c == k])
        if not summ.is_equal(numeric(-32,3)):
            print "numeric contraction of ", e, " erroneously returned ", summ
            print "instead of -32/3"
            result += 1

        self.assertEqual(result, 0)

    def test_color2(self):
        """checks general identities and contractions of the generators"""

        result = 0

        a = idx(symbol('a'), 8)
        b = idx(symbol('b'), 8)
        c = idx(symbol('c'), 8)
        k = idx(symbol('k'), 8)

        e = color_T(k) * color_T(k)
        result += check_equal_simplify(e, 4 * color_ONE() / 3)
        e = color_T(k) * color_T(a) * color_T(k)
        result += check_equal_simplify(e, -color_T(a) / 6)
        e = color_T(k) * color_T(a) * color_T(b) *  color_T(k)
        result += check_equal_simplify(e, delta_tensor(a, b) * \
                                       color_ONE() / 4 - color_T(a) * color_T(b) / 6)
        e = color_T(k) * color_T(a) * color_T(b) *  color_T(c) * color_T(k)
        result += check_equal_simplify(e, (color_h(a, b, c) * color_ONE() / 8).expand() \
                                       - color_T(a) * color_T(b) * color_T(c) / 6)
        e = color_T(a) * color_T(b) * color_T(a) *  color_T(b)
        result += check_equal_simplify(e, -2 * color_ONE() / 9)
        e = color_T(a) * color_T(b) * color_T(b) *  color_T(a)
        result += check_equal_simplify(e, 16 * color_ONE() / 9)
        e = color_T(a) * color_T(b) * color_T(c) * color_T(c) * color_T(b) *  color_T(a)
        result += check_equal_simplify(e, 64 * color_ONE() / 27)
        e = color_T(a) * color_T(b) * color_T(c) * color_T(k) * color_T(a) \
            * color_T(k) *  color_T(c) * color_T(b)
        result += check_equal_simplify(e, -color_ONE() / 162)

        self.assertEqual(result, 0)

    def test_color3(self):
        """checks traces """

        result = 0

        a = idx(symbol('a'), 8)
        b = idx(symbol('b'), 8)
        c = idx(symbol('c'), 8)

        e = color_ONE()
        result += check_equal(color_trace(e), 3)
        e = color_T(a)
        result += check_equal(color_trace(e), 0)
        e = color_T(a) * color_T(b)
        result += check_equal(color_trace(e), delta_tensor(a, b) / 2)
        e = color_T(a) * color_T(b) * color_T(c)
        result += check_equal(color_trace(e), color_h(a, b, c) / 4)

        e = color_ONE(0) * color_ONE(1) / 9
        result += check_equal(color_trace(e, 0), color_ONE(1) / 3)
        result += check_equal(color_trace(e, 1), color_ONE(0) / 3)
        result += check_equal(color_trace(e, 2), e)
        result += check_equal(color_trace(e, [0, 1]), 1)

        e = color_T(a, 0) * color_T(a, 1) * color_T(b, 0) * color_T(b, 1)
        result += check_equal_simplify(color_trace(e, 0), 2 * color_ONE(1) / 3)
        result += check_equal_simplify(color_trace(e, 1), 2 * color_ONE(0) / 3)
        result += check_equal_simplify(color_trace(e, 2), e)
        result += check_equal_simplify(color_trace(e, [0, 1]), 2)

        self.assertEqual(result, 0)

