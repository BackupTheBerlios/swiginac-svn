# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _swiginac

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class refcounted(_object):
    """Proxy of C++ refcounted class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, refcounted, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, refcounted, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::refcounted instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> refcounted"""
        _swig_setattr(self, refcounted, 'this', _swiginac.new_refcounted(*args))
        _swig_setattr(self, refcounted, 'thisown', 1)
    def add_reference(*args):
        """add_reference(self) -> size_t"""
        return _swiginac.refcounted_add_reference(*args)

    def remove_reference(*args):
        """remove_reference(self) -> size_t"""
        return _swiginac.refcounted_remove_reference(*args)

    def get_refcount(*args):
        """get_refcount(self) -> size_t"""
        return _swiginac.refcounted_get_refcount(*args)

    def set_refcount(*args):
        """set_refcount(self, size_t r)"""
        return _swiginac.refcounted_set_refcount(*args)

    def __del__(self, destroy=_swiginac.delete_refcounted):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class refcountedPtr(refcounted):
    def __init__(self, this):
        _swig_setattr(self, refcounted, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, refcounted, 'thisown', 0)
        _swig_setattr(self, refcounted,self.__class__,refcounted)
_swiginac.refcounted_swigregister(refcountedPtr)

class registered_class_options(_object):
    """Proxy of C++ registered_class_options class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, registered_class_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, registered_class_options, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::registered_class_options instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, char n, char p, unsigned int ti, unarch_func f) -> registered_class_options"""
        _swig_setattr(self, registered_class_options, 'this', _swiginac.new_registered_class_options(*args))
        _swig_setattr(self, registered_class_options, 'thisown', 1)
    def get_name(*args):
        """get_name(self) -> char"""
        return _swiginac.registered_class_options_get_name(*args)

    def get_parent_name(*args):
        """get_parent_name(self) -> char"""
        return _swiginac.registered_class_options_get_parent_name(*args)

    def get_id(*args):
        """get_id(self) -> unsigned int"""
        return _swiginac.registered_class_options_get_id(*args)

    def get_unarch_func(*args):
        """get_unarch_func(self) -> unarch_func"""
        return _swiginac.registered_class_options_get_unarch_func(*args)

    def get_print_dispatch_table(*args):
        """get_print_dispatch_table(self) -> std::vector<(print_functor)>"""
        return _swiginac.registered_class_options_get_print_dispatch_table(*args)

    def set_print_func(*args):
        """set_print_func(self, unsigned int id, print_functor f)"""
        return _swiginac.registered_class_options_set_print_func(*args)

    def __del__(self, destroy=_swiginac.delete_registered_class_options):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class registered_class_optionsPtr(registered_class_options):
    def __init__(self, this):
        _swig_setattr(self, registered_class_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, registered_class_options, 'thisown', 0)
        _swig_setattr(self, registered_class_options,self.__class__,registered_class_options)
_swiginac.registered_class_options_swigregister(registered_class_optionsPtr)


def find_tinfo_key(*args):
    """find_tinfo_key(string class_name) -> unsigned int"""
    return _swiginac.find_tinfo_key(*args)

def find_unarch_func(*args):
    """find_unarch_func(string class_name) -> unarch_func"""
    return _swiginac.find_unarch_func(*args)
class basic(refcounted):
    """Proxy of C++ basic class"""
    __swig_setmethods__ = {}
    for _s in [refcounted]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, basic, name, value)
    __swig_getmethods__ = {}
    for _s in [refcounted]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, basic, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::basic instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_swiginac.delete_basic):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass

    def __init__(self, *args):
        """__init__(self, basic other) -> basic"""
        _swig_setattr(self, basic, 'this', _swiginac.new_basic(*args))
        _swig_setattr(self, basic, 'thisown', 1)
    def duplicate(*args):
        """duplicate(self) -> basic"""
        return _swiginac.basic_duplicate(*args)

    def eval(*args):
        """
        eval(self, int level=0) -> ex
        eval(self) -> ex
        """
        return _swiginac.basic_eval(*args)

    def evalf(*args):
        """
        evalf(self, int level=0) -> ex
        evalf(self) -> ex
        """
        return _swiginac.basic_evalf(*args)

    def evalm(*args):
        """evalm(self) -> ex"""
        return _swiginac.basic_evalm(*args)

    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.basic_eval_indexed(*args)

    def dbgprint(*args):
        """dbgprint(self)"""
        return _swiginac.basic_dbgprint(*args)

    def dbgprinttree(*args):
        """dbgprinttree(self)"""
        return _swiginac.basic_dbgprinttree(*args)

    def precedence(*args):
        """precedence(self) -> unsigned int"""
        return _swiginac.basic_precedence(*args)

    def info(*args):
        """info(self, unsigned int inf) -> bool"""
        return _swiginac.basic_info(*args)

    def nops(*args):
        """nops(self) -> size_t"""
        return _swiginac.basic_nops(*args)

    def op(*args):
        """op(self, size_t i) -> ex"""
        return _swiginac.basic_op(*args)

    def let_op(*args):
        """let_op(self, size_t i) -> ex"""
        return _swiginac.basic_let_op(*args)

    def has(*args):
        """has(self, ex other) -> bool"""
        return _swiginac.basic_has(*args)

    def match(*args):
        """match(self, ex pattern, lst repl_lst) -> bool"""
        return _swiginac.basic_match(*args)

    def map(*args):
        """map(self, map_function f) -> ex"""
        return _swiginac.basic_map(*args)

    def accept(*args):
        """accept(self, GiNaC::visitor v)"""
        return _swiginac.basic_accept(*args)

    def degree(*args):
        """degree(self, ex s) -> int"""
        return _swiginac.basic_degree(*args)

    def ldegree(*args):
        """ldegree(self, ex s) -> int"""
        return _swiginac.basic_ldegree(*args)

    def coeff(*args):
        """
        coeff(self, ex s, int n=1) -> ex
        coeff(self, ex s) -> ex
        """
        return _swiginac.basic_coeff(*args)

    def expand(*args):
        """
        expand(self, unsigned int options=0) -> ex
        expand(self) -> ex
        """
        return _swiginac.basic_expand(*args)

    def collect(*args):
        """
        collect(self, ex s, bool distributed=False) -> ex
        collect(self, ex s) -> ex
        """
        return _swiginac.basic_collect(*args)

    def series(*args):
        """
        series(self, relational r, int order, unsigned int options=0) -> ex
        series(self, relational r, int order) -> ex
        """
        return _swiginac.basic_series(*args)

    def to_rational(*args):
        """to_rational(self, exmap repl) -> ex"""
        return _swiginac.basic_to_rational(*args)

    def to_polynomial(*args):
        """to_polynomial(self, exmap repl) -> ex"""
        return _swiginac.basic_to_polynomial(*args)

    def integer_content(*args):
        """integer_content(self) -> numeric"""
        return _swiginac.basic_integer_content(*args)

    def smod(*args):
        """smod(self, numeric xi) -> ex"""
        return _swiginac.basic_smod(*args)

    def max_coefficient(*args):
        """max_coefficient(self) -> numeric"""
        return _swiginac.basic_max_coefficient(*args)

    def get_free_indices(*args):
        """get_free_indices(self) -> exvector"""
        return _swiginac.basic_get_free_indices(*args)

    def add_indexed(*args):
        """add_indexed(self, ex self, ex other) -> ex"""
        return _swiginac.basic_add_indexed(*args)

    def scalar_mul_indexed(*args):
        """scalar_mul_indexed(self, ex self, numeric other) -> ex"""
        return _swiginac.basic_scalar_mul_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.basic_contract_with(*args)

    def return_type(*args):
        """return_type(self) -> unsigned int"""
        return _swiginac.basic_return_type(*args)

    def return_type_tinfo(*args):
        """return_type_tinfo(self) -> unsigned int"""
        return _swiginac.basic_return_type_tinfo(*args)

    def conjugate(*args):
        """conjugate(self) -> ex"""
        return _swiginac.basic_conjugate(*args)

    def print_dispatch(*args):
        """print_dispatch(self, registered_class_info ri, print_context c, unsigned int level)"""
        return _swiginac.basic_print_dispatch(*args)

    def subs_one_level(*args):
        """subs_one_level(self, exmap m, unsigned int options) -> ex"""
        return _swiginac.basic_subs_one_level(*args)

    def diff(*args):
        """
        diff(self, symbol s, unsigned int nth=1) -> ex
        diff(self, symbol s) -> ex
        """
        return _swiginac.basic_diff(*args)

    def compare(*args):
        """compare(self, basic other) -> int"""
        return _swiginac.basic_compare(*args)

    def is_equal(*args):
        """is_equal(self, basic other) -> bool"""
        return _swiginac.basic_is_equal(*args)

    def hold(*args):
        """hold(self) -> basic"""
        return _swiginac.basic_hold(*args)

    def gethash(*args):
        """gethash(self) -> unsigned int"""
        return _swiginac.basic_gethash(*args)

    def tinfo(*args):
        """tinfo(self) -> unsigned int"""
        return _swiginac.basic_tinfo(*args)

    def setflag(*args):
        """setflag(self, unsigned int f) -> basic"""
        return _swiginac.basic_setflag(*args)

    def clearflag(*args):
        """clearflag(self, unsigned int f) -> basic"""
        return _swiginac.basic_clearflag(*args)

    def printpython(*args):
        """printpython(self) -> string"""
        return _swiginac.basic_printpython(*args)

    def printlatex(*args):
        """printlatex(self) -> string"""
        return _swiginac.basic_printlatex(*args)

    def printc(*args):
        """printc(self) -> string"""
        return _swiginac.basic_printc(*args)

    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _swiginac.basic___nonzero__(*args)

    def __add__(*args):
        """
        __add__(self, basic b) -> ex
        __add__(self, int b) -> ex
        __add__(self, float b) -> ex
        """
        return _swiginac.basic___add__(*args)

    def __radd__(*args):
        """
        __radd__(self, basic b) -> ex
        __radd__(self, int b) -> ex
        __radd__(self, float b) -> ex
        """
        return _swiginac.basic___radd__(*args)

    def __sub__(*args):
        """
        __sub__(self, basic b) -> ex
        __sub__(self, int b) -> ex
        __sub__(self, float b) -> ex
        """
        return _swiginac.basic___sub__(*args)

    def __rsub__(*args):
        """
        __rsub__(self, basic b) -> ex
        __rsub__(self, int b) -> ex
        __rsub__(self, float b) -> ex
        """
        return _swiginac.basic___rsub__(*args)

    def __mul__(*args):
        """
        __mul__(self, basic b) -> ex
        __mul__(self, int b) -> ex
        __mul__(self, float b) -> ex
        """
        return _swiginac.basic___mul__(*args)

    def __rmul__(*args):
        """
        __rmul__(self, basic b) -> ex
        __rmul__(self, int b) -> ex
        __rmul__(self, float b) -> ex
        """
        return _swiginac.basic___rmul__(*args)

    def __div__(*args):
        """
        __div__(self, basic b) -> ex
        __div__(self, int b) -> ex
        __div__(self, float b) -> ex
        """
        return _swiginac.basic___div__(*args)

    def __rdiv__(*args):
        """
        __rdiv__(self, basic b) -> ex
        __rdiv__(self, int b) -> ex
        __rdiv__(self, float b) -> ex
        """
        return _swiginac.basic___rdiv__(*args)

    def __pow__(*args):
        """
        __pow__(self, basic b) -> ex
        __pow__(self, int b) -> ex
        __pow__(self, float b) -> ex
        """
        return _swiginac.basic___pow__(*args)

    def __rpow__(*args):
        """
        __rpow__(self, basic b) -> ex
        __rpow__(self, int b) -> ex
        __rpow__(self, float b) -> ex
        """
        return _swiginac.basic___rpow__(*args)

    def __pos__(*args):
        """__pos__(self) -> ex"""
        return _swiginac.basic___pos__(*args)

    def __neg__(*args):
        """__neg__(self) -> ex"""
        return _swiginac.basic___neg__(*args)

    def __lt__(*args):
        """
        __lt__(self, basic b) -> ex
        __lt__(self, int b) -> ex
        __lt__(self, float b) -> ex
        """
        return _swiginac.basic___lt__(*args)

    def __le__(*args):
        """
        __le__(self, basic b) -> ex
        __le__(self, int b) -> ex
        __le__(self, float b) -> ex
        """
        return _swiginac.basic___le__(*args)

    def __eq__(*args):
        """
        __eq__(self, basic b) -> ex
        __eq__(self, int b) -> ex
        __eq__(self, float b) -> ex
        """
        return _swiginac.basic___eq__(*args)

    def __ne__(*args):
        """
        __ne__(self, basic b) -> ex
        __ne__(self, int b) -> ex
        __ne__(self, float b) -> ex
        """
        return _swiginac.basic___ne__(*args)

    def __gt__(*args):
        """
        __gt__(self, basic b) -> ex
        __gt__(self, int b) -> ex
        __gt__(self, float b) -> ex
        """
        return _swiginac.basic___gt__(*args)

    def __ge__(*args):
        """
        __ge__(self, basic b) -> ex
        __ge__(self, int b) -> ex
        __ge__(self, float b) -> ex
        """
        return _swiginac.basic___ge__(*args)

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



    def subs(*args):
        """
        subs(self, lst ls, lst lr) -> ex
        subs(self, ex e, unsigned int options=0) -> ex
        subs(self, ex e) -> ex
        """
        return _swiginac.basic_subs(*args)

    def normal(*args):
        """
        normal(self, int level=0) -> ex
        normal(self) -> ex
        """
        return _swiginac.basic_normal(*args)

    def denom(*args):
        """denom(self) -> ex"""
        return _swiginac.basic_denom(*args)

    def is_zero(*args):
        """is_zero(self) -> bool"""
        return _swiginac.basic_is_zero(*args)

    def content(*args):
        """content(self, ex x) -> ex"""
        return _swiginac.basic_content(*args)

    def primpart(*args):
        """primpart(self, ex x) -> ex"""
        return _swiginac.basic_primpart(*args)

    def unit(*args):
        """unit(self, ex x) -> ex"""
        return _swiginac.basic_unit(*args)

    def simplify_indexed(*args):
        """
        simplify_indexed(self, unsigned int options=0) -> ex
        simplify_indexed(self) -> ex
        simplify_indexed(self, scalar_products sp, unsigned int options=0) -> ex
        simplify_indexed(self, scalar_products sp) -> ex
        """
        return _swiginac.basic_simplify_indexed(*args)


class basicPtr(basic):
    def __init__(self, this):
        _swig_setattr(self, basic, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, basic, 'thisown', 0)
        _swig_setattr(self, basic,self.__class__,basic)
_swiginac.basic_swigregister(basicPtr)

class symbol(basic):
    """Proxy of C++ symbol class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, symbol, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, symbol, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::symbol instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, string initname) -> symbol
        __init__(self, string initname, string texname) -> symbol
        """
        _swig_setattr(self, symbol, 'this', _swiginac.new_symbol(*args))
        _swig_setattr(self, symbol, 'thisown', 1)
    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_symbol):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class symbolPtr(symbol):
    def __init__(self, this):
        _swig_setattr(self, symbol, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, symbol, 'thisown', 0)
        _swig_setattr(self, symbol,self.__class__,symbol)
_swiginac.symbol_swigregister(symbolPtr)
cvar = _swiginac.cvar

class numeric(basic):
    """Proxy of C++ numeric class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, numeric, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, numeric, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::numeric instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def add(*args):
        """add(self, numeric other) -> numeric"""
        return _swiginac.numeric_add(*args)

    def sub(*args):
        """sub(self, numeric other) -> numeric"""
        return _swiginac.numeric_sub(*args)

    def mul(*args):
        """mul(self, numeric other) -> numeric"""
        return _swiginac.numeric_mul(*args)

    def div(*args):
        """div(self, numeric other) -> numeric"""
        return _swiginac.numeric_div(*args)

    def power(*args):
        """power(self, numeric other) -> numeric"""
        return _swiginac.numeric_power(*args)

    def add_dyn(*args):
        """add_dyn(self, numeric other) -> numeric"""
        return _swiginac.numeric_add_dyn(*args)

    def sub_dyn(*args):
        """sub_dyn(self, numeric other) -> numeric"""
        return _swiginac.numeric_sub_dyn(*args)

    def mul_dyn(*args):
        """mul_dyn(self, numeric other) -> numeric"""
        return _swiginac.numeric_mul_dyn(*args)

    def div_dyn(*args):
        """div_dyn(self, numeric other) -> numeric"""
        return _swiginac.numeric_div_dyn(*args)

    def power_dyn(*args):
        """power_dyn(self, numeric other) -> numeric"""
        return _swiginac.numeric_power_dyn(*args)

    def inverse(*args):
        """inverse(self) -> numeric"""
        return _swiginac.numeric_inverse(*args)

    def csgn(*args):
        """csgn(self) -> int"""
        return _swiginac.numeric_csgn(*args)

    def compare(*args):
        """compare(self, numeric other) -> int"""
        return _swiginac.numeric_compare(*args)

    def is_equal(*args):
        """is_equal(self, numeric other) -> bool"""
        return _swiginac.numeric_is_equal(*args)

    def is_zero(*args):
        """is_zero(self) -> bool"""
        return _swiginac.numeric_is_zero(*args)

    def is_positive(*args):
        """is_positive(self) -> bool"""
        return _swiginac.numeric_is_positive(*args)

    def is_negative(*args):
        """is_negative(self) -> bool"""
        return _swiginac.numeric_is_negative(*args)

    def is_integer(*args):
        """is_integer(self) -> bool"""
        return _swiginac.numeric_is_integer(*args)

    def is_pos_integer(*args):
        """is_pos_integer(self) -> bool"""
        return _swiginac.numeric_is_pos_integer(*args)

    def is_nonneg_integer(*args):
        """is_nonneg_integer(self) -> bool"""
        return _swiginac.numeric_is_nonneg_integer(*args)

    def is_even(*args):
        """is_even(self) -> bool"""
        return _swiginac.numeric_is_even(*args)

    def is_odd(*args):
        """is_odd(self) -> bool"""
        return _swiginac.numeric_is_odd(*args)

    def is_prime(*args):
        """is_prime(self) -> bool"""
        return _swiginac.numeric_is_prime(*args)

    def is_rational(*args):
        """is_rational(self) -> bool"""
        return _swiginac.numeric_is_rational(*args)

    def is_real(*args):
        """is_real(self) -> bool"""
        return _swiginac.numeric_is_real(*args)

    def is_cinteger(*args):
        """is_cinteger(self) -> bool"""
        return _swiginac.numeric_is_cinteger(*args)

    def is_crational(*args):
        """is_crational(self) -> bool"""
        return _swiginac.numeric_is_crational(*args)

    def to_int(*args):
        """to_int(self) -> int"""
        return _swiginac.numeric_to_int(*args)

    def to_long(*args):
        """to_long(self) -> long"""
        return _swiginac.numeric_to_long(*args)

    def to_double(*args):
        """to_double(self) -> double"""
        return _swiginac.numeric_to_double(*args)

    def to_cl_N(*args):
        """to_cl_N(self) -> cln::cl_N"""
        return _swiginac.numeric_to_cl_N(*args)

    def real(*args):
        """real(self) -> numeric"""
        return _swiginac.numeric_real(*args)

    def imag(*args):
        """imag(self) -> numeric"""
        return _swiginac.numeric_imag(*args)

    def numer(*args):
        """numer(self) -> numeric"""
        return _swiginac.numeric_numer(*args)

    def denom(*args):
        """denom(self) -> numeric"""
        return _swiginac.numeric_denom(*args)

    def int_length(*args):
        """int_length(self) -> int"""
        return _swiginac.numeric_int_length(*args)

    def __init__(self, *args):
        """
        __init__(self, int i) -> numeric
        __init__(self, unsigned int i) -> numeric
        __init__(self, long i) -> numeric
        __init__(self, unsigned long i) -> numeric
        __init__(self, long numer, long denom) -> numeric
        __init__(self, double d) -> numeric
        __init__(self, char ??) -> numeric
        __init__(self, cln::cl_N z) -> numeric
        """
        _swig_setattr(self, numeric, 'this', _swiginac.new_numeric(*args))
        _swig_setattr(self, numeric, 'thisown', 1)
    def __float__(*args):
        """__float__(self) -> double"""
        return _swiginac.numeric___float__(*args)

    def __int__(*args):
        """__int__(self) -> int"""
        return _swiginac.numeric___int__(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_numeric):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class numericPtr(numeric):
    def __init__(self, this):
        _swig_setattr(self, numeric, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, numeric, 'thisown', 0)
        _swig_setattr(self, numeric,self.__class__,numeric)
_swiginac.numeric_swigregister(numericPtr)


def PiEvalf(*args):
    """PiEvalf() -> ex"""
    return _swiginac.PiEvalf(*args)

def EulerEvalf(*args):
    """EulerEvalf() -> ex"""
    return _swiginac.EulerEvalf(*args)

def CatalanEvalf(*args):
    """CatalanEvalf() -> ex"""
    return _swiginac.CatalanEvalf(*args)
class relational(basic):
    """Proxy of C++ relational class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, relational, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, relational, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::relational instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    equal = _swiginac.relational_equal
    not_equal = _swiginac.relational_not_equal
    less = _swiginac.relational_less
    less_or_equal = _swiginac.relational_less_or_equal
    greater = _swiginac.relational_greater
    greater_or_equal = _swiginac.relational_greater_or_equal
    def __init__(self, *args):
        """
        __init__(self, ex lhs, ex rhs, operators oper=equal) -> relational
        __init__(self, ex lhs, ex rhs) -> relational
        """
        _swig_setattr(self, relational, 'this', _swiginac.new_relational(*args))
        _swig_setattr(self, relational, 'thisown', 1)
    def lhs(*args):
        """lhs(self) -> ex"""
        return _swiginac.relational_lhs(*args)

    def rhs(*args):
        """rhs(self) -> ex"""
        return _swiginac.relational_rhs(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_relational):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class relationalPtr(relational):
    def __init__(self, this):
        _swig_setattr(self, relational, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, relational, 'thisown', 0)
        _swig_setattr(self, relational,self.__class__,relational)
_swiginac.relational_swigregister(relationalPtr)


def decomp_rational(*args):
    """decomp_rational(ex a, ex x) -> ex"""
    return _swiginac.decomp_rational(*args)

def sqrfree_parfrac(*args):
    """sqrfree_parfrac(ex a, symbol x) -> ex"""
    return _swiginac.sqrfree_parfrac(*args)

def collect_common_factors(*args):
    """collect_common_factors(ex e) -> ex"""
    return _swiginac.collect_common_factors(*args)

def resultant(*args):
    """resultant(ex e1, ex e2, ex s) -> ex"""
    return _swiginac.resultant(*args)
class constant(basic):
    """Proxy of C++ constant class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, constant, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, constant, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::constant instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, string initname, evalffunctype efun=0, string texname=std::string()) -> constant
        __init__(self, string initname, evalffunctype efun=0) -> constant
        __init__(self, string initname) -> constant
        __init__(self, string initname, numeric initnumber, string texname=std::string()) -> constant
        __init__(self, string initname, numeric initnumber) -> constant
        """
        _swig_setattr(self, constant, 'this', _swiginac.new_constant(*args))
        _swig_setattr(self, constant, 'thisown', 1)
    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_constant):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class constantPtr(constant):
    def __init__(self, this):
        _swig_setattr(self, constant, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, constant, 'thisown', 0)
        _swig_setattr(self, constant,self.__class__,constant)
_swiginac.constant_swigregister(constantPtr)

def quo(*args):
    """
    quo(ex a, ex b, ex x, bool check_args=True) -> ex
    quo(ex a, ex b, ex x) -> ex
    """
    return _swiginac.quo(*args)

def rem(*args):
    """
    rem(ex a, ex b, ex x, bool check_args=True) -> ex
    rem(ex a, ex b, ex x) -> ex
    """
    return _swiginac.rem(*args)

def prem(*args):
    """
    prem(ex a, ex b, ex x, bool check_args=True) -> ex
    prem(ex a, ex b, ex x) -> ex
    """
    return _swiginac.prem(*args)

def sprem(*args):
    """
    sprem(ex a, ex b, ex x, bool check_args=True) -> ex
    sprem(ex a, ex b, ex x) -> ex
    """
    return _swiginac.sprem(*args)

def divide(*args):
    """
    divide(ex a, ex b, ex q, bool check_args=True) -> bool
    divide(ex a, ex b, ex q) -> bool
    """
    return _swiginac.divide(*args)

def gcd(*args):
    """
    gcd(ex a, ex b, ex ca=None, ex cb=None, bool check_args=True) -> ex
    gcd(ex a, ex b, ex ca=None, ex cb=None) -> ex
    gcd(ex a, ex b, ex ca=None) -> ex
    gcd(ex a, ex b) -> ex
    """
    return _swiginac.gcd(*args)

def lcm(*args):
    """
    lcm(ex a, ex b, bool check_args=True) -> ex
    lcm(ex a, ex b) -> ex
    """
    return _swiginac.lcm(*args)

def sqrfree(*args):
    """
    sqrfree(ex a, lst l=lst()) -> ex
    sqrfree(ex a) -> ex
    """
    return _swiginac.sqrfree(*args)

Pi=cvar.Pi
I=cvar.I

class integral(basic):
    """Proxy of C++ integral class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, integral, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, integral, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::integral instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, ex x_, ex a_, ex b_, ex f_) -> integral"""
        _swig_setattr(self, integral, 'this', _swiginac.new_integral(*args))
        _swig_setattr(self, integral, 'thisown', 1)
    def get_free_indices(*args):
        """get_free_indices(self) -> exvector"""
        return _swiginac.integral_get_free_indices(*args)

    def return_type(*args):
        """return_type(self) -> unsigned int"""
        return _swiginac.integral_return_type(*args)

    def return_type_tinfo(*args):
        """return_type_tinfo(self) -> unsigned int"""
        return _swiginac.integral_return_type_tinfo(*args)

    def eval_integ(*args):
        """eval_integ(self) -> ex"""
        return _swiginac.integral_eval_integ(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_integral):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class integralPtr(integral):
    def __init__(self, this):
        _swig_setattr(self, integral, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, integral, 'thisown', 0)
        _swig_setattr(self, integral,self.__class__,integral)
_swiginac.integral_swigregister(integralPtr)
Pi = cvar.Pi
Catalan = cvar.Catalan
Euler = cvar.Euler
I = cvar.I

class matrix(basic):
    """Proxy of C++ matrix class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, matrix, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, matrix, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::matrix instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.matrix_eval_indexed(*args)

    def add_indexed(*args):
        """add_indexed(self, ex self, ex other) -> ex"""
        return _swiginac.matrix_add_indexed(*args)

    def scalar_mul_indexed(*args):
        """scalar_mul_indexed(self, ex self, numeric other) -> ex"""
        return _swiginac.matrix_scalar_mul_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.matrix_contract_with(*args)

    def rows(*args):
        """rows(self) -> unsigned int"""
        return _swiginac.matrix_rows(*args)

    def cols(*args):
        """cols(self) -> unsigned int"""
        return _swiginac.matrix_cols(*args)

    def add(*args):
        """add(self, matrix other) -> matrix"""
        return _swiginac.matrix_add(*args)

    def sub(*args):
        """sub(self, matrix other) -> matrix"""
        return _swiginac.matrix_sub(*args)

    def mul(*args):
        """
        mul(self, matrix other) -> matrix
        mul(self, numeric other) -> matrix
        """
        return _swiginac.matrix_mul(*args)

    def mul_scalar(*args):
        """mul_scalar(self, ex other) -> matrix"""
        return _swiginac.matrix_mul_scalar(*args)

    def pow(*args):
        """pow(self, ex expn) -> matrix"""
        return _swiginac.matrix_pow(*args)

    def __call__(*args):
        """
        __call__(self, unsigned int ro, unsigned int co) -> ex
        __call__(self, unsigned int ro, unsigned int co) -> ex
        """
        return _swiginac.matrix___call__(*args)

    def set(*args):
        """set(self, unsigned int ro, unsigned int co, ex value) -> matrix"""
        return _swiginac.matrix_set(*args)

    def transpose(*args):
        """transpose(self) -> matrix"""
        return _swiginac.matrix_transpose(*args)

    def determinant(*args):
        """
        determinant(self, unsigned int algo=automatic) -> ex
        determinant(self) -> ex
        """
        return _swiginac.matrix_determinant(*args)

    def trace(*args):
        """trace(self) -> ex"""
        return _swiginac.matrix_trace(*args)

    def charpoly(*args):
        """charpoly(self, ex lambda) -> ex"""
        return _swiginac.matrix_charpoly(*args)

    def inverse(*args):
        """inverse(self) -> matrix"""
        return _swiginac.matrix_inverse(*args)

    def solve(*args):
        """
        solve(self, matrix vars, matrix rhs, unsigned int algo=solve_algo::automatic) -> matrix
        solve(self, matrix vars, matrix rhs) -> matrix
        """
        return _swiginac.matrix_solve(*args)

    def rank(*args):
        """rank(self) -> unsigned int"""
        return _swiginac.matrix_rank(*args)

    def __init__(self, *args):
        """
        __init__(self, unsigned int r, unsigned int c) -> matrix
        __init__(self, unsigned int r, unsigned int c, lst l) -> matrix
        __init__(self, lst l) -> matrix
        """
        _swig_setattr(self, matrix, 'this', _swiginac.new_matrix(*args))
        _swig_setattr(self, matrix, 'thisown', 1)
    def __setitem__(*args):
        """__setitem__(self, int idx0, ex e)"""
        return _swiginac.matrix___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, int idx0) -> ex"""
        return _swiginac.matrix___getitem__(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_matrix):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class matrixPtr(matrix):
    def __init__(self, this):
        _swig_setattr(self, matrix, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, matrix, 'thisown', 0)
        _swig_setattr(self, matrix,self.__class__,matrix)
_swiginac.matrix_swigregister(matrixPtr)

def adaptivesimpson(*args):
    """
    adaptivesimpson(ex x, ex a, ex b, ex f, ex error=relative_integration_error) -> ex
    adaptivesimpson(ex x, ex a, ex b, ex f) -> ex
    """
    return _swiginac.adaptivesimpson(*args)

def matrix2(x):
    return lst_to_matrix(x)


def nops(*args):
    """nops(matrix m) -> size_t"""
    return _swiginac.nops(*args)

def rows(*args):
    """rows(matrix m) -> unsigned int"""
    return _swiginac.rows(*args)

def cols(*args):
    """cols(matrix m) -> unsigned int"""
    return _swiginac.cols(*args)

def transpose(*args):
    """transpose(matrix m) -> matrix"""
    return _swiginac.transpose(*args)

def trace(*args):
    """trace(matrix m) -> ex"""
    return _swiginac.trace(*args)

def charpoly(*args):
    """charpoly(matrix m, ex lambda) -> ex"""
    return _swiginac.charpoly(*args)

def inverse(*args):
    """inverse(matrix m) -> matrix"""
    return _swiginac.inverse(*args)

def rank(*args):
    """rank(matrix m) -> unsigned int"""
    return _swiginac.rank(*args)

def lst_to_matrix(*args):
    """lst_to_matrix(lst l) -> ex"""
    return _swiginac.lst_to_matrix(*args)

def diag_matrix(*args):
    """diag_matrix(lst l) -> ex"""
    return _swiginac.diag_matrix(*args)
EXPAIRSEQ_USE_HASHTAB = _swiginac.EXPAIRSEQ_USE_HASHTAB

def conjugateepvector(*args):
    """conjugateepvector(epvector ??) -> epvector"""
    return _swiginac.conjugateepvector(*args)
class expairseq(basic):
    """Proxy of C++ expairseq class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, expairseq, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, expairseq, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::expairseq instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex lh, ex rh) -> expairseq
        __init__(self, exvector v) -> expairseq
        """
        _swig_setattr(self, expairseq, 'this', _swiginac.new_expairseq(*args))
        _swig_setattr(self, expairseq, 'thisown', 1)
    def precedence(*args):
        """precedence(self) -> unsigned int"""
        return _swiginac.expairseq_precedence(*args)

    def __del__(self, destroy=_swiginac.delete_expairseq):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class expairseqPtr(expairseq):
    def __init__(self, this):
        _swig_setattr(self, expairseq, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, expairseq, 'thisown', 0)
        _swig_setattr(self, expairseq,self.__class__,expairseq)
_swiginac.expairseq_swigregister(expairseqPtr)

def eval(*args):
    """
    eval(matrix m, int level=0) -> ex
    eval(matrix m) -> ex
    """
    return _swiginac.eval(*args)

def evalf(*args):
    """
    evalf(matrix m, int level=0) -> ex
    evalf(matrix m) -> ex
    """
    return _swiginac.evalf(*args)

def determinant(*args):
    """
    determinant(matrix m, unsigned int options=automatic) -> ex
    determinant(matrix m) -> ex
    """
    return _swiginac.determinant(*args)

def unit_matrix(*args):
    """
    unit_matrix(unsigned int r, unsigned int c) -> ex
    unit_matrix(unsigned int x) -> ex
    """
    return _swiginac.unit_matrix(*args)

def symbolic_matrix(*args):
    """
    symbolic_matrix(unsigned int r, unsigned int c, string base_name, string tex_base_name) -> ex
    symbolic_matrix(unsigned int r, unsigned int c, string base_name) -> ex
    """
    return _swiginac.symbolic_matrix(*args)

class mul(expairseq):
    """Proxy of C++ mul class"""
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, mul, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, mul, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::mul instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex lh, ex rh) -> mul
        __init__(self, exvector v) -> mul
        __init__(self, epvector v) -> mul
        __init__(self, ex lh, ex mh, ex rh) -> mul
        """
        _swig_setattr(self, mul, 'this', _swiginac.new_mul(*args))
        _swig_setattr(self, mul, 'thisown', 1)
    def algebraic_subs_mul(*args):
        """algebraic_subs_mul(self, exmap m, unsigned int options) -> ex"""
        return _swiginac.mul_algebraic_subs_mul(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_mul):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class mulPtr(mul):
    def __init__(self, this):
        _swig_setattr(self, mul, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mul, 'thisown', 0)
        _swig_setattr(self, mul,self.__class__,mul)
_swiginac.mul_swigregister(mulPtr)

class ncmul(basic):
    """Proxy of C++ ncmul class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ncmul, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ncmul, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::ncmul instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex lh, ex rh) -> ncmul
        __init__(self, ex f1, ex f2, ex f3) -> ncmul
        __init__(self, ex f1, ex f2, ex f3, ex f4) -> ncmul
        __init__(self, ex f1, ex f2, ex f3, ex f4, ex f5) -> ncmul
        __init__(self, ex f1, ex f2, ex f3, ex f4, ex f5, ex f6) -> ncmul
        """
        _swig_setattr(self, ncmul, 'this', _swiginac.new_ncmul(*args))
        _swig_setattr(self, ncmul, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_ncmul):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class ncmulPtr(ncmul):
    def __init__(self, this):
        _swig_setattr(self, ncmul, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ncmul, 'thisown', 0)
        _swig_setattr(self, ncmul,self.__class__,ncmul)
_swiginac.ncmul_swigregister(ncmulPtr)

class power(basic):
    """Proxy of C++ power class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, power, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, power, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::power instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, ex lh, ex rh) -> power"""
        _swig_setattr(self, power, 'this', _swiginac.new_power(*args))
        _swig_setattr(self, power, 'thisown', 1)
    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_power):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class powerPtr(power):
    def __init__(self, this):
        _swig_setattr(self, power, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, power, 'thisown', 0)
        _swig_setattr(self, power,self.__class__,power)
_swiginac.power_swigregister(powerPtr)

class add(expairseq):
    """Proxy of C++ add class"""
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, add, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, add, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::add instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex lh, ex rh) -> add
        __init__(self, exvector v) -> add
        __init__(self, epvector v) -> add
        """
        _swig_setattr(self, add, 'this', _swiginac.new_add(*args))
        _swig_setattr(self, add, 'thisown', 1)
    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_add):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class addPtr(add):
    def __init__(self, this):
        _swig_setattr(self, add, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, add, 'thisown', 0)
        _swig_setattr(self, add,self.__class__,add)
_swiginac.add_swigregister(addPtr)

class function_options(_object):
    """Proxy of C++ function_options class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, function_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, function_options, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::function_options instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self) -> function_options
        __init__(self, string n, string tn=std::string()) -> function_options
        __init__(self, string n) -> function_options
        __init__(self, string n, unsigned int np) -> function_options
        """
        _swig_setattr(self, function_options, 'this', _swiginac.new_function_options(*args))
        _swig_setattr(self, function_options, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_function_options):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass

    def initialize(*args):
        """initialize(self)"""
        return _swiginac.function_options_initialize(*args)

    def dummy(*args):
        """dummy(self) -> function_options"""
        return _swiginac.function_options_dummy(*args)

    def set_name(*args):
        """
        set_name(self, string n, string tn=std::string()) -> function_options
        set_name(self, string n) -> function_options
        """
        return _swiginac.function_options_set_name(*args)

    def latex_name(*args):
        """latex_name(self, string tn) -> function_options"""
        return _swiginac.function_options_latex_name(*args)

    def eval_func(*args):
        """
        eval_func(self, eval_funcp_1 e) -> function_options
        eval_func(self, eval_funcp_2 e) -> function_options
        eval_func(self, eval_funcp_3 e) -> function_options
        eval_func(self, eval_funcp_4 e) -> function_options
        eval_func(self, eval_funcp_5 e) -> function_options
        eval_func(self, eval_funcp_exvector e) -> function_options
        """
        return _swiginac.function_options_eval_func(*args)

    def evalf_func(*args):
        """
        evalf_func(self, evalf_funcp_1 ef) -> function_options
        evalf_func(self, evalf_funcp_2 ef) -> function_options
        evalf_func(self, evalf_funcp_3 ef) -> function_options
        evalf_func(self, evalf_funcp_4 ef) -> function_options
        evalf_func(self, evalf_funcp_5 ef) -> function_options
        evalf_func(self, evalf_funcp_exvector ef) -> function_options
        """
        return _swiginac.function_options_evalf_func(*args)

    def conjugate_func(*args):
        """
        conjugate_func(self, conjugate_funcp_1 d) -> function_options
        conjugate_func(self, conjugate_funcp_2 d) -> function_options
        conjugate_func(self, conjugate_funcp_3 d) -> function_options
        conjugate_func(self, conjugate_funcp_4 d) -> function_options
        conjugate_func(self, conjugate_funcp_5 d) -> function_options
        conjugate_func(self, conjugate_funcp_exvector d) -> function_options
        """
        return _swiginac.function_options_conjugate_func(*args)

    def derivative_func(*args):
        """
        derivative_func(self, derivative_funcp_1 d) -> function_options
        derivative_func(self, derivative_funcp_2 d) -> function_options
        derivative_func(self, derivative_funcp_3 d) -> function_options
        derivative_func(self, derivative_funcp_4 d) -> function_options
        derivative_func(self, derivative_funcp_5 d) -> function_options
        derivative_func(self, derivative_funcp_exvector d) -> function_options
        """
        return _swiginac.function_options_derivative_func(*args)

    def series_func(*args):
        """
        series_func(self, series_funcp_1 s) -> function_options
        series_func(self, series_funcp_2 s) -> function_options
        series_func(self, series_funcp_3 s) -> function_options
        series_func(self, series_funcp_4 s) -> function_options
        series_func(self, series_funcp_5 s) -> function_options
        series_func(self, series_funcp_exvector s) -> function_options
        """
        return _swiginac.function_options_series_func(*args)

    def set_return_type(*args):
        """
        set_return_type(self, unsigned int rt, unsigned int rtt=0) -> function_options
        set_return_type(self, unsigned int rt) -> function_options
        """
        return _swiginac.function_options_set_return_type(*args)

    def do_not_evalf_params(*args):
        """do_not_evalf_params(self) -> function_options"""
        return _swiginac.function_options_do_not_evalf_params(*args)

    def remember(*args):
        """
        remember(self, unsigned int size, unsigned int assoc_size=0, unsigned int strategy=remember_strategies::delete_never) -> function_options
        remember(self, unsigned int size, unsigned int assoc_size=0) -> function_options
        remember(self, unsigned int size) -> function_options
        """
        return _swiginac.function_options_remember(*args)

    def overloaded(*args):
        """overloaded(self, unsigned int o) -> function_options"""
        return _swiginac.function_options_overloaded(*args)

    def set_symmetry(*args):
        """set_symmetry(self, symmetry s) -> function_options"""
        return _swiginac.function_options_set_symmetry(*args)

    def get_name(*args):
        """get_name(self) -> string"""
        return _swiginac.function_options_get_name(*args)

    def get_nparams(*args):
        """get_nparams(self) -> unsigned int"""
        return _swiginac.function_options_get_nparams(*args)


class function_optionsPtr(function_options):
    def __init__(self, this):
        _swig_setattr(self, function_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, function_options, 'thisown', 0)
        _swig_setattr(self, function_options,self.__class__,function_options)
_swiginac.function_options_swigregister(function_optionsPtr)

class do_taylor(_object):
    """Proxy of C++ do_taylor class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, do_taylor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, do_taylor, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::do_taylor instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> do_taylor"""
        _swig_setattr(self, do_taylor, 'this', _swiginac.new_do_taylor(*args))
        _swig_setattr(self, do_taylor, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_do_taylor):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class do_taylorPtr(do_taylor):
    def __init__(self, this):
        _swig_setattr(self, do_taylor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, do_taylor, 'thisown', 0)
        _swig_setattr(self, do_taylor,self.__class__,do_taylor)
_swiginac.do_taylor_swigregister(do_taylorPtr)

class function(basic):
    """Proxy of C++ function class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, function, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, function, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::function instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, unsigned int ser) -> function
        __init__(self, unsigned int ser, ex param1) -> function
        __init__(self, unsigned int ser, ex param1, ex param2) -> function
        __init__(self, unsigned int ser, ex param1, ex param2, ex param3) -> function
        __init__(self, unsigned int ser, ex param1, ex param2, ex param3, 
            ex param4) -> function
        __init__(self, unsigned int ser, ex param1, ex param2, ex param3, 
            ex param4, ex param5) -> function
        """
        _swig_setattr(self, function, 'this', _swiginac.new_function(*args))
        _swig_setattr(self, function, 'thisown', 1)
    def precedence(*args):
        """precedence(self) -> unsigned int"""
        return _swiginac.function_precedence(*args)

    def calchash(*args):
        """calchash(self) -> unsigned int"""
        return _swiginac.function_calchash(*args)

    def thiscontainer(*args):
        """thiscontainer(self, exvector v) -> ex"""
        return _swiginac.function_thiscontainer(*args)

    def register_new(*args):
        """register_new(function_options opt) -> unsigned int"""
        return _swiginac.function_register_new(*args)

    if _newclass:register_new = staticmethod(register_new)
    __swig_getmethods__["register_new"] = lambda x: register_new
    def find_function(*args):
        """find_function(string name, unsigned int nparams) -> unsigned int"""
        return _swiginac.function_find_function(*args)

    if _newclass:find_function = staticmethod(find_function)
    __swig_getmethods__["find_function"] = lambda x: find_function
    def get_serial(*args):
        """get_serial(self) -> unsigned int"""
        return _swiginac.function_get_serial(*args)

    def get_name(*args):
        """get_name(self) -> string"""
        return _swiginac.function_get_name(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_function):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class functionPtr(function):
    def __init__(self, this):
        _swig_setattr(self, function, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, function, 'thisown', 0)
        _swig_setattr(self, function,self.__class__,function)
_swiginac.function_swigregister(functionPtr)

def function_register_new(*args):
    """function_register_new(function_options opt) -> unsigned int"""
    return _swiginac.function_register_new(*args)

def function_find_function(*args):
    """function_find_function(string name, unsigned int nparams) -> unsigned int"""
    return _swiginac.function_find_function(*args)


def conjugate(*args):
    """conjugate(ex thisex) -> ex"""
    return _swiginac.conjugate(*args)

def has(*args):
    """has(ex thisex, ex pattern) -> bool"""
    return _swiginac.has(*args)

def find(*args):
    """find(ex thisex, ex pattern, lst found) -> bool"""
    return _swiginac.find(*args)

def degree(*args):
    """degree(ex thisex, ex s) -> int"""
    return _swiginac.degree(*args)

def ldegree(*args):
    """ldegree(ex thisex, ex s) -> int"""
    return _swiginac.ldegree(*args)

def numer(*args):
    """numer(ex thisex) -> ex"""
    return _swiginac.numer(*args)

def denom(*args):
    """denom(ex thisex) -> ex"""
    return _swiginac.denom(*args)

def numer_denom(*args):
    """numer_denom(ex thisex) -> ex"""
    return _swiginac.numer_denom(*args)

def to_rational(*args):
    """to_rational(ex thisex, lst repl_lst) -> ex"""
    return _swiginac.to_rational(*args)

def to_polynomial(*args):
    """to_polynomial(ex thisex, lst repl_lst) -> ex"""
    return _swiginac.to_polynomial(*args)

def evalm(*args):
    """evalm(ex thisex) -> ex"""
    return _swiginac.evalm(*args)

def eval_integ(*args):
    """eval_integ(ex thisex) -> ex"""
    return _swiginac.eval_integ(*args)

def match(*args):
    """match(ex thisex, ex pattern, lst repl_lst) -> bool"""
    return _swiginac.match(*args)

def op(*args):
    """op(ex thisex, size_t i) -> ex"""
    return _swiginac.op(*args)

def lhs(*args):
    """lhs(ex thisex) -> ex"""
    return _swiginac.lhs(*args)

def rhs(*args):
    """rhs(ex thisex) -> ex"""
    return _swiginac.rhs(*args)

def swap(*args):
    """swap(ex e1, ex e2)"""
    return _swiginac.swap(*args)

def sqrt(*args):
    """sqrt(ex a) -> ex"""
    return _swiginac.sqrt(*args)

def expand(*args):
    """expand(ex thisex) -> ex"""
    return _swiginac.expand(*args)
class conjugate_function_SERIAL(_object):
    """Proxy of C++ conjugate_function_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, conjugate_function_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, conjugate_function_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::conjugate_function_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> conjugate_function_SERIAL"""
        _swig_setattr(self, conjugate_function_SERIAL, 'this', _swiginac.new_conjugate_function_SERIAL(*args))
        _swig_setattr(self, conjugate_function_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_conjugate_function_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class conjugate_function_SERIALPtr(conjugate_function_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, conjugate_function_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, conjugate_function_SERIAL, 'thisown', 0)
        _swig_setattr(self, conjugate_function_SERIAL,self.__class__,conjugate_function_SERIAL)
_swiginac.conjugate_function_SERIAL_swigregister(conjugate_function_SERIALPtr)

def coeff(*args):
    """
    coeff(ex thisex, ex s, int n=1) -> ex
    coeff(ex thisex, ex s) -> ex
    """
    return _swiginac.coeff(*args)

def normal(*args):
    """
    normal(ex thisex, int level=0) -> ex
    normal(ex thisex) -> ex
    """
    return _swiginac.normal(*args)

def collect(*args):
    """
    collect(ex thisex, ex s, bool distributed=False) -> ex
    collect(ex thisex, ex s) -> ex
    """
    return _swiginac.collect(*args)

def diff(*args):
    """
    diff(ex thisex, symbol s, unsigned int nth=1) -> ex
    diff(ex thisex, symbol s) -> ex
    """
    return _swiginac.diff(*args)

def series(*args):
    """
    series(ex thisex, ex r, int order, unsigned int options=0) -> ex
    series(ex thisex, ex r, int order) -> ex
    """
    return _swiginac.series(*args)

def simplify_indexed(*args):
    """
    simplify_indexed(ex thisex, unsigned int options=0) -> ex
    simplify_indexed(ex thisex) -> ex
    simplify_indexed(ex thisex, scalar_products sp, unsigned int options=0) -> ex
    simplify_indexed(ex thisex, scalar_products sp) -> ex
    """
    return _swiginac.simplify_indexed(*args)

def subs(*args):
    """
    subs(ex thisex, lst ls, lst lr, unsigned int options=0) -> ex
    subs(ex thisex, lst ls, lst lr) -> ex
    subs(ex thisex, ex e) -> ex
    """
    return _swiginac.subs(*args)


def conjugate_function_ex(*args):
    """conjugate_function_ex(ex p1) -> function"""
    return _swiginac.conjugate_function_ex(*args)

def conjugate_function_basic(*args):
    """conjugate_function_basic(basic p1) -> function"""
    return _swiginac.conjugate_function_basic(*args)

def conjugate_function_int(*args):
    """conjugate_function_int(int p1) -> function"""
    return _swiginac.conjugate_function_int(*args)

def conjugate_function_double(*args):
    """conjugate_function_double(double p1) -> function"""
    return _swiginac.conjugate_function_double(*args)
def conjugate_function(x):
    if isinstance(x,basic):
        return conjugate_function_basic(x).eval()
    elif isinstance(x,int):
        return conjugate_function_int(x).eval()
    elif isinstance(x,float):
        return conjugate_function_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class abs_SERIAL(_object):
    """Proxy of C++ abs_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, abs_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, abs_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::abs_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> abs_SERIAL"""
        _swig_setattr(self, abs_SERIAL, 'this', _swiginac.new_abs_SERIAL(*args))
        _swig_setattr(self, abs_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_abs_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class abs_SERIALPtr(abs_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, abs_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, abs_SERIAL, 'thisown', 0)
        _swig_setattr(self, abs_SERIAL,self.__class__,abs_SERIAL)
_swiginac.abs_SERIAL_swigregister(abs_SERIALPtr)
conjugate_function_NPARAMS = cvar.conjugate_function_NPARAMS


def abs_ex(*args):
    """abs_ex(ex p1) -> function"""
    return _swiginac.abs_ex(*args)

def abs_basic(*args):
    """abs_basic(basic p1) -> function"""
    return _swiginac.abs_basic(*args)

def abs_int(*args):
    """abs_int(int p1) -> function"""
    return _swiginac.abs_int(*args)

def abs_double(*args):
    """abs_double(double p1) -> function"""
    return _swiginac.abs_double(*args)
def abs(x):
    if isinstance(x,basic):
        return abs_basic(x).eval()
    elif isinstance(x,int):
        return abs_int(x).eval()
    elif isinstance(x,float):
        return abs_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class csgn_SERIAL(_object):
    """Proxy of C++ csgn_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, csgn_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, csgn_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::csgn_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> csgn_SERIAL"""
        _swig_setattr(self, csgn_SERIAL, 'this', _swiginac.new_csgn_SERIAL(*args))
        _swig_setattr(self, csgn_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_csgn_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class csgn_SERIALPtr(csgn_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, csgn_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, csgn_SERIAL, 'thisown', 0)
        _swig_setattr(self, csgn_SERIAL,self.__class__,csgn_SERIAL)
_swiginac.csgn_SERIAL_swigregister(csgn_SERIALPtr)
abs_NPARAMS = cvar.abs_NPARAMS


def csgn_ex(*args):
    """csgn_ex(ex p1) -> function"""
    return _swiginac.csgn_ex(*args)

def csgn_basic(*args):
    """csgn_basic(basic p1) -> function"""
    return _swiginac.csgn_basic(*args)

def csgn_int(*args):
    """csgn_int(int p1) -> function"""
    return _swiginac.csgn_int(*args)

def csgn_double(*args):
    """csgn_double(double p1) -> function"""
    return _swiginac.csgn_double(*args)
def csgn(x):
    if isinstance(x,basic):
        return csgn_basic(x).eval()
    elif isinstance(x,int):
        return csgn_int(x).eval()
    elif isinstance(x,float):
        return csgn_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class eta_SERIAL(_object):
    """Proxy of C++ eta_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eta_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::eta_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> eta_SERIAL"""
        _swig_setattr(self, eta_SERIAL, 'this', _swiginac.new_eta_SERIAL(*args))
        _swig_setattr(self, eta_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_eta_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class eta_SERIALPtr(eta_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, eta_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, eta_SERIAL, 'thisown', 0)
        _swig_setattr(self, eta_SERIAL,self.__class__,eta_SERIAL)
_swiginac.eta_SERIAL_swigregister(eta_SERIALPtr)
csgn_NPARAMS = cvar.csgn_NPARAMS

class sin_SERIAL(_object):
    """Proxy of C++ sin_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sin_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::sin_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> sin_SERIAL"""
        _swig_setattr(self, sin_SERIAL, 'this', _swiginac.new_sin_SERIAL(*args))
        _swig_setattr(self, sin_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_sin_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class sin_SERIALPtr(sin_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, sin_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, sin_SERIAL, 'thisown', 0)
        _swig_setattr(self, sin_SERIAL,self.__class__,sin_SERIAL)
_swiginac.sin_SERIAL_swigregister(sin_SERIALPtr)
eta_NPARAMS = cvar.eta_NPARAMS


def sin_ex(*args):
    """sin_ex(ex p1) -> function"""
    return _swiginac.sin_ex(*args)

def sin_basic(*args):
    """sin_basic(basic p1) -> function"""
    return _swiginac.sin_basic(*args)

def sin_int(*args):
    """sin_int(int p1) -> function"""
    return _swiginac.sin_int(*args)

def sin_double(*args):
    """sin_double(double p1) -> function"""
    return _swiginac.sin_double(*args)
def sin(x):
    if isinstance(x,basic):
        return sin_basic(x).eval()
    elif isinstance(x,int):
        return sin_int(x).eval()
    elif isinstance(x,float):
        return sin_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class cos_SERIAL(_object):
    """Proxy of C++ cos_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cos_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::cos_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> cos_SERIAL"""
        _swig_setattr(self, cos_SERIAL, 'this', _swiginac.new_cos_SERIAL(*args))
        _swig_setattr(self, cos_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_cos_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class cos_SERIALPtr(cos_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, cos_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cos_SERIAL, 'thisown', 0)
        _swig_setattr(self, cos_SERIAL,self.__class__,cos_SERIAL)
_swiginac.cos_SERIAL_swigregister(cos_SERIALPtr)
sin_NPARAMS = cvar.sin_NPARAMS


def cos_ex(*args):
    """cos_ex(ex p1) -> function"""
    return _swiginac.cos_ex(*args)

def cos_basic(*args):
    """cos_basic(basic p1) -> function"""
    return _swiginac.cos_basic(*args)

def cos_int(*args):
    """cos_int(int p1) -> function"""
    return _swiginac.cos_int(*args)

def cos_double(*args):
    """cos_double(double p1) -> function"""
    return _swiginac.cos_double(*args)
def cos(x):
    if isinstance(x,basic):
        return cos_basic(x).eval()
    elif isinstance(x,int):
        return cos_int(x).eval()
    elif isinstance(x,float):
        return cos_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class tan_SERIAL(_object):
    """Proxy of C++ tan_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tan_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tan_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> tan_SERIAL"""
        _swig_setattr(self, tan_SERIAL, 'this', _swiginac.new_tan_SERIAL(*args))
        _swig_setattr(self, tan_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_tan_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tan_SERIALPtr(tan_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, tan_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tan_SERIAL, 'thisown', 0)
        _swig_setattr(self, tan_SERIAL,self.__class__,tan_SERIAL)
_swiginac.tan_SERIAL_swigregister(tan_SERIALPtr)
cos_NPARAMS = cvar.cos_NPARAMS


def tan_ex(*args):
    """tan_ex(ex p1) -> function"""
    return _swiginac.tan_ex(*args)

def tan_basic(*args):
    """tan_basic(basic p1) -> function"""
    return _swiginac.tan_basic(*args)

def tan_int(*args):
    """tan_int(int p1) -> function"""
    return _swiginac.tan_int(*args)

def tan_double(*args):
    """tan_double(double p1) -> function"""
    return _swiginac.tan_double(*args)
def tan(x):
    if isinstance(x,basic):
        return tan_basic(x).eval()
    elif isinstance(x,int):
        return tan_int(x).eval()
    elif isinstance(x,float):
        return tan_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class exp_SERIAL(_object):
    """Proxy of C++ exp_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, exp_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, exp_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::exp_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> exp_SERIAL"""
        _swig_setattr(self, exp_SERIAL, 'this', _swiginac.new_exp_SERIAL(*args))
        _swig_setattr(self, exp_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_exp_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class exp_SERIALPtr(exp_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, exp_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, exp_SERIAL, 'thisown', 0)
        _swig_setattr(self, exp_SERIAL,self.__class__,exp_SERIAL)
_swiginac.exp_SERIAL_swigregister(exp_SERIALPtr)
tan_NPARAMS = cvar.tan_NPARAMS


def exp_ex(*args):
    """exp_ex(ex p1) -> function"""
    return _swiginac.exp_ex(*args)

def exp_basic(*args):
    """exp_basic(basic p1) -> function"""
    return _swiginac.exp_basic(*args)

def exp_int(*args):
    """exp_int(int p1) -> function"""
    return _swiginac.exp_int(*args)

def exp_double(*args):
    """exp_double(double p1) -> function"""
    return _swiginac.exp_double(*args)
def exp(x):
    if isinstance(x,basic):
        return exp_basic(x).eval()
    elif isinstance(x,int):
        return exp_int(x).eval()
    elif isinstance(x,float):
        return exp_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class log_SERIAL(_object):
    """Proxy of C++ log_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, log_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, log_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::log_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> log_SERIAL"""
        _swig_setattr(self, log_SERIAL, 'this', _swiginac.new_log_SERIAL(*args))
        _swig_setattr(self, log_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_log_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class log_SERIALPtr(log_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, log_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, log_SERIAL, 'thisown', 0)
        _swig_setattr(self, log_SERIAL,self.__class__,log_SERIAL)
_swiginac.log_SERIAL_swigregister(log_SERIALPtr)
exp_NPARAMS = cvar.exp_NPARAMS


def log_ex(*args):
    """log_ex(ex p1) -> function"""
    return _swiginac.log_ex(*args)

def log_basic(*args):
    """log_basic(basic p1) -> function"""
    return _swiginac.log_basic(*args)

def log_int(*args):
    """log_int(int p1) -> function"""
    return _swiginac.log_int(*args)

def log_double(*args):
    """log_double(double p1) -> function"""
    return _swiginac.log_double(*args)
def log(x):
    if isinstance(x,basic):
        return log_basic(x).eval()
    elif isinstance(x,int):
        return log_int(x).eval()
    elif isinstance(x,float):
        return log_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class asin_SERIAL(_object):
    """Proxy of C++ asin_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asin_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::asin_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> asin_SERIAL"""
        _swig_setattr(self, asin_SERIAL, 'this', _swiginac.new_asin_SERIAL(*args))
        _swig_setattr(self, asin_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_asin_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class asin_SERIALPtr(asin_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, asin_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, asin_SERIAL, 'thisown', 0)
        _swig_setattr(self, asin_SERIAL,self.__class__,asin_SERIAL)
_swiginac.asin_SERIAL_swigregister(asin_SERIALPtr)
log_NPARAMS = cvar.log_NPARAMS


def asin_ex(*args):
    """asin_ex(ex p1) -> function"""
    return _swiginac.asin_ex(*args)

def asin_basic(*args):
    """asin_basic(basic p1) -> function"""
    return _swiginac.asin_basic(*args)

def asin_int(*args):
    """asin_int(int p1) -> function"""
    return _swiginac.asin_int(*args)

def asin_double(*args):
    """asin_double(double p1) -> function"""
    return _swiginac.asin_double(*args)
def asin(x):
    if isinstance(x,basic):
        return asin_basic(x).eval()
    elif isinstance(x,int):
        return asin_int(x).eval()
    elif isinstance(x,float):
        return asin_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class acos_SERIAL(_object):
    """Proxy of C++ acos_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acos_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::acos_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> acos_SERIAL"""
        _swig_setattr(self, acos_SERIAL, 'this', _swiginac.new_acos_SERIAL(*args))
        _swig_setattr(self, acos_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_acos_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class acos_SERIALPtr(acos_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, acos_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, acos_SERIAL, 'thisown', 0)
        _swig_setattr(self, acos_SERIAL,self.__class__,acos_SERIAL)
_swiginac.acos_SERIAL_swigregister(acos_SERIALPtr)
asin_NPARAMS = cvar.asin_NPARAMS


def acos_ex(*args):
    """acos_ex(ex p1) -> function"""
    return _swiginac.acos_ex(*args)

def acos_basic(*args):
    """acos_basic(basic p1) -> function"""
    return _swiginac.acos_basic(*args)

def acos_int(*args):
    """acos_int(int p1) -> function"""
    return _swiginac.acos_int(*args)

def acos_double(*args):
    """acos_double(double p1) -> function"""
    return _swiginac.acos_double(*args)
def acos(x):
    if isinstance(x,basic):
        return acos_basic(x).eval()
    elif isinstance(x,int):
        return acos_int(x).eval()
    elif isinstance(x,float):
        return acos_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class atan_SERIAL(_object):
    """Proxy of C++ atan_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::atan_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> atan_SERIAL"""
        _swig_setattr(self, atan_SERIAL, 'this', _swiginac.new_atan_SERIAL(*args))
        _swig_setattr(self, atan_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_atan_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class atan_SERIALPtr(atan_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, atan_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atan_SERIAL, 'thisown', 0)
        _swig_setattr(self, atan_SERIAL,self.__class__,atan_SERIAL)
_swiginac.atan_SERIAL_swigregister(atan_SERIALPtr)
acos_NPARAMS = cvar.acos_NPARAMS


def atan_ex(*args):
    """atan_ex(ex p1) -> function"""
    return _swiginac.atan_ex(*args)

def atan_basic(*args):
    """atan_basic(basic p1) -> function"""
    return _swiginac.atan_basic(*args)

def atan_int(*args):
    """atan_int(int p1) -> function"""
    return _swiginac.atan_int(*args)

def atan_double(*args):
    """atan_double(double p1) -> function"""
    return _swiginac.atan_double(*args)
def atan(x):
    if isinstance(x,basic):
        return atan_basic(x).eval()
    elif isinstance(x,int):
        return atan_int(x).eval()
    elif isinstance(x,float):
        return atan_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class atan2_SERIAL(_object):
    """Proxy of C++ atan2_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan2_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::atan2_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> atan2_SERIAL"""
        _swig_setattr(self, atan2_SERIAL, 'this', _swiginac.new_atan2_SERIAL(*args))
        _swig_setattr(self, atan2_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_atan2_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class atan2_SERIALPtr(atan2_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, atan2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atan2_SERIAL, 'thisown', 0)
        _swig_setattr(self, atan2_SERIAL,self.__class__,atan2_SERIAL)
_swiginac.atan2_SERIAL_swigregister(atan2_SERIALPtr)
atan_NPARAMS = cvar.atan_NPARAMS

class sinh_SERIAL(_object):
    """Proxy of C++ sinh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sinh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::sinh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> sinh_SERIAL"""
        _swig_setattr(self, sinh_SERIAL, 'this', _swiginac.new_sinh_SERIAL(*args))
        _swig_setattr(self, sinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_sinh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class sinh_SERIALPtr(sinh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, sinh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, sinh_SERIAL, 'thisown', 0)
        _swig_setattr(self, sinh_SERIAL,self.__class__,sinh_SERIAL)
_swiginac.sinh_SERIAL_swigregister(sinh_SERIALPtr)
atan2_NPARAMS = cvar.atan2_NPARAMS


def sinh_ex(*args):
    """sinh_ex(ex p1) -> function"""
    return _swiginac.sinh_ex(*args)

def sinh_basic(*args):
    """sinh_basic(basic p1) -> function"""
    return _swiginac.sinh_basic(*args)

def sinh_int(*args):
    """sinh_int(int p1) -> function"""
    return _swiginac.sinh_int(*args)

def sinh_double(*args):
    """sinh_double(double p1) -> function"""
    return _swiginac.sinh_double(*args)
def sinh(x):
    if isinstance(x,basic):
        return sinh_basic(x).eval()
    elif isinstance(x,int):
        return sinh_int(x).eval()
    elif isinstance(x,float):
        return sinh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class cosh_SERIAL(_object):
    """Proxy of C++ cosh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cosh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::cosh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> cosh_SERIAL"""
        _swig_setattr(self, cosh_SERIAL, 'this', _swiginac.new_cosh_SERIAL(*args))
        _swig_setattr(self, cosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_cosh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class cosh_SERIALPtr(cosh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, cosh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cosh_SERIAL, 'thisown', 0)
        _swig_setattr(self, cosh_SERIAL,self.__class__,cosh_SERIAL)
_swiginac.cosh_SERIAL_swigregister(cosh_SERIALPtr)
sinh_NPARAMS = cvar.sinh_NPARAMS


def cosh_ex(*args):
    """cosh_ex(ex p1) -> function"""
    return _swiginac.cosh_ex(*args)

def cosh_basic(*args):
    """cosh_basic(basic p1) -> function"""
    return _swiginac.cosh_basic(*args)

def cosh_int(*args):
    """cosh_int(int p1) -> function"""
    return _swiginac.cosh_int(*args)

def cosh_double(*args):
    """cosh_double(double p1) -> function"""
    return _swiginac.cosh_double(*args)
def cosh(x):
    if isinstance(x,basic):
        return cosh_basic(x).eval()
    elif isinstance(x,int):
        return cosh_int(x).eval()
    elif isinstance(x,float):
        return cosh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class tanh_SERIAL(_object):
    """Proxy of C++ tanh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tanh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tanh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> tanh_SERIAL"""
        _swig_setattr(self, tanh_SERIAL, 'this', _swiginac.new_tanh_SERIAL(*args))
        _swig_setattr(self, tanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_tanh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tanh_SERIALPtr(tanh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, tanh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tanh_SERIAL, 'thisown', 0)
        _swig_setattr(self, tanh_SERIAL,self.__class__,tanh_SERIAL)
_swiginac.tanh_SERIAL_swigregister(tanh_SERIALPtr)
cosh_NPARAMS = cvar.cosh_NPARAMS


def tanh_ex(*args):
    """tanh_ex(ex p1) -> function"""
    return _swiginac.tanh_ex(*args)

def tanh_basic(*args):
    """tanh_basic(basic p1) -> function"""
    return _swiginac.tanh_basic(*args)

def tanh_int(*args):
    """tanh_int(int p1) -> function"""
    return _swiginac.tanh_int(*args)

def tanh_double(*args):
    """tanh_double(double p1) -> function"""
    return _swiginac.tanh_double(*args)
def tanh(x):
    if isinstance(x,basic):
        return tanh_basic(x).eval()
    elif isinstance(x,int):
        return tanh_int(x).eval()
    elif isinstance(x,float):
        return tanh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class asinh_SERIAL(_object):
    """Proxy of C++ asinh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asinh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::asinh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> asinh_SERIAL"""
        _swig_setattr(self, asinh_SERIAL, 'this', _swiginac.new_asinh_SERIAL(*args))
        _swig_setattr(self, asinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_asinh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class asinh_SERIALPtr(asinh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, asinh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, asinh_SERIAL, 'thisown', 0)
        _swig_setattr(self, asinh_SERIAL,self.__class__,asinh_SERIAL)
_swiginac.asinh_SERIAL_swigregister(asinh_SERIALPtr)
tanh_NPARAMS = cvar.tanh_NPARAMS


def asinh_ex(*args):
    """asinh_ex(ex p1) -> function"""
    return _swiginac.asinh_ex(*args)

def asinh_basic(*args):
    """asinh_basic(basic p1) -> function"""
    return _swiginac.asinh_basic(*args)

def asinh_int(*args):
    """asinh_int(int p1) -> function"""
    return _swiginac.asinh_int(*args)

def asinh_double(*args):
    """asinh_double(double p1) -> function"""
    return _swiginac.asinh_double(*args)
def asinh(x):
    if isinstance(x,basic):
        return asinh_basic(x).eval()
    elif isinstance(x,int):
        return asinh_int(x).eval()
    elif isinstance(x,float):
        return asinh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class acosh_SERIAL(_object):
    """Proxy of C++ acosh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acosh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::acosh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> acosh_SERIAL"""
        _swig_setattr(self, acosh_SERIAL, 'this', _swiginac.new_acosh_SERIAL(*args))
        _swig_setattr(self, acosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_acosh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class acosh_SERIALPtr(acosh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, acosh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, acosh_SERIAL, 'thisown', 0)
        _swig_setattr(self, acosh_SERIAL,self.__class__,acosh_SERIAL)
_swiginac.acosh_SERIAL_swigregister(acosh_SERIALPtr)
asinh_NPARAMS = cvar.asinh_NPARAMS


def acosh_ex(*args):
    """acosh_ex(ex p1) -> function"""
    return _swiginac.acosh_ex(*args)

def acosh_basic(*args):
    """acosh_basic(basic p1) -> function"""
    return _swiginac.acosh_basic(*args)

def acosh_int(*args):
    """acosh_int(int p1) -> function"""
    return _swiginac.acosh_int(*args)

def acosh_double(*args):
    """acosh_double(double p1) -> function"""
    return _swiginac.acosh_double(*args)
def acosh(x):
    if isinstance(x,basic):
        return acosh_basic(x).eval()
    elif isinstance(x,int):
        return acosh_int(x).eval()
    elif isinstance(x,float):
        return acosh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class atanh_SERIAL(_object):
    """Proxy of C++ atanh_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atanh_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::atanh_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> atanh_SERIAL"""
        _swig_setattr(self, atanh_SERIAL, 'this', _swiginac.new_atanh_SERIAL(*args))
        _swig_setattr(self, atanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_atanh_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class atanh_SERIALPtr(atanh_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, atanh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atanh_SERIAL, 'thisown', 0)
        _swig_setattr(self, atanh_SERIAL,self.__class__,atanh_SERIAL)
_swiginac.atanh_SERIAL_swigregister(atanh_SERIALPtr)
acosh_NPARAMS = cvar.acosh_NPARAMS


def atanh_ex(*args):
    """atanh_ex(ex p1) -> function"""
    return _swiginac.atanh_ex(*args)

def atanh_basic(*args):
    """atanh_basic(basic p1) -> function"""
    return _swiginac.atanh_basic(*args)

def atanh_int(*args):
    """atanh_int(int p1) -> function"""
    return _swiginac.atanh_int(*args)

def atanh_double(*args):
    """atanh_double(double p1) -> function"""
    return _swiginac.atanh_double(*args)
def atanh(x):
    if isinstance(x,basic):
        return atanh_basic(x).eval()
    elif isinstance(x,int):
        return atanh_int(x).eval()
    elif isinstance(x,float):
        return atanh_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class Li2_SERIAL(_object):
    """Proxy of C++ Li2_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li2_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::Li2_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> Li2_SERIAL"""
        _swig_setattr(self, Li2_SERIAL, 'this', _swiginac.new_Li2_SERIAL(*args))
        _swig_setattr(self, Li2_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_Li2_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class Li2_SERIALPtr(Li2_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, Li2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Li2_SERIAL, 'thisown', 0)
        _swig_setattr(self, Li2_SERIAL,self.__class__,Li2_SERIAL)
_swiginac.Li2_SERIAL_swigregister(Li2_SERIALPtr)
atanh_NPARAMS = cvar.atanh_NPARAMS


def Li2_ex(*args):
    """Li2_ex(ex p1) -> function"""
    return _swiginac.Li2_ex(*args)

def Li2_basic(*args):
    """Li2_basic(basic p1) -> function"""
    return _swiginac.Li2_basic(*args)

def Li2_int(*args):
    """Li2_int(int p1) -> function"""
    return _swiginac.Li2_int(*args)

def Li2_double(*args):
    """Li2_double(double p1) -> function"""
    return _swiginac.Li2_double(*args)
def Li2(x):
    if isinstance(x,basic):
        return Li2_basic(x).eval()
    elif isinstance(x,int):
        return Li2_int(x).eval()
    elif isinstance(x,float):
        return Li2_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class Li3_SERIAL(_object):
    """Proxy of C++ Li3_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li3_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li3_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::Li3_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> Li3_SERIAL"""
        _swig_setattr(self, Li3_SERIAL, 'this', _swiginac.new_Li3_SERIAL(*args))
        _swig_setattr(self, Li3_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_Li3_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class Li3_SERIALPtr(Li3_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, Li3_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Li3_SERIAL, 'thisown', 0)
        _swig_setattr(self, Li3_SERIAL,self.__class__,Li3_SERIAL)
_swiginac.Li3_SERIAL_swigregister(Li3_SERIALPtr)
Li2_NPARAMS = cvar.Li2_NPARAMS


def Li3_ex(*args):
    """Li3_ex(ex p1) -> function"""
    return _swiginac.Li3_ex(*args)

def Li3_basic(*args):
    """Li3_basic(basic p1) -> function"""
    return _swiginac.Li3_basic(*args)

def Li3_int(*args):
    """Li3_int(int p1) -> function"""
    return _swiginac.Li3_int(*args)

def Li3_double(*args):
    """Li3_double(double p1) -> function"""
    return _swiginac.Li3_double(*args)
def Li3(x):
    if isinstance(x,basic):
        return Li3_basic(x).eval()
    elif isinstance(x,int):
        return Li3_int(x).eval()
    elif isinstance(x,float):
        return Li3_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class zetaderiv_SERIAL(_object):
    """Proxy of C++ zetaderiv_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zetaderiv_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zetaderiv_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::zetaderiv_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> zetaderiv_SERIAL"""
        _swig_setattr(self, zetaderiv_SERIAL, 'this', _swiginac.new_zetaderiv_SERIAL(*args))
        _swig_setattr(self, zetaderiv_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_zetaderiv_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class zetaderiv_SERIALPtr(zetaderiv_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, zetaderiv_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, zetaderiv_SERIAL, 'thisown', 0)
        _swig_setattr(self, zetaderiv_SERIAL,self.__class__,zetaderiv_SERIAL)
_swiginac.zetaderiv_SERIAL_swigregister(zetaderiv_SERIALPtr)
Li3_NPARAMS = cvar.Li3_NPARAMS

class Li_SERIAL(_object):
    """Proxy of C++ Li_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::Li_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> Li_SERIAL"""
        _swig_setattr(self, Li_SERIAL, 'this', _swiginac.new_Li_SERIAL(*args))
        _swig_setattr(self, Li_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_Li_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class Li_SERIALPtr(Li_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, Li_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Li_SERIAL, 'thisown', 0)
        _swig_setattr(self, Li_SERIAL,self.__class__,Li_SERIAL)
_swiginac.Li_SERIAL_swigregister(Li_SERIALPtr)
zetaderiv_NPARAMS = cvar.zetaderiv_NPARAMS

class S_SERIAL(_object):
    """Proxy of C++ S_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, S_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, S_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::S_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> S_SERIAL"""
        _swig_setattr(self, S_SERIAL, 'this', _swiginac.new_S_SERIAL(*args))
        _swig_setattr(self, S_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_S_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class S_SERIALPtr(S_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, S_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, S_SERIAL, 'thisown', 0)
        _swig_setattr(self, S_SERIAL,self.__class__,S_SERIAL)
_swiginac.S_SERIAL_swigregister(S_SERIALPtr)
Li_NPARAMS = cvar.Li_NPARAMS

class H_SERIAL(_object):
    """Proxy of C++ H_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, H_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, H_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::H_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> H_SERIAL"""
        _swig_setattr(self, H_SERIAL, 'this', _swiginac.new_H_SERIAL(*args))
        _swig_setattr(self, H_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_H_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class H_SERIALPtr(H_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, H_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, H_SERIAL, 'thisown', 0)
        _swig_setattr(self, H_SERIAL,self.__class__,H_SERIAL)
_swiginac.H_SERIAL_swigregister(H_SERIALPtr)
S_NPARAMS = cvar.S_NPARAMS

class lgamma_SERIAL(_object):
    """Proxy of C++ lgamma_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lgamma_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::lgamma_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> lgamma_SERIAL"""
        _swig_setattr(self, lgamma_SERIAL, 'this', _swiginac.new_lgamma_SERIAL(*args))
        _swig_setattr(self, lgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_lgamma_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class lgamma_SERIALPtr(lgamma_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, lgamma_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, lgamma_SERIAL, 'thisown', 0)
        _swig_setattr(self, lgamma_SERIAL,self.__class__,lgamma_SERIAL)
_swiginac.lgamma_SERIAL_swigregister(lgamma_SERIALPtr)
H_NPARAMS = cvar.H_NPARAMS


def lgamma_ex(*args):
    """lgamma_ex(ex p1) -> function"""
    return _swiginac.lgamma_ex(*args)

def lgamma_basic(*args):
    """lgamma_basic(basic p1) -> function"""
    return _swiginac.lgamma_basic(*args)

def lgamma_int(*args):
    """lgamma_int(int p1) -> function"""
    return _swiginac.lgamma_int(*args)

def lgamma_double(*args):
    """lgamma_double(double p1) -> function"""
    return _swiginac.lgamma_double(*args)
def lgamma(x):
    if isinstance(x,basic):
        return lgamma_basic(x).eval()
    elif isinstance(x,int):
        return lgamma_int(x).eval()
    elif isinstance(x,float):
        return lgamma_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class tgamma_SERIAL(_object):
    """Proxy of C++ tgamma_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tgamma_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tgamma_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> tgamma_SERIAL"""
        _swig_setattr(self, tgamma_SERIAL, 'this', _swiginac.new_tgamma_SERIAL(*args))
        _swig_setattr(self, tgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_tgamma_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tgamma_SERIALPtr(tgamma_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, tgamma_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tgamma_SERIAL, 'thisown', 0)
        _swig_setattr(self, tgamma_SERIAL,self.__class__,tgamma_SERIAL)
_swiginac.tgamma_SERIAL_swigregister(tgamma_SERIALPtr)
lgamma_NPARAMS = cvar.lgamma_NPARAMS


def tgamma_ex(*args):
    """tgamma_ex(ex p1) -> function"""
    return _swiginac.tgamma_ex(*args)

def tgamma_basic(*args):
    """tgamma_basic(basic p1) -> function"""
    return _swiginac.tgamma_basic(*args)

def tgamma_int(*args):
    """tgamma_int(int p1) -> function"""
    return _swiginac.tgamma_int(*args)

def tgamma_double(*args):
    """tgamma_double(double p1) -> function"""
    return _swiginac.tgamma_double(*args)
def tgamma(x):
    if isinstance(x,basic):
        return tgamma_basic(x).eval()
    elif isinstance(x,int):
        return tgamma_int(x).eval()
    elif isinstance(x,float):
        return tgamma_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class beta_SERIAL(_object):
    """Proxy of C++ beta_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, beta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, beta_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::beta_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> beta_SERIAL"""
        _swig_setattr(self, beta_SERIAL, 'this', _swiginac.new_beta_SERIAL(*args))
        _swig_setattr(self, beta_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_beta_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class beta_SERIALPtr(beta_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, beta_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, beta_SERIAL, 'thisown', 0)
        _swig_setattr(self, beta_SERIAL,self.__class__,beta_SERIAL)
_swiginac.beta_SERIAL_swigregister(beta_SERIALPtr)
tgamma_NPARAMS = cvar.tgamma_NPARAMS

class factorial_SERIAL(_object):
    """Proxy of C++ factorial_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, factorial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, factorial_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::factorial_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> factorial_SERIAL"""
        _swig_setattr(self, factorial_SERIAL, 'this', _swiginac.new_factorial_SERIAL(*args))
        _swig_setattr(self, factorial_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_factorial_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class factorial_SERIALPtr(factorial_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, factorial_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, factorial_SERIAL, 'thisown', 0)
        _swig_setattr(self, factorial_SERIAL,self.__class__,factorial_SERIAL)
_swiginac.factorial_SERIAL_swigregister(factorial_SERIALPtr)
beta_NPARAMS = cvar.beta_NPARAMS


def factorial_ex(*args):
    """factorial_ex(ex p1) -> function"""
    return _swiginac.factorial_ex(*args)

def factorial_basic(*args):
    """factorial_basic(basic p1) -> function"""
    return _swiginac.factorial_basic(*args)

def factorial_int(*args):
    """factorial_int(int p1) -> function"""
    return _swiginac.factorial_int(*args)

def factorial_double(*args):
    """factorial_double(double p1) -> function"""
    return _swiginac.factorial_double(*args)
def factorial(x):
    if isinstance(x,basic):
        return factorial_basic(x).eval()
    elif isinstance(x,int):
        return factorial_int(x).eval()
    elif isinstance(x,float):
        return factorial_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class binomial_SERIAL(_object):
    """Proxy of C++ binomial_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, binomial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, binomial_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::binomial_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> binomial_SERIAL"""
        _swig_setattr(self, binomial_SERIAL, 'this', _swiginac.new_binomial_SERIAL(*args))
        _swig_setattr(self, binomial_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_binomial_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class binomial_SERIALPtr(binomial_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, binomial_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, binomial_SERIAL, 'thisown', 0)
        _swig_setattr(self, binomial_SERIAL,self.__class__,binomial_SERIAL)
_swiginac.binomial_SERIAL_swigregister(binomial_SERIALPtr)
factorial_NPARAMS = cvar.factorial_NPARAMS

class Order_SERIAL(_object):
    """Proxy of C++ Order_SERIAL class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Order_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Order_SERIAL, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::Order_SERIAL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self) -> Order_SERIAL"""
        _swig_setattr(self, Order_SERIAL, 'this', _swiginac.new_Order_SERIAL(*args))
        _swig_setattr(self, Order_SERIAL, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_Order_SERIAL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class Order_SERIALPtr(Order_SERIAL):
    def __init__(self, this):
        _swig_setattr(self, Order_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Order_SERIAL, 'thisown', 0)
        _swig_setattr(self, Order_SERIAL,self.__class__,Order_SERIAL)
_swiginac.Order_SERIAL_swigregister(Order_SERIALPtr)
binomial_NPARAMS = cvar.binomial_NPARAMS


def Order_ex(*args):
    """Order_ex(ex p1) -> function"""
    return _swiginac.Order_ex(*args)

def Order_basic(*args):
    """Order_basic(basic p1) -> function"""
    return _swiginac.Order_basic(*args)

def Order_int(*args):
    """Order_int(int p1) -> function"""
    return _swiginac.Order_int(*args)

def Order_double(*args):
    """Order_double(double p1) -> function"""
    return _swiginac.Order_double(*args)
def Order(x):
    if isinstance(x,basic):
        return Order_basic(x).eval()
    elif isinstance(x,int):
        return Order_int(x).eval()
    elif isinstance(x,float):
        return Order_double(x).eval()
    else:
        raise "Unimplented type. Fix in main.i."

class tensor(basic):
    """Proxy of C++ tensor class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, tensor, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, tensor, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tensor instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def replace_contr_index(*args):
        """replace_contr_index(self, exvector::iterator self, exvector::iterator other) -> bool"""
        return _swiginac.tensor_replace_contr_index(*args)

    def __del__(self, destroy=_swiginac.delete_tensor):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tensorPtr(tensor):
    def __init__(self, this):
        _swig_setattr(self, tensor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tensor, 'thisown', 0)
        _swig_setattr(self, tensor,self.__class__,tensor)
_swiginac.tensor_swigregister(tensorPtr)
Order_NPARAMS = cvar.Order_NPARAMS

def lsolve(*args):
    """
    lsolve(ex eqns, ex symbols, unsigned int options=solve_algo::automatic) -> ex
    lsolve(ex eqns, ex symbols) -> ex
    """
    return _swiginac.lsolve(*args)

class tensdelta(tensor):
    """Proxy of C++ tensdelta class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, tensdelta, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, tensdelta, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tensdelta instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.tensdelta_eval_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.tensdelta_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_tensdelta):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tensdeltaPtr(tensdelta):
    def __init__(self, this):
        _swig_setattr(self, tensdelta, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tensdelta, 'thisown', 0)
        _swig_setattr(self, tensdelta,self.__class__,tensdelta)
_swiginac.tensdelta_swigregister(tensdeltaPtr)

class tensmetric(tensor):
    """Proxy of C++ tensmetric class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, tensmetric, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, tensmetric, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tensmetric instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.tensmetric_eval_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.tensmetric_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_tensmetric):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tensmetricPtr(tensmetric):
    def __init__(self, this):
        _swig_setattr(self, tensmetric, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tensmetric, 'thisown', 0)
        _swig_setattr(self, tensmetric,self.__class__,tensmetric)
_swiginac.tensmetric_swigregister(tensmetricPtr)

class minkmetric(tensmetric):
    """Proxy of C++ minkmetric class"""
    __swig_setmethods__ = {}
    for _s in [tensmetric]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, minkmetric, name, value)
    __swig_getmethods__ = {}
    for _s in [tensmetric]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, minkmetric, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::minkmetric instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, bool pos_sig) -> minkmetric"""
        _swig_setattr(self, minkmetric, 'this', _swiginac.new_minkmetric(*args))
        _swig_setattr(self, minkmetric, 'thisown', 1)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.minkmetric_eval_indexed(*args)

    def __del__(self, destroy=_swiginac.delete_minkmetric):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class minkmetricPtr(minkmetric):
    def __init__(self, this):
        _swig_setattr(self, minkmetric, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, minkmetric, 'thisown', 0)
        _swig_setattr(self, minkmetric,self.__class__,minkmetric)
_swiginac.minkmetric_swigregister(minkmetricPtr)

class spinmetric(tensmetric):
    """Proxy of C++ spinmetric class"""
    __swig_setmethods__ = {}
    for _s in [tensmetric]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, spinmetric, name, value)
    __swig_getmethods__ = {}
    for _s in [tensmetric]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, spinmetric, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::spinmetric instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.spinmetric_eval_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.spinmetric_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_spinmetric):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class spinmetricPtr(spinmetric):
    def __init__(self, this):
        _swig_setattr(self, spinmetric, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, spinmetric, 'thisown', 0)
        _swig_setattr(self, spinmetric,self.__class__,spinmetric)
_swiginac.spinmetric_swigregister(spinmetricPtr)

class tensepsilon(tensor):
    """Proxy of C++ tensepsilon class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, tensepsilon, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, tensepsilon, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::tensepsilon instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, bool minkowski, bool pos_sig) -> tensepsilon"""
        _swig_setattr(self, tensepsilon, 'this', _swiginac.new_tensepsilon(*args))
        _swig_setattr(self, tensepsilon, 'thisown', 1)
    def eval_indexed(*args):
        """eval_indexed(self, basic i) -> ex"""
        return _swiginac.tensepsilon_eval_indexed(*args)

    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.tensepsilon_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_tensepsilon):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class tensepsilonPtr(tensepsilon):
    def __init__(self, this):
        _swig_setattr(self, tensepsilon, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tensepsilon, 'thisown', 0)
        _swig_setattr(self, tensepsilon,self.__class__,tensepsilon)
_swiginac.tensepsilon_swigregister(tensepsilonPtr)


def delta_tensor(*args):
    """delta_tensor(ex i1, ex i2) -> ex"""
    return _swiginac.delta_tensor(*args)

def metric_tensor(*args):
    """metric_tensor(ex i1, ex i2) -> ex"""
    return _swiginac.metric_tensor(*args)

def spinor_metric(*args):
    """spinor_metric(ex i1, ex i2) -> ex"""
    return _swiginac.spinor_metric(*args)
class indexed(basic):
    """Proxy of C++ indexed class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, indexed, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, indexed, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::indexed instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex b) -> indexed
        __init__(self, ex b, ex i1) -> indexed
        __init__(self, ex b, ex i1, ex i2) -> indexed
        __init__(self, ex b, ex i1, ex i2, ex i3) -> indexed
        __init__(self, ex b, ex i1, ex i2, ex i3, ex i4) -> indexed
        __init__(self, ex b, symmetry symm, ex i1, ex i2) -> indexed
        __init__(self, ex b, symmetry symm, ex i1, ex i2, ex i3) -> indexed
        __init__(self, ex b, symmetry symm, ex i1, ex i2, ex i3, ex i4) -> indexed
        __init__(self, ex b, exvector iv) -> indexed
        __init__(self, ex b, symmetry symm, exvector iv) -> indexed
        __init__(self, symmetry symm, exprseq es) -> indexed
        __init__(self, symmetry symm, exvector v, bool discardable=False) -> indexed
        __init__(self, symmetry symm, exvector v) -> indexed
        """
        _swig_setattr(self, indexed, 'this', _swiginac.new_indexed(*args))
        _swig_setattr(self, indexed, 'thisown', 1)
    def get_free_indices(*args):
        """get_free_indices(self) -> exvector"""
        return _swiginac.indexed_get_free_indices(*args)

    def all_index_values_are(*args):
        """all_index_values_are(self, unsigned int inf) -> bool"""
        return _swiginac.indexed_all_index_values_are(*args)

    def get_indices(*args):
        """get_indices(self) -> exvector"""
        return _swiginac.indexed_get_indices(*args)

    def get_dummy_indices(*args):
        """
        get_dummy_indices(self) -> exvector
        get_dummy_indices(self, indexed other) -> exvector
        """
        return _swiginac.indexed_get_dummy_indices(*args)

    def has_dummy_index_for(*args):
        """has_dummy_index_for(self, ex i) -> bool"""
        return _swiginac.indexed_has_dummy_index_for(*args)

    def get_symmetry(*args):
        """get_symmetry(self) -> ex"""
        return _swiginac.indexed_get_symmetry(*args)

    def __del__(self, destroy=_swiginac.delete_indexed):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class indexedPtr(indexed):
    def __init__(self, this):
        _swig_setattr(self, indexed, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, indexed, 'thisown', 0)
        _swig_setattr(self, indexed,self.__class__,indexed)
_swiginac.indexed_swigregister(indexedPtr)

def lorentz_g(*args):
    """
    lorentz_g(ex i1, ex i2, bool pos_sig=False) -> ex
    lorentz_g(ex i1, ex i2) -> ex
    """
    return _swiginac.lorentz_g(*args)

def epsilon_tensor(*args):
    """
    epsilon_tensor(ex i1, ex i2) -> ex
    epsilon_tensor(ex i1, ex i2, ex i3) -> ex
    """
    return _swiginac.epsilon_tensor(*args)

def lorentz_eps(*args):
    """
    lorentz_eps(ex i1, ex i2, ex i3, ex i4, bool pos_sig=False) -> ex
    lorentz_eps(ex i1, ex i2, ex i3, ex i4) -> ex
    """
    return _swiginac.lorentz_eps(*args)

class spmapkey(_object):
    """Proxy of C++ spmapkey class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, spmapkey, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, spmapkey, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::spmapkey instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self) -> spmapkey
        __init__(self, ex v1, ex v2, ex dim=wild()) -> spmapkey
        __init__(self, ex v1, ex v2) -> spmapkey
        """
        _swig_setattr(self, spmapkey, 'this', _swiginac.new_spmapkey(*args))
        _swig_setattr(self, spmapkey, 'thisown', 1)
    def __eq__(*args):
        """__eq__(self, spmapkey other) -> bool"""
        return _swiginac.spmapkey___eq__(*args)

    def __lt__(*args):
        """__lt__(self, spmapkey other) -> bool"""
        return _swiginac.spmapkey___lt__(*args)

    def debugprint(*args):
        """debugprint(self)"""
        return _swiginac.spmapkey_debugprint(*args)

    def __del__(self, destroy=_swiginac.delete_spmapkey):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class spmapkeyPtr(spmapkey):
    def __init__(self, this):
        _swig_setattr(self, spmapkey, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, spmapkey, 'thisown', 0)
        _swig_setattr(self, spmapkey,self.__class__,spmapkey)
_swiginac.spmapkey_swigregister(spmapkeyPtr)

class scalar_products(_object):
    """Proxy of C++ scalar_products class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, scalar_products, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, scalar_products, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::scalar_products instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def add(*args):
        """
        add(self, ex v1, ex v2, ex sp)
        add(self, ex v1, ex v2, ex dim, ex sp)
        """
        return _swiginac.scalar_products_add(*args)

    def add_vectors(*args):
        """
        add_vectors(self, lst l, ex dim=wild())
        add_vectors(self, lst l)
        """
        return _swiginac.scalar_products_add_vectors(*args)

    def clear(*args):
        """clear(self)"""
        return _swiginac.scalar_products_clear(*args)

    def is_defined(*args):
        """is_defined(self, ex v1, ex v2, ex dim) -> bool"""
        return _swiginac.scalar_products_is_defined(*args)

    def evaluate(*args):
        """evaluate(self, ex v1, ex v2, ex dim) -> ex"""
        return _swiginac.scalar_products_evaluate(*args)

    def debugprint(*args):
        """debugprint(self)"""
        return _swiginac.scalar_products_debugprint(*args)

    def __init__(self, *args):
        """__init__(self) -> scalar_products"""
        _swig_setattr(self, scalar_products, 'this', _swiginac.new_scalar_products(*args))
        _swig_setattr(self, scalar_products, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_scalar_products):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class scalar_productsPtr(scalar_products):
    def __init__(self, this):
        _swig_setattr(self, scalar_products, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, scalar_products, 'thisown', 0)
        _swig_setattr(self, scalar_products,self.__class__,scalar_products)
_swiginac.scalar_products_swigregister(scalar_productsPtr)


def get_all_dummy_indices(*args):
    """get_all_dummy_indices(ex e) -> exvector"""
    return _swiginac.get_all_dummy_indices(*args)

def rename_dummy_indices_uniquely(*args):
    """rename_dummy_indices_uniquely(ex a, ex b) -> ex"""
    return _swiginac.rename_dummy_indices_uniquely(*args)
class idx(basic):
    """Proxy of C++ idx class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, idx, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, idx, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::idx instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, ex v, ex dim) -> idx"""
        _swig_setattr(self, idx, 'this', _swiginac.new_idx(*args))
        _swig_setattr(self, idx, 'thisown', 1)
    def is_dummy_pair_same_type(*args):
        """is_dummy_pair_same_type(self, basic other) -> bool"""
        return _swiginac.idx_is_dummy_pair_same_type(*args)

    def get_value(*args):
        """get_value(self) -> ex"""
        return _swiginac.idx_get_value(*args)

    def is_numeric(*args):
        """is_numeric(self) -> bool"""
        return _swiginac.idx_is_numeric(*args)

    def is_symbolic(*args):
        """is_symbolic(self) -> bool"""
        return _swiginac.idx_is_symbolic(*args)

    def get_dim(*args):
        """get_dim(self) -> ex"""
        return _swiginac.idx_get_dim(*args)

    def is_dim_numeric(*args):
        """is_dim_numeric(self) -> bool"""
        return _swiginac.idx_is_dim_numeric(*args)

    def is_dim_symbolic(*args):
        """is_dim_symbolic(self) -> bool"""
        return _swiginac.idx_is_dim_symbolic(*args)

    def replace_dim(*args):
        """replace_dim(self, ex new_dim) -> ex"""
        return _swiginac.idx_replace_dim(*args)

    def minimal_dim(*args):
        """minimal_dim(self, idx other) -> ex"""
        return _swiginac.idx_minimal_dim(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_idx):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class idxPtr(idx):
    def __init__(self, this):
        _swig_setattr(self, idx, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, idx, 'thisown', 0)
        _swig_setattr(self, idx,self.__class__,idx)
_swiginac.idx_swigregister(idxPtr)

def expand_dummy_sum(*args):
    """
    expand_dummy_sum(ex e, bool subs_idx=False) -> ex
    expand_dummy_sum(ex e) -> ex
    """
    return _swiginac.expand_dummy_sum(*args)

class varidx(idx):
    """Proxy of C++ varidx class"""
    __swig_setmethods__ = {}
    for _s in [idx]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, varidx, name, value)
    __swig_getmethods__ = {}
    for _s in [idx]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, varidx, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::varidx instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex v, ex dim, bool covariant=False) -> varidx
        __init__(self, ex v, ex dim) -> varidx
        """
        _swig_setattr(self, varidx, 'this', _swiginac.new_varidx(*args))
        _swig_setattr(self, varidx, 'thisown', 1)
    def is_dummy_pair_same_type(*args):
        """is_dummy_pair_same_type(self, basic other) -> bool"""
        return _swiginac.varidx_is_dummy_pair_same_type(*args)

    def is_covariant(*args):
        """is_covariant(self) -> bool"""
        return _swiginac.varidx_is_covariant(*args)

    def is_contravariant(*args):
        """is_contravariant(self) -> bool"""
        return _swiginac.varidx_is_contravariant(*args)

    def toggle_variance(*args):
        """toggle_variance(self) -> ex"""
        return _swiginac.varidx_toggle_variance(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_varidx):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class varidxPtr(varidx):
    def __init__(self, this):
        _swig_setattr(self, varidx, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, varidx, 'thisown', 0)
        _swig_setattr(self, varidx,self.__class__,varidx)
_swiginac.varidx_swigregister(varidxPtr)

class spinidx(varidx):
    """Proxy of C++ spinidx class"""
    __swig_setmethods__ = {}
    for _s in [varidx]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, spinidx, name, value)
    __swig_getmethods__ = {}
    for _s in [varidx]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, spinidx, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::spinidx instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex v, ex dim=2, bool covariant=False, bool dotted=False) -> spinidx
        __init__(self, ex v, ex dim=2, bool covariant=False) -> spinidx
        __init__(self, ex v, ex dim=2) -> spinidx
        __init__(self, ex v) -> spinidx
        """
        _swig_setattr(self, spinidx, 'this', _swiginac.new_spinidx(*args))
        _swig_setattr(self, spinidx, 'thisown', 1)
    def is_dummy_pair_same_type(*args):
        """is_dummy_pair_same_type(self, basic other) -> bool"""
        return _swiginac.spinidx_is_dummy_pair_same_type(*args)

    def is_dotted(*args):
        """is_dotted(self) -> bool"""
        return _swiginac.spinidx_is_dotted(*args)

    def is_undotted(*args):
        """is_undotted(self) -> bool"""
        return _swiginac.spinidx_is_undotted(*args)

    def toggle_dot(*args):
        """toggle_dot(self) -> ex"""
        return _swiginac.spinidx_toggle_dot(*args)

    def toggle_variance_dot(*args):
        """toggle_variance_dot(self) -> ex"""
        return _swiginac.spinidx_toggle_variance_dot(*args)

    def __del__(self, destroy=_swiginac.delete_spinidx):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class spinidxPtr(spinidx):
    def __init__(self, this):
        _swig_setattr(self, spinidx, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, spinidx, 'thisown', 0)
        _swig_setattr(self, spinidx,self.__class__,spinidx)
_swiginac.spinidx_swigregister(spinidxPtr)


def find_dummy_indices(*args):
    """find_dummy_indices(exvector v, exvector out_dummy)"""
    return _swiginac.find_dummy_indices(*args)

def count_dummy_indices(*args):
    """count_dummy_indices(exvector v) -> size_t"""
    return _swiginac.count_dummy_indices(*args)

def count_free_indices(*args):
    """count_free_indices(exvector v) -> size_t"""
    return _swiginac.count_free_indices(*args)

def minimal_dim(*args):
    """minimal_dim(ex dim1, ex dim2) -> ex"""
    return _swiginac.minimal_dim(*args)
class symmetry(basic):
    """Proxy of C++ symmetry class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, symmetry, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, symmetry, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::symmetry instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    none = _swiginac.symmetry_none
    symmetric = _swiginac.symmetry_symmetric
    antisymmetric = _swiginac.symmetry_antisymmetric
    cyclic = _swiginac.symmetry_cyclic
    def __init__(self, *args):
        """
        __init__(self, unsigned int i) -> symmetry
        __init__(self, symmetry_type t, symmetry c1, symmetry c2) -> symmetry
        """
        _swig_setattr(self, symmetry, 'this', _swiginac.new_symmetry(*args))
        _swig_setattr(self, symmetry, 'thisown', 1)
    def get_type(*args):
        """get_type(self) -> int"""
        return _swiginac.symmetry_get_type(*args)

    def set_type(*args):
        """set_type(self, symmetry_type t)"""
        return _swiginac.symmetry_set_type(*args)

    def add(*args):
        """
        add(self, symmetry c) -> symmetry
        add(self, unsigned int c) -> symmetry
        """
        return _swiginac.symmetry_add(*args)

    def validate(*args):
        """validate(self, unsigned int n)"""
        return _swiginac.symmetry_validate(*args)

    def has_symmetry(*args):
        """has_symmetry(self) -> bool"""
        return _swiginac.symmetry_has_symmetry(*args)

    def __del__(self, destroy=_swiginac.delete_symmetry):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class symmetryPtr(symmetry):
    def __init__(self, this):
        _swig_setattr(self, symmetry, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, symmetry, 'thisown', 0)
        _swig_setattr(self, symmetry,self.__class__,symmetry)
_swiginac.symmetry_swigregister(symmetryPtr)

def is_dummy_pair(*args):
    """
    is_dummy_pair(idx i1, idx i2) -> bool
    is_dummy_pair(ex e1, ex e2) -> bool
    """
    return _swiginac.is_dummy_pair(*args)

def find_free_and_dummy(*args):
    """
    find_free_and_dummy(exvector::const_iterator it, exvector::const_iterator itend, 
        exvector out_free, exvector out_dummy)
    find_free_and_dummy(exvector v, exvector out_free, exvector out_dummy)
    """
    return _swiginac.find_free_and_dummy(*args)


def not_symmetric(*args):
    """not_symmetric() -> symmetry"""
    return _swiginac.not_symmetric(*args)

def symmetric2(*args):
    """symmetric2() -> symmetry"""
    return _swiginac.symmetric2(*args)

def symmetric3(*args):
    """symmetric3() -> symmetry"""
    return _swiginac.symmetric3(*args)

def symmetric4(*args):
    """symmetric4() -> symmetry"""
    return _swiginac.symmetric4(*args)

def antisymmetric2(*args):
    """antisymmetric2() -> symmetry"""
    return _swiginac.antisymmetric2(*args)

def antisymmetric3(*args):
    """antisymmetric3() -> symmetry"""
    return _swiginac.antisymmetric3(*args)

def antisymmetric4(*args):
    """antisymmetric4() -> symmetry"""
    return _swiginac.antisymmetric4(*args)

def canonicalize(*args):
    """canonicalize(exvector::iterator v, symmetry symm) -> int"""
    return _swiginac.canonicalize(*args)
class clifford(indexed):
    """Proxy of C++ clifford class"""
    __swig_setmethods__ = {}
    for _s in [indexed]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, clifford, name, value)
    __swig_getmethods__ = {}
    for _s in [indexed]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, clifford, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::clifford instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """
        __init__(self, ex b, unsigned char rl=0) -> clifford
        __init__(self, ex b) -> clifford
        __init__(self, ex b, ex mu, ex metr, unsigned char rl=0) -> clifford
        __init__(self, ex b, ex mu, ex metr) -> clifford
        """
        _swig_setattr(self, clifford, 'this', _swiginac.new_clifford(*args))
        _swig_setattr(self, clifford, 'thisown', 1)
    def precedence(*args):
        """precedence(self) -> unsigned int"""
        return _swiginac.clifford_precedence(*args)

    def get_representation_label(*args):
        """get_representation_label(self) -> unsigned char"""
        return _swiginac.clifford_get_representation_label(*args)

    def get_metric(*args):
        """
        get_metric(self) -> ex
        get_metric(self, ex i, ex j) -> ex
        """
        return _swiginac.clifford_get_metric(*args)

    def same_metric(*args):
        """same_metric(self, ex other) -> bool"""
        return _swiginac.clifford_same_metric(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_clifford):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class cliffordPtr(clifford):
    def __init__(self, this):
        _swig_setattr(self, clifford, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, clifford, 'thisown', 0)
        _swig_setattr(self, clifford,self.__class__,clifford)
_swiginac.clifford_swigregister(cliffordPtr)

def sy_none(*args):
    """
    sy_none() -> symmetry
    sy_none(symmetry c1, symmetry c2) -> symmetry
    sy_none(symmetry c1, symmetry c2, symmetry c3) -> symmetry
    sy_none(symmetry c1, symmetry c2, symmetry c3, symmetry c4) -> symmetry
    """
    return _swiginac.sy_none(*args)

def sy_symm(*args):
    """
    sy_symm() -> symmetry
    sy_symm(symmetry c1, symmetry c2) -> symmetry
    sy_symm(symmetry c1, symmetry c2, symmetry c3) -> symmetry
    sy_symm(symmetry c1, symmetry c2, symmetry c3, symmetry c4) -> symmetry
    """
    return _swiginac.sy_symm(*args)

def sy_anti(*args):
    """
    sy_anti() -> symmetry
    sy_anti(symmetry c1, symmetry c2) -> symmetry
    sy_anti(symmetry c1, symmetry c2, symmetry c3) -> symmetry
    sy_anti(symmetry c1, symmetry c2, symmetry c3, symmetry c4) -> symmetry
    """
    return _swiginac.sy_anti(*args)

def sy_cycl(*args):
    """
    sy_cycl() -> symmetry
    sy_cycl(symmetry c1, symmetry c2) -> symmetry
    sy_cycl(symmetry c1, symmetry c2, symmetry c3) -> symmetry
    sy_cycl(symmetry c1, symmetry c2, symmetry c3, symmetry c4) -> symmetry
    """
    return _swiginac.sy_cycl(*args)

def symmetrize(*args):
    """
    symmetrize(ex thisex) -> ex
    symmetrize(ex thisex, lst l) -> ex
    symmetrize(ex e, exvector::const_iterator first, exvector::const_iterator last) -> ex
    symmetrize(ex e, exvector v) -> ex
    """
    return _swiginac.symmetrize(*args)

def antisymmetrize(*args):
    """
    antisymmetrize(ex thisex) -> ex
    antisymmetrize(ex thisex, lst l) -> ex
    antisymmetrize(ex e, exvector::const_iterator first, exvector::const_iterator last) -> ex
    antisymmetrize(ex e, exvector v) -> ex
    """
    return _swiginac.antisymmetrize(*args)

def symmetrize_cyclic(*args):
    """
    symmetrize_cyclic(ex thisex) -> ex
    symmetrize_cyclic(ex thisex, lst l) -> ex
    symmetrize_cyclic(ex e, exvector::const_iterator first, exvector::const_iterator last) -> ex
    symmetrize_cyclic(ex e, exvector v) -> ex
    """
    return _swiginac.symmetrize_cyclic(*args)

class diracone(tensor):
    """Proxy of C++ diracone class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, diracone, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, diracone, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::diracone instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_swiginac.delete_diracone):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class diraconePtr(diracone):
    def __init__(self, this):
        _swig_setattr(self, diracone, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, diracone, 'thisown', 0)
        _swig_setattr(self, diracone,self.__class__,diracone)
_swiginac.diracone_swigregister(diraconePtr)

class cliffordunit(tensor):
    """Proxy of C++ cliffordunit class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, cliffordunit, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, cliffordunit, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::cliffordunit instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.cliffordunit_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_cliffordunit):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class cliffordunitPtr(cliffordunit):
    def __init__(self, this):
        _swig_setattr(self, cliffordunit, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cliffordunit, 'thisown', 0)
        _swig_setattr(self, cliffordunit,self.__class__,cliffordunit)
_swiginac.cliffordunit_swigregister(cliffordunitPtr)

class diracgamma(cliffordunit):
    """Proxy of C++ diracgamma class"""
    __swig_setmethods__ = {}
    for _s in [cliffordunit]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, diracgamma, name, value)
    __swig_getmethods__ = {}
    for _s in [cliffordunit]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, diracgamma, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::diracgamma instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def contract_with(*args):
        """
        contract_with(self, exvector::iterator self, exvector::iterator other, 
            exvector v) -> bool
        """
        return _swiginac.diracgamma_contract_with(*args)

    def __del__(self, destroy=_swiginac.delete_diracgamma):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class diracgammaPtr(diracgamma):
    def __init__(self, this):
        _swig_setattr(self, diracgamma, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, diracgamma, 'thisown', 0)
        _swig_setattr(self, diracgamma,self.__class__,diracgamma)
_swiginac.diracgamma_swigregister(diracgammaPtr)

class diracgamma5(tensor):
    """Proxy of C++ diracgamma5 class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, diracgamma5, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, diracgamma5, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::diracgamma5 instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_swiginac.delete_diracgamma5):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class diracgamma5Ptr(diracgamma5):
    def __init__(self, this):
        _swig_setattr(self, diracgamma5, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, diracgamma5, 'thisown', 0)
        _swig_setattr(self, diracgamma5,self.__class__,diracgamma5)
_swiginac.diracgamma5_swigregister(diracgamma5Ptr)

class diracgammaL(tensor):
    """Proxy of C++ diracgammaL class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, diracgammaL, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, diracgammaL, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::diracgammaL instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_swiginac.delete_diracgammaL):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class diracgammaLPtr(diracgammaL):
    def __init__(self, this):
        _swig_setattr(self, diracgammaL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, diracgammaL, 'thisown', 0)
        _swig_setattr(self, diracgammaL,self.__class__,diracgammaL)
_swiginac.diracgammaL_swigregister(diracgammaLPtr)

class diracgammaR(tensor):
    """Proxy of C++ diracgammaR class"""
    __swig_setmethods__ = {}
    for _s in [tensor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, diracgammaR, name, value)
    __swig_getmethods__ = {}
    for _s in [tensor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, diracgammaR, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::diracgammaR instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_swiginac.delete_diracgammaR):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class diracgammaRPtr(diracgammaR):
    def __init__(self, this):
        _swig_setattr(self, diracgammaR, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, diracgammaR, 'thisown', 0)
        _swig_setattr(self, diracgammaR,self.__class__,diracgammaR)
_swiginac.diracgammaR_swigregister(diracgammaRPtr)


def canonicalize_clifford(*args):
    """canonicalize_clifford(ex e) -> ex"""
    return _swiginac.canonicalize_clifford(*args)

def clifford_prime(*args):
    """clifford_prime(ex e) -> ex"""
    return _swiginac.clifford_prime(*args)

def clifford_bar(*args):
    """clifford_bar(ex e) -> ex"""
    return _swiginac.clifford_bar(*args)

def clifford_star(*args):
    """clifford_star(ex e) -> ex"""
    return _swiginac.clifford_star(*args)

def clifford_norm(*args):
    """clifford_norm(ex e) -> ex"""
    return _swiginac.clifford_norm(*args)

def clifford_inverse(*args):
    """clifford_inverse(ex e) -> ex"""
    return _swiginac.clifford_inverse(*args)
class wildcard(basic):
    """Proxy of C++ wildcard class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, wildcard, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, wildcard, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::wildcard instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, unsigned int label) -> wildcard"""
        _swig_setattr(self, wildcard, 'this', _swiginac.new_wildcard(*args))
        _swig_setattr(self, wildcard, 'thisown', 1)
    def get_label(*args):
        """get_label(self) -> unsigned int"""
        return _swiginac.wildcard_get_label(*args)

    def __del__(self, destroy=_swiginac.delete_wildcard):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class wildcardPtr(wildcard):
    def __init__(self, this):
        _swig_setattr(self, wildcard, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, wildcard, 'thisown', 0)
        _swig_setattr(self, wildcard,self.__class__,wildcard)
_swiginac.wildcard_swigregister(wildcardPtr)

def dirac_ONE(*args):
    """
    dirac_ONE(unsigned char rl=0) -> ex
    dirac_ONE() -> ex
    """
    return _swiginac.dirac_ONE(*args)

def clifford_unit(*args):
    """
    clifford_unit(ex mu, ex metr, unsigned char rl=0) -> ex
    clifford_unit(ex mu, ex metr) -> ex
    """
    return _swiginac.clifford_unit(*args)

def dirac_gamma(*args):
    """
    dirac_gamma(ex mu, unsigned char rl=0) -> ex
    dirac_gamma(ex mu) -> ex
    """
    return _swiginac.dirac_gamma(*args)

def dirac_gamma5(*args):
    """
    dirac_gamma5(unsigned char rl=0) -> ex
    dirac_gamma5() -> ex
    """
    return _swiginac.dirac_gamma5(*args)

def dirac_gammaL(*args):
    """
    dirac_gammaL(unsigned char rl=0) -> ex
    dirac_gammaL() -> ex
    """
    return _swiginac.dirac_gammaL(*args)

def dirac_gammaR(*args):
    """
    dirac_gammaR(unsigned char rl=0) -> ex
    dirac_gammaR() -> ex
    """
    return _swiginac.dirac_gammaR(*args)

def dirac_slash(*args):
    """
    dirac_slash(ex e, ex dim, unsigned char rl=0) -> ex
    dirac_slash(ex e, ex dim) -> ex
    """
    return _swiginac.dirac_slash(*args)

def dirac_trace(*args):
    """
    dirac_trace(ex e, lst rll, ex trONE=4) -> ex
    dirac_trace(ex e, lst rll) -> ex
    """
    return _swiginac.dirac_trace(*args)

def remove_dirac_ONE(*args):
    """
    remove_dirac_ONE(ex e) -> ex
    remove_dirac_ONE(ex e, unsigned char rl) -> ex
    """
    return _swiginac.remove_dirac_ONE(*args)

def lst_to_clifford(*args):
    """
    lst_to_clifford(ex v, ex mu, ex metr, unsigned char rl=0) -> ex
    lst_to_clifford(ex v, ex mu, ex metr) -> ex
    lst_to_clifford(ex v, ex e) -> ex
    """
    return _swiginac.lst_to_clifford(*args)

def clifford_to_lst(*args):
    """
    clifford_to_lst(ex e, ex c, bool algebraic=True) -> lst
    clifford_to_lst(ex e, ex c) -> lst
    """
    return _swiginac.clifford_to_lst(*args)

def clifford_moebius_map(*args):
    """
    clifford_moebius_map(ex a, ex b, ex c, ex d, ex v, ex G, unsigned char rl) -> ex
    clifford_moebius_map(ex a, ex b, ex c, ex d, ex v, ex G) -> ex
    clifford_moebius_map(ex M, ex v, ex G, unsigned char rl) -> ex
    clifford_moebius_map(ex M, ex v, ex G) -> ex
    """
    return _swiginac.clifford_moebius_map(*args)


def haswild(*args):
    """haswild(ex x) -> bool"""
    return _swiginac.haswild(*args)
class expand_options(_object):
    """Proxy of C++ expand_options class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, expand_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, expand_options, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::expand_options instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    expand_indexed = _swiginac.expand_options_expand_indexed
    expand_function_args = _swiginac.expand_options_expand_function_args
    def __init__(self, *args):
        """__init__(self) -> expand_options"""
        _swig_setattr(self, expand_options, 'this', _swiginac.new_expand_options(*args))
        _swig_setattr(self, expand_options, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_expand_options):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class expand_optionsPtr(expand_options):
    def __init__(self, this):
        _swig_setattr(self, expand_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, expand_options, 'thisown', 0)
        _swig_setattr(self, expand_options,self.__class__,expand_options)
_swiginac.expand_options_swigregister(expand_optionsPtr)

def wild(*args):
    """
    wild(unsigned int label=0) -> ex
    wild() -> ex
    """
    return _swiginac.wild(*args)

class subs_options(_object):
    """Proxy of C++ subs_options class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, subs_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, subs_options, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::subs_options instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    no_pattern = _swiginac.subs_options_no_pattern
    subs_no_pattern = _swiginac.subs_options_subs_no_pattern
    algebraic = _swiginac.subs_options_algebraic
    subs_algebraic = _swiginac.subs_options_subs_algebraic
    pattern_is_product = _swiginac.subs_options_pattern_is_product
    pattern_is_not_product = _swiginac.subs_options_pattern_is_not_product
    def __init__(self, *args):
        """__init__(self) -> subs_options"""
        _swig_setattr(self, subs_options, 'this', _swiginac.new_subs_options(*args))
        _swig_setattr(self, subs_options, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_subs_options):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class subs_optionsPtr(subs_options):
    def __init__(self, this):
        _swig_setattr(self, subs_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, subs_options, 'thisown', 0)
        _swig_setattr(self, subs_options,self.__class__,subs_options)
_swiginac.subs_options_swigregister(subs_optionsPtr)

class determinant_algo(_object):
    """Proxy of C++ determinant_algo class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, determinant_algo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, determinant_algo, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::determinant_algo instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    automatic = _swiginac.determinant_algo_automatic
    gauss = _swiginac.determinant_algo_gauss
    divfree = _swiginac.determinant_algo_divfree
    laplace = _swiginac.determinant_algo_laplace
    bareiss = _swiginac.determinant_algo_bareiss
    def __init__(self, *args):
        """__init__(self) -> determinant_algo"""
        _swig_setattr(self, determinant_algo, 'this', _swiginac.new_determinant_algo(*args))
        _swig_setattr(self, determinant_algo, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_determinant_algo):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class determinant_algoPtr(determinant_algo):
    def __init__(self, this):
        _swig_setattr(self, determinant_algo, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, determinant_algo, 'thisown', 0)
        _swig_setattr(self, determinant_algo,self.__class__,determinant_algo)
_swiginac.determinant_algo_swigregister(determinant_algoPtr)

class info_flags(_object):
    """Proxy of C++ info_flags class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, info_flags, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, info_flags, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::info_flags instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    numeric = _swiginac.info_flags_numeric
    real = _swiginac.info_flags_real
    rational = _swiginac.info_flags_rational
    integer = _swiginac.info_flags_integer
    crational = _swiginac.info_flags_crational
    cinteger = _swiginac.info_flags_cinteger
    positive = _swiginac.info_flags_positive
    negative = _swiginac.info_flags_negative
    nonnegative = _swiginac.info_flags_nonnegative
    posint = _swiginac.info_flags_posint
    negint = _swiginac.info_flags_negint
    nonnegint = _swiginac.info_flags_nonnegint
    even = _swiginac.info_flags_even
    odd = _swiginac.info_flags_odd
    prime = _swiginac.info_flags_prime
    relation = _swiginac.info_flags_relation
    relation_equal = _swiginac.info_flags_relation_equal
    relation_not_equal = _swiginac.info_flags_relation_not_equal
    relation_less = _swiginac.info_flags_relation_less
    relation_less_or_equal = _swiginac.info_flags_relation_less_or_equal
    relation_greater = _swiginac.info_flags_relation_greater
    relation_greater_or_equal = _swiginac.info_flags_relation_greater_or_equal
    symbol = _swiginac.info_flags_symbol
    list = _swiginac.info_flags_list
    exprseq = _swiginac.info_flags_exprseq
    polynomial = _swiginac.info_flags_polynomial
    integer_polynomial = _swiginac.info_flags_integer_polynomial
    cinteger_polynomial = _swiginac.info_flags_cinteger_polynomial
    rational_polynomial = _swiginac.info_flags_rational_polynomial
    crational_polynomial = _swiginac.info_flags_crational_polynomial
    rational_function = _swiginac.info_flags_rational_function
    algebraic = _swiginac.info_flags_algebraic
    indexed = _swiginac.info_flags_indexed
    has_indices = _swiginac.info_flags_has_indices
    idx = _swiginac.info_flags_idx
    def __init__(self, *args):
        """__init__(self) -> info_flags"""
        _swig_setattr(self, info_flags, 'this', _swiginac.new_info_flags(*args))
        _swig_setattr(self, info_flags, 'thisown', 1)
    def __del__(self, destroy=_swiginac.delete_info_flags):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class info_flagsPtr(info_flags):
    def __init__(self, this):
        _swig_setattr(self, info_flags, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, info_flags, 'thisown', 0)
        _swig_setattr(self, info_flags,self.__class__,info_flags)
_swiginac.info_flags_swigregister(info_flagsPtr)

class pseries(basic):
    """Proxy of C++ pseries class"""
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, pseries, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, pseries, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ GiNaC::pseries instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        """__init__(self, ex rel_, epvector ops_) -> pseries"""
        _swig_setattr(self, pseries, 'this', _swiginac.new_pseries(*args))
        _swig_setattr(self, pseries, 'thisown', 1)
    def get_var(*args):
        """get_var(self) -> ex"""
        return _swiginac.pseries_get_var(*args)

    def get_point(*args):
        """get_point(self) -> ex"""
        return _swiginac.pseries_get_point(*args)

    def convert_to_poly(*args):
        """
        convert_to_poly(self, bool no_order=False) -> ex
        convert_to_poly(self) -> ex
        """
        return _swiginac.pseries_convert_to_poly(*args)

    def is_compatible_to(*args):
        """is_compatible_to(self, pseries other) -> bool"""
        return _swiginac.pseries_is_compatible_to(*args)

    def is_zero(*args):
        """is_zero(self) -> bool"""
        return _swiginac.pseries_is_zero(*args)

    def is_terminating(*args):
        """is_terminating(self) -> bool"""
        return _swiginac.pseries_is_terminating(*args)

    def coeffop(*args):
        """coeffop(self, size_t i) -> ex"""
        return _swiginac.pseries_coeffop(*args)

    def exponop(*args):
        """exponop(self, size_t i) -> ex"""
        return _swiginac.pseries_exponop(*args)

    def add_series(*args):
        """add_series(self, pseries other) -> ex"""
        return _swiginac.pseries_add_series(*args)

    def mul_const(*args):
        """mul_const(self, numeric other) -> ex"""
        return _swiginac.pseries_mul_const(*args)

    def mul_series(*args):
        """mul_series(self, pseries other) -> ex"""
        return _swiginac.pseries_mul_series(*args)

    def power_const(*args):
        """power_const(self, numeric p, int deg) -> ex"""
        return _swiginac.pseries_power_const(*args)

    def shift_exponents(*args):
        """shift_exponents(self, int deg) -> pseries"""
        return _swiginac.pseries_shift_exponents(*args)

    def __repr__(self):
        return self.__str__()

    def __del__(self, destroy=_swiginac.delete_pseries):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class pseriesPtr(pseries):
    def __init__(self, this):
        _swig_setattr(self, pseries, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pseries, 'thisown', 0)
        _swig_setattr(self, pseries,self.__class__,pseries)
_swiginac.pseries_swigregister(pseriesPtr)


def series_to_poly(*args):
    """series_to_poly(ex e) -> ex"""
    return _swiginac.series_to_poly(*args)

def is_terminating(*args):
    """is_terminating(pseries s) -> bool"""
    return _swiginac.is_terminating(*args)

def parse_string(*args):
    """parse_string(string str, lst ls) -> ex"""
    return _swiginac.parse_string(*args)

