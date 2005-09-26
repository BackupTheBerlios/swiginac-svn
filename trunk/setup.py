#!/usr/bin/env python

"""
At the moment, this setup.py file is very crude. I expect it will
only work on Debian systems (no platform independence yet).

Make sure that you have at least SWIG version 1.3.24 and GiNaC
version 1.3.1.

To build and install swiginac, type:
python setup.py build
python setup.py install

To check your installation, change directory to ./tests, and run 
python checkall.py

Ola Skavhaug
Ondrej Certik
"""

from distutils.core import setup, Extension
import distutils
from  sys import argv



# The command line argument for running swig in c++ mode has changed from
# Python 2.3 to 2.4. We support both.
swig_opt = '--swig-cpp'
if distutils.__version__ >= '2.4': swig_opt = '--swig-opts=-c++'

if argv[1] == 'build':
    argv[1] = 'build_ext'
    argv.insert(2, swig_opt)

e = Extension(name='_swiginac', 
              sources=['swiginac.i'],
              include_dirs=['/usr/include/ginac'],
              library_dirs=['/usr/lib'],
              libraries=['ginac'],
              )

setup(name='swiginac',
    version='0.1',
    description='swiginac extention module',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    ext_modules=[e],
    py_modules = ['swiginac'],
    )
