'''
Created on Feb 9, 2015

@author: ryan
'''
import numpy as np

from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.lumped.Series import Series
from python.ee.rf.network.elements.distributed.TRL import TRL
from python.ee.rf.network.elements.lumped.TNetwork import TNetwork
from python.ee.rf.network.elements.lumped.Shunt import Shunt
from python.ee.rf.network.elements.S2Port import S2Port
from python.ee.rf.network.elements.lumped.Amplifier import Amplifier

def p1():
    L = 3e-9
    w = 2 * np.pi * 7.5e9
    impedance = 1j* w * L
    sh = Series(1, 2, impedance = impedance, z0=50.0, zs=50.0, zl=50.0)
    print "s11", ComplexToPhasor(sh.GetS11())
    print "s12", ComplexToPhasor(sh.GetS12())
    print "s21", ComplexToPhasor(sh.GetS21())
    print "s22", ComplexToPhasor(sh.GetS22())
    
    
def p12_4():
    
    s11 = PhasorToComplex(.88, -115.0)
    s12 = PhasorToComplex(.029, 31.0)
    s21 = PhasorToComplex(9.4, 110.0)
    s22 = PhasorToComplex(.328, -67.0)
    
    a = Amplifier(1, 2, s11, s12, s21, s22)
    print a.IsStable()

def p12_9():
    s11_8GHz = PhasorToComplex(.52, 179.0)
    s12_8GHz = PhasorToComplex(.14, -1.0)
    s21_8GHz = PhasorToComplex(2.0, 20.0)
    s22_8GHz = PhasorToComplex(.42, -129.0)
    a = Amplifier(1, 2, s11_8GHz, s12_8GHz, s21_8GHz, s22_8GHz)
    gammaS = a.GetGammaSMaxGain()
    gammaL = a.GetGammaLMaxGain()
    
    print "Gamma S matched", ComplexToPhasor(gammaS)
    print "Gamma L matched", ComplexToPhasor(gammaL)
    
def p12_11():
    s11_6GHz = PhasorToComplex(.61, -170.0)
    s12_6GHz = 0.0
    s21_6GHz = PhasorToComplex(2.24, 32.0)
    s22_6GHz = PhasorToComplex(.72, -83.0)
    
    a = Amplifier(1, 2, s11_6GHz, s12_6GHz, s21_6GHz, s22_6GHz)
    
    gammaS = a.GetGammaSMaxGain()
    gammaL = a.GetGammaLMaxGain()
    print "Gamma S matched", ComplexToPhasor(gammaS)
    print "Gamma L matched", ComplexToPhasor(gammaL)    

if __name__ == '__main__':
    p12_11()