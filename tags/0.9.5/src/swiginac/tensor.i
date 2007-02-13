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

class tensor : public basic
{
public:
        tensor();
	bool replace_contr_index(exvector::iterator self, exvector::iterator other) const;
};


class tensdelta : public tensor
{
public:
        tensdelta();
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class tensmetric : public tensor
{
public:
        tensmetric();
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class minkmetric : public tensmetric
{
public:
        minkmetric();
	minkmetric(bool pos_sig);
	ex eval_indexed(const basic & i) const;
};

class spinmetric : public tensmetric
{
public:
        spinmetric();
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class tensepsilon : public tensor
{
public:
        tensepsilon();
	tensepsilon(bool minkowski, bool pos_sig);
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};

ex delta_tensor(const ex & i1, const ex & i2);
ex metric_tensor(const ex & i1, const ex & i2);
ex lorentz_g(const ex & i1, const ex & i2, bool pos_sig = false);
ex spinor_metric(const ex & i1, const ex & i2);
ex epsilon_tensor(const ex & i1, const ex & i2);
ex epsilon_tensor(const ex & i1, const ex & i2, const ex & i3);
ex lorentz_eps(const ex & i1, const ex & i2, const ex & i3, const ex & i4, bool pos_sig = false);

// vim:ft=cpp:
