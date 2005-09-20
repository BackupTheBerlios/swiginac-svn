%module numeric

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

class numeric : public basic
{
public:
    numeric(int i);
    numeric(unsigned int i);
    numeric(long i);
    numeric(unsigned long i);
    numeric(long numer, long denom);
    numeric(double d);
    numeric(const char *);
    unsigned precedence() const {return 30;}
    bool info(unsigned inf) const;
    int degree(const ex & s) const;
    int ldegree(const ex & s) const;
    ex coeff(const ex & s, int n = 1) const;
    bool has(const ex &other) const;
    ex eval(int level = 0) const;
    ex evalf(int level = 0) const;
   // ex subs(const exmap & m, unsigned options = 0) const;
    //ex normal(exmap & repl, exmap & rev_lookup, int level = 0) const;
    ex to_rational(exmap & repl) const;
    ex to_polynomial(exmap & repl) const;
    numeric integer_content() const;
    ex smod(const numeric &xi) const;
    numeric max_coefficient() const;
    ex conjugate() const;
    const numeric add(const numeric &other) const;
    const numeric sub(const numeric &other) const;
    const numeric mul(const numeric &other) const;
    const numeric div(const numeric &other) const;
    const numeric power(const numeric &other) const;
    const numeric & add_dyn(const numeric &other) const;
    const numeric & sub_dyn(const numeric &other) const;
    const numeric & mul_dyn(const numeric &other) const;
    const numeric & div_dyn(const numeric &other) const;
    const numeric & power_dyn(const numeric &other) const;
    const numeric inverse() const;
    int csgn() const;
    int compare(const numeric &other) const;
    bool is_equal(const numeric &other) const;
    bool is_zero() const;
    bool is_positive() const;
    bool is_negative() const;
    bool is_integer() const;
    bool is_pos_integer() const;
    bool is_nonneg_integer() const;
    bool is_even() const;
    bool is_odd() const;
    bool is_prime() const;
    bool is_rational() const;
    bool is_real() const;
    bool is_cinteger() const;
    bool is_crational() const;
//    bool operator==(const numeric &other) const;
//    bool operator!=(const numeric &other) const;
//    bool operator<(const numeric &other) const;
//    bool operator<=(const numeric &other) const;
//    bool operator>(const numeric &other) const;
//    bool operator>=(const numeric &other) const;
    int to_int() const;
    long to_long() const;
    double to_double() const;
    cln::cl_N to_cl_N() const;
    const numeric real() const;
    const numeric imag() const;
    const numeric numer() const;
    const numeric denom() const;
    int int_length() const;
    numeric(const cln::cl_N &z);
};


%extend numeric {
    double __float__() {
        return (*self).to_double();
    }
    int __int__() {
        return (*self).to_int();
    }
};

ex PiEvalf(void);
ex EulerEvalf(void);
ex CatalanEvalf(void);

// vim:ft=cpp:
