from Symbolic import *
from Famms import *
import unittest

class PythonCBTestCase(unittest.TestCase):

    def testPython(self):
        
        def F(u):
            return div(grad(u))
        
        famms = Famms(2, simtype="Python")
        (x, y) = famms.x
        v = sin(x)*cos(y)
        
        famms.assign(equation=F, solution=v)
        
        (solution, source) = famms.getCallbacks()
        
        pt = (1.0, 1.0)
        print "\nThe callbacks return the folloging values at the points (%f, %f)" % (pt[0], pt[1])
        print "Analytical solution:\t%10f" % solution.evalPt(pt)
        print "Source term:\t\t%10f" % source.evalPt(pt)
        
        import math
        import operator
        epsilon = 1e-15 # Allow slightly different answers due to different number handling
        print "\nThe precomputed solution at this point is:"
        print "Analytical solution:\t%10f" % (math.sin(pt[0]) * math.cos(pt[1]))
        print "Source term:\t\t%10f" % (-2*math.sin(pt[0])*math.cos(pt[1]))
        assert operator.abs(solution.evalPt(pt) - math.sin(pt[0]) * math.cos(pt[1])) < epsilon
        assert operator.abs(source.evalPt(pt) - -2*math.sin(pt[0])*math.cos(pt[1])) < epsilon 
        
suite = unittest.makeSuite(PythonCBTestCase)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
    
