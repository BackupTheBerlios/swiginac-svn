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

class subs_options {
    public:
        enum {
            no_pattern = 0x0001,
            subs_no_pattern = 0x0001,
            algebraic = 0x0002,
            subs_algebraic = 0x0002,
            pattern_is_product = 0x0004,
            pattern_is_not_product = 0x0008
        };
};

class determinant_algo {
public:
	enum {
		automatic,
		gauss,
		divfree,
		laplace,
		bareiss
	};
};

class info_flags {
public:
	enum {
		numeric,
		real,
		rational,
		integer,
		crational,
		cinteger,
		positive,
		negative,
		nonnegative,
		posint,
		negint,
		nonnegint,
		even,
		odd,
		prime,
		relation,
		relation_equal,
		relation_not_equal,
		relation_less,
		relation_less_or_equal,
		relation_greater,
		relation_greater_or_equal,
		symbol,
		list,
		exprseq,
		polynomial,
		integer_polynomial,
		cinteger_polynomial,
		rational_polynomial,
		crational_polynomial,
		rational_function,
		algebraic,
		indexed,  
		has_indices,
		idx
	};
};

// vim:ft=cpp:
