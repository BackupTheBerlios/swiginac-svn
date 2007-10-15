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

%include "pyexceptions.i"

%include stl.i
%include std_string.i
%include std_map.i
%include std_vector.i


%feature("autodoc", "1");

namespace GiNaC {

%feature("ref")   refcounted "$this->add_reference();"
%feature("unref") refcounted "$this->remove_reference();"


%include "ex.i"
%include "typemaps.i"
%include "ptr.i"
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
%include "idx.i"
%include "symmetry.i"
%include "clifford.i"
%include "color.i"
%include "wildcard.i"
%include "flags.i"
%include "pseries.i"
%include "inifcns.i"



%define ADD_REPR(name)
%extend name {
%pythoncode %{
    def __repr__(self):
        return self.__str__()
%}
};
%enddef

ADD_REPR(add);
ADD_REPR(mul);
ADD_REPR(power);
ADD_REPR(matrix);
ADD_REPR(clifford);
ADD_REPR(relational);
ADD_REPR(numeric);
ADD_REPR(function);
ADD_REPR(constant);
ADD_REPR(symbol);
ADD_REPR(integral);
ADD_REPR(idx);
ADD_REPR(varidx);
ADD_REPR(pseries);

};


// typedefs and template instantiations for stl containers with ginac objects

%typedef             std::vector<GiNaC::ex> GiNaC::exvector;
%template(exvector)  std::vector<GiNaC::ex>;

%typedef             std::map<GiNaC::ex, GiNaC::ex, GiNaC::ex_is_less> GiNaC::exmap;
%template(exmap)     std::map<GiNaC::ex, GiNaC::ex, GiNaC::ex_is_less>;

%pythoncode %{
_dict = {}
def get_symbols(name, number):
    global _dict
    if not _dict.has_key(name):
         _dict[name] = [symbol("%s%d" % (name,i)) for i in xrange(number)]
    else:
        x = _dict[name]
        n = len(x)
        if n >= number:
            return x[:]
        else:
            _dict[name] += [symbol("%s%d" % (name,i)) for i in xrange(n, number)]

    return _dict[name][:]
%}

%inline %{
namespace GiNaC {
    ex parse_string(const std::string &str, lst &ls) {
        return ex(str,ls);
    }

    ex * toex(lst& l) {
        return new ex(l);
    }

    ex * toex(lst* l) {
        return new ex(*l);
    }

    ex * toex(basic & b) {
        return new ex(b);
    }

}

%};

// vim:ft=cpp:
