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
from  sys import argv, exit
import os
from os.path import join as pjoin, sep as psep
import commands

def pkgconfig(*packages, **kw):
    """
    Use pkgconfig to find out where ginac is installed. Function found here:
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/502261.
    Modified by Skavhaug 2008 to better catch errors.
    """
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = commands.getoutput("pkg-config --libs --cflags %s" % ' '.join(packages))
    if "not found" in output:
        exit(1)

    for token in output.split():
        if token[:2] != "-W":
            kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

os.chdir(pjoin("src", "swiginac"))

# The command line argument for running swig in c++ mode has changed from
# Python 2.3 to 2.4. We support both.
swig_opt = '--swig-cpp'
if distutils.__version__ >= '2.4': swig_opt = '--swig-opts=-c++'

if argv[1] == 'build':
    argv[1] = 'build_ext'
if argv[1] == 'build_ext':
    argv.insert(2, swig_opt)
    
e = Extension(name='_swiginac',
              sources=['swiginac.i'],
              **pkgconfig("ginac")
             )

setup(name='swiginac',
    version='1.5.1',
    description='interface to GiNaC, providing Python with symbolic mathematics',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    ext_modules=[e],
    py_modules= ['swiginac'],
    )

os.chdir(os.pardir)

setup(name='Symbolic',
    version='0.3',
    description='Higher level mathematics module',
    author='Ola Skavhaug',
    author_email='skavhaug@simula.no',
    url='http://swiginac.berlios.de/',
    packages=["Symbolic"]
    )
