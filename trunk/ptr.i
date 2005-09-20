%module ptr

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

#ifndef __GINAC_PTR_H__
#define __GINAC_PTR_H__



/** Base class for reference-counted objects. */
class refcounted {
public:
	refcounted() throw() : refcount(0) {}

	size_t add_reference() throw() { return ++refcount; }
	size_t remove_reference() throw() { return --refcount; }
	size_t get_refcount() const throw() { return refcount; }
	void set_refcount(size_t r) throw() { refcount = r; }

private:
	size_t refcount; ///< reference counter
};


/** Class of (intrusively) reference-counted pointers that support
 *  copy-on-write semantics.
 *
 *  Requirements for T:
 *    must support the refcounted interface (usually by being derived
 *      from refcounted)
 *    T* T::duplicate() member function (only if makewriteable() is used) */
template <class T> class ptr {
	friend class std::less< ptr<T> >;

	// NB: This implementation of reference counting is not thread-safe.
	// The reference counter needs to be incremented/decremented atomically,
	// and makewritable() requires locking.

public:
    // no default ctor: a ptr is never unbound

	/** Bind ptr to newly created object, start reference counting. */
	ptr(T *t) throw() : p(t) { GINAC_ASSERT(p); p->set_refcount(1); }

	/** Bind ptr to existing reference-counted object. */
	explicit ptr(T &t) throw() : p(&t) { p->add_reference(); }

	ptr(const ptr & other) throw() : p(other.p) { p->add_reference(); }

	~ptr()
	{
		if (p->remove_reference() == 0)
			delete p;
	}

//	ptr &operator=(const ptr & other)
//	{
//		// NB: must first add reference to "other", since other might be *this.
//		other.p->add_reference();
//		if (p->remove_reference() == 0)
//			delete p;
//		p = other.p;
//		return *this;
//	}

	T &operator*() const throw() { return *p; }
	T *operator->() const throw() { return p; }

	friend inline T *get_pointer(const ptr & x) throw() { return x.p; }

	/** Announce your intention to modify the object bound to this ptr.
	 *  This ensures that the object is not shared by any other ptrs. */
	void makewritable()
	{
		if (p->get_refcount() > 1) {
			T *p2 = p->duplicate();
			p2->set_refcount(1);
			p->remove_reference();
			p = p2;
		}
	}

	/** Swap the bound object of this ptr with another ptr. */
	void swap(ptr & other) throw()
	{
		T *t = p;
		p = other.p;
		other.p = t;
	}


	template <class U>
	bool operator==(const ptr<U> & rhs) const throw() { return p == get_pointer(rhs); }

	template <class U>
	bool operator!=(const ptr<U> & rhs) const throw() { return p != get_pointer(rhs); }

	template <class U>
	inline friend bool operator==(const ptr & lhs, const U * rhs) throw() { return lhs.p == rhs; }

	template <class U>
	inline friend bool operator!=(const ptr & lhs, const U * rhs) throw() { return lhs.p != rhs; }

	template <class U>
	inline friend bool operator==(const U * lhs, const ptr & rhs) throw() { return lhs == rhs.p; }

	template <class U>
	inline friend bool operator!=(const U * lhs, const ptr & rhs) throw() { return lhs != rhs.p; }

	inline friend std::ostream & operator<<(std::ostream & os, const ptr<T> & rhs)
	{
		os << rhs.p;
	}

private:
	T *p;
};



namespace std {

/** Specialization of std::less for ptr<T> to enable ordering of ptr<T>
 *  objects (e.g. for the use as std::map keys). */
 /*
template <class T> struct less< ptr<T> >
 : public binary_function<ptr<T>, ptr<T>, bool> {
	bool operator()(const ptr<T> &lhs, const ptr<T> &rhs) const
	{
		return less<T*>()(lhs.p, rhs.p);
	}
};
*/

} // namespace std

#endif // ndef __GINAC_PTR_H__
// vim:ft=cpp:
