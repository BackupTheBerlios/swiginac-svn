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

%typemap(in) (int idx0, int idx1) {
    $1 = PyInt_AsLong(PyTuple_GetItem($input,0));
    $2 = PyInt_AsLong(PyTuple_GetItem($input,1));
}

%typemap(in) lst & {
    $1=list2lst($input);
    if (!$1) return NULL;
}

%typemap(typecheck, precedence=1200) lst & {
    $1 = (PyList_Check($input)) ? 1 : 0;
}

%typemap(in) ex & {
    $1 = type2ex($input);
    if (!$1) return NULL;
}

%typemap(in) numeric & {
    $1 = type2numeric($input);
    if (!$1) return NULL;
}

%typemap(typecheck, precedence=1210) ex & {
    $1 = (checktype2ex($input)) ? 1 : 0;
}

%typemap(out) ex {
    $result = ex2type(&($1));
}

//%typemap(out) ex *{
//    $result = ex2type($1);
//    delete $1;
//}


%typemap(out) exvector {
    $result = exvector2list(&($1));
}

//it seems we don't need these
/*%typemap(out) lst & {
    $result = lst2list($1);
}

%typemap(out) ex &{
    $result = ex2type($1);
}*/

// vim:ft=cpp:
