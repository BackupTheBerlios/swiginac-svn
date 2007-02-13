#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Standard setup.py file using Python's native distutils module for installation.
Make sure that you have at least SWIG version 1.3.24 and GiNaC version 1.3.2.

To build and install swiginac, type:
python setup.py build
python setup.py install

To check your installation, change directory to ./tests/swiginac, and run 
python checkall.py

Ola Skavhaug
Ondrej Certik
Åsmund Ødegård
"""

from distutils.core import setup, Extension
import distutils
from  sys import argv
import os
from os.path import join as pjoin, sep as psep

os.chdir(pjoin("src", "swiginac"))

# The command line argument for running swig in c++ mode has changed from
# Python 2.3 to 2.4. We support both.
swig_opt = '--swig-cpp'
if distutils.__version__ >= '2.4': swig_opt = '--swig-opts=-c++'

if argv[1] == 'build':
    argv[1] = 'build_ext'
if argv[1] == 'build_ext':
    argv.insert(2, swig_opt)
    

ginac_prefix=os.popen('ginac-config --prefix','r').readline().rstrip()
cln_prefix=os.popen('cln-config --prefix','r').readline().rstrip()

inclist = [psep, 'include', 'ginac']

e = Extension(name='_swiginac',
              sources=['swiginac.i'],
              include_dirs=['%s%s' % (ginac_prefix, pjoin(*inclist)),
                            '%s%s' % (cln_prefix, pjoin(*inclist[:-1]))],
              library_dirs=['%s%s' % (ginac_prefix, pjoin(psep, "lib")),
                            '%s%s' % (cln_prefix, pjoin(psep, "lib"))],
              libraries=['ginac'],
              )


#e = Extension(name='_swiginac', 
#              sources=['swiginac.i'],
#              include_dirs=['/usr/include/ginac'],
#              library_dirs=['/usr/lib'],
#              libraries=['ginac'],
#              )

setup(name='swiginac',
    version='0.9.5',
    description='interface to GiNaC, providing Python with symbolic mathematics',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    ext_modules=[e],
    py_modules= ['swiginac'],
    )


#os.chdir(os.path.join("src", "swiginac"))
os.chdir(os.pardir)

setup(name='Symbolic',
    version='0.3',
    description='Higher level mathematics module',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    packages=["Symbolic"]
    )


