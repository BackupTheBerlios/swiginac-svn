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

/* 
     Contributors: Matti Peltomäki, Martin Sandve Alnæs
*/

%newobject *::copy;

class ex { public: ex eval(int level=0) const;};
class lst {};
class ex_is_less;
class symbol;
class scalar_products;
class numeric;
class relational;
class archive_node;
class print_context;

//typedef std::vector<ex> exvector;
typedef std::map<ex, ex, ex_is_less> exmap;

struct map_function;

class basic : public refcounted
{
public:
    virtual ~basic();
    basic(const basic & other);
    virtual basic * duplicate() const { return new basic(*this); }
    virtual ex eval(int level = 0) const;
    virtual ex evalf(int level = 0) const;
    virtual ex evalm() const;
    virtual ex eval_indexed(const basic & i) const;
    virtual void dbgprint() const;
    virtual void dbgprinttree() const;
    virtual unsigned precedence() const;
    virtual bool info(unsigned inf) const;
    virtual size_t nops() const;
    virtual ex op(size_t i) const;
//    virtual ex operator[](const ex & index) const;
//    virtual ex operator[](size_t i) const;
    virtual ex & let_op(size_t i);
//    virtual ex & operator[](const ex & index);
//    virtual ex & operator[](size_t i);
    virtual bool has(const ex & other, unsigned options=0) const;
    virtual bool match(const ex & pattern, lst & repl_lst) const;
    virtual ex subs(const exmap & m, unsigned options = 0) const;
    virtual ex map(map_function & f) const;
    virtual void accept(GiNaC::visitor & v) const;
    virtual bool is_polynomial(const ex& var) const;
    virtual int degree(const ex & s) const;
    virtual int ldegree(const ex & s) const;
    virtual ex coeff(const ex & s, int n = 1) const;
    virtual ex expand(unsigned options = 0) const;
    virtual ex collect(const ex & s, bool distributed = false) const;
    virtual ex series(const relational & r, int order, unsigned options = 0) const;
    virtual ex normal(exmap & repl, exmap & rev_lookup, int level = 0) const;
    virtual ex to_rational(exmap & repl) const;
    virtual ex to_polynomial(exmap & repl) const;
    virtual numeric integer_content() const;
    virtual ex smod(const numeric &xi) const;
    virtual numeric max_coefficient() const;
    virtual exvector get_free_indices() const;
    virtual ex add_indexed(const ex & self, const ex & other) const;
    virtual ex scalar_mul_indexed(const ex & self, const numeric & other) const;
    virtual bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
    virtual unsigned return_type() const;
    virtual tinfo_t return_type_tinfo() const;
    virtual ex conjugate() const;
    virtual ex real_part() const;
    virtual ex imag_part() const;
    void print_dispatch(const registered_class_info & ri, const print_context & c, unsigned level) const;
    ex subs_one_level(const exmap & m, unsigned options) const;
    ex diff(const symbol & s, unsigned nth = 1) const;
    int compare(const basic & other) const;
    bool is_equal(const basic & other) const;
    const basic & hold() const;
    unsigned gethash() const { if (flags & status_flags::hash_calculated) return hashvalue; else return calchash(); }
    tinfo_t tinfo() const {return tinfo_key;}
    const basic & setflag(unsigned f) const {flags |= f; return *this;}
    const basic & clearflag(unsigned f) const {flags &= ~f; return *this;}

};

extern int max_recursion_level;
template <class T> inline bool is_a(const basic &obj);
template <class T> inline bool is_exactly_a(const basic &obj);

%extend basic {
    std::string printpython() {
        std::ostringstream out;
        (*self).print(print_python(out));
        return out.str();
    }

    std::string printlatex() {
        std::ostringstream out;
        (*self).print(print_latex(out));
        return out.str();
    }

    std::string printc() {
        std::ostringstream out;
        (*self).print(print_csrc_double(out));
        return out.str();
    }

    unsigned __hash__() const {
        return self->gethash();
    }

    bool __nonzero__() const throw(std::logic_error) {
        if (is_exactly_a<relational>(*self))
            return ex_to<relational>((*self).eval());
        else
            throw (std::logic_error("Cannot convert to bool."));
    }

    ex __add__(const basic &b) const { return (*self)+b; }
    //ex __add__(const ex &b) const { return (*self)+b; }
    ex __add__(const int &b) const { return (*self)+b; }
    ex __add__(const double &b) const { return (*self)+b; }
    ex __radd__(const basic &b) const { return b+(*self); }
    //ex __radd__(const ex &b) const { return b+(*self); }
    ex __radd__(const int &b) const { return b+(*self); }
    ex __radd__(const double &b) const { return b+(*self); }
    
    ex __sub__(const basic &b) const { return (*self)-b; }
    //ex __sub__(const ex &b) const { return (*self)-b; }
    ex __sub__(const int &b) const { return (*self)-b; }
    ex __sub__(const double &b) const { return (*self)-b; }
    ex __rsub__(const basic &b) const { return b-(*self); }
    //ex __rsub__(const ex &b) const { return b-(*self); }
    ex __rsub__(const int &b) const { return b-(*self); }
    ex __rsub__(const double &b) const { return b-(*self); }
    
    ex __mul__(const basic &b) const { return (*self)*b; }
    //ex __mul__(const ex &b) const { return (*self)*b; }
    ex __mul__(const int &b) const { return (*self)*b; }
    ex __mul__(const double &b) const { return (*self)*b; }
    ex __rmul__(const basic &b) const { return b*(*self); }
    //ex __rmul__(const ex &b) const { return b*(*self); }
    ex __rmul__(const int &b) const { return b*(*self); }
    ex __rmul__(const double &b) const { return b*(*self); }
    
    ex __div__(const basic &b) const { return (*self)/b; }
    //ex __div__(const ex &b) const { return (*self)/b; }
    ex __div__(const int &b) const { return (*self)/b; }
    ex __div__(const double &b) const { return (*self)/b; }
    ex __rdiv__(const basic &b) const { return b/(*self); }
    //ex __rdiv__(const ex &b) const { return b/(*self); }
    ex __rdiv__(const int &b) const { return b/(*self); }
    ex __rdiv__(const double &b) const { return b/(*self); }
    
    ex __pow__(const basic &b)const{return pow(*self,b); }
    //ex __pow__(const ex &b)const{return pow(*self,b); }
    ex __pow__(const int &b) const { return pow(*self,b); }
    ex __pow__(const double &b) const { return pow(*self,b); }
    ex __rpow__(const basic &b)const{return pow(b,*self); }
    //ex __rpow__(const ex &b)const{return pow(b,*self);}
    ex __rpow__(const int &b) const { return pow(b,*self); }
    ex __rpow__(const double &b) const { return pow(b,*self);}

    ex __pos__() const { return +(*self); }
    ex __neg__() const { return -(*self); }

    ex __lt__(const basic &b) const {return *self < b;}
    //ex __lt__(const ex &b) const {return *self < b;}
    ex __lt__(const int &b) const {return *self < b;}
    ex __lt__(const double &b) const {return *self < b;}

    ex __le__(const basic &b) const {return *self <= b;}
    //ex __le__(const ex &b) const {return *self <= b;}
    ex __le__(const int &b) const {return *self <= b;}
    ex __le__(const double &b) const {return *self <= b;}

    ex __eq__(const basic &b) const {return *self == b;}
    //ex __eq__(const ex &b) const {return *self == b;}
    ex __eq__(const int &b) const {return *self == b;}
    ex __eq__(const double &b) const {return *self == b;}

    ex __ne__(const basic &b) const {return *self != b;}
    //ex __ne__(const ex &b) const {return *self != b;}
    ex __ne__(const int &b) const {return *self != b;}
    ex __ne__(const double &b) const {return *self != b;}

    ex __gt__(const basic &b) const {return *self > b;}
    //ex __gt__(const ex &b) const {return *self > b;}
    ex __gt__(const int &b) const {return *self > b;}
    ex __gt__(const double &b) const {return *self > b;}

    ex __ge__(const basic &b) const {return *self >= b;}
    //ex __ge__(const ex &b) const {return *self >= b;}
    ex __ge__(const int &b) const {return *self >= b;}
    ex __ge__(const double &b) const {return *self >= b;}

%pythoncode %{
def set_print_context(self, context_type):
    if context_type == "python":
        self.str = self.printpython
    elif context_type == "tex":
        self.str = self.printlatex
    elif context_type == "c":
        self.str = self.printc

def __str__(self):
    if not self.__dict__.has_key("str"):
        self.str = self.printpython
    return self.str()

def __copy__(self):
    return self.copy()

%}

    //these are defined in the ex class - which we don't use in swiginac,
    //so we need to define them here
    ex subs(const lst & ls, const lst & lr) {
        return self->eval().subs(ls,lr);
    }
    ex subs(const ex & e, unsigned options = 0) const {
        return self->eval().subs(e,options);
    }

    ex normal(int level = 0) const {
        return self->eval().normal(level);
    }
    ex denom() const {
        return self->eval().denom();
    };
    bool is_zero() const {
        return self->eval().is_zero();
    }
    ex content(const ex &x) const {
        return self->eval().content(x);
    }
    ex primpart(const ex &x) const {
        return self->eval().primpart(x);
    }
    ex unit(const ex &x) const {
        return self->eval().unit(x);
    }
    ex simplify_indexed(unsigned options = 0) const {
        return self->eval().simplify_indexed(options);
    }
    ex simplify_indexed(const scalar_products & sp, unsigned options = 0) const{
        return self->eval().simplify_indexed(sp,options);
    }

    ex copy() {
        return ex(*self);
    }

    ex * toex() {
        return new ex(*self);
    }
};

// vim:ft=cpp:
