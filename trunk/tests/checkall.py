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
import sys

quick_tests = """
check_aritmetic
check_relat
check_lst
check_print
exam_matrices
exam_paranoia
exam_misc
exam_normalization
exam_diff
exam_lsolve
exam_polygcd
""".split()

time_consuming_tests = """
check_matrices
check_numeric
check_inifcns
check_lsolve
""".split()

modules = quick_tests
if len(sys.argv)==1:
    modules+= time_consuming_tests

sys.path.append(".")

tests=[]
for mod in modules:
        m=__import__(mod)
        tests.append(unittest.defaultTestLoader.loadTestsFromModule(m))
alltests=unittest.TestSuite(tests)
#print "Test suite loaded."
unittest.TextTestRunner(verbosity=1).run(alltests)
