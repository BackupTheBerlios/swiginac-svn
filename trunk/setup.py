#!/usr/bin/env python

"""
At the moment, this setup.py file is very crude. I expect it will
only work on Debian systems (no platform independence yet).

Make sure that you have at least SWIG version 1.3.24 and GiNaC
version 1.3.2.

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
import os

os.chdir(os.path.join("src", "swiginac"))

# The command line argument for running swig in c++ mode has changed from
# Python 2.3 to 2.4. We support both.
swig_opt = '--swig-cpp'
if distutils.__version__ >= '2.4': swig_opt = '--swig-opts=-c++'

if argv[1] == 'build':
    argv[1] = 'build_ext'
    argv.insert(2, swig_opt)

ginac_prefix=os.popen('ginac-config --prefix','r').readline().rstrip()
cln_prefix=os.popen('cln-config --prefix','r').readline().rstrip()

e = Extension(name='_swiginac',
              sources=['swiginac.i'],
              include_dirs=['%s/include/ginac' % (ginac_prefix),
                            '%s/include' % (cln_prefix)],
              library_dirs=['%s/lib' % (ginac_prefix),
                            '%s/lib' % (cln_prefix)],
              libraries=['ginac'],
              )


#e = Extension(name='_swiginac', 
#              sources=['swiginac.i'],
#              include_dirs=['/usr/include/ginac'],
#              library_dirs=['/usr/lib'],
#              libraries=['ginac'],
#              )

setup(name='swiginac',
    version='0.9.1',
    description='swiginac extention module',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    ext_modules=[e],
    py_modules= ['swiginac'],
    )


#os.chdir(os.path.join("src", "swiginac"))
os.chdir(os.pardir)

setup(name='Symbolic',
    version='0.2',
    description='Higher level mathematics module',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    packages=["Symbolic"]
    )


