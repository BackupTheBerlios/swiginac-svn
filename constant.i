%module constant

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "constant.h"
%}
%include "basic.i"

namespace GiNaC {

typedef ex (*evalffunctype)(void);

class constant : public basic
{
public:
        constant(const std::string & initname, evalffunctype efun = 0, const std::string & texname = std::string());
        constant(const std::string & initname, const numeric & initnumber, const std::string & texname = std::string());
public:
        void print(const print_context & c, unsigned level = 0) const;
        ex evalf(int level = 0) const;
};

extern const constant Pi;
extern const constant Catalan;
extern const constant Euler;
}
