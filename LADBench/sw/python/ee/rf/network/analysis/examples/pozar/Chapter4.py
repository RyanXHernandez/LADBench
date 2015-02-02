'''
Created on Feb 1, 2015

@author: ryan
'''
from python.math.number.complex.Util import PhasorToComplex
from python.ee.rf.network.elements.S2Port import S2Port

def Example5():
    z0 = 50.0
    zs = z0
    zl = zs
    s11 = PhasorToComplex(.15, 0.0)
    s12 = PhasorToComplex(.85, -45.0)
    s21 = PhasorToComplex(.85, 45.0)
    s22 = PhasorToComplex(.2, 0.0)
    sm = S2Port(1, 2, s11, s12, s21, s22, z0, zs, zl)
    print sm.GetReturnLoss()

if __name__ == '__main__':
    
    Example5()