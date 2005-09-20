%module container

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

#ifndef __GINAC_CONTAINER_H__
#define __GINAC_CONTAINER_H__


template <template <class> class C>
//class container : public basic, public container_storage<C> {
class container : public basic {
public:
	typedef typename container_storage<C>::STLT STLT;
	typedef typename STLT::const_iterator const_iterator;
	typedef typename STLT::const_reverse_iterator const_reverse_iterator;
//	container(exvector::const_iterator b, exvector::const_iterator e) : inherited(get_tinfo()), container_storage<C>(b, e);
	explicit container(const ex & p1) : inherited(get_tinfo()), container_storage<C>(1, p1);
	container(const ex & p1, const ex & p2) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7) : inherited(get_tinfo()); container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11, const ex & p12) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11, const ex & p12, const ex & p13) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11, const ex & p12, const ex & p13, const ex & p14) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11, const ex & p12, const ex & p13, const ex & p14, const ex & p15) : inherited(get_tinfo());
	container(const ex & p1, const ex & p2, const ex & p3, const ex & p4, const ex & p5, const ex & p6, const ex & p7, const ex & p8, const ex & p9, const ex & p10, const ex & p11, const ex & p12, const ex & p13, const ex & p14, const ex & p15, const ex & p16) : inherited(get_tinfo());
	bool info(unsigned inf) const { return inherited::info(inf); }
	unsigned precedence() const { return 10; }
	size_t nops() const { return this->seq.size(); }
	ex op(size_t i) const;
	ex & let_op(size_t i);
	ex eval(int level = 0) const;
//	ex subs(const exmap & m, unsigned options = 0) const;
//	container & prepend(const ex & b);
	container & append(const ex & b);
//	container & remove_first();
	container & remove_last();
	container & remove_all();
	container & sort();
	container & unique();
	const_iterator begin() const {return this->seq.begin();}
	const_iterator end() const {return this->seq.end();}
	const_reverse_iterator rbegin() const {return this->seq.rbegin();}
	const_reverse_iterator rend() const {return this->seq.rend();}
};



template <template <class> class C> container<C> & container<C>::remove_first();
template <template <class> class C> container<C> & container<C>::remove_last();
template <template <class> class C> container<C> & container<C>::remove_all();
template <template <class> class C> container<C> & container<C>::sort();
template<> inline void container<std::list>::unique_();
template <template <class> class C> container<C> & container<C>::unique();
template <template <class> class C> void container<C>::printseq(const print_context & c, char openbracket, char delim, char closebracket, unsigned this_precedence, unsigned upper_precedence) const;
template <template <class> class C> typename container<C>::STLT container<C>::evalchildren(int level) const;

template <template <class> class C> std::auto_ptr<typename container<C>::STLT> container<C>::subschildren(const exmap & m, unsigned options) const;




%extend container {
    void let_op(int i, ex& rh) {
        self->let_op(i) = rh;
    }

    void set_op(int i, ex& n) {
        self->let_op(i) = n;
    }
};

#endif // ndef __GINAC_CONTAINER_H__
// vim:ft=cpp:
