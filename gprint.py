# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.
import _gprint
def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

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


class print_context(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_context, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, print_context, name)
    def __init__(self,*args):
        _swig_setattr(self, print_context, 'this', apply(_gprint.new_print_context,args))
        _swig_setattr(self, print_context, 'thisown', 1)
    def getstream(*args): return apply(_gprint.print_context_getstream,args)
    def getstringstream(*args): return apply(_gprint.print_context_getstringstream,args)
    def extractstring(*args): return apply(_gprint.print_context_extractstring,args)
    def __del__(self, destroy= _gprint.delete_print_context):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_context instance at %s>" % (self.this,)

class print_contextPtr(print_context):
    def __init__(self,this):
        _swig_setattr(self, print_context, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_context, 'thisown', 0)
        _swig_setattr(self, print_context,self.__class__,print_context)
_gprint.print_context_swigregister(print_contextPtr)

class print_latex(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_latex, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_latex, name)
    def __init__(self,*args):
        _swig_setattr(self, print_latex, 'this', apply(_gprint.new_print_latex,args))
        _swig_setattr(self, print_latex, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_latex):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_latex instance at %s>" % (self.this,)

class print_latexPtr(print_latex):
    def __init__(self,this):
        _swig_setattr(self, print_latex, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_latex, 'thisown', 0)
        _swig_setattr(self, print_latex,self.__class__,print_latex)
_gprint.print_latex_swigregister(print_latexPtr)

class print_python(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_python, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_python, name)
    def __init__(self,*args):
        _swig_setattr(self, print_python, 'this', apply(_gprint.new_print_python,args))
        _swig_setattr(self, print_python, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_python):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_python instance at %s>" % (self.this,)

class print_pythonPtr(print_python):
    def __init__(self,this):
        _swig_setattr(self, print_python, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_python, 'thisown', 0)
        _swig_setattr(self, print_python,self.__class__,print_python)
_gprint.print_python_swigregister(print_pythonPtr)

class print_python_repr(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_python_repr, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_python_repr, name)
    def __init__(self,*args):
        _swig_setattr(self, print_python_repr, 'this', apply(_gprint.new_print_python_repr,args))
        _swig_setattr(self, print_python_repr, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_python_repr):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_python_repr instance at %s>" % (self.this,)

class print_python_reprPtr(print_python_repr):
    def __init__(self,this):
        _swig_setattr(self, print_python_repr, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_python_repr, 'thisown', 0)
        _swig_setattr(self, print_python_repr,self.__class__,print_python_repr)
_gprint.print_python_repr_swigregister(print_python_reprPtr)

class print_tree(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_tree, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_tree, name)
    def __init__(self,*args):
        _swig_setattr(self, print_tree, 'this', apply(_gprint.new_print_tree,args))
        _swig_setattr(self, print_tree, 'thisown', 1)
    __swig_getmethods__["delta_indent"] = _gprint.print_tree_delta_indent_get
    if _newclass:delta_indent = property(_gprint.print_tree_delta_indent_get)
    def __del__(self, destroy= _gprint.delete_print_tree):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_tree instance at %s>" % (self.this,)

class print_treePtr(print_tree):
    def __init__(self,this):
        _swig_setattr(self, print_tree, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_tree, 'thisown', 0)
        _swig_setattr(self, print_tree,self.__class__,print_tree)
_gprint.print_tree_swigregister(print_treePtr)

class print_csrc(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc, 'this', apply(_gprint.new_print_csrc,args))
        _swig_setattr(self, print_csrc, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_csrc):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_csrc instance at %s>" % (self.this,)

class print_csrcPtr(print_csrc):
    def __init__(self,this):
        _swig_setattr(self, print_csrc, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_csrc, 'thisown', 0)
        _swig_setattr(self, print_csrc,self.__class__,print_csrc)
_gprint.print_csrc_swigregister(print_csrcPtr)

class print_csrc_float(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_float, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_float, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_float, 'this', apply(_gprint.new_print_csrc_float,args))
        _swig_setattr(self, print_csrc_float, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_csrc_float):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_csrc_float instance at %s>" % (self.this,)

class print_csrc_floatPtr(print_csrc_float):
    def __init__(self,this):
        _swig_setattr(self, print_csrc_float, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_csrc_float, 'thisown', 0)
        _swig_setattr(self, print_csrc_float,self.__class__,print_csrc_float)
_gprint.print_csrc_float_swigregister(print_csrc_floatPtr)

class print_csrc_double(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_double, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_double, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_double, 'this', apply(_gprint.new_print_csrc_double,args))
        _swig_setattr(self, print_csrc_double, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_csrc_double):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_csrc_double instance at %s>" % (self.this,)

class print_csrc_doublePtr(print_csrc_double):
    def __init__(self,this):
        _swig_setattr(self, print_csrc_double, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_csrc_double, 'thisown', 0)
        _swig_setattr(self, print_csrc_double,self.__class__,print_csrc_double)
_gprint.print_csrc_double_swigregister(print_csrc_doublePtr)

class print_csrc_cl_N(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_cl_N, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_cl_N, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_cl_N, 'this', apply(_gprint.new_print_csrc_cl_N,args))
        _swig_setattr(self, print_csrc_cl_N, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_print_csrc_cl_N):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C print_csrc_cl_N instance at %s>" % (self.this,)

class print_csrc_cl_NPtr(print_csrc_cl_N):
    def __init__(self,this):
        _swig_setattr(self, print_csrc_cl_N, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, print_csrc_cl_N, 'thisown', 0)
        _swig_setattr(self, print_csrc_cl_N,self.__class__,print_csrc_cl_N)
_gprint.print_csrc_cl_N_swigregister(print_csrc_cl_NPtr)

class refcounted(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, refcounted, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, refcounted, name)
    def __init__(self,*args):
        _swig_setattr(self, refcounted, 'this', apply(_gprint.new_refcounted,args))
        _swig_setattr(self, refcounted, 'thisown', 1)
    def add_reference(*args): return apply(_gprint.refcounted_add_reference,args)
    def remove_reference(*args): return apply(_gprint.refcounted_remove_reference,args)
    def get_refcount(*args): return apply(_gprint.refcounted_get_refcount,args)
    def set_refcount(*args): return apply(_gprint.refcounted_set_refcount,args)
    def __del__(self, destroy= _gprint.delete_refcounted):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C refcounted instance at %s>" % (self.this,)

class refcountedPtr(refcounted):
    def __init__(self,this):
        _swig_setattr(self, refcounted, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, refcounted, 'thisown', 0)
        _swig_setattr(self, refcounted,self.__class__,refcounted)
_gprint.refcounted_swigregister(refcountedPtr)

class registered_class_options(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, registered_class_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, registered_class_options, name)
    def __init__(self,*args):
        _swig_setattr(self, registered_class_options, 'this', apply(_gprint.new_registered_class_options,args))
        _swig_setattr(self, registered_class_options, 'thisown', 1)
    def get_name(*args): return apply(_gprint.registered_class_options_get_name,args)
    def get_parent_name(*args): return apply(_gprint.registered_class_options_get_parent_name,args)
    def get_id(*args): return apply(_gprint.registered_class_options_get_id,args)
    def get_unarch_func(*args): return apply(_gprint.registered_class_options_get_unarch_func,args)
    def get_print_dispatch_table(*args): return apply(_gprint.registered_class_options_get_print_dispatch_table,args)
    def set_print_func(*args): return apply(_gprint.registered_class_options_set_print_func,args)
    def __del__(self, destroy= _gprint.delete_registered_class_options):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C registered_class_options instance at %s>" % (self.this,)

class registered_class_optionsPtr(registered_class_options):
    def __init__(self,this):
        _swig_setattr(self, registered_class_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, registered_class_options, 'thisown', 0)
        _swig_setattr(self, registered_class_options,self.__class__,registered_class_options)
_gprint.registered_class_options_swigregister(registered_class_optionsPtr)

find_tinfo_key = _gprint.find_tinfo_key

find_unarch_func = _gprint.find_unarch_func

class library_init(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, library_init, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, library_init, name)
    def __init__(self,*args):
        _swig_setattr(self, library_init, 'this', apply(_gprint.new_library_init,args))
        _swig_setattr(self, library_init, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_library_init):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C library_init instance at %s>" % (self.this,)

class library_initPtr(library_init):
    def __init__(self,this):
        _swig_setattr(self, library_init, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, library_init, 'thisown', 0)
        _swig_setattr(self, library_init,self.__class__,library_init)
_gprint.library_init_swigregister(library_initPtr)

class ex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ex, name)
    def __del__(self, destroy= _gprint.delete_ex):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self,*args):
        _swig_setattr(self, ex, 'this', apply(_gprint.new_ex,args))
        _swig_setattr(self, ex, 'thisown', 1)
    def swap(*args): return apply(_gprint.ex_swap,args)
    def gprint(*args): return apply(_gprint.ex_gprint,args)
    def eval(*args): return apply(_gprint.ex_eval,args)
    def evalf(*args): return apply(_gprint.ex_evalf,args)
    def evalm(*args): return apply(_gprint.ex_evalm,args)
    def diff(*args): return apply(_gprint.ex_diff,args)
    def subs(*args): return apply(_gprint.ex_subs,args)
    def __add__(*args): return apply(_gprint.ex___add__,args)
    def __sub__(*args): return apply(_gprint.ex___sub__,args)
    def __mul__(*args): return apply(_gprint.ex___mul__,args)
    def __div__(*args): return apply(_gprint.ex___div__,args)
    def __imul__(*args): return apply(_gprint.ex___imul__,args)
    def __isub(*args): return apply(_gprint.ex___isub,args)
    def __iadd__(*args): return apply(_gprint.ex___iadd__,args)
    def __idiv(*args): return apply(_gprint.ex___idiv,args)
    def __pos__(*args): return apply(_gprint.ex___pos__,args)
    def __neg__(*args): return apply(_gprint.ex___neg__,args)
    def __call__(*args): return apply(_gprint.ex___call__,args)
    def __repr__(self):
        return "<C ex instance at %s>" % (self.this,)

class exPtr(ex):
    def __init__(self,this):
        _swig_setattr(self, ex, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ex, 'thisown', 0)
        _swig_setattr(self, ex,self.__class__,ex)
_gprint.ex_swigregister(exPtr)
cvar = _gprint.cvar

class visitor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, visitor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, visitor, name)
    def __init__(self,*args):
        _swig_setattr(self, visitor, 'this', apply(_gprint.new_visitor,args))
        _swig_setattr(self, visitor, 'thisown', 1)
    def __repr__(self):
        return "<C visitor instance at %s>" % (self.this,)

class visitorPtr(visitor):
    def __init__(self,this):
        _swig_setattr(self, visitor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, visitor, 'thisown', 0)
        _swig_setattr(self, visitor,self.__class__,visitor)
_gprint.visitor_swigregister(visitorPtr)

class basic(refcounted):
    __swig_setmethods__ = {}
    for _s in [refcounted]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, basic, name, value)
    __swig_getmethods__ = {}
    for _s in [refcounted]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, basic, name)
    def __del__(self, destroy= _gprint.delete_basic):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self,*args):
        _swig_setattr(self, basic, 'this', apply(_gprint.new_basic,args))
        _swig_setattr(self, basic, 'thisown', 1)
    def duplicate(*args): return apply(_gprint.basic_duplicate,args)
    def eval(*args): return apply(_gprint.basic_eval,args)
    def evalf(*args): return apply(_gprint.basic_evalf,args)
    def evalm(*args): return apply(_gprint.basic_evalm,args)
    def eval_indexed(*args): return apply(_gprint.basic_eval_indexed,args)
    def gprint(*args): return apply(_gprint.basic_gprint,args)
    def dbgprint(*args): return apply(_gprint.basic_dbgprint,args)
    def dbgprinttree(*args): return apply(_gprint.basic_dbgprinttree,args)
    def precedence(*args): return apply(_gprint.basic_precedence,args)
    def info(*args): return apply(_gprint.basic_info,args)
    def nops(*args): return apply(_gprint.basic_nops,args)
    def op(*args): return apply(_gprint.basic_op,args)
    def let_op(*args): return apply(_gprint.basic_let_op,args)
    def has(*args): return apply(_gprint.basic_has,args)
    def match(*args): return apply(_gprint.basic_match,args)
    def subs(*args): return apply(_gprint.basic_subs,args)
    def map(*args): return apply(_gprint.basic_map,args)
    def accept(*args): return apply(_gprint.basic_accept,args)
    def degree(*args): return apply(_gprint.basic_degree,args)
    def ldegree(*args): return apply(_gprint.basic_ldegree,args)
    def coeff(*args): return apply(_gprint.basic_coeff,args)
    def expand(*args): return apply(_gprint.basic_expand,args)
    def collect(*args): return apply(_gprint.basic_collect,args)
    def series(*args): return apply(_gprint.basic_series,args)
    def normal(*args): return apply(_gprint.basic_normal,args)
    def to_rational(*args): return apply(_gprint.basic_to_rational,args)
    def to_polynomial(*args): return apply(_gprint.basic_to_polynomial,args)
    def integer_content(*args): return apply(_gprint.basic_integer_content,args)
    def smod(*args): return apply(_gprint.basic_smod,args)
    def max_coefficient(*args): return apply(_gprint.basic_max_coefficient,args)
    def get_free_indices(*args): return apply(_gprint.basic_get_free_indices,args)
    def add_indexed(*args): return apply(_gprint.basic_add_indexed,args)
    def scalar_mul_indexed(*args): return apply(_gprint.basic_scalar_mul_indexed,args)
    def contract_with(*args): return apply(_gprint.basic_contract_with,args)
    def return_type(*args): return apply(_gprint.basic_return_type,args)
    def return_type_tinfo(*args): return apply(_gprint.basic_return_type_tinfo,args)
    def conjugate(*args): return apply(_gprint.basic_conjugate,args)
    def print_dispatch(*args): return apply(_gprint.basic_print_dispatch,args)
    def subs_one_level(*args): return apply(_gprint.basic_subs_one_level,args)
    def diff(*args): return apply(_gprint.basic_diff,args)
    def compare(*args): return apply(_gprint.basic_compare,args)
    def is_equal(*args): return apply(_gprint.basic_is_equal,args)
    def hold(*args): return apply(_gprint.basic_hold,args)
    def gethash(*args): return apply(_gprint.basic_gethash,args)
    def tinfo(*args): return apply(_gprint.basic_tinfo,args)
    def setflag(*args): return apply(_gprint.basic_setflag,args)
    def clearflag(*args): return apply(_gprint.basic_clearflag,args)
    def __repr__(self):
        return "<C basic instance at %s>" % (self.this,)

class basicPtr(basic):
    def __init__(self,this):
        _swig_setattr(self, basic, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, basic, 'thisown', 0)
        _swig_setattr(self, basic,self.__class__,basic)
_gprint.basic_swigregister(basicPtr)

quo = _gprint.quo

rem = _gprint.rem

decomp_rational = _gprint.decomp_rational

prem = _gprint.prem

sprem = _gprint.sprem

divide = _gprint.divide

sqrfree = _gprint.sqrfree

sqrfree_parfrac = _gprint.sqrfree_parfrac

collect_common_factors = _gprint.collect_common_factors

resultant = _gprint.resultant

class constant(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, constant, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, constant, name)
    def __init__(self,*args):
        _swig_setattr(self, constant, 'this', apply(_gprint.new_constant,args))
        _swig_setattr(self, constant, 'thisown', 1)
    def gprint(*args): return apply(_gprint.constant_gprint,args)
    def evalf(*args): return apply(_gprint.constant_evalf,args)
    def __del__(self, destroy= _gprint.delete_constant):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C constant instance at %s>" % (self.this,)

class constantPtr(constant):
    def __init__(self,this):
        _swig_setattr(self, constant, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, constant, 'thisown', 0)
        _swig_setattr(self, constant,self.__class__,constant)
_gprint.constant_swigregister(constantPtr)

class matrix(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, matrix, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, matrix, name)
    def __init__(self,*args):
        _swig_setattr(self, matrix, 'this', apply(_gprint.new_matrix,args))
        _swig_setattr(self, matrix, 'thisown', 1)
    def nops(*args): return apply(_gprint.matrix_nops,args)
    def op(*args): return apply(_gprint.matrix_op,args)
    def let_op(*args): return apply(_gprint.matrix_let_op,args)
    def eval(*args): return apply(_gprint.matrix_eval,args)
    def evalm(*args): return apply(_gprint.matrix_evalm,args)
    def subs(*args): return apply(_gprint.matrix_subs,args)
    def eval_indexed(*args): return apply(_gprint.matrix_eval_indexed,args)
    def add_indexed(*args): return apply(_gprint.matrix_add_indexed,args)
    def scalar_mul_indexed(*args): return apply(_gprint.matrix_scalar_mul_indexed,args)
    def contract_with(*args): return apply(_gprint.matrix_contract_with,args)
    def conjugate(*args): return apply(_gprint.matrix_conjugate,args)
    def rows(*args): return apply(_gprint.matrix_rows,args)
    def cols(*args): return apply(_gprint.matrix_cols,args)
    def add(*args): return apply(_gprint.matrix_add,args)
    def sub(*args): return apply(_gprint.matrix_sub,args)
    def mul(*args): return apply(_gprint.matrix_mul,args)
    def mul_scalar(*args): return apply(_gprint.matrix_mul_scalar,args)
    def pow(*args): return apply(_gprint.matrix_pow,args)
    def __call__(*args): return apply(_gprint.matrix___call__,args)
    def set(*args): return apply(_gprint.matrix_set,args)
    def transpose(*args): return apply(_gprint.matrix_transpose,args)
    def determinant(*args): return apply(_gprint.matrix_determinant,args)
    def trace(*args): return apply(_gprint.matrix_trace,args)
    def charpoly(*args): return apply(_gprint.matrix_charpoly,args)
    def inverse(*args): return apply(_gprint.matrix_inverse,args)
    def solve(*args): return apply(_gprint.matrix_solve,args)
    def rank(*args): return apply(_gprint.matrix_rank,args)
    def __del__(self, destroy= _gprint.delete_matrix):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C matrix instance at %s>" % (self.this,)

class matrixPtr(matrix):
    def __init__(self,this):
        _swig_setattr(self, matrix, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, matrix, 'thisown', 0)
        _swig_setattr(self, matrix,self.__class__,matrix)
_gprint.matrix_swigregister(matrixPtr)
Pi = cvar.Pi
Catalan = cvar.Catalan
Euler = cvar.Euler

nops = _gprint.nops

expand = _gprint.expand

eval = _gprint.eval

evalf = _gprint.evalf

rows = _gprint.rows

cols = _gprint.cols

transpose = _gprint.transpose

determinant = _gprint.determinant

trace = _gprint.trace

charpoly = _gprint.charpoly

inverse = _gprint.inverse

rank = _gprint.rank

lst_to_matrix = _gprint.lst_to_matrix

diag_matrix = _gprint.diag_matrix

class numeric(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, numeric, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, numeric, name)
    def __init__(self,*args):
        _swig_setattr(self, numeric, 'this', apply(_gprint.new_numeric,args))
        _swig_setattr(self, numeric, 'thisown', 1)
    def gprint(*args): return apply(_gprint.numeric_gprint,args)
    def coeff(*args): return apply(_gprint.numeric_coeff,args)
    def eval(*args): return apply(_gprint.numeric_eval,args)
    def evalf(*args): return apply(_gprint.numeric_evalf,args)
    def add(*args): return apply(_gprint.numeric_add,args)
    def sub(*args): return apply(_gprint.numeric_sub,args)
    def mul(*args): return apply(_gprint.numeric_mul,args)
    def div(*args): return apply(_gprint.numeric_div,args)
    def power(*args): return apply(_gprint.numeric_power,args)
    def __eq__(*args): return apply(_gprint.numeric___eq__,args)
    def __ne__(*args): return apply(_gprint.numeric___ne__,args)
    def __lt__(*args): return apply(_gprint.numeric___lt__,args)
    def __le__(*args): return apply(_gprint.numeric___le__,args)
    def __gt__(*args): return apply(_gprint.numeric___gt__,args)
    def __ge__(*args): return apply(_gprint.numeric___ge__,args)
    def to_int(*args): return apply(_gprint.numeric_to_int,args)
    def to_long(*args): return apply(_gprint.numeric_to_long,args)
    def to_double(*args): return apply(_gprint.numeric_to_double,args)
    def real(*args): return apply(_gprint.numeric_real,args)
    def imag(*args): return apply(_gprint.numeric_imag,args)
    def __add__(*args): return apply(_gprint.numeric___add__,args)
    def __sub__(*args): return apply(_gprint.numeric___sub__,args)
    def __mul__(*args): return apply(_gprint.numeric___mul__,args)
    def __div__(*args): return apply(_gprint.numeric___div__,args)
    def __imul__(*args): return apply(_gprint.numeric___imul__,args)
    def __isub(*args): return apply(_gprint.numeric___isub,args)
    def __iadd__(*args): return apply(_gprint.numeric___iadd__,args)
    def __idiv(*args): return apply(_gprint.numeric___idiv,args)
    def __pos__(*args): return apply(_gprint.numeric___pos__,args)
    def __neg__(*args): return apply(_gprint.numeric___neg__,args)
    def __call__(*args): return apply(_gprint.numeric___call__,args)
    def __del__(self, destroy= _gprint.delete_numeric):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C numeric instance at %s>" % (self.this,)

class numericPtr(numeric):
    def __init__(self,this):
        _swig_setattr(self, numeric, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, numeric, 'thisown', 0)
        _swig_setattr(self, numeric,self.__class__,numeric)
_gprint.numeric_swigregister(numericPtr)
unit_matrix = _gprint.unit_matrix

symbolic_matrix = _gprint.symbolic_matrix


exp = _gprint.exp

log = _gprint.log

sin = _gprint.sin

cos = _gprint.cos

tan = _gprint.tan

asin = _gprint.asin

acos = _gprint.acos

sinh = _gprint.sinh

cosh = _gprint.cosh

tanh = _gprint.tanh

asinh = _gprint.asinh

acosh = _gprint.acosh

atanh = _gprint.atanh

Li2 = _gprint.Li2

zeta = _gprint.zeta

lgamma = _gprint.lgamma

tgamma = _gprint.tgamma

factorial = _gprint.factorial

doublefactorial = _gprint.doublefactorial

binomial = _gprint.binomial

bernoulli = _gprint.bernoulli

fibonacci = _gprint.fibonacci

isqrt = _gprint.isqrt

abs = _gprint.abs

mod = _gprint.mod

smod = _gprint.smod

PiEvalf = _gprint.PiEvalf

EulerEvalf = _gprint.EulerEvalf

CatalanEvalf = _gprint.CatalanEvalf

class power(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, power, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, power, name)
    def __init__(self,*args):
        _swig_setattr(self, power, 'this', apply(_gprint.new_power,args))
        _swig_setattr(self, power, 'thisown', 1)
    def precedence(*args): return apply(_gprint.power_precedence,args)
    def info(*args): return apply(_gprint.power_info,args)
    def nops(*args): return apply(_gprint.power_nops,args)
    def op(*args): return apply(_gprint.power_op,args)
    def map(*args): return apply(_gprint.power_map,args)
    def degree(*args): return apply(_gprint.power_degree,args)
    def ldegree(*args): return apply(_gprint.power_ldegree,args)
    def coeff(*args): return apply(_gprint.power_coeff,args)
    def eval(*args): return apply(_gprint.power_eval,args)
    def evalf(*args): return apply(_gprint.power_evalf,args)
    def evalm(*args): return apply(_gprint.power_evalm,args)
    def series(*args): return apply(_gprint.power_series,args)
    def subs(*args): return apply(_gprint.power_subs,args)
    def normal(*args): return apply(_gprint.power_normal,args)
    def to_rational(*args): return apply(_gprint.power_to_rational,args)
    def to_polynomial(*args): return apply(_gprint.power_to_polynomial,args)
    def get_free_indices(*args): return apply(_gprint.power_get_free_indices,args)
    def conjugate(*args): return apply(_gprint.power_conjugate,args)
    def __del__(self, destroy= _gprint.delete_power):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C power instance at %s>" % (self.this,)

class powerPtr(power):
    def __init__(self,this):
        _swig_setattr(self, power, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, power, 'thisown', 0)
        _swig_setattr(self, power,self.__class__,power)
_gprint.power_swigregister(powerPtr)
atan = _gprint.atan

psi = _gprint.psi

irem = _gprint.irem

iquo = _gprint.iquo

gcd = _gprint.gcd

lcm = _gprint.lcm


pow = _gprint.pow

class relational(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, relational, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, relational, name)
    equal = _gprint.relational_equal
    not_equal = _gprint.relational_not_equal
    less = _gprint.relational_less
    less_or_equal = _gprint.relational_less_or_equal
    greater = _gprint.relational_greater
    greater_or_equal = _gprint.relational_greater_or_equal
    def __init__(self,*args):
        _swig_setattr(self, relational, 'this', apply(_gprint.new_relational,args))
        _swig_setattr(self, relational, 'thisown', 1)
    def gprint(*args): return apply(_gprint.relational_gprint,args)
    def op(*args): return apply(_gprint.relational_op,args)
    def eval(*args): return apply(_gprint.relational_eval,args)
    def lhs(*args): return apply(_gprint.relational_lhs,args)
    def rhs(*args): return apply(_gprint.relational_rhs,args)
    def __del__(self, destroy= _gprint.delete_relational):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C relational instance at %s>" % (self.this,)

class relationalPtr(relational):
    def __init__(self,this):
        _swig_setattr(self, relational, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, relational, 'thisown', 0)
        _swig_setattr(self, relational,self.__class__,relational)
_gprint.relational_swigregister(relationalPtr)
sqrt = _gprint.sqrt


class symbol(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, symbol, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, symbol, name)
    def __init__(self,*args):
        _swig_setattr(self, symbol, 'this', apply(_gprint.new_symbol,args))
        _swig_setattr(self, symbol, 'thisown', 1)
    def gprint(*args): return apply(_gprint.symbol_gprint,args)
    def eval(*args): return apply(_gprint.symbol_eval,args)
    def evalf(*args): return apply(_gprint.symbol_evalf,args)
    def __call__(*args): return apply(_gprint.symbol___call__,args)
    def __del__(self, destroy= _gprint.delete_symbol):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C symbol instance at %s>" % (self.this,)

class symbolPtr(symbol):
    def __init__(self,this):
        _swig_setattr(self, symbol, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, symbol, 'thisown', 0)
        _swig_setattr(self, symbol,self.__class__,symbol)
_gprint.symbol_swigregister(symbolPtr)

EXPAIRSEQ_USE_HASHTAB = _gprint.EXPAIRSEQ_USE_HASHTAB
conjugateepvector = _gprint.conjugateepvector

class expairseq(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, expairseq, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, expairseq, name)
    def __init__(self,*args):
        _swig_setattr(self, expairseq, 'this', apply(_gprint.new_expairseq,args))
        _swig_setattr(self, expairseq, 'thisown', 1)
    def precedence(*args): return apply(_gprint.expairseq_precedence,args)
    def info(*args): return apply(_gprint.expairseq_info,args)
    def nops(*args): return apply(_gprint.expairseq_nops,args)
    def op(*args): return apply(_gprint.expairseq_op,args)
    def map(*args): return apply(_gprint.expairseq_map,args)
    def eval(*args): return apply(_gprint.expairseq_eval,args)
    def to_rational(*args): return apply(_gprint.expairseq_to_rational,args)
    def to_polynomial(*args): return apply(_gprint.expairseq_to_polynomial,args)
    def match(*args): return apply(_gprint.expairseq_match,args)
    def subs(*args): return apply(_gprint.expairseq_subs,args)
    def conjugate(*args): return apply(_gprint.expairseq_conjugate,args)
    def __del__(self, destroy= _gprint.delete_expairseq):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C expairseq instance at %s>" % (self.this,)

class expairseqPtr(expairseq):
    def __init__(self,this):
        _swig_setattr(self, expairseq, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, expairseq, 'thisown', 0)
        _swig_setattr(self, expairseq,self.__class__,expairseq)
_gprint.expairseq_swigregister(expairseqPtr)

class add(expairseq):
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, add, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, add, name)
    __swig_getmethods__["get_class_info_static"] = lambda x: _gprint.add_get_class_info_static
    if _newclass:get_class_info_static = staticmethod(_gprint.add_get_class_info_static)
    def get_class_info(*args): return apply(_gprint.add_get_class_info,args)
    def class_name(*args): return apply(_gprint.add_class_name,args)
    def archive(*args): return apply(_gprint.add_archive,args)
    __swig_getmethods__["unarchive"] = lambda x: _gprint.add_unarchive
    if _newclass:unarchive = staticmethod(_gprint.add_unarchive)
    def duplicate(*args): return apply(_gprint.add_duplicate,args)
    def accept(*args): return apply(_gprint.add_accept,args)
    def __init__(self,*args):
        _swig_setattr(self, add, 'this', apply(_gprint.new_add,args))
        _swig_setattr(self, add, 'thisown', 1)
    def precedence(*args): return apply(_gprint.add_precedence,args)
    def info(*args): return apply(_gprint.add_info,args)
    def degree(*args): return apply(_gprint.add_degree,args)
    def ldegree(*args): return apply(_gprint.add_ldegree,args)
    def coeff(*args): return apply(_gprint.add_coeff,args)
    def eval(*args): return apply(_gprint.add_eval,args)
    def evalm(*args): return apply(_gprint.add_evalm,args)
    def series(*args): return apply(_gprint.add_series,args)
    def normal(*args): return apply(_gprint.add_normal,args)
    def integer_content(*args): return apply(_gprint.add_integer_content,args)
    def smod(*args): return apply(_gprint.add_smod,args)
    def max_coefficient(*args): return apply(_gprint.add_max_coefficient,args)
    def conjugate(*args): return apply(_gprint.add_conjugate,args)
    def get_free_indices(*args): return apply(_gprint.add_get_free_indices,args)
    def eval_ncmul(*args): return apply(_gprint.add_eval_ncmul,args)
    def __del__(self, destroy= _gprint.delete_add):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C add instance at %s>" % (self.this,)

class addPtr(add):
    def __init__(self,this):
        _swig_setattr(self, add, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, add, 'thisown', 0)
        _swig_setattr(self, add,self.__class__,add)
_gprint.add_swigregister(addPtr)
add_get_class_info_static = _gprint.add_get_class_info_static

add_unarchive = _gprint.add_unarchive


class mul(expairseq):
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, mul, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, mul, name)
    def __init__(self,*args):
        _swig_setattr(self, mul, 'this', apply(_gprint.new_mul,args))
        _swig_setattr(self, mul, 'thisown', 1)
    def precedence(*args): return apply(_gprint.mul_precedence,args)
    def info(*args): return apply(_gprint.mul_info,args)
    def degree(*args): return apply(_gprint.mul_degree,args)
    def ldegree(*args): return apply(_gprint.mul_ldegree,args)
    def coeff(*args): return apply(_gprint.mul_coeff,args)
    def eval(*args): return apply(_gprint.mul_eval,args)
    def evalf(*args): return apply(_gprint.mul_evalf,args)
    def evalm(*args): return apply(_gprint.mul_evalm,args)
    def series(*args): return apply(_gprint.mul_series,args)
    def normal(*args): return apply(_gprint.mul_normal,args)
    def integer_content(*args): return apply(_gprint.mul_integer_content,args)
    def smod(*args): return apply(_gprint.mul_smod,args)
    def max_coefficient(*args): return apply(_gprint.mul_max_coefficient,args)
    def get_free_indices(*args): return apply(_gprint.mul_get_free_indices,args)
    def algebraic_subs_mul(*args): return apply(_gprint.mul_algebraic_subs_mul,args)
    def __del__(self, destroy= _gprint.delete_mul):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C mul instance at %s>" % (self.this,)

class mulPtr(mul):
    def __init__(self,this):
        _swig_setattr(self, mul, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mul, 'thisown', 0)
        _swig_setattr(self, mul,self.__class__,mul)
_gprint.mul_swigregister(mulPtr)

class function_options(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, function_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, function_options, name)
    def __init__(self,*args):
        _swig_setattr(self, function_options, 'this', apply(_gprint.new_function_options,args))
        _swig_setattr(self, function_options, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_function_options):
        try:
            if self.thisown: destroy(self)
        except: pass
    def initialize(*args): return apply(_gprint.function_options_initialize,args)
    def dummy(*args): return apply(_gprint.function_options_dummy,args)
    def set_name(*args): return apply(_gprint.function_options_set_name,args)
    def latex_name(*args): return apply(_gprint.function_options_latex_name,args)
    def eval_func(*args): return apply(_gprint.function_options_eval_func,args)
    def evalf_func(*args): return apply(_gprint.function_options_evalf_func,args)
    def conjugate_func(*args): return apply(_gprint.function_options_conjugate_func,args)
    def derivative_func(*args): return apply(_gprint.function_options_derivative_func,args)
    def series_func(*args): return apply(_gprint.function_options_series_func,args)
    def set_return_type(*args): return apply(_gprint.function_options_set_return_type,args)
    def do_not_evalf_params(*args): return apply(_gprint.function_options_do_not_evalf_params,args)
    def remember(*args): return apply(_gprint.function_options_remember,args)
    def overloaded(*args): return apply(_gprint.function_options_overloaded,args)
    def set_symmetry(*args): return apply(_gprint.function_options_set_symmetry,args)
    def get_name(*args): return apply(_gprint.function_options_get_name,args)
    def get_nparams(*args): return apply(_gprint.function_options_get_nparams,args)
    def __repr__(self):
        return "<C function_options instance at %s>" % (self.this,)

class function_optionsPtr(function_options):
    def __init__(self,this):
        _swig_setattr(self, function_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, function_options, 'thisown', 0)
        _swig_setattr(self, function_options,self.__class__,function_options)
_gprint.function_options_swigregister(function_optionsPtr)

class do_taylor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, do_taylor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, do_taylor, name)
    def __init__(self,*args):
        _swig_setattr(self, do_taylor, 'this', apply(_gprint.new_do_taylor,args))
        _swig_setattr(self, do_taylor, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_do_taylor):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C do_taylor instance at %s>" % (self.this,)

class do_taylorPtr(do_taylor):
    def __init__(self,this):
        _swig_setattr(self, do_taylor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, do_taylor, 'thisown', 0)
        _swig_setattr(self, do_taylor,self.__class__,do_taylor)
_gprint.do_taylor_swigregister(do_taylorPtr)

class function(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, function, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, function, name)
    def __init__(self,*args):
        _swig_setattr(self, function, 'this', apply(_gprint.new_function,args))
        _swig_setattr(self, function, 'thisown', 1)
    def gprint(*args): return apply(_gprint.function_gprint,args)
    def precedence(*args): return apply(_gprint.function_precedence,args)
    def expand(*args): return apply(_gprint.function_expand,args)
    def eval(*args): return apply(_gprint.function_eval,args)
    def evalf(*args): return apply(_gprint.function_evalf,args)
    def calchash(*args): return apply(_gprint.function_calchash,args)
    def series(*args): return apply(_gprint.function_series,args)
    def thiscontainer(*args): return apply(_gprint.function_thiscontainer,args)
    def conjugate(*args): return apply(_gprint.function_conjugate,args)
    __swig_getmethods__["register_new"] = lambda x: _gprint.function_register_new
    if _newclass:register_new = staticmethod(_gprint.function_register_new)
    __swig_getmethods__["find_function"] = lambda x: _gprint.function_find_function
    if _newclass:find_function = staticmethod(_gprint.function_find_function)
    def get_serial(*args): return apply(_gprint.function_get_serial,args)
    def get_name(*args): return apply(_gprint.function_get_name,args)
    def __del__(self, destroy= _gprint.delete_function):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C function instance at %s>" % (self.this,)

class functionPtr(function):
    def __init__(self,this):
        _swig_setattr(self, function, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, function, 'thisown', 0)
        _swig_setattr(self, function,self.__class__,function)
_gprint.function_swigregister(functionPtr)
function_register_new = _gprint.function_register_new

function_find_function = _gprint.function_find_function


class abs_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, abs_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, abs_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, abs_SERIAL, 'this', apply(_gprint.new_abs_SERIAL,args))
        _swig_setattr(self, abs_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_abs_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C abs_SERIAL instance at %s>" % (self.this,)

class abs_SERIALPtr(abs_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, abs_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, abs_SERIAL, 'thisown', 0)
        _swig_setattr(self, abs_SERIAL,self.__class__,abs_SERIAL)
_gprint.abs_SERIAL_swigregister(abs_SERIALPtr)

class csgn_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, csgn_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, csgn_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, csgn_SERIAL, 'this', apply(_gprint.new_csgn_SERIAL,args))
        _swig_setattr(self, csgn_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_csgn_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C csgn_SERIAL instance at %s>" % (self.this,)

class csgn_SERIALPtr(csgn_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, csgn_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, csgn_SERIAL, 'thisown', 0)
        _swig_setattr(self, csgn_SERIAL,self.__class__,csgn_SERIAL)
_gprint.csgn_SERIAL_swigregister(csgn_SERIALPtr)
abs_NPARAMS = cvar.abs_NPARAMS

class eta_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eta_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, eta_SERIAL, 'this', apply(_gprint.new_eta_SERIAL,args))
        _swig_setattr(self, eta_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_eta_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C eta_SERIAL instance at %s>" % (self.this,)

class eta_SERIALPtr(eta_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, eta_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, eta_SERIAL, 'thisown', 0)
        _swig_setattr(self, eta_SERIAL,self.__class__,eta_SERIAL)
_gprint.eta_SERIAL_swigregister(eta_SERIALPtr)
csgn_NPARAMS = cvar.csgn_NPARAMS

class sin_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sin_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, sin_SERIAL, 'this', apply(_gprint.new_sin_SERIAL,args))
        _swig_setattr(self, sin_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_sin_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C sin_SERIAL instance at %s>" % (self.this,)

class sin_SERIALPtr(sin_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, sin_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, sin_SERIAL, 'thisown', 0)
        _swig_setattr(self, sin_SERIAL,self.__class__,sin_SERIAL)
_gprint.sin_SERIAL_swigregister(sin_SERIALPtr)
eta_NPARAMS = cvar.eta_NPARAMS

class cos_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cos_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, cos_SERIAL, 'this', apply(_gprint.new_cos_SERIAL,args))
        _swig_setattr(self, cos_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_cos_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C cos_SERIAL instance at %s>" % (self.this,)

class cos_SERIALPtr(cos_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, cos_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cos_SERIAL, 'thisown', 0)
        _swig_setattr(self, cos_SERIAL,self.__class__,cos_SERIAL)
_gprint.cos_SERIAL_swigregister(cos_SERIALPtr)
sin_NPARAMS = cvar.sin_NPARAMS

class tan_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tan_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tan_SERIAL, 'this', apply(_gprint.new_tan_SERIAL,args))
        _swig_setattr(self, tan_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_tan_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C tan_SERIAL instance at %s>" % (self.this,)

class tan_SERIALPtr(tan_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, tan_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tan_SERIAL, 'thisown', 0)
        _swig_setattr(self, tan_SERIAL,self.__class__,tan_SERIAL)
_gprint.tan_SERIAL_swigregister(tan_SERIALPtr)
cos_NPARAMS = cvar.cos_NPARAMS

class exp_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, exp_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, exp_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, exp_SERIAL, 'this', apply(_gprint.new_exp_SERIAL,args))
        _swig_setattr(self, exp_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_exp_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C exp_SERIAL instance at %s>" % (self.this,)

class exp_SERIALPtr(exp_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, exp_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, exp_SERIAL, 'thisown', 0)
        _swig_setattr(self, exp_SERIAL,self.__class__,exp_SERIAL)
_gprint.exp_SERIAL_swigregister(exp_SERIALPtr)
tan_NPARAMS = cvar.tan_NPARAMS

class log_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, log_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, log_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, log_SERIAL, 'this', apply(_gprint.new_log_SERIAL,args))
        _swig_setattr(self, log_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_log_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C log_SERIAL instance at %s>" % (self.this,)

class log_SERIALPtr(log_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, log_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, log_SERIAL, 'thisown', 0)
        _swig_setattr(self, log_SERIAL,self.__class__,log_SERIAL)
_gprint.log_SERIAL_swigregister(log_SERIALPtr)
exp_NPARAMS = cvar.exp_NPARAMS

class asin_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asin_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, asin_SERIAL, 'this', apply(_gprint.new_asin_SERIAL,args))
        _swig_setattr(self, asin_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_asin_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C asin_SERIAL instance at %s>" % (self.this,)

class asin_SERIALPtr(asin_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, asin_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, asin_SERIAL, 'thisown', 0)
        _swig_setattr(self, asin_SERIAL,self.__class__,asin_SERIAL)
_gprint.asin_SERIAL_swigregister(asin_SERIALPtr)
log_NPARAMS = cvar.log_NPARAMS

class acos_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acos_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, acos_SERIAL, 'this', apply(_gprint.new_acos_SERIAL,args))
        _swig_setattr(self, acos_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_acos_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C acos_SERIAL instance at %s>" % (self.this,)

class acos_SERIALPtr(acos_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, acos_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, acos_SERIAL, 'thisown', 0)
        _swig_setattr(self, acos_SERIAL,self.__class__,acos_SERIAL)
_gprint.acos_SERIAL_swigregister(acos_SERIALPtr)
asin_NPARAMS = cvar.asin_NPARAMS

class atan_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atan_SERIAL, 'this', apply(_gprint.new_atan_SERIAL,args))
        _swig_setattr(self, atan_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_atan_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C atan_SERIAL instance at %s>" % (self.this,)

class atan_SERIALPtr(atan_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, atan_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atan_SERIAL, 'thisown', 0)
        _swig_setattr(self, atan_SERIAL,self.__class__,atan_SERIAL)
_gprint.atan_SERIAL_swigregister(atan_SERIALPtr)
acos_NPARAMS = cvar.acos_NPARAMS

class atan2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atan2_SERIAL, 'this', apply(_gprint.new_atan2_SERIAL,args))
        _swig_setattr(self, atan2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_atan2_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C atan2_SERIAL instance at %s>" % (self.this,)

class atan2_SERIALPtr(atan2_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, atan2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atan2_SERIAL, 'thisown', 0)
        _swig_setattr(self, atan2_SERIAL,self.__class__,atan2_SERIAL)
_gprint.atan2_SERIAL_swigregister(atan2_SERIALPtr)
atan_NPARAMS = cvar.atan_NPARAMS

class sinh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sinh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, sinh_SERIAL, 'this', apply(_gprint.new_sinh_SERIAL,args))
        _swig_setattr(self, sinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_sinh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C sinh_SERIAL instance at %s>" % (self.this,)

class sinh_SERIALPtr(sinh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, sinh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, sinh_SERIAL, 'thisown', 0)
        _swig_setattr(self, sinh_SERIAL,self.__class__,sinh_SERIAL)
_gprint.sinh_SERIAL_swigregister(sinh_SERIALPtr)
atan2_NPARAMS = cvar.atan2_NPARAMS

class cosh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cosh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, cosh_SERIAL, 'this', apply(_gprint.new_cosh_SERIAL,args))
        _swig_setattr(self, cosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_cosh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C cosh_SERIAL instance at %s>" % (self.this,)

class cosh_SERIALPtr(cosh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, cosh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, cosh_SERIAL, 'thisown', 0)
        _swig_setattr(self, cosh_SERIAL,self.__class__,cosh_SERIAL)
_gprint.cosh_SERIAL_swigregister(cosh_SERIALPtr)
sinh_NPARAMS = cvar.sinh_NPARAMS

class tanh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tanh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tanh_SERIAL, 'this', apply(_gprint.new_tanh_SERIAL,args))
        _swig_setattr(self, tanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_tanh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C tanh_SERIAL instance at %s>" % (self.this,)

class tanh_SERIALPtr(tanh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, tanh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tanh_SERIAL, 'thisown', 0)
        _swig_setattr(self, tanh_SERIAL,self.__class__,tanh_SERIAL)
_gprint.tanh_SERIAL_swigregister(tanh_SERIALPtr)
cosh_NPARAMS = cvar.cosh_NPARAMS

class asinh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asinh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, asinh_SERIAL, 'this', apply(_gprint.new_asinh_SERIAL,args))
        _swig_setattr(self, asinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_asinh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C asinh_SERIAL instance at %s>" % (self.this,)

class asinh_SERIALPtr(asinh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, asinh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, asinh_SERIAL, 'thisown', 0)
        _swig_setattr(self, asinh_SERIAL,self.__class__,asinh_SERIAL)
_gprint.asinh_SERIAL_swigregister(asinh_SERIALPtr)
tanh_NPARAMS = cvar.tanh_NPARAMS

class acosh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acosh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, acosh_SERIAL, 'this', apply(_gprint.new_acosh_SERIAL,args))
        _swig_setattr(self, acosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_acosh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C acosh_SERIAL instance at %s>" % (self.this,)

class acosh_SERIALPtr(acosh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, acosh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, acosh_SERIAL, 'thisown', 0)
        _swig_setattr(self, acosh_SERIAL,self.__class__,acosh_SERIAL)
_gprint.acosh_SERIAL_swigregister(acosh_SERIALPtr)
asinh_NPARAMS = cvar.asinh_NPARAMS

class atanh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atanh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atanh_SERIAL, 'this', apply(_gprint.new_atanh_SERIAL,args))
        _swig_setattr(self, atanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_atanh_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C atanh_SERIAL instance at %s>" % (self.this,)

class atanh_SERIALPtr(atanh_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, atanh_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, atanh_SERIAL, 'thisown', 0)
        _swig_setattr(self, atanh_SERIAL,self.__class__,atanh_SERIAL)
_gprint.atanh_SERIAL_swigregister(atanh_SERIALPtr)
acosh_NPARAMS = cvar.acosh_NPARAMS

class Li2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Li2_SERIAL, 'this', apply(_gprint.new_Li2_SERIAL,args))
        _swig_setattr(self, Li2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_Li2_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C Li2_SERIAL instance at %s>" % (self.this,)

class Li2_SERIALPtr(Li2_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, Li2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Li2_SERIAL, 'thisown', 0)
        _swig_setattr(self, Li2_SERIAL,self.__class__,Li2_SERIAL)
_gprint.Li2_SERIAL_swigregister(Li2_SERIALPtr)
atanh_NPARAMS = cvar.atanh_NPARAMS

class Li3_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li3_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li3_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Li3_SERIAL, 'this', apply(_gprint.new_Li3_SERIAL,args))
        _swig_setattr(self, Li3_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_Li3_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C Li3_SERIAL instance at %s>" % (self.this,)

class Li3_SERIALPtr(Li3_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, Li3_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Li3_SERIAL, 'thisown', 0)
        _swig_setattr(self, Li3_SERIAL,self.__class__,Li3_SERIAL)
_gprint.Li3_SERIAL_swigregister(Li3_SERIALPtr)
Li2_NPARAMS = cvar.Li2_NPARAMS

class zeta1_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zeta1_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zeta1_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, zeta1_SERIAL, 'this', apply(_gprint.new_zeta1_SERIAL,args))
        _swig_setattr(self, zeta1_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_zeta1_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C zeta1_SERIAL instance at %s>" % (self.this,)

class zeta1_SERIALPtr(zeta1_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, zeta1_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, zeta1_SERIAL, 'thisown', 0)
        _swig_setattr(self, zeta1_SERIAL,self.__class__,zeta1_SERIAL)
_gprint.zeta1_SERIAL_swigregister(zeta1_SERIALPtr)
Li3_NPARAMS = cvar.Li3_NPARAMS

class zeta2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zeta2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zeta2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, zeta2_SERIAL, 'this', apply(_gprint.new_zeta2_SERIAL,args))
        _swig_setattr(self, zeta2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_zeta2_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C zeta2_SERIAL instance at %s>" % (self.this,)

class zeta2_SERIALPtr(zeta2_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, zeta2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, zeta2_SERIAL, 'thisown', 0)
        _swig_setattr(self, zeta2_SERIAL,self.__class__,zeta2_SERIAL)
_gprint.zeta2_SERIAL_swigregister(zeta2_SERIALPtr)

class lgamma_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lgamma_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, lgamma_SERIAL, 'this', apply(_gprint.new_lgamma_SERIAL,args))
        _swig_setattr(self, lgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_lgamma_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C lgamma_SERIAL instance at %s>" % (self.this,)

class lgamma_SERIALPtr(lgamma_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, lgamma_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, lgamma_SERIAL, 'thisown', 0)
        _swig_setattr(self, lgamma_SERIAL,self.__class__,lgamma_SERIAL)
_gprint.lgamma_SERIAL_swigregister(lgamma_SERIALPtr)

class tgamma_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tgamma_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tgamma_SERIAL, 'this', apply(_gprint.new_tgamma_SERIAL,args))
        _swig_setattr(self, tgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_tgamma_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C tgamma_SERIAL instance at %s>" % (self.this,)

class tgamma_SERIALPtr(tgamma_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, tgamma_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, tgamma_SERIAL, 'thisown', 0)
        _swig_setattr(self, tgamma_SERIAL,self.__class__,tgamma_SERIAL)
_gprint.tgamma_SERIAL_swigregister(tgamma_SERIALPtr)
lgamma_NPARAMS = cvar.lgamma_NPARAMS

class beta_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, beta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, beta_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, beta_SERIAL, 'this', apply(_gprint.new_beta_SERIAL,args))
        _swig_setattr(self, beta_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_beta_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C beta_SERIAL instance at %s>" % (self.this,)

class beta_SERIALPtr(beta_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, beta_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, beta_SERIAL, 'thisown', 0)
        _swig_setattr(self, beta_SERIAL,self.__class__,beta_SERIAL)
_gprint.beta_SERIAL_swigregister(beta_SERIALPtr)
tgamma_NPARAMS = cvar.tgamma_NPARAMS

class psi1_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psi1_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psi1_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, psi1_SERIAL, 'this', apply(_gprint.new_psi1_SERIAL,args))
        _swig_setattr(self, psi1_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_psi1_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C psi1_SERIAL instance at %s>" % (self.this,)

class psi1_SERIALPtr(psi1_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, psi1_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, psi1_SERIAL, 'thisown', 0)
        _swig_setattr(self, psi1_SERIAL,self.__class__,psi1_SERIAL)
_gprint.psi1_SERIAL_swigregister(psi1_SERIALPtr)
beta_NPARAMS = cvar.beta_NPARAMS

class psi2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psi2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psi2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, psi2_SERIAL, 'this', apply(_gprint.new_psi2_SERIAL,args))
        _swig_setattr(self, psi2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_psi2_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C psi2_SERIAL instance at %s>" % (self.this,)

class psi2_SERIALPtr(psi2_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, psi2_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, psi2_SERIAL, 'thisown', 0)
        _swig_setattr(self, psi2_SERIAL,self.__class__,psi2_SERIAL)
_gprint.psi2_SERIAL_swigregister(psi2_SERIALPtr)

class factorial_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, factorial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, factorial_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, factorial_SERIAL, 'this', apply(_gprint.new_factorial_SERIAL,args))
        _swig_setattr(self, factorial_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_factorial_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C factorial_SERIAL instance at %s>" % (self.this,)

class factorial_SERIALPtr(factorial_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, factorial_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, factorial_SERIAL, 'thisown', 0)
        _swig_setattr(self, factorial_SERIAL,self.__class__,factorial_SERIAL)
_gprint.factorial_SERIAL_swigregister(factorial_SERIALPtr)

class binomial_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, binomial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, binomial_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, binomial_SERIAL, 'this', apply(_gprint.new_binomial_SERIAL,args))
        _swig_setattr(self, binomial_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_binomial_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C binomial_SERIAL instance at %s>" % (self.this,)

class binomial_SERIALPtr(binomial_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, binomial_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, binomial_SERIAL, 'thisown', 0)
        _swig_setattr(self, binomial_SERIAL,self.__class__,binomial_SERIAL)
_gprint.binomial_SERIAL_swigregister(binomial_SERIALPtr)
factorial_NPARAMS = cvar.factorial_NPARAMS

class Order_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Order_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Order_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Order_SERIAL, 'this', apply(_gprint.new_Order_SERIAL,args))
        _swig_setattr(self, Order_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _gprint.delete_Order_SERIAL):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C Order_SERIAL instance at %s>" % (self.this,)

class Order_SERIALPtr(Order_SERIAL):
    def __init__(self,this):
        _swig_setattr(self, Order_SERIAL, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Order_SERIAL, 'thisown', 0)
        _swig_setattr(self, Order_SERIAL,self.__class__,Order_SERIAL)
_gprint.Order_SERIAL_swigregister(Order_SERIALPtr)
binomial_NPARAMS = cvar.binomial_NPARAMS

__eq__ = _gprint.__eq__

__ne__ = _gprint.__ne__

__lt__ = _gprint.__lt__

__le__ = _gprint.__le__

__gt__ = _gprint.__gt__

__ge__ = _gprint.__ge__

__lshift__ = _gprint.__lshift__

__rshift__ = _gprint.__rshift__

dflt = _gprint.dflt

latex = _gprint.latex

python = _gprint.python

python_repr = _gprint.python_repr

tree = _gprint.tree

csrc = _gprint.csrc

csrc_float = _gprint.csrc_float

csrc_double = _gprint.csrc_double

csrc_cl_N = _gprint.csrc_cl_N

index_dimensions = _gprint.index_dimensions

no_index_dimensions = _gprint.no_index_dimensions

exp_ex = _gprint.exp_ex

log_ex = _gprint.log_ex

sin_ex = _gprint.sin_ex

cos_ex = _gprint.cos_ex

tan_ex = _gprint.tan_ex

asin_ex = _gprint.asin_ex

acos_ex = _gprint.acos_ex

atan_ex = _gprint.atan_ex

sinh_ex = _gprint.sinh_ex

cosh_ex = _gprint.cosh_ex

tanh_ex = _gprint.tanh_ex

asinh_ex = _gprint.asinh_ex

acosh_ex = _gprint.acosh_ex

atanh_ex = _gprint.atanh_ex

Li2_ex = _gprint.Li2_ex

zeta_ex = _gprint.zeta_ex

lgamma_ex = _gprint.lgamma_ex

tgamma_ex = _gprint.tgamma_ex

psi_ex = _gprint.psi_ex

factorial_ex = _gprint.factorial_ex

binomial_ex_ex = _gprint.binomial_ex_ex

abs_ex = _gprint.abs_ex

Order_NPARAMS = cvar.Order_NPARAMS
__mul__ = _gprint.__mul__

__div__ = _gprint.__div__

__iadd__ = _gprint.__iadd__

__isub__ = _gprint.__isub__

__imul__ = _gprint.__imul__

__idiv__ = _gprint.__idiv__

__add__ = _gprint.__add__

__sub__ = _gprint.__sub__


