Proposed road map:

- this testsuite doesn't run:

  exam_normalization: xtest_exam_normal2 - factoring out doesn't work

  the "x" in the front prevents "make check" to run it. Delete the "x" and
  fix it. Is it a bug in GiNaC, or in swiginac, or is it a feature?
  Needs investigating.

- Solve the Makefile problem, so that it compiles with every python version
  (>=2.2?) automatically.

- Play with the code (refactoring)

Maybe implement these, but maybe not - just an idea:

- tests/check_lst.py, make this work (the same issue as with lsolve)
  self.assertEqual(g.diag_matrix([x,y]),[[x,0],[0,y]])

- tests/check_matrices.py, the same
  self.assertEqual((A*B-(C*2)).evalm(),[[-13,-6],[1,2]])


How to contribute:

- Please make sure that the testsuites run without error prior to commiting
  changes, by running "make all check" (during the development, you can
  also use "make checkquick", which only runs a few quick tests, but prior to
  commiting, always run "make check"). 

- Improve the usability of swiginac by writing tutorials and document the
  source code (interface files).

- Add more tests in the tests/ directory and especially add tests to every
  new feature.

- Use swiginac in your research activity, and tell other people about it.

- Improve the project home page at berlios.

- Improve the Python module built on top of swiginac (Symbolic): swiginac
  should be able to do exactly the same things as ginac (ie matrices
  implemented using python lists belongs to swiginac), everything else should
  come to Symbolic.

Feature requests:

- Given an expression f, compute the gradient, and the eigenvalues of the
  corresponding matrix (Is this possible in GiNac?).
