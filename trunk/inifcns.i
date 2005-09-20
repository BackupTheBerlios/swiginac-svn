%module inifcns

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


class zeta1_SERIAL { public: static unsigned serial; };
template<typename T1>
inline function zeta(const T1 & p1) {
	return function(zeta1_SERIAL::serial, ex(p1));
}
class zeta2_SERIAL { public: static unsigned serial; };
template<typename T1, typename T2>
inline function zeta(const T1 & p1, const T2 & p2) {
	return function(zeta2_SERIAL::serial, ex(p1), ex(p2));
}
/*
class zeta_SERIAL;
template<> inline bool is_the_function<class zeta_SERIAL>(const ex & x)
{
	return is_the_function<zeta1_SERIAL>(x) || is_the_function<zeta2_SERIAL>(x);
}
*/

class psi1_SERIAL { public: static unsigned serial; };
template<typename T1>
inline function psi(const T1 & p1) {
	return function(psi1_SERIAL::serial, ex(p1));
}
class psi2_SERIAL { public: static unsigned serial; };
template<typename T1, typename T2>
inline function psi(const T1 & p1, const T2 & p2) {
	return function(psi2_SERIAL::serial, ex(p1), ex(p2));
}
class psi_SERIAL;
template<> inline bool is_the_function<class psi_SERIAL>(const ex & x)
{
	return is_the_function<psi1_SERIAL>(x) || is_the_function<psi2_SERIAL>(x);
}

// vim:ft=cpp:
