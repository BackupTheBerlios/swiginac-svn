%module exprseq

// Copyright 2003, Simula Research Laboratory and Ola Skavhaug. All rights
// reserved.

%rename (gprint) print;
namespace GiNaC{};

%{
#include "exprseq.h"
using namespace GiNaC;
%}
%include "basic.i"


#ifndef __GINAC_EXPRSEQ_H__
#define __GINAC_EXPRSEQ_H__

#include <vector>
#include "container.h"

namespace GiNaC {

typedef container<std::vector> exprseq;

/** Specialization of container::get_tinfo() for exprseq. */
template<> inline unsigned exprseq::get_tinfo() { return TINFO_exprseq; }

// defined in exprseq.cpp
template<> bool exprseq::info(unsigned inf) const;

/** Specialization of is_exactly_a<exprseq>(obj) for exprseq objects. */
template<> inline bool is_exactly_a<exprseq>(const basic & obj)
{
	return obj.tinfo() == TINFO_exprseq;
}

} // namespace GiNaC

#endif // ndef __GINAC_EXPRSEQ_H__
