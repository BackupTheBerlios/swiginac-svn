%module operators

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "operators.h"
%}

%include "numeric.i"
%include "relational.i"

namespace GiNaC {

class ex;
class numeric;
class relational;


const ex operator+(const ex & lh, const ex & rh);
const ex operator-(const ex & lh, const ex & rh);
const ex operator*(const ex & lh, const ex & rh);
const ex operator/(const ex & lh, const ex & rh);


const numeric operator+(const numeric & lh, const numeric & rh);
const numeric operator-(const numeric & lh, const numeric & rh);
const numeric operator*(const numeric & lh, const numeric & rh);
const numeric operator/(const numeric & lh, const numeric & rh);


ex & operator+=(ex & lh, const ex & rh);
ex & operator-=(ex & lh, const ex & rh);
ex & operator*=(ex & lh, const ex & rh);
ex & operator/=(ex & lh, const ex & rh);


numeric & operator+=(numeric & lh, const numeric & rh);
numeric & operator-=(numeric & lh, const numeric & rh);
numeric & operator*=(numeric & lh, const numeric & rh);
numeric & operator/=(numeric & lh, const numeric & rh);


const ex operator+(const ex & lh);
const ex operator-(const ex & lh);

const numeric operator+(const numeric & lh);
const numeric operator-(const numeric & lh);


//ex & operator++(ex & rh);
//ex & operator--(ex & rh);
//const ex operator++(ex & lh, int);
//const ex operator--(ex & lh, int);

//numeric& operator++(numeric & rh);
//numeric& operator--(numeric & rh);
//const numeric operator++(numeric & lh, int);
//const numeric operator--(numeric & lh, int);


const relational operator==(const ex & lh, const ex & rh);
const relational operator!=(const ex & lh, const ex & rh);
const relational operator<(const ex & lh, const ex & rh);
const relational operator<=(const ex & lh, const ex & rh);
const relational operator>(const ex & lh, const ex & rh);
const relational operator>=(const ex & lh, const ex & rh);


std::ostream & operator<<(std::ostream & os, const ex & e);
std::istream & operator>>(std::istream & is, ex & e);


std::ostream & dflt(std::ostream & os);
std::ostream & latex(std::ostream & os);
std::ostream & python(std::ostream & os);
std::ostream & python_repr(std::ostream & os);
std::ostream & tree(std::ostream & os);
std::ostream & csrc(std::ostream & os);
std::ostream & csrc_float(std::ostream & os);
std::ostream & csrc_double(std::ostream & os);
std::ostream & csrc_cl_N(std::ostream & os);

std::ostream & index_dimensions(std::ostream & os);
std::ostream & no_index_dimensions(std::ostream & os);

}
