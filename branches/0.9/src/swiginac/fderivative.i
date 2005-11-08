namespace GiNaC {


typedef std::multiset<unsigned> paramset;

/** This class represents the (abstract) derivative of a symbolic function.
 *  It is used to represent the derivatives of functions that do not have
 *  a derivative or series expansion procedure defined. */
class fderivative : public function
{
public:
	fderivative(unsigned ser, unsigned param, const exvector & args);
	fderivative(unsigned ser, const paramset & params, const exvector & args);
	fderivative(unsigned ser, const paramset & params, std::auto_ptr<exvector> vp);
	void print(const print_context & c, unsigned level = 0) const;
	ex eval(int level = 0) const;
	ex evalf(int level = 0) const;
	ex series(const relational & r, int order, unsigned options = 0) const;
	ex thiscontainer(const exvector & v) const;
	ex thiscontainer(std::auto_ptr<exvector> vp) const;
};


template<> inline bool is_exactly_a<fderivative>(const basic & obj);
} // namespace GiNaC

// vim:ft=cpp:

