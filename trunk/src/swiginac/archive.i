/*
 (c) Copyright 2008
     Author: Ola Skavhaug
     
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

class archive;

typedef unsigned archive_node_id;
typedef unsigned archive_atom;

class archive_node
{
    //friend std::ostream &operator<<(std::ostream &os, const archive_node &ar);
    //friend std::istream &operator>>(std::istream &is, archive_node &ar);

public:
    archive_node() : a(*dummy_ar_creator()), has_expression(false) {} // hack for cint which always requires a default constructor
    archive_node(archive &ar) : a(ar), has_expression(false) {}
    archive_node(archive &ar, const ex &expr);

    //const archive_node &operator=(const archive_node &other);
    void add_bool(const std::string &name, bool value);
    void add_unsigned(const std::string &name, unsigned value);
    void add_string(const std::string &name, const std::string &value);
    void add_ex(const std::string &name, const ex &value);
    bool find_bool(const std::string &name, bool &ret, unsigned index = 0) const;
    bool find_unsigned(const std::string &name, unsigned &ret, unsigned index = 0) const;
    bool find_string(const std::string &name, std::string &ret, unsigned index = 0) const;
    bool find_ex(const std::string &name, ex &ret, lst &sym_lst, unsigned index = 0) const;
    const archive_node &find_ex_node(const std::string &name, unsigned index = 0) const;

    ex unarchive(lst &sym_lst) const;
    bool has_same_ex_as(const archive_node &other) const;
    bool has_ex() const;
    ex get_ex() const;

    void forget();
    void printraw(std::ostream &os) const;
};

class archive
{
    friend std::ostream &operator<<(std::ostream &os, const archive &ar);
    friend std::istream &operator>>(std::istream &is, archive &ar);

public:
    archive() {}
    ~archive() {}

    archive(const ex &e) {archive_ex(e, "ex");}

    archive(const ex &e, const char *n) {archive_ex(e, n);}

    void archive_ex(const ex &e, const char *name);

    ex unarchive_ex(const lst &sym_lst, const char *name) const;

    ex unarchive_ex(const lst &sym_lst, unsigned index = 0) const;

    ex unarchive_ex(const lst &sym_lst, std::string &name, unsigned index = 0) const;

    unsigned num_expressions() const;

    const archive_node &get_top_node(unsigned index = 0) const;

    void clear();

    archive_node_id add_node(const archive_node &n);
    archive_node &get_node(archive_node_id id);

    void forget();
    void printraw(std::ostream &os) const;

public:
    archive_atom atomize(const std::string &s) const;
    const std::string &unatomize(archive_atom id) const;

};

std::ostream &operator<<(std::ostream &os, const archive &ar);
std::istream &operator>>(std::istream &is, archive &ar);

%extend archive {
%{
#include <fstream>
%}
void load(std::string filename) {
    std::ifstream infile(filename.c_str());
    infile >> *self;
}

void dump(std::string filename) {
    std::ofstream outfile(filename.c_str());
    outfile << *self;
    //*self >> outfile;
}



}
