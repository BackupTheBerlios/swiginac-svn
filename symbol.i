%module symbol

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%rename (gprint) print;
namespace GiNaC {};

%{
#include <string>
#include "basic.h"
#include "ex.h"
#include "symbol.h"
using namespace GiNaC;
%}
%include "registrar.i"
%include "basic.i"
using namespace GiNaC;

namespace GiNaC {

class symbol : public basic
{
//	GINAC_DECLARE_REGISTERED_CLASS(symbol, basic)
public:
   explicit symbol(const std::string & initname);
   explicit symbol(const std::string & initname, const std::string & texname);
public:
   void print(const print_context & c, unsigned level = 0) const;
   ex eval(int level = 0) const;
   ex evalf(int level = 0) const { return *this; }
};

%extend  symbol {
ex __call__() {
   return self->eval();
}
};
}
