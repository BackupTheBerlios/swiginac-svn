# include definitions of Diffpack Makefile variables:

# SWIG-specific make variables:

#PYTHONVERSION = 2.4
PYTHONVERSION = 2.3
#GCC=g++-3.3
GCC=g++

#SWIG       = swig -v -Wall
SWIG       = swig 
INTERFACE  = swiginac
CXX        = $(GCC) 
CXXSHARED  = $(GCC) -shared
INCLUDES   = -I/usr/include/python$(PYTHONVERSION) -I/usr/include/ginac
CFLAGS     = -g -c -fpic
LDFLAGS = -lginac
PREFIX = $(HOME)/home/devel/pygin/

all:: python lib

python::
	$(SWIG) -c++ -python $(INTERFACE).i

lib::
	$(CXX) $(CFLAGS) $(INTERFACE)_wrap.cxx -o $(INTERFACE)_wrap.o  $(INCLUDES)
	$(CXXSHARED) $(INTERFACE)_wrap.o $(LDFLAGS) -o _$(INTERFACE).so
clean::
	rm -f *_wrap* *.so *.o $(OBJ_FILES)  *~ swiginac.py swiginac.pyc tests/*.pyc

install::
	mkdir -p $(PREFIX)/swiginac
	cp _$(INTERFACE).so $(PREFIX)/swiginac
	cp $(INTERFACE).py $(PREFIX)/swiginac/__init__.py

check::
	python tests/checkall.py

checkquick::
	python tests/checkall.py quick
