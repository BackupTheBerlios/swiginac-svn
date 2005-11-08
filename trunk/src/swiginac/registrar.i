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

class ex;
class archive_node;

typedef ex (*unarch_func)(const archive_node &n, lst &sym_lst);

class registered_class_options {
public:
	registered_class_options(const char *n, const char *p, unsigned ti, unarch_func f) : name(n), parent_name(p), tinfo_key(ti), unarchive(f) {}
	const char *get_name() const;
	const char *get_parent_name() const;
	unsigned get_id() const;
	unarch_func get_unarch_func() const;
	const std::vector<print_functor> &get_print_dispatch_table() const { return print_dispatch_table; }
	template <class Ctx, class T, class C> registered_class_options & print_func(void f(const T &, const C & c, unsigned));
	template <class Ctx, class T, class C> registered_class_options & print_func(void (T::*f)(const C &, unsigned));
	template <class Ctx> registered_class_options & print_func(const print_functor & f);
	void set_print_func(unsigned id, const print_functor & f);
};

typedef class_info<registered_class_options> registered_class_info;

#define GINAC_DECLARE_REGISTERED_CLASS_NO_CTORS(classname, supername) \
public: \
	typedef supername inherited; \
private: \
	static GiNaC::registered_class_info reg_info; \
public: \
	static GiNaC::registered_class_info &get_class_info_static() { return reg_info; } \
	virtual const GiNaC::registered_class_info &get_class_info() const { return classname::get_class_info_static(); } \
	virtual GiNaC::registered_class_info &get_class_info() { return classname::get_class_info_static(); } \
	virtual const char *class_name() const { return classname::get_class_info_static().options.get_name(); } \
	\
	classname(const GiNaC::archive_node &n, GiNaC::lst &sym_lst); \
	virtual void archive(GiNaC::archive_node &n) const; \
	static GiNaC::ex unarchive(const GiNaC::archive_node &n, GiNaC::lst &sym_lst); \
	\
	class visitor { \
	public: \
		virtual void visit(const classname &) = 0; \
	};

#define GINAC_DECLARE_REGISTERED_CLASS(classname, supername) \
	GINAC_DECLARE_REGISTERED_CLASS_NO_CTORS(classname, supername) \
public: \
	classname(); \
	virtual classname * duplicate() const { return new classname(*this); } \
	\
	virtual void accept(GiNaC::visitor & v) const \
	{ \
		if (visitor *p = dynamic_cast<visitor *>(&v)) \
			p->visit(*this); \
		else \
			inherited::accept(v); \
	} \
protected: \
	virtual int compare_same_type(const GiNaC::basic & other) const; \
private:

/** Macro for inclusion in the implementation of each registered class. */
#define GINAC_IMPLEMENT_REGISTERED_CLASS(classname, supername) \
	GiNaC::registered_class_info classname::reg_info = GiNaC::registered_class_info(GiNaC::registered_class_options(#classname, #supername, TINFO_##classname, &classname::unarchive));

/** Macro for inclusion in the implementation of each registered class.
 *  Additional options can be specified. */
#define GINAC_IMPLEMENT_REGISTERED_CLASS_OPT(classname, supername, options) \
	GiNaC::registered_class_info classname::reg_info = GiNaC::registered_class_info(GiNaC::registered_class_options(#classname, #supername, TINFO_##classname, &classname::unarchive).options);


/** Find TINFO_* key by class name. */
extern unsigned find_tinfo_key(const std::string &class_name);

/** Find unarchiving function by class name. */
extern unarch_func find_unarch_func(const std::string &class_name);


/** Add or replace a print method. */
template <class Alg, class Ctx, class T, class C>
extern void set_print_func(void f(const T &, const C & c, unsigned))
{
	Alg::get_class_info_static().options.set_print_func(Ctx::get_class_info_static().options.get_id(), f);
}

/** Add or replace a print method. */
template <class Alg, class Ctx, class T, class C>
extern void set_print_func(void (T::*f)(const C &, unsigned))
{
	Alg::get_class_info_static().options.set_print_func(Ctx::get_class_info_static().options.get_id(), f);
}

// vim:ft=cpp:
