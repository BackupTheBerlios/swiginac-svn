%module lst 

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

#ifndef __GINAC_LST_H__
#define __GINAC_LST_H__

template<> inline unsigned lst::get_tinfo();
template<> inline unsigned lst::get_default_flags();
template<> inline char lst::get_open_delim();
template<> inline char lst::get_close_delim();
template<> bool lst::info(unsigned inf) const;
template<> inline bool is_exactly_a<lst>(const basic & obj);

#endif // ndef __GINAC_LST_H__
// vim:ft=cpp: