#!/usr/bin/env python

"""Fully Automated Method of Manufactured Solutions

Usage: f=famms.famms(nsd=2, time=None, space_symbs=None, simtype='DP', **kwargs)

f.assign(equation=eq, solution=sol, simulator=sim)
where equation is a function defining the governing equation, solution is a
solution defined in GiNaC, and simulator is a C++ simulator, equipped with a
Python interface, and extended with two methods: 
set_v_func(anaytical solution) and set_b_func (source) """


"""Notes to self: Consider replacing the type switch with a polymorphism (or as
an argument to the SimType method getfunctors()"""

FammsError = "Famms Error"

"""Polymorphism for the callbacks"""

class PyFunctor(object):
    """Python callback functor. The method 'attach' must be defined and accept the
    Famms methods _vValue, b_Value, and _vGrad arguments.  Various methods for
    point evaluation could be added to this class, if needed in a spesific
    application."""

    def attach(self, *args):
        self.funcs = args

    def evalPt(self, point, time=0.0):
        return self.funcs[0](point, time)

    def evalGradPt(self, point, time=0.0):
        return self.funcs[1](point, time)

    def __call__(self, point, time=0.0):
        return self.evalPt(point, time)

class SimType(object):
    def __init__(self):
        self.type=None

    def getfunctors(self):
        return (None, None)

class DPSim(SimType):
    def __init__(self):
        self.type = "Diffpack Simulator"

    def getfunctors(self):
        return (FieldFuncPython, FieldsFuncPython)

class CppSim(SimType):
    def __init__(self):
        self.type = "C++ Simulator using functors"

    def getfunctors(self):
        return (PyCppFunctor, PyCppFunctor)

class PythonSim(SimType):
    def __init__(self):
        self.type = "Python Simulator"

    def getfunctors(self):
        return (PyFunctor, PyFunctor)

"""Factory method for selecting simulator type"""
def SimTypeFactory(type):
    if type == "DP":
        return DPSim()
    elif type == "Cpp":
        return CppSim()
    elif (type == "Fortran" or type == "Python"):
        return PythonSim()
    else:
        raise TypeError, "Unknown Simulator Type %s" % type

from Symbolic import Symbol, Expr, grad
try:
    from dputils.DP import FieldFuncPython, FieldsFuncPython
#    from dputils.utils import *
except:
    pass
#    raise FammsError, "Could not import Diffpack Callback modules"
try:
    from Callback.PyCppFunctor import PyCppFunctor 
except:
    pass
#    raise FammsError, "Could not import Python-C++ Callback modules"


class Famms(object):
      
    """Fully Automatic Method of Manufactured Solutions
    Lightweight class for attaching a manufactured solution and the
    corresponding source terms to scalar or vector PDEs.
    """ 

    __module__ = __name__

    def __init__(self, nsd=2, time=None, space_symbs=None, simtype="DP", **kwargs):
        """ Instansiate the famms object. Arguments are: 
        * nsd (int=2) : The number of space dimensions for the PDE
        * time (symbol=None): The symbol for time
        * space_symbs (symbol=None): List of the symbols involved.
        * simtype (string='DP'): The simulator type """
        if space_symbs:
            self.x = space_symbs
            self.n = len(space_symbs)
        else:
            self.x = []
            self.n = nsd
            for i in range(nsd):
                symb = "x_%i"%i
                self.x.append(Symbol(symb))
        self.t = None
        if isinstance(time, Symbol): 
            self.t = time
        elif time:
            self.t = Symbol('t')
        self.simtype = simtype
        """Replace conditional with polymorphism"""
        self.simtype_obj = SimTypeFactory(simtype) 
        # Todo: Move the definition of the method to attach callbacks to SimType
        self.v_func_name = "set_v_func"
        self.b_func_name = "set_b_func"
        if kwargs: # Additional Python callbacks can be passed as keyword arguments
            self.extra_callbacks = kwargs
 
    def setCallBackNames(self, v_name, b_name):
        """If the simulator interface requires a non default function name for
        binding the functor callback, set these names here"""
        # Todo: update the v_func_name in self.simtype_obj 
        self.v_func_name = v_name
        self.b_func_name = b_name
 
    def assign(self, equation=None, solution=None, simulator=None, couple_list=None):
        """Based on equation and solution, build source term and send 
        the Python callbacks to the simulator.
        """
        if (not equation) or (not solution):
            raise FammsError, "You must at least specify the equation and the solution in assign()"
 
        solution.setSpatialSymbols(self.x)
        if not (couple_list):
        #    solution.set_spatial_symbs(self.x)
            couple_list = [solution]
        self.initMMS(equation, solution, couple_list)
        self.createCallbacks()
        if simulator:
            self.insertCallbacks(simulator)
            if self.__dict__.has_key('extra_callbacks'):
                self.insertExtraCallbacks(self, simulator, self.extra_callbacks)
        self.sim = simulator
 

    def insertExtraCallbacks(self, sim, extra_callbacks, type_='scalar'):
        """Insert Python functions as callbacks in the simulator. We assume that
        the simulator can set the Python callback using 'set_%s', where %s is the
        dictionary key for the Python function."""
        for k in extra_callbacks:
            exec("sim.set_%s(self._as_callback(extra_callbacks[k], type_=type_))" % k)
 
    def initMMS(self, F, v, couple_list):
        self.F = F; self.v = v
        all_symbs = []
        all_symbs.extend(self.x); 
        if self.t:
            all_symbs.append(self.t)
        self.b = F(*couple_list).simplify()
        self.v.initEval(all_symbs)
        self.b.initEval(all_symbs)
        self.v_grad = grad(self.v)
        self.v_grad.initEval(all_symbs)
 
    def createCallbacks(self):
        """Wrap the functions _value_v and _value_b in functors"""        
        if isinstance(self.v, Expr):
            type_ = 'scalar'
        else:
            type_ = 'vector' # Lazy assumption
        self.v_func = self._asCallback(self._vValue, self._vGrad, type_ = type_)
        self.b_func = self._asCallback(self._bValue, type_ = type_)

    def insertCallbacks(self, simulator):
        """Attach the callbacks to the simulator by calling the simulator
        methods v_func_name and b_func_name."""
        try:
            exec("simulator.%s(self.v_func)" % self.v_func_name)
            exec("simulator.%s(self.b_func)" % self.b_func_name)
        except:
            raise FammsError, "Could not attach functors to the simulator using \
            the method '%s' and '%s'" % (self.v_func_name, self.b_func_name)

#    def setCallback(self,cb):
#        self.userfunc = cb

    def getCallbacks(self):
        return (self.v_func, self. b_func)
 
    def _asCallback(self, *args, **kwargs):
        """ Convert the Python function objects to a Python callback. If using
        Famms with some exotic C++/Fortran or even Python simulator, extend this
        method fit the framework."""
        functype = None; funcstype = None
        """Replace conditional with polymorphism"""
        (functype, funcstype) = self.simtype_obj.getfunctors()
        """Old construct:
        if self.simtype == "DP":
            functype = FieldFuncPython; funcstype = FieldsFuncPython
        elif self.simtype == "C++":
            functype = pyevalPt; funcstype = pyevalPt
        elif self.simtype == "UserDefined":
            functype = self.userfunc
        else:
            raise FammsError, "Python Callback for '%s' not implemented!\n" % (self.simtype, )
"""
        if kwargs['type_'] == 'scalar':
            func = functype()
        else :
            func = funcstype()
#        print type(func)
        func.thisown = 0
        func.attach(*args)
        return func
 
    def _vValue(self, point, time):
        """This is the point eval of the analytical solution. Pass the point to
        the symbolic.expression v, that returns float
        """
        try:
            retVal = self.v.eval(*(point+(time, )))
        except:
            raise FammsError, "Could not evaluate the analytical solution"
        return retVal 
 
    def _bValue(self, point, time):
        """This is the point eval of the source term. Pass the point to
        the symbolic.expr b, that returns float
        """
        try:
            retVal = self.b.eval(*(point+(time, )))
        except:
            raise FammsError, "Could not evaluate the source term"
        return retVal 
 
    def _vGrad(self, point, time):
        try:
            retVal = self.v_grad.eval(*(point+(time, )))
        except:
            raise FammsError, "Could not evaluate the gradient of the analytical solution"
        return retVal
