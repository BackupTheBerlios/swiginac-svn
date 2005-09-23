%module constant

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

class constant : public basic
{
public:
        constant(const std::string & initname, evalffunctype efun = 0, const std::string & texname = std::string());
        constant(const std::string & initname, const numeric & initnumber, const std::string & texname = std::string());
};

extern const constant Pi;
extern const constant Catalan;
extern const constant Euler;
extern const numeric I;

%pythoncode %{
    Pi=cvar.Pi
    I=cvar.I
%} 

// vim:ft=cpp:
