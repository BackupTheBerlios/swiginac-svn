%module lst 

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%{
#include "lst.h"
%}

%include "basic.i"

#ifndef __GINAC_LST_H__
#define __GINAC_LST_H__

#include <list>

#include "container.h"

namespace GiNaC {


//typedef container<std::list> lst;


//%template(exlist) lst<ex>;

/** Specialization of container::get_tinfo() for lst. */
template<> inline unsigned lst::get_tinfo() { return TINFO_lst; }

/** Specialization of container::get_default_flags() for lst. */
template<> inline unsigned lst::get_default_flags() { return status_flags::not_shareable; }

/** Specialization of container::get_open_delim() for lst. */
template<> inline char lst::get_open_delim() { return '{'; }

/** Specialization of container::get_close_delim() for lst. */
template<> inline char lst::get_close_delim() { return '}'; }

// defined in lst.cpp
template<> bool lst::info(unsigned inf) const;

/** Specialization of is_exactly_a<lst>(obj) for lst objects. */
template<> inline bool is_exactly_a<lst>(const basic & obj)
{
	return obj.tinfo() == TINFO_lst;
}

} // namespace GiNaC

#endif // ndef __GINAC_LST_H__
