/*
 (c) Copyright 2006
     Author: Matti Peltomaki
     
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

class color : public indexed
{
public:
        color(const ex & b, unsigned char rl = 0);
        color(const ex & b, const ex & i1, unsigned char rl = 0);

        // internal constructors
        color(unsigned char rl, const exvector & v, bool discardable = false);
        color(unsigned char rl, std::auto_ptr<exvector> vp);

        unsigned char get_representation_label() const {return representation_label;}
};

class su3one : public tensor { };

class su3t : public tensor { };

class su3f : public tensor { };

class su3d : public tensor { };

ex color_ONE(unsigned char rl = 0);
ex color_T(const ex & a, unsigned char rl = 0);
ex color_f(const ex & a, const ex & b, const ex & c);
ex color_d(const ex & a, const ex & b, const ex & c);
ex color_h(const ex & a, const ex & b, const ex & c);
ex color_trace(const ex & e, const std::set<unsigned char> & rls);
ex color_trace(const ex & e, const lst & rll);
ex color_trace(const ex & e, unsigned char rl = 0);
