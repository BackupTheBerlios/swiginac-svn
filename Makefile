prefix     = $(EXTSOFT)# E.g. /usr/local
pylibdir	  = $(HOME)/home/devel/pygin/# E.g. a place in $PYTHONPATH 
SWIGMAKEFILE = $(prefix)/SWIG-1.3.19/Examples/Makefile
SWIG       = $(prefix)/bin/swig -v
#SWIG       = /usr/bin/swig-1.3
CXXSRCS    = 
TARGET     = swiginac
INTERFACE  = swiginac.i
LIBS       = -lm
INC     = -I$(prefix)/include # -I$(prefix)/include/ginac
LDFLAGS = -L$(prefix)/lib

all::
	$(MAKE) -f $(SWIGMAKEFILE) CXXSRCS='$(CXXSRCS)' SWIG='$(SWIG)' \
	INCLUDES='$(INCLUDES) $(INC)' \
	LIBS='$(LIBS) $(LDFLAGS) -lginac' \
	TARGET='$(TARGET)' INTERFACE='$(INTERFACE)' python_cpp

static::
	$(MAKE) -f $(SWIGMAKEFILE) CXXSRCS='$(CXXSRCS)' SWIG='$(SWIG)' \
	TARGET='mypython' INTERFACE='$(INTERFACE)' python_cpp_static

clean::
	$(MAKE) -f $(SWIGMAKEFILE) python_clean
	rm -f example.py

check: all

export::
	cp Makefile *i ~/export/swiginac/.
install::
	cp _swiginac.so $(pylibdir)/Swiginac/.
	cp swiginac.py  $(pylibdir)/Swiginac/__init__.py
