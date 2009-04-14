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

class idx : public basic
{
public:
    explicit idx(const ex & v, const ex & dim);
    virtual bool is_dummy_pair_same_type(const basic & other) const;
    ex get_value() const {return value;}
    bool is_numeric() const {return is_exactly_a<numeric>(value);}
    bool is_symbolic() const {return !is_exactly_a<numeric>(value);}
    ex get_dim() const {return dim;}
    bool is_dim_numeric() const {return is_exactly_a<numeric>(dim);}
    bool is_dim_symbolic() const {return !is_exactly_a<numeric>(dim);}
    ex replace_dim(const ex & new_dim) const;
    ex minimal_dim(const idx & other) const;
};


class varidx : public idx
{
public:
    varidx(const ex & v, const ex & dim, bool covariant = false);
    bool is_dummy_pair_same_type(const basic & other) const;
    bool is_covariant() const {return covariant;}
    bool is_contravariant() const {return !covariant;}
    ex toggle_variance() const;
};

class spinidx : public varidx
{
public:
    spinidx(const ex & v, const ex & dim = 2, bool covariant = false, bool dotted = false);
    bool is_dummy_pair_same_type(const basic & other) const;
    bool is_dotted() const {return dotted;}
    bool is_undotted() const {return !dotted;}
    ex toggle_dot() const;
    ex toggle_variance_dot() const;
};

bool is_dummy_pair(const idx & i1, const idx & i2);
bool is_dummy_pair(const ex & e1, const ex & e2);
void find_free_and_dummy(exvector::const_iterator it, exvector::const_iterator itend, exvector & out_free, exvector & out_dummy);
void find_free_and_dummy(const exvector & v, exvector & out_free, exvector & out_dummy);
void find_dummy_indices(const exvector & v, exvector & out_dummy);
size_t count_dummy_indices(const exvector & v);
size_t count_free_indices(const exvector & v);
ex minimal_dim(const ex & dim1, const ex & dim2);

// vim:ft=cpp:
