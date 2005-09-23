/*
 (c) Copyright 2003, 2004, 2005
     Author: Ola Skavhaug and Ondrej Certik
     
     This file is part of swiginac.

     swiginac is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

     swiginac is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with swiginac; if not, write to the Free Software
     Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

%module swiginac

%{
#include "ginac.h"
using namespace GiNaC;
#include <sstream>
%}

%include std_string.i

namespace GiNaC {

%include "ex.i"
%include "ptr.i"
%include "typemaps.i"
%include "registrar.i"
%include "basic.i"
%include "symbol.i"
%include "numeric.i"
%include "relational.i"
%include "normal.i"
%include "constant.i"
%include "container.i"
%include "integral.i"
%include "matrix.i"
%include "expairseq.i"
%include "mul.i"
%include "ncmul.i"
%include "power.i"
%include "add.i"
%include "function.i"
%include "tensor.i"
%include "indexed.i"
%include "clifford.i"
%include "wildcard.i"
%include "flags.i"

};

%inline %{
namespace GiNaC {
    ex parse_string(const std::string &str, lst &ls) {
        return ex(str,ls);
    }
}
%};

// vim:ft=cpp:
