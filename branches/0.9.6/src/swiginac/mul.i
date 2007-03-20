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

/** Product of expressions. */
class mul : public expairseq
{
	friend class add;
	friend class ncmul;
	friend class power;
	
public:
	mul(const ex & lh, const ex & rh);
	mul(const exvector & v);
	mul(const epvector & v);
//	mul(const epvector & v, const ex & oc);
//	mul(std::auto_ptr<epvector> vp, const ex & oc);
	mul(const ex & lh, const ex & mh, const ex & rh);
	ex algebraic_subs_mul(const exmap & m, unsigned options) const;
};

// vim:ft=cpp:
