class tensor : public basic
{
public:
	bool replace_contr_index(exvector::iterator self, exvector::iterator other) const;
};


class tensdelta : public tensor
{
public:
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class tensmetric : public tensor
{
public:
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class minkmetric : public tensmetric
{
public:
	minkmetric(bool pos_sig);
	ex eval_indexed(const basic & i) const;
};

class spinmetric : public tensmetric
{
public:
	ex eval_indexed(const basic & i) const;
	bool contract_with(exvector::iterator self, exvector::iterator other, exvector & v) const;
};


class tensepsilon : public tensor
{
public:
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
