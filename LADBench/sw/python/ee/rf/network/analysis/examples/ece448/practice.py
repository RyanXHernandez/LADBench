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

def p1():
    L = 3e-9
    w = 2 * np.pi * 7.5e9
    impedance = 1j* w * L
    sh = Series(1, 2, impedance = impedance, z0=50.0, zs=50.0, zl=50.0)
    print "s11", ComplexToPhasor(sh.GetS11())
    print "s12", ComplexToPhasor(sh.GetS12())
    print "s21", ComplexToPhasor(sh.GetS21())
    print "s22", ComplexToPhasor(sh.GetS22())
    
    

def template():
    print "s11",
    print "s12",
    print "s21",
    print "s22",
    

p1()