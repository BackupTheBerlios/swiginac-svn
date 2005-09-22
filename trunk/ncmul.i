%module ncmul

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

#ifndef __GINAC_NCMUL_H__
#define __GINAC_NCMUL_H__

//class ncmul : public exprseq
class ncmul : public basic
{
    /*
	friend class power;
	friend ex reeval_ncmul(const exvector & v);
	friend ex hold_ncmul(const exvector & v);
    */

public:
	ncmul(const ex & lh, const ex & rh);
	ncmul(const ex & f1, const ex & f2, const ex & f3);
	ncmul(const ex & f1, const ex & f2, const ex & f3,
	      const ex & f4);
	ncmul(const ex & f1, const ex & f2, const ex & f3,
	      const ex & f4, const ex & f5);
	ncmul(const ex & f1, const ex & f2, const ex & f3,
	      const ex & f4, const ex & f5, const ex & f6);
//	ncmul(const exvector & v, bool discardable=false);
//	ncmul(std::auto_ptr<exvector> vp);
	unsigned precedence() const {return 50;}
	//bool info(unsigned inf) const;
	//int degree(const ex & s) const;
	//int ldegree(const ex & s) const;
	//ex expand(unsigned options=0) const;
	//ex coeff(const ex & s, int n=1) const;
	//ex eval(int level=0) const;
	//ex evalm() const;
	//exvector get_free_indices() const;
	//ex thiscontainer(const exvector & v) const;
//	ex thiscontainer(std::auto_ptr<exvector> vp) const;
	//ex conjugate() const;
	//const exvector & get_factors() const;
};

// friend funtions 

/*
ex reeval_ncmul(const exvector & v);
ex hold_ncmul(const exvector & v);

// utility functions

* Specialization of is_exactly_a<ncmul>(obj) for ncmul objects. *
template<> inline bool is_exactly_a<ncmul>(const basic & obj)
{
	return obj.tinfo()==TINFO_ncmul;
}
*/

#endif // ndef __GINAC_NCMUL_H__

// vim:ft=cpp:
