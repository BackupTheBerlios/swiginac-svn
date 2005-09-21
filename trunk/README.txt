Proposed road map:

- matrix([[a,b],[c,d]]) should do the same as lst_to_matrix([[a,b],[c,d]])

- tests/check_lst.py, make this work (the same issue as with lsolve)
  self.assertEqual(g.diag_matrix([x,y]),[[x,0],[0,y]])

- tests/check_matrices.py, the same
  self.assertEqual((A*B-(C*2)).evalm(),[[-13,-6],[1,2]])

- testsuites: 

  exam_misc - subs algebraic - overloaded typemaps problems
  exam_normalization - normal2

  search for "xtest" in the testsuite to find these failing tests.

- Solve the Makefile problem, so that it compiles with every python version
  (>=2.2?) automatically.

- Play with the code (refactoring)

How to contribute:

- Please make sure that the testsuites run without error prior to commiting
  changes, by running "make all check"

- Improve the usability of swiginac by writing tutorials and document the
  source code (interface files).

- Add more tests in the tests/ directory

- Use swiginac in your research activity, and tell other people about it.

- Set up a nice project home page (sourceforge? do they have svn repository?)

- Improve the Python module built on top of swiginac (Symbolic): swiginac should be able to do exactly the same things as ginac (ie matrices implemented using python lists belongs to swiginac), everything else should come to Symbolic.

Feature requests:


- Given an expression f, compute the gradient, and the eigenvalues of the
  corresponding matrix (Is this possible in GiNac?).
