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
        relational(const ex & lhs, const ex & rhs, operators oper=equal);
        virtual ex lhs(void) const;
        virtual ex rhs(void) const;
};

%extend relational {

%pythoncode %{
def __str__(self):
    if not self.__dict__.has_key("str"):
        self.str = self.printpython
    return self.str()

def __repr__(self):
    return self.__str__()

%}

};

// vim:ft=cpp:
