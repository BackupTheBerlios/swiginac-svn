# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.
import _swiginac
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
        _swig_setattr(self, print_context, 'this', apply(_swiginac.new_print_context,args))
        _swig_setattr(self, print_context, 'thisown', 1)
    def getstream(*args): return apply(_swiginac.print_context_getstream,args)
    def getstringstream(*args): return apply(_swiginac.print_context_getstringstream,args)
    def extractstring(*args): return apply(_swiginac.print_context_extractstring,args)
    def __del__(self, destroy= _swiginac.delete_print_context):
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
_swiginac.print_context_swigregister(print_contextPtr)

class print_latex(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_latex, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_latex, name)
    def __init__(self,*args):
        _swig_setattr(self, print_latex, 'this', apply(_swiginac.new_print_latex,args))
        _swig_setattr(self, print_latex, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_latex):
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
_swiginac.print_latex_swigregister(print_latexPtr)

class print_python(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_python, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_python, name)
    def __init__(self,*args):
        _swig_setattr(self, print_python, 'this', apply(_swiginac.new_print_python,args))
        _swig_setattr(self, print_python, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_python):
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
_swiginac.print_python_swigregister(print_pythonPtr)

class print_python_repr(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_python_repr, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_python_repr, name)
    def __init__(self,*args):
        _swig_setattr(self, print_python_repr, 'this', apply(_swiginac.new_print_python_repr,args))
        _swig_setattr(self, print_python_repr, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_python_repr):
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
_swiginac.print_python_repr_swigregister(print_python_reprPtr)

class print_tree(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_tree, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_tree, name)
    def __init__(self,*args):
        _swig_setattr(self, print_tree, 'this', apply(_swiginac.new_print_tree,args))
        _swig_setattr(self, print_tree, 'thisown', 1)
    __swig_getmethods__["delta_indent"] = _swiginac.print_tree_delta_indent_get
    if _newclass:delta_indent = property(_swiginac.print_tree_delta_indent_get)
    def __del__(self, destroy= _swiginac.delete_print_tree):
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
_swiginac.print_tree_swigregister(print_treePtr)

class print_csrc(print_context):
    __swig_setmethods__ = {}
    for _s in [print_context]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc, name, value)
    __swig_getmethods__ = {}
    for _s in [print_context]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc, 'this', apply(_swiginac.new_print_csrc,args))
        _swig_setattr(self, print_csrc, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_csrc):
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
_swiginac.print_csrc_swigregister(print_csrcPtr)

class print_csrc_float(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_float, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_float, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_float, 'this', apply(_swiginac.new_print_csrc_float,args))
        _swig_setattr(self, print_csrc_float, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_csrc_float):
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
_swiginac.print_csrc_float_swigregister(print_csrc_floatPtr)

class print_csrc_double(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_double, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_double, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_double, 'this', apply(_swiginac.new_print_csrc_double,args))
        _swig_setattr(self, print_csrc_double, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_csrc_double):
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
_swiginac.print_csrc_double_swigregister(print_csrc_doublePtr)

class print_csrc_cl_N(print_csrc):
    __swig_setmethods__ = {}
    for _s in [print_csrc]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, print_csrc_cl_N, name, value)
    __swig_getmethods__ = {}
    for _s in [print_csrc]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, print_csrc_cl_N, name)
    def __init__(self,*args):
        _swig_setattr(self, print_csrc_cl_N, 'this', apply(_swiginac.new_print_csrc_cl_N,args))
        _swig_setattr(self, print_csrc_cl_N, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_print_csrc_cl_N):
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
_swiginac.print_csrc_cl_N_swigregister(print_csrc_cl_NPtr)

class refcounted(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, refcounted, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, refcounted, name)
    def __init__(self,*args):
        _swig_setattr(self, refcounted, 'this', apply(_swiginac.new_refcounted,args))
        _swig_setattr(self, refcounted, 'thisown', 1)
    def add_reference(*args): return apply(_swiginac.refcounted_add_reference,args)
    def remove_reference(*args): return apply(_swiginac.refcounted_remove_reference,args)
    def get_refcount(*args): return apply(_swiginac.refcounted_get_refcount,args)
    def set_refcount(*args): return apply(_swiginac.refcounted_set_refcount,args)
    def __del__(self, destroy= _swiginac.delete_refcounted):
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
_swiginac.refcounted_swigregister(refcountedPtr)

class registered_class_options(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, registered_class_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, registered_class_options, name)
    def __init__(self,*args):
        _swig_setattr(self, registered_class_options, 'this', apply(_swiginac.new_registered_class_options,args))
        _swig_setattr(self, registered_class_options, 'thisown', 1)
    def get_name(*args): return apply(_swiginac.registered_class_options_get_name,args)
    def get_parent_name(*args): return apply(_swiginac.registered_class_options_get_parent_name,args)
    def get_id(*args): return apply(_swiginac.registered_class_options_get_id,args)
    def get_unarch_func(*args): return apply(_swiginac.registered_class_options_get_unarch_func,args)
    def get_print_dispatch_table(*args): return apply(_swiginac.registered_class_options_get_print_dispatch_table,args)
    def set_print_func(*args): return apply(_swiginac.registered_class_options_set_print_func,args)
    def __del__(self, destroy= _swiginac.delete_registered_class_options):
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
_swiginac.registered_class_options_swigregister(registered_class_optionsPtr)

find_tinfo_key = _swiginac.find_tinfo_key

find_unarch_func = _swiginac.find_unarch_func

class library_init(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, library_init, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, library_init, name)
    def __init__(self,*args):
        _swig_setattr(self, library_init, 'this', apply(_swiginac.new_library_init,args))
        _swig_setattr(self, library_init, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_library_init):
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
_swiginac.library_init_swigregister(library_initPtr)

class ex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ex, name)
    def __del__(self, destroy= _swiginac.delete_ex):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self,*args):
        _swig_setattr(self, ex, 'this', apply(_swiginac.new_ex,args))
        _swig_setattr(self, ex, 'thisown', 1)
    def swap(*args): return apply(_swiginac.ex_swap,args)
    def gprint(*args): return apply(_swiginac.ex_gprint,args)
    def eval(*args): return apply(_swiginac.ex_eval,args)
    def evalf(*args): return apply(_swiginac.ex_evalf,args)
    def evalm(*args): return apply(_swiginac.ex_evalm,args)
    def diff(*args): return apply(_swiginac.ex_diff,args)
    def subs(*args): return apply(_swiginac.ex_subs,args)
    def __add__(*args): return apply(_swiginac.ex___add__,args)
    def __sub__(*args): return apply(_swiginac.ex___sub__,args)
    def __mul__(*args): return apply(_swiginac.ex___mul__,args)
    def __div__(*args): return apply(_swiginac.ex___div__,args)
    def __imul__(*args): return apply(_swiginac.ex___imul__,args)
    def __isub(*args): return apply(_swiginac.ex___isub,args)
    def __iadd__(*args): return apply(_swiginac.ex___iadd__,args)
    def __idiv(*args): return apply(_swiginac.ex___idiv,args)
    def __pos__(*args): return apply(_swiginac.ex___pos__,args)
    def __neg__(*args): return apply(_swiginac.ex___neg__,args)
    def __call__(*args): return apply(_swiginac.ex___call__,args)
    def to_double(*args): return apply(_swiginac.ex_to_double,args)
    def __repr__(self):
        return "<C ex instance at %s>" % (self.this,)

class exPtr(ex):
    def __init__(self,this):
        _swig_setattr(self, ex, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ex, 'thisown', 0)
        _swig_setattr(self, ex,self.__class__,ex)
_swiginac.ex_swigregister(exPtr)
cvar = _swiginac.cvar

class visitor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, visitor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, visitor, name)
    def __init__(self,*args):
        _swig_setattr(self, visitor, 'this', apply(_swiginac.new_visitor,args))
        _swig_setattr(self, visitor, 'thisown', 1)
    def __repr__(self):
        return "<C visitor instance at %s>" % (self.this,)

class visitorPtr(visitor):
    def __init__(self,this):
        _swig_setattr(self, visitor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, visitor, 'thisown', 0)
        _swig_setattr(self, visitor,self.__class__,visitor)
_swiginac.visitor_swigregister(visitorPtr)

class basic(refcounted):
    __swig_setmethods__ = {}
    for _s in [refcounted]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, basic, name, value)
    __swig_getmethods__ = {}
    for _s in [refcounted]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, basic, name)
    def __del__(self, destroy= _swiginac.delete_basic):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self,*args):
        _swig_setattr(self, basic, 'this', apply(_swiginac.new_basic,args))
        _swig_setattr(self, basic, 'thisown', 1)
    def duplicate(*args): return apply(_swiginac.basic_duplicate,args)
    def eval(*args): return apply(_swiginac.basic_eval,args)
    def evalf(*args): return apply(_swiginac.basic_evalf,args)
    def evalm(*args): return apply(_swiginac.basic_evalm,args)
    def eval_indexed(*args): return apply(_swiginac.basic_eval_indexed,args)
    def gprint(*args): return apply(_swiginac.basic_gprint,args)
    def dbgprint(*args): return apply(_swiginac.basic_dbgprint,args)
    def dbgprinttree(*args): return apply(_swiginac.basic_dbgprinttree,args)
    def precedence(*args): return apply(_swiginac.basic_precedence,args)
    def info(*args): return apply(_swiginac.basic_info,args)
    def nops(*args): return apply(_swiginac.basic_nops,args)
    def op(*args): return apply(_swiginac.basic_op,args)
    def let_op(*args): return apply(_swiginac.basic_let_op,args)
    def has(*args): return apply(_swiginac.basic_has,args)
    def match(*args): return apply(_swiginac.basic_match,args)
    def subs(*args): return apply(_swiginac.basic_subs,args)
    def map(*args): return apply(_swiginac.basic_map,args)
    def accept(*args): return apply(_swiginac.basic_accept,args)
    def degree(*args): return apply(_swiginac.basic_degree,args)
    def ldegree(*args): return apply(_swiginac.basic_ldegree,args)
    def coeff(*args): return apply(_swiginac.basic_coeff,args)
    def expand(*args): return apply(_swiginac.basic_expand,args)
    def collect(*args): return apply(_swiginac.basic_collect,args)
    def series(*args): return apply(_swiginac.basic_series,args)
    def normal(*args): return apply(_swiginac.basic_normal,args)
    def to_rational(*args): return apply(_swiginac.basic_to_rational,args)
    def to_polynomial(*args): return apply(_swiginac.basic_to_polynomial,args)
    def integer_content(*args): return apply(_swiginac.basic_integer_content,args)
    def smod(*args): return apply(_swiginac.basic_smod,args)
    def max_coefficient(*args): return apply(_swiginac.basic_max_coefficient,args)
    def get_free_indices(*args): return apply(_swiginac.basic_get_free_indices,args)
    def add_indexed(*args): return apply(_swiginac.basic_add_indexed,args)
    def scalar_mul_indexed(*args): return apply(_swiginac.basic_scalar_mul_indexed,args)
    def contract_with(*args): return apply(_swiginac.basic_contract_with,args)
    def return_type(*args): return apply(_swiginac.basic_return_type,args)
    def return_type_tinfo(*args): return apply(_swiginac.basic_return_type_tinfo,args)
    def conjugate(*args): return apply(_swiginac.basic_conjugate,args)
    def print_dispatch(*args): return apply(_swiginac.basic_print_dispatch,args)
    def subs_one_level(*args): return apply(_swiginac.basic_subs_one_level,args)
    def diff(*args): return apply(_swiginac.basic_diff,args)
    def compare(*args): return apply(_swiginac.basic_compare,args)
    def is_equal(*args): return apply(_swiginac.basic_is_equal,args)
    def hold(*args): return apply(_swiginac.basic_hold,args)
    def gethash(*args): return apply(_swiginac.basic_gethash,args)
    def tinfo(*args): return apply(_swiginac.basic_tinfo,args)
    def setflag(*args): return apply(_swiginac.basic_setflag,args)
    def clearflag(*args): return apply(_swiginac.basic_clearflag,args)
    def __repr__(self):
        return "<C basic instance at %s>" % (self.this,)

class basicPtr(basic):
    def __init__(self,this):
        _swig_setattr(self, basic, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, basic, 'thisown', 0)
        _swig_setattr(self, basic,self.__class__,basic)
_swiginac.basic_swigregister(basicPtr)

quo = _swiginac.quo

rem = _swiginac.rem

decomp_rational = _swiginac.decomp_rational

prem = _swiginac.prem

sprem = _swiginac.sprem

divide = _swiginac.divide

sqrfree = _swiginac.sqrfree

sqrfree_parfrac = _swiginac.sqrfree_parfrac

collect_common_factors = _swiginac.collect_common_factors

resultant = _swiginac.resultant

class constant(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, constant, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, constant, name)
    def __init__(self,*args):
        _swig_setattr(self, constant, 'this', apply(_swiginac.new_constant,args))
        _swig_setattr(self, constant, 'thisown', 1)
    def gprint(*args): return apply(_swiginac.constant_gprint,args)
    def evalf(*args): return apply(_swiginac.constant_evalf,args)
    def __del__(self, destroy= _swiginac.delete_constant):
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
_swiginac.constant_swigregister(constantPtr)

class ex_lst(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ex_lst, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ex_lst, name)
    __swig_getmethods__["get_class_info_static"] = lambda x: _swiginac.ex_lst_get_class_info_static
    if _newclass:get_class_info_static = staticmethod(_swiginac.ex_lst_get_class_info_static)
    def get_class_info(*args): return apply(_swiginac.ex_lst_get_class_info,args)
    def class_name(*args): return apply(_swiginac.ex_lst_class_name,args)
    def archive(*args): return apply(_swiginac.ex_lst_archive,args)
    __swig_getmethods__["unarchive"] = lambda x: _swiginac.ex_lst_unarchive
    if _newclass:unarchive = staticmethod(_swiginac.ex_lst_unarchive)
    def duplicate(*args): return apply(_swiginac.ex_lst_duplicate,args)
    def accept(*args): return apply(_swiginac.ex_lst_accept,args)
    def __init__(self,*args):
        _swig_setattr(self, ex_lst, 'this', apply(_swiginac.new_ex_lst,args))
        _swig_setattr(self, ex_lst, 'thisown', 1)
    def info(*args): return apply(_swiginac.ex_lst_info,args)
    def precedence(*args): return apply(_swiginac.ex_lst_precedence,args)
    def nops(*args): return apply(_swiginac.ex_lst_nops,args)
    def op(*args): return apply(_swiginac.ex_lst_op,args)
    def eval(*args): return apply(_swiginac.ex_lst_eval,args)
    def subs(*args): return apply(_swiginac.ex_lst_subs,args)
    def prepend(*args): return apply(_swiginac.ex_lst_prepend,args)
    def append(*args): return apply(_swiginac.ex_lst_append,args)
    def remove_first(*args): return apply(_swiginac.ex_lst_remove_first,args)
    def remove_last(*args): return apply(_swiginac.ex_lst_remove_last,args)
    def remove_all(*args): return apply(_swiginac.ex_lst_remove_all,args)
    def sort(*args): return apply(_swiginac.ex_lst_sort,args)
    def unique(*args): return apply(_swiginac.ex_lst_unique,args)
    def begin(*args): return apply(_swiginac.ex_lst_begin,args)
    def end(*args): return apply(_swiginac.ex_lst_end,args)
    def rbegin(*args): return apply(_swiginac.ex_lst_rbegin,args)
    def rend(*args): return apply(_swiginac.ex_lst_rend,args)
    def let_op(*args): return apply(_swiginac.ex_lst_let_op,args)
    def set_op(*args): return apply(_swiginac.ex_lst_set_op,args)
    def __del__(self, destroy= _swiginac.delete_ex_lst):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C ex_lst instance at %s>" % (self.this,)

class ex_lstPtr(ex_lst):
    def __init__(self,this):
        _swig_setattr(self, ex_lst, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ex_lst, 'thisown', 0)
        _swig_setattr(self, ex_lst,self.__class__,ex_lst)
_swiginac.ex_lst_swigregister(ex_lstPtr)
Pi = cvar.Pi
Catalan = cvar.Catalan
Euler = cvar.Euler
ex_lst_get_class_info_static = _swiginac.ex_lst_get_class_info_static

ex_lst_unarchive = _swiginac.ex_lst_unarchive


class matrix(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, matrix, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, matrix, name)
    def __init__(self,*args):
        _swig_setattr(self, matrix, 'this', apply(_swiginac.new_matrix,args))
        _swig_setattr(self, matrix, 'thisown', 1)
    def nops(*args): return apply(_swiginac.matrix_nops,args)
    def op(*args): return apply(_swiginac.matrix_op,args)
    def let_op(*args): return apply(_swiginac.matrix_let_op,args)
    def eval(*args): return apply(_swiginac.matrix_eval,args)
    def evalm(*args): return apply(_swiginac.matrix_evalm,args)
    def subs(*args): return apply(_swiginac.matrix_subs,args)
    def eval_indexed(*args): return apply(_swiginac.matrix_eval_indexed,args)
    def add_indexed(*args): return apply(_swiginac.matrix_add_indexed,args)
    def scalar_mul_indexed(*args): return apply(_swiginac.matrix_scalar_mul_indexed,args)
    def contract_with(*args): return apply(_swiginac.matrix_contract_with,args)
    def conjugate(*args): return apply(_swiginac.matrix_conjugate,args)
    def rows(*args): return apply(_swiginac.matrix_rows,args)
    def cols(*args): return apply(_swiginac.matrix_cols,args)
    def add(*args): return apply(_swiginac.matrix_add,args)
    def sub(*args): return apply(_swiginac.matrix_sub,args)
    def mul(*args): return apply(_swiginac.matrix_mul,args)
    def mul_scalar(*args): return apply(_swiginac.matrix_mul_scalar,args)
    def pow(*args): return apply(_swiginac.matrix_pow,args)
    def __call__(*args): return apply(_swiginac.matrix___call__,args)
    def set(*args): return apply(_swiginac.matrix_set,args)
    def transpose(*args): return apply(_swiginac.matrix_transpose,args)
    def determinant(*args): return apply(_swiginac.matrix_determinant,args)
    def trace(*args): return apply(_swiginac.matrix_trace,args)
    def charpoly(*args): return apply(_swiginac.matrix_charpoly,args)
    def inverse(*args): return apply(_swiginac.matrix_inverse,args)
    def solve(*args): return apply(_swiginac.matrix_solve,args)
    def rank(*args): return apply(_swiginac.matrix_rank,args)
    def __del__(self, destroy= _swiginac.delete_matrix):
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
_swiginac.matrix_swigregister(matrixPtr)

nops = _swiginac.nops

expand = _swiginac.expand

eval = _swiginac.eval

evalf = _swiginac.evalf

rows = _swiginac.rows

cols = _swiginac.cols

transpose = _swiginac.transpose

determinant = _swiginac.determinant

trace = _swiginac.trace

charpoly = _swiginac.charpoly

inverse = _swiginac.inverse

rank = _swiginac.rank

lst_to_matrix = _swiginac.lst_to_matrix

diag_matrix = _swiginac.diag_matrix

class numeric(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, numeric, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, numeric, name)
    def __init__(self,*args):
        _swig_setattr(self, numeric, 'this', apply(_swiginac.new_numeric,args))
        _swig_setattr(self, numeric, 'thisown', 1)
    def gprint(*args): return apply(_swiginac.numeric_gprint,args)
    def coeff(*args): return apply(_swiginac.numeric_coeff,args)
    def eval(*args): return apply(_swiginac.numeric_eval,args)
    def evalf(*args): return apply(_swiginac.numeric_evalf,args)
    def add(*args): return apply(_swiginac.numeric_add,args)
    def sub(*args): return apply(_swiginac.numeric_sub,args)
    def mul(*args): return apply(_swiginac.numeric_mul,args)
    def div(*args): return apply(_swiginac.numeric_div,args)
    def power(*args): return apply(_swiginac.numeric_power,args)
    def __eq__(*args): return apply(_swiginac.numeric___eq__,args)
    def __ne__(*args): return apply(_swiginac.numeric___ne__,args)
    def __lt__(*args): return apply(_swiginac.numeric___lt__,args)
    def __le__(*args): return apply(_swiginac.numeric___le__,args)
    def __gt__(*args): return apply(_swiginac.numeric___gt__,args)
    def __ge__(*args): return apply(_swiginac.numeric___ge__,args)
    def to_int(*args): return apply(_swiginac.numeric_to_int,args)
    def to_long(*args): return apply(_swiginac.numeric_to_long,args)
    def to_double(*args): return apply(_swiginac.numeric_to_double,args)
    def real(*args): return apply(_swiginac.numeric_real,args)
    def imag(*args): return apply(_swiginac.numeric_imag,args)
    def __add__(*args): return apply(_swiginac.numeric___add__,args)
    def __sub__(*args): return apply(_swiginac.numeric___sub__,args)
    def __mul__(*args): return apply(_swiginac.numeric___mul__,args)
    def __div__(*args): return apply(_swiginac.numeric___div__,args)
    def __imul__(*args): return apply(_swiginac.numeric___imul__,args)
    def __isub(*args): return apply(_swiginac.numeric___isub,args)
    def __iadd__(*args): return apply(_swiginac.numeric___iadd__,args)
    def __idiv(*args): return apply(_swiginac.numeric___idiv,args)
    def __pos__(*args): return apply(_swiginac.numeric___pos__,args)
    def __neg__(*args): return apply(_swiginac.numeric___neg__,args)
    def __call__(*args): return apply(_swiginac.numeric___call__,args)
    def __del__(self, destroy= _swiginac.delete_numeric):
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
_swiginac.numeric_swigregister(numericPtr)
unit_matrix = _swiginac.unit_matrix

symbolic_matrix = _swiginac.symbolic_matrix


exp = _swiginac.exp

log = _swiginac.log

sin = _swiginac.sin

cos = _swiginac.cos

tan = _swiginac.tan

asin = _swiginac.asin

acos = _swiginac.acos

sinh = _swiginac.sinh

cosh = _swiginac.cosh

tanh = _swiginac.tanh

asinh = _swiginac.asinh

acosh = _swiginac.acosh

atanh = _swiginac.atanh

Li2 = _swiginac.Li2

zeta = _swiginac.zeta

lgamma = _swiginac.lgamma

tgamma = _swiginac.tgamma

factorial = _swiginac.factorial

doublefactorial = _swiginac.doublefactorial

binomial = _swiginac.binomial

bernoulli = _swiginac.bernoulli

fibonacci = _swiginac.fibonacci

isqrt = _swiginac.isqrt

abs = _swiginac.abs

mod = _swiginac.mod

smod = _swiginac.smod

PiEvalf = _swiginac.PiEvalf

EulerEvalf = _swiginac.EulerEvalf

CatalanEvalf = _swiginac.CatalanEvalf

class power(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, power, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, power, name)
    def __init__(self,*args):
        _swig_setattr(self, power, 'this', apply(_swiginac.new_power,args))
        _swig_setattr(self, power, 'thisown', 1)
    def precedence(*args): return apply(_swiginac.power_precedence,args)
    def info(*args): return apply(_swiginac.power_info,args)
    def nops(*args): return apply(_swiginac.power_nops,args)
    def op(*args): return apply(_swiginac.power_op,args)
    def map(*args): return apply(_swiginac.power_map,args)
    def degree(*args): return apply(_swiginac.power_degree,args)
    def ldegree(*args): return apply(_swiginac.power_ldegree,args)
    def coeff(*args): return apply(_swiginac.power_coeff,args)
    def eval(*args): return apply(_swiginac.power_eval,args)
    def evalf(*args): return apply(_swiginac.power_evalf,args)
    def evalm(*args): return apply(_swiginac.power_evalm,args)
    def series(*args): return apply(_swiginac.power_series,args)
    def subs(*args): return apply(_swiginac.power_subs,args)
    def normal(*args): return apply(_swiginac.power_normal,args)
    def to_rational(*args): return apply(_swiginac.power_to_rational,args)
    def to_polynomial(*args): return apply(_swiginac.power_to_polynomial,args)
    def get_free_indices(*args): return apply(_swiginac.power_get_free_indices,args)
    def conjugate(*args): return apply(_swiginac.power_conjugate,args)
    def __del__(self, destroy= _swiginac.delete_power):
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
_swiginac.power_swigregister(powerPtr)
atan = _swiginac.atan

psi = _swiginac.psi

irem = _swiginac.irem

iquo = _swiginac.iquo

gcd = _swiginac.gcd

lcm = _swiginac.lcm


pow = _swiginac.pow

class relational(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, relational, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, relational, name)
    equal = _swiginac.relational_equal
    not_equal = _swiginac.relational_not_equal
    less = _swiginac.relational_less
    less_or_equal = _swiginac.relational_less_or_equal
    greater = _swiginac.relational_greater
    greater_or_equal = _swiginac.relational_greater_or_equal
    def __init__(self,*args):
        _swig_setattr(self, relational, 'this', apply(_swiginac.new_relational,args))
        _swig_setattr(self, relational, 'thisown', 1)
    def gprint(*args): return apply(_swiginac.relational_gprint,args)
    def op(*args): return apply(_swiginac.relational_op,args)
    def eval(*args): return apply(_swiginac.relational_eval,args)
    def lhs(*args): return apply(_swiginac.relational_lhs,args)
    def rhs(*args): return apply(_swiginac.relational_rhs,args)
    def __del__(self, destroy= _swiginac.delete_relational):
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
_swiginac.relational_swigregister(relationalPtr)
sqrt = _swiginac.sqrt


class symbol(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, symbol, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, symbol, name)
    def __init__(self,*args):
        _swig_setattr(self, symbol, 'this', apply(_swiginac.new_symbol,args))
        _swig_setattr(self, symbol, 'thisown', 1)
    def gprint(*args): return apply(_swiginac.symbol_gprint,args)
    def eval(*args): return apply(_swiginac.symbol_eval,args)
    def evalf(*args): return apply(_swiginac.symbol_evalf,args)
    def __call__(*args): return apply(_swiginac.symbol___call__,args)
    def __del__(self, destroy= _swiginac.delete_symbol):
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
_swiginac.symbol_swigregister(symbolPtr)

EXPAIRSEQ_USE_HASHTAB = _swiginac.EXPAIRSEQ_USE_HASHTAB
conjugateepvector = _swiginac.conjugateepvector

class expairseq(basic):
    __swig_setmethods__ = {}
    for _s in [basic]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, expairseq, name, value)
    __swig_getmethods__ = {}
    for _s in [basic]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, expairseq, name)
    def __init__(self,*args):
        _swig_setattr(self, expairseq, 'this', apply(_swiginac.new_expairseq,args))
        _swig_setattr(self, expairseq, 'thisown', 1)
    def precedence(*args): return apply(_swiginac.expairseq_precedence,args)
    def info(*args): return apply(_swiginac.expairseq_info,args)
    def nops(*args): return apply(_swiginac.expairseq_nops,args)
    def op(*args): return apply(_swiginac.expairseq_op,args)
    def map(*args): return apply(_swiginac.expairseq_map,args)
    def eval(*args): return apply(_swiginac.expairseq_eval,args)
    def to_rational(*args): return apply(_swiginac.expairseq_to_rational,args)
    def to_polynomial(*args): return apply(_swiginac.expairseq_to_polynomial,args)
    def match(*args): return apply(_swiginac.expairseq_match,args)
    def subs(*args): return apply(_swiginac.expairseq_subs,args)
    def conjugate(*args): return apply(_swiginac.expairseq_conjugate,args)
    def __del__(self, destroy= _swiginac.delete_expairseq):
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
_swiginac.expairseq_swigregister(expairseqPtr)

class add(expairseq):
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, add, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, add, name)
    __swig_getmethods__["get_class_info_static"] = lambda x: _swiginac.add_get_class_info_static
    if _newclass:get_class_info_static = staticmethod(_swiginac.add_get_class_info_static)
    def get_class_info(*args): return apply(_swiginac.add_get_class_info,args)
    def class_name(*args): return apply(_swiginac.add_class_name,args)
    def archive(*args): return apply(_swiginac.add_archive,args)
    __swig_getmethods__["unarchive"] = lambda x: _swiginac.add_unarchive
    if _newclass:unarchive = staticmethod(_swiginac.add_unarchive)
    def duplicate(*args): return apply(_swiginac.add_duplicate,args)
    def accept(*args): return apply(_swiginac.add_accept,args)
    def __init__(self,*args):
        _swig_setattr(self, add, 'this', apply(_swiginac.new_add,args))
        _swig_setattr(self, add, 'thisown', 1)
    def precedence(*args): return apply(_swiginac.add_precedence,args)
    def info(*args): return apply(_swiginac.add_info,args)
    def degree(*args): return apply(_swiginac.add_degree,args)
    def ldegree(*args): return apply(_swiginac.add_ldegree,args)
    def coeff(*args): return apply(_swiginac.add_coeff,args)
    def eval(*args): return apply(_swiginac.add_eval,args)
    def evalm(*args): return apply(_swiginac.add_evalm,args)
    def series(*args): return apply(_swiginac.add_series,args)
    def normal(*args): return apply(_swiginac.add_normal,args)
    def integer_content(*args): return apply(_swiginac.add_integer_content,args)
    def smod(*args): return apply(_swiginac.add_smod,args)
    def max_coefficient(*args): return apply(_swiginac.add_max_coefficient,args)
    def conjugate(*args): return apply(_swiginac.add_conjugate,args)
    def get_free_indices(*args): return apply(_swiginac.add_get_free_indices,args)
    def eval_ncmul(*args): return apply(_swiginac.add_eval_ncmul,args)
    def __del__(self, destroy= _swiginac.delete_add):
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
_swiginac.add_swigregister(addPtr)
add_get_class_info_static = _swiginac.add_get_class_info_static

add_unarchive = _swiginac.add_unarchive


class mul(expairseq):
    __swig_setmethods__ = {}
    for _s in [expairseq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, mul, name, value)
    __swig_getmethods__ = {}
    for _s in [expairseq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, mul, name)
    def __init__(self,*args):
        _swig_setattr(self, mul, 'this', apply(_swiginac.new_mul,args))
        _swig_setattr(self, mul, 'thisown', 1)
    def precedence(*args): return apply(_swiginac.mul_precedence,args)
    def info(*args): return apply(_swiginac.mul_info,args)
    def degree(*args): return apply(_swiginac.mul_degree,args)
    def ldegree(*args): return apply(_swiginac.mul_ldegree,args)
    def coeff(*args): return apply(_swiginac.mul_coeff,args)
    def eval(*args): return apply(_swiginac.mul_eval,args)
    def evalf(*args): return apply(_swiginac.mul_evalf,args)
    def evalm(*args): return apply(_swiginac.mul_evalm,args)
    def series(*args): return apply(_swiginac.mul_series,args)
    def normal(*args): return apply(_swiginac.mul_normal,args)
    def integer_content(*args): return apply(_swiginac.mul_integer_content,args)
    def smod(*args): return apply(_swiginac.mul_smod,args)
    def max_coefficient(*args): return apply(_swiginac.mul_max_coefficient,args)
    def get_free_indices(*args): return apply(_swiginac.mul_get_free_indices,args)
    def algebraic_subs_mul(*args): return apply(_swiginac.mul_algebraic_subs_mul,args)
    def __del__(self, destroy= _swiginac.delete_mul):
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
_swiginac.mul_swigregister(mulPtr)

class function_options(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, function_options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, function_options, name)
    def __init__(self,*args):
        _swig_setattr(self, function_options, 'this', apply(_swiginac.new_function_options,args))
        _swig_setattr(self, function_options, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_function_options):
        try:
            if self.thisown: destroy(self)
        except: pass
    def initialize(*args): return apply(_swiginac.function_options_initialize,args)
    def dummy(*args): return apply(_swiginac.function_options_dummy,args)
    def set_name(*args): return apply(_swiginac.function_options_set_name,args)
    def latex_name(*args): return apply(_swiginac.function_options_latex_name,args)
    def eval_func(*args): return apply(_swiginac.function_options_eval_func,args)
    def evalf_func(*args): return apply(_swiginac.function_options_evalf_func,args)
    def conjugate_func(*args): return apply(_swiginac.function_options_conjugate_func,args)
    def derivative_func(*args): return apply(_swiginac.function_options_derivative_func,args)
    def series_func(*args): return apply(_swiginac.function_options_series_func,args)
    def set_return_type(*args): return apply(_swiginac.function_options_set_return_type,args)
    def do_not_evalf_params(*args): return apply(_swiginac.function_options_do_not_evalf_params,args)
    def remember(*args): return apply(_swiginac.function_options_remember,args)
    def overloaded(*args): return apply(_swiginac.function_options_overloaded,args)
    def set_symmetry(*args): return apply(_swiginac.function_options_set_symmetry,args)
    def get_name(*args): return apply(_swiginac.function_options_get_name,args)
    def get_nparams(*args): return apply(_swiginac.function_options_get_nparams,args)
    def __repr__(self):
        return "<C function_options instance at %s>" % (self.this,)

class function_optionsPtr(function_options):
    def __init__(self,this):
        _swig_setattr(self, function_options, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, function_options, 'thisown', 0)
        _swig_setattr(self, function_options,self.__class__,function_options)
_swiginac.function_options_swigregister(function_optionsPtr)

class do_taylor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, do_taylor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, do_taylor, name)
    def __init__(self,*args):
        _swig_setattr(self, do_taylor, 'this', apply(_swiginac.new_do_taylor,args))
        _swig_setattr(self, do_taylor, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_do_taylor):
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
_swiginac.do_taylor_swigregister(do_taylorPtr)

class function(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, function, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, function, name)
    def __init__(self,*args):
        _swig_setattr(self, function, 'this', apply(_swiginac.new_function,args))
        _swig_setattr(self, function, 'thisown', 1)
    def gprint(*args): return apply(_swiginac.function_gprint,args)
    def precedence(*args): return apply(_swiginac.function_precedence,args)
    def expand(*args): return apply(_swiginac.function_expand,args)
    def eval(*args): return apply(_swiginac.function_eval,args)
    def evalf(*args): return apply(_swiginac.function_evalf,args)
    def calchash(*args): return apply(_swiginac.function_calchash,args)
    def series(*args): return apply(_swiginac.function_series,args)
    def thiscontainer(*args): return apply(_swiginac.function_thiscontainer,args)
    def conjugate(*args): return apply(_swiginac.function_conjugate,args)
    __swig_getmethods__["register_new"] = lambda x: _swiginac.function_register_new
    if _newclass:register_new = staticmethod(_swiginac.function_register_new)
    __swig_getmethods__["find_function"] = lambda x: _swiginac.function_find_function
    if _newclass:find_function = staticmethod(_swiginac.function_find_function)
    def get_serial(*args): return apply(_swiginac.function_get_serial,args)
    def get_name(*args): return apply(_swiginac.function_get_name,args)
    def __del__(self, destroy= _swiginac.delete_function):
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
_swiginac.function_swigregister(functionPtr)
function_register_new = _swiginac.function_register_new

function_find_function = _swiginac.function_find_function


class abs_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, abs_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, abs_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, abs_SERIAL, 'this', apply(_swiginac.new_abs_SERIAL,args))
        _swig_setattr(self, abs_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_abs_SERIAL):
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
_swiginac.abs_SERIAL_swigregister(abs_SERIALPtr)

class csgn_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, csgn_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, csgn_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, csgn_SERIAL, 'this', apply(_swiginac.new_csgn_SERIAL,args))
        _swig_setattr(self, csgn_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_csgn_SERIAL):
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
_swiginac.csgn_SERIAL_swigregister(csgn_SERIALPtr)
abs_NPARAMS = cvar.abs_NPARAMS

class eta_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eta_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, eta_SERIAL, 'this', apply(_swiginac.new_eta_SERIAL,args))
        _swig_setattr(self, eta_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_eta_SERIAL):
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
_swiginac.eta_SERIAL_swigregister(eta_SERIALPtr)
csgn_NPARAMS = cvar.csgn_NPARAMS

class sin_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sin_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, sin_SERIAL, 'this', apply(_swiginac.new_sin_SERIAL,args))
        _swig_setattr(self, sin_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_sin_SERIAL):
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
_swiginac.sin_SERIAL_swigregister(sin_SERIALPtr)
eta_NPARAMS = cvar.eta_NPARAMS

class cos_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cos_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, cos_SERIAL, 'this', apply(_swiginac.new_cos_SERIAL,args))
        _swig_setattr(self, cos_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_cos_SERIAL):
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
_swiginac.cos_SERIAL_swigregister(cos_SERIALPtr)
sin_NPARAMS = cvar.sin_NPARAMS

class tan_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tan_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tan_SERIAL, 'this', apply(_swiginac.new_tan_SERIAL,args))
        _swig_setattr(self, tan_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_tan_SERIAL):
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
_swiginac.tan_SERIAL_swigregister(tan_SERIALPtr)
cos_NPARAMS = cvar.cos_NPARAMS

class exp_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, exp_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, exp_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, exp_SERIAL, 'this', apply(_swiginac.new_exp_SERIAL,args))
        _swig_setattr(self, exp_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_exp_SERIAL):
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
_swiginac.exp_SERIAL_swigregister(exp_SERIALPtr)
tan_NPARAMS = cvar.tan_NPARAMS

class log_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, log_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, log_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, log_SERIAL, 'this', apply(_swiginac.new_log_SERIAL,args))
        _swig_setattr(self, log_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_log_SERIAL):
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
_swiginac.log_SERIAL_swigregister(log_SERIALPtr)
exp_NPARAMS = cvar.exp_NPARAMS

class asin_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asin_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asin_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, asin_SERIAL, 'this', apply(_swiginac.new_asin_SERIAL,args))
        _swig_setattr(self, asin_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_asin_SERIAL):
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
_swiginac.asin_SERIAL_swigregister(asin_SERIALPtr)
log_NPARAMS = cvar.log_NPARAMS

class acos_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acos_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acos_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, acos_SERIAL, 'this', apply(_swiginac.new_acos_SERIAL,args))
        _swig_setattr(self, acos_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_acos_SERIAL):
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
_swiginac.acos_SERIAL_swigregister(acos_SERIALPtr)
asin_NPARAMS = cvar.asin_NPARAMS

class atan_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atan_SERIAL, 'this', apply(_swiginac.new_atan_SERIAL,args))
        _swig_setattr(self, atan_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_atan_SERIAL):
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
_swiginac.atan_SERIAL_swigregister(atan_SERIALPtr)
acos_NPARAMS = cvar.acos_NPARAMS

class atan2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atan2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atan2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atan2_SERIAL, 'this', apply(_swiginac.new_atan2_SERIAL,args))
        _swig_setattr(self, atan2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_atan2_SERIAL):
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
_swiginac.atan2_SERIAL_swigregister(atan2_SERIALPtr)
atan_NPARAMS = cvar.atan_NPARAMS

class sinh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sinh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, sinh_SERIAL, 'this', apply(_swiginac.new_sinh_SERIAL,args))
        _swig_setattr(self, sinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_sinh_SERIAL):
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
_swiginac.sinh_SERIAL_swigregister(sinh_SERIALPtr)
atan2_NPARAMS = cvar.atan2_NPARAMS

class cosh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cosh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, cosh_SERIAL, 'this', apply(_swiginac.new_cosh_SERIAL,args))
        _swig_setattr(self, cosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_cosh_SERIAL):
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
_swiginac.cosh_SERIAL_swigregister(cosh_SERIALPtr)
sinh_NPARAMS = cvar.sinh_NPARAMS

class tanh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tanh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tanh_SERIAL, 'this', apply(_swiginac.new_tanh_SERIAL,args))
        _swig_setattr(self, tanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_tanh_SERIAL):
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
_swiginac.tanh_SERIAL_swigregister(tanh_SERIALPtr)
cosh_NPARAMS = cvar.cosh_NPARAMS

class asinh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, asinh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, asinh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, asinh_SERIAL, 'this', apply(_swiginac.new_asinh_SERIAL,args))
        _swig_setattr(self, asinh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_asinh_SERIAL):
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
_swiginac.asinh_SERIAL_swigregister(asinh_SERIALPtr)
tanh_NPARAMS = cvar.tanh_NPARAMS

class acosh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, acosh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, acosh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, acosh_SERIAL, 'this', apply(_swiginac.new_acosh_SERIAL,args))
        _swig_setattr(self, acosh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_acosh_SERIAL):
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
_swiginac.acosh_SERIAL_swigregister(acosh_SERIALPtr)
asinh_NPARAMS = cvar.asinh_NPARAMS

class atanh_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, atanh_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, atanh_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, atanh_SERIAL, 'this', apply(_swiginac.new_atanh_SERIAL,args))
        _swig_setattr(self, atanh_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_atanh_SERIAL):
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
_swiginac.atanh_SERIAL_swigregister(atanh_SERIALPtr)
acosh_NPARAMS = cvar.acosh_NPARAMS

class Li2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Li2_SERIAL, 'this', apply(_swiginac.new_Li2_SERIAL,args))
        _swig_setattr(self, Li2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_Li2_SERIAL):
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
_swiginac.Li2_SERIAL_swigregister(Li2_SERIALPtr)
atanh_NPARAMS = cvar.atanh_NPARAMS

class Li3_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Li3_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Li3_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Li3_SERIAL, 'this', apply(_swiginac.new_Li3_SERIAL,args))
        _swig_setattr(self, Li3_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_Li3_SERIAL):
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
_swiginac.Li3_SERIAL_swigregister(Li3_SERIALPtr)
Li2_NPARAMS = cvar.Li2_NPARAMS

class zeta1_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zeta1_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zeta1_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, zeta1_SERIAL, 'this', apply(_swiginac.new_zeta1_SERIAL,args))
        _swig_setattr(self, zeta1_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_zeta1_SERIAL):
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
_swiginac.zeta1_SERIAL_swigregister(zeta1_SERIALPtr)
Li3_NPARAMS = cvar.Li3_NPARAMS

class zeta2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zeta2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zeta2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, zeta2_SERIAL, 'this', apply(_swiginac.new_zeta2_SERIAL,args))
        _swig_setattr(self, zeta2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_zeta2_SERIAL):
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
_swiginac.zeta2_SERIAL_swigregister(zeta2_SERIALPtr)

class lgamma_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lgamma_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, lgamma_SERIAL, 'this', apply(_swiginac.new_lgamma_SERIAL,args))
        _swig_setattr(self, lgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_lgamma_SERIAL):
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
_swiginac.lgamma_SERIAL_swigregister(lgamma_SERIALPtr)

class tgamma_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tgamma_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tgamma_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, tgamma_SERIAL, 'this', apply(_swiginac.new_tgamma_SERIAL,args))
        _swig_setattr(self, tgamma_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_tgamma_SERIAL):
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
_swiginac.tgamma_SERIAL_swigregister(tgamma_SERIALPtr)
lgamma_NPARAMS = cvar.lgamma_NPARAMS

class beta_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, beta_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, beta_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, beta_SERIAL, 'this', apply(_swiginac.new_beta_SERIAL,args))
        _swig_setattr(self, beta_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_beta_SERIAL):
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
_swiginac.beta_SERIAL_swigregister(beta_SERIALPtr)
tgamma_NPARAMS = cvar.tgamma_NPARAMS

class psi1_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psi1_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psi1_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, psi1_SERIAL, 'this', apply(_swiginac.new_psi1_SERIAL,args))
        _swig_setattr(self, psi1_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_psi1_SERIAL):
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
_swiginac.psi1_SERIAL_swigregister(psi1_SERIALPtr)
beta_NPARAMS = cvar.beta_NPARAMS

class psi2_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psi2_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psi2_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, psi2_SERIAL, 'this', apply(_swiginac.new_psi2_SERIAL,args))
        _swig_setattr(self, psi2_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_psi2_SERIAL):
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
_swiginac.psi2_SERIAL_swigregister(psi2_SERIALPtr)

class factorial_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, factorial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, factorial_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, factorial_SERIAL, 'this', apply(_swiginac.new_factorial_SERIAL,args))
        _swig_setattr(self, factorial_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_factorial_SERIAL):
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
_swiginac.factorial_SERIAL_swigregister(factorial_SERIALPtr)

class binomial_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, binomial_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, binomial_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, binomial_SERIAL, 'this', apply(_swiginac.new_binomial_SERIAL,args))
        _swig_setattr(self, binomial_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_binomial_SERIAL):
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
_swiginac.binomial_SERIAL_swigregister(binomial_SERIALPtr)
factorial_NPARAMS = cvar.factorial_NPARAMS

class Order_SERIAL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Order_SERIAL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Order_SERIAL, name)
    def __init__(self,*args):
        _swig_setattr(self, Order_SERIAL, 'this', apply(_swiginac.new_Order_SERIAL,args))
        _swig_setattr(self, Order_SERIAL, 'thisown', 1)
    def __del__(self, destroy= _swiginac.delete_Order_SERIAL):
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
_swiginac.Order_SERIAL_swigregister(Order_SERIALPtr)
binomial_NPARAMS = cvar.binomial_NPARAMS

__eq__ = _swiginac.__eq__

__ne__ = _swiginac.__ne__

__lt__ = _swiginac.__lt__

__le__ = _swiginac.__le__

__gt__ = _swiginac.__gt__

__ge__ = _swiginac.__ge__

__lshift__ = _swiginac.__lshift__

__rshift__ = _swiginac.__rshift__

dflt = _swiginac.dflt

latex = _swiginac.latex

python = _swiginac.python

python_repr = _swiginac.python_repr

tree = _swiginac.tree

csrc = _swiginac.csrc

csrc_float = _swiginac.csrc_float

csrc_double = _swiginac.csrc_double

csrc_cl_N = _swiginac.csrc_cl_N

index_dimensions = _swiginac.index_dimensions

no_index_dimensions = _swiginac.no_index_dimensions

exp_ex = _swiginac.exp_ex

log_ex = _swiginac.log_ex

sin_ex = _swiginac.sin_ex

cos_ex = _swiginac.cos_ex

tan_ex = _swiginac.tan_ex

asin_ex = _swiginac.asin_ex

acos_ex = _swiginac.acos_ex

atan_ex = _swiginac.atan_ex

sinh_ex = _swiginac.sinh_ex

cosh_ex = _swiginac.cosh_ex

tanh_ex = _swiginac.tanh_ex

asinh_ex = _swiginac.asinh_ex

acosh_ex = _swiginac.acosh_ex

atanh_ex = _swiginac.atanh_ex

Li2_ex = _swiginac.Li2_ex

zeta_ex = _swiginac.zeta_ex

lgamma_ex = _swiginac.lgamma_ex

tgamma_ex = _swiginac.tgamma_ex

psi_ex = _swiginac.psi_ex

factorial_ex = _swiginac.factorial_ex

binomial_ex_ex = _swiginac.binomial_ex_ex

abs_ex = _swiginac.abs_ex

Order_NPARAMS = cvar.Order_NPARAMS
__mul__ = _swiginac.__mul__

__div__ = _swiginac.__div__

__iadd__ = _swiginac.__iadd__

__isub__ = _swiginac.__isub__

__imul__ = _swiginac.__imul__

__idiv__ = _swiginac.__idiv__

__add__ = _swiginac.__add__

__sub__ = _swiginac.__sub__


