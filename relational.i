%module relational

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "relational.h"
%}
%include "basic.i"

namespace GiNaC {

class relational : public basic
{
public:
        enum operators {
                equal,
                not_equal,
                less,
                less_or_equal,
                greater,
                greater_or_equal
        };
public:
        relational(const ex & lhs, const ex & rhs, operators oper=equal);
public:
        void print(const print_context & c, unsigned level = 0) const;
        ex op(size_t i) const;
        ex eval(int level=0) const;
public:
        virtual ex lhs(void) const;
        virtual ex rhs(void) const;
//public:
//        operator safe_bool(void) const;
//        safe_bool operator!(void) const;
};
}
