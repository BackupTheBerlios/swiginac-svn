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

class pseries : public basic
{
public:
	pseries(const ex &rel_, const epvector &ops_);
	ex get_var() const {return var;}
	ex get_point() const {return point;}
	ex convert_to_poly(bool no_order = false) const;
	bool is_compatible_to(const pseries &other) const {return var.is_equal(other.var) && point.is_equal(other.point);}
	bool is_zero() const {return seq.size() == 0;}
	bool is_terminating() const;
	ex coeffop(size_t i) const;
	ex exponop(size_t i) const;
	ex add_series(const pseries &other) const;
	ex mul_const(const numeric &other) const;
	ex mul_series(const pseries &other) const;
	ex power_const(const numeric &p, int deg) const;
	pseries shift_exponents(int deg) const;
};

inline ex series_to_poly(const ex &e);
inline bool is_terminating(const pseries & s);

// vim:ft=cpp:
