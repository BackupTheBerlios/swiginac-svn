#PYTHONVERSION = 2.4
PYTHONVERSION = 2.3




PREFIX = /usr/lib/python$(PYTHONVERSION)/site-packages

all:: install

clean::
	rm -f __init__.pyc
	rm -rf ../build

install::
	mkdir -p $(PREFIX)/Symbolic
	cp __init__.py $(PREFIX)/Symbolic
	python $(PREFIX)/../compileall.py $(PREFIX)/Symbolic/

check::
	python ../../tests/Symbolic/SymbolicTests.py
