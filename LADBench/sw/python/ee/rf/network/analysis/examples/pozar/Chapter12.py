'''
Created on Feb 10, 2015

@author: ryan
'''
from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.S2Port import S2Port

def Example2():
    print "Example 2"
    print "#################################################################"
    s11 = PhasorToComplex(.869, -159.0)
    s12 = PhasorToComplex(.031, -9.0)
    s21 = PhasorToComplex(4.250, 61.0)
    s22 = PhasorToComplex(.507, -117.0)
    s = S2Port(1, 2, s11, s12, s21, s22)
    
    print "K", s.CalcK()
    print "Delta", ComplexToPhasor(s.CalcDelta())
    print "Is stable?", s.IsStable()
    print "Cl", ComplexToPhasor(s.CalcCl())
    print "Rl", ComplexToPhasor(s.CalcRl())
    print "Cs", ComplexToPhasor(s.CalcCs())
    print "Rs", ComplexToPhasor(s.CalcRs())
    
if __name__ == '__main__':
    Example2()