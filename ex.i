%module ex

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%rename (gprint) print;

%{
#include "ex.h"
#include "operators.h"
%}
%include "basic.i"

namespace GiNaC {
class library_init {
public:
        library_init();
        ~library_init();
};

static library_init library_initializer;

class ex
{
        template<class T> friend const T &ex_to(const ex &);
        template<class T> friend bool is_a(const ex &);
        template<class T> friend bool is_exactly_a(const ex &);
public:
        ex();
        ~ex();
        ex(const ex & other);
//        ex & operator=(const ex & other);
public:
        ex(const basic & other);
        ex(int i);
        ex(double const d);
        ex(const std::string &s, const ex &l);
public:
        void swap(ex & other);
        void print(const print_context & c, unsigned level = 0) const;
        ex eval(int level = 0) const { return bp->eval(level); }
        ex evalf(int level = 0) const { return bp->evalf(level); }
        ex evalm(void) const { return bp->evalm(); }
        ex diff(const symbol & s, unsigned nth = 1) const;
        ex subs(const lst & ls, const lst & lr, unsigned options = 0) const { return bp->subs(ls, lr, options); }
        ex subs(const ex & e, unsigned options = 0) const { return bp->subs(e, options); }
};

%extend ex {
ex __add__(ex& other) { return *self + other; }
ex __sub__(ex& other) { return *self - other; }
ex __mul__(ex& other) { return *self * other; }
ex __div__(ex& other) { return *self / other; }
ex & __imul__(ex& other) {
   *self *= other; return *self;
}
ex & __isub(ex& other) {
   *self -= other; return *self;
}
ex & __iadd__(ex& other) {
//   ex* e = new ex(*self);
//   *e += other; return *e;
   *self += other; return *self;
}
ex & __idiv(ex& other) {
   *self /= other; return *self;
}
ex __pos__() {
   return +*self;
}
ex __neg__() {
   return -*self;
}
ex __call__() {
   return *self;
}

};
}


