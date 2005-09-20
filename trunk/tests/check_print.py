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


class test_print(unittest.TestCase):

    def test_basic_print(self):
        a = g.symbol('a','\\alpha')
        self.assertEqual(str(a), "a")
        a.set_print_context('tex')
        self.assertEqual(str(a), "\\alpha")

        b = a-a+g.Pi
        b.set_print_context('tex')
        self.assertEqual(str(b), "\\pi")
        b.set_print_context('c')
        self.assertEqual(str(b), "Pi")

if __name__ == "__main__":
    unittest.main()

