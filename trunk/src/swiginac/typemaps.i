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
    if(PyTuple_Check($input))
    {
        $1 = PyInt_AsLong(PyTuple_GetItem($input,0));
        if(PyTuple_Size($input) > 1)
            $2 = PyInt_AsLong(PyTuple_GetItem($input,1));
        else
            $2 = 0;
    }
    else
    {
        $1 = PyInt_AsLong($input);
        $2 = 0;
    }
}

%typemap(in) lst & {
    $1=list2lst($input);
    if (!$1) return NULL;
}

%typemap(in) const lst & {
    $1=list2lst($input);
    if (!$1) return NULL;
}

%typemap(typecheck, precedence=1200) lst & {
    $1 = (PyList_Check($input)) ? 1 : 0;
}

%{
// class to handle deleting a temporary resource in an input typemap
template<class T>
class TDeleter
{
public:

  T * obj;
  
  TDeleter():
    obj(0)
  {
    //std::cout << "TDeleter constructor." << std::endl;
  }
  
  ~TDeleter()
  {
    //std::cout << "TDeleter destructor, obj = " << obj << std::endl;
    if(obj)
    {
      //std::cout << "TDeleter deleting obj:" << std::endl;
      delete obj;
      //std::cout << "TDeleter done deleting obj." << std::endl;
    }
    //std::cout << "TDeleter is now destroyed." << std::endl;
  }

};

typedef TDeleter<GiNaC::ex> ex_deleter;
typedef TDeleter<const GiNaC::ex> const_ex_deleter;
%}

%typemap(in) ex & (ex_deleter deleter) {
  $1 = type2ex($input);
  if ($1 == NULL ) {
      return NULL;
  }
  deleter.obj = $1;
}

%typemap(in) const ex & (const_ex_deleter deleter) {
  $1 = type2ex($input);
  if ($1 == NULL ) {
      return NULL;
  }
  deleter.obj = $1;
}

//%typemap(in) const ex & = ex &;

%typemap(in) ex  {
  ex *tmp = type2ex($input);
  if (tmp == NULL ) {
      return NULL;
  }
  $1 = *(tmp); 
  delete tmp; 
}

%typemap(in) const ex = ex;

%typemap(in) numeric & {
    $1 = type2numeric($input);
    if (!$1) return NULL;
}

%typemap(typecheck, precedence=1210) ex & {
    $1 = (checktype2ex($input)) ? 1 : 0;
}

%typemap(typecheck, precedence=1209) ex {
    $1 = (checktype2ex($input)) ? 1 : 0; // TODO: This could be wrong, while ex& is treated as a pointer by swig, ex is not, at least in the typemap(in) above.
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

%typemap(out) lst & {
    $result = lst2list($1);
}

//it seems we don't need these
/*
%typemap(out) ex &{
    $result = ex2type($1);
}*/

// vim:ft=cpp:
