%module gprint

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include <sstream>
#include "print.h"
%}

class std::ostringstream: public std::ostream {
public:
      string str() const;
};

namespace GiNaC {

class print_context
{
public:
	print_context();
	print_context(std::ostream &);

%extend {
std::ostream* getstream() { return &(self->s); }

std::ostringstream* getstringstream() { 
   std::ostringstream* ss;
   ss = new std::ostringstream();
   return ss; 
}

std::string extractstring(std::ostringstream& ss) {
   return ss.str();
}
}

private:
	// dummy virtual function to make the class polymorphic
	virtual void dummy(void) {}
};


/** Context for latex-parsable output. */
class print_latex : public print_context
{
public:
	print_latex();
	print_latex(std::ostream &);
};

/** Context for python pretty-print output. */
class print_python : public print_context
{
public:
	print_python();
	print_python(std::ostream &);
};

/** Context for python-parsable output. */
class print_python_repr : public print_context
{
public:
	print_python_repr();
	print_python_repr(std::ostream &);
};

/** Context for tree-like output for debugging. */
class print_tree : public print_context
{
public:
	print_tree(unsigned d = 4);
	print_tree(std::ostream &, unsigned d = 4);
	const unsigned delta_indent; /**< size of indentation step */
};

/** Base context for C source output. */
class print_csrc : public print_context
{
public:
	print_csrc();
	print_csrc(std::ostream &);
};

/** Context for C source output using float numbers. */
class print_csrc_float : public print_csrc
{
public:
	print_csrc_float();
	print_csrc_float(std::ostream &);
};

/** Context for C source output using double numbers. */
class print_csrc_double : public print_csrc
{
public:
	print_csrc_double();
	print_csrc_double(std::ostream &);
};

/** Context for C source output using CLN numbers. */
class print_csrc_cl_N : public print_csrc
{
public:
	print_csrc_cl_N();
	print_csrc_cl_N(std::ostream &);
};
} // namespace GiNaC

