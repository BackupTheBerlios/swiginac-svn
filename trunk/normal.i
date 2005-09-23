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

//ex quo(const ex &a, const ex &b, const ex &x, bool check_args = true);
ex quo(const ex &a, const ex &b, const ex &x) throw(std::invalid_argument);
ex rem(const ex &a, const ex &b, const ex &x, bool check_args = true);
ex decomp_rational(const ex &a, const ex &x);
ex prem(const ex &a, const ex &b, const ex &x, bool check_args = true);
ex sprem(const ex &a, const ex &b, const ex &x, bool check_args = true);
bool divide(const ex &a, const ex &b, ex &q, bool check_args = true);
//ex gcd(const ex &a, const ex &b, ex *ca = NULL, ex *cb = NULL, bool check_args = true);
ex gcd(const ex &a, const ex &b) throw(std::invalid_argument);
ex lcm(const ex &a, const ex &b, bool check_args = true);
ex sqrfree(const ex &a, const lst &l = lst());
ex sqrfree_parfrac(const ex & a, const symbol & x);
ex collect_common_factors(const ex & e);
ex resultant(const ex & e1, const ex & e2, const ex & s);

// vim:ft=cpp:
