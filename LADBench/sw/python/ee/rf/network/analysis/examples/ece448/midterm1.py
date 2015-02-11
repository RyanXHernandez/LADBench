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
    pass

def p2():
    z0 = 50.0
    zs = 50.0
    zl = 50.0
    zs = 50.0#20.0 - 22.5j
    t = TRL(node1=1, node2=2, impedance=50.0, alpha=0.0, beta=2*np.pi, length=.092, z0=z0, zs=zs, zl=zl)
    se = Series(node1=1, node2=2, impedance=-60j, z0=z0, zs=zs, zl=zl)
    cascade = t * se
    print cascade.GetInputVSWR()

def p3():
    s11 = PhasorToComplex(.45, 150.0)
    s12 = PhasorToComplex(.01, -10.0)
    s21 = PhasorToComplex(2.05, 10.0)
    s22 = PhasorToComplex(.4, -150.0)
    zs = 50.0
    zl = 50.0
    z0 = 50.0
    s2 = S2Port(node1=1, node2=2, s11=s11, s12=s12, s21=s21, s22=s22, z0=z0, zs=zs, zl=zl)
    print "Insertion Loss", s2.GetInsertionLoss()
    gammaL = PhasorToComplex(.25, 150.0)
    gammaS = PhasorToComplex(.43, -170.0)
    s2.SetGammaL(gammaL)
    s2.SetGammaS(gammaS)
    print "Insertion Loss Prime", s2.GetInsertionLossPrime()
    print ComplexToPhasor(2.42191 + .224847j)

def p4():
    L = .8e-9
    w = 2* np.pi * 10e9
    impedanceL = 1j*w*L
    z0 = 50.0
    zl = 50.0
    zs = 50.0
    se = Series(node1=1, node2=2, impedance=impedanceL, z0=z0, zs=zs, zl=zl)
    C = .64e-12
    impedanceC = 1.0/(1j*w*C)
    sh = Shunt(node1=1, node2=2, impedance=impedanceC, z0=z0, zs=zs, zl=zl)
    
    cascade = se * sh
    print "s11", ComplexToPhasor(cascade.GetS11())
    print "s12", ComplexToPhasor(cascade.GetS12())
    print "s21", ComplexToPhasor(cascade.GetS21())
    print "s22", ComplexToPhasor(cascade.GetS22())
    print "Return Loss", cascade.GetReturnLoss()
    print "Insertion Loss", cascade.GetInsertionLoss()

def p4Chk():
    z = 2*np.pi*10e9 * .8e-9 *1j
    y = 2*np.pi*10e9 * .64e-12 * 1j
    A = 1.0 + z*y
    B = z
    C = y
    D = 1.0
    z0 = 50.0
    s11 = S2Port.__CalcS11__(z0, A, B, C, D)
    s12 = S2Port.__CalcS12__(z0, A, B, C, D)
    s21 = S2Port.__CalcS21__(z0, A, B, C, D)
    s22 = S2Port.__CalcS22__(z0, A, B, C, D)
    s = S2Port(node1=1, node2=2,s11=s11,s12=s12,s21=s21,s22=s22,z0=50.0,zs=50.0,zl=50.0)
    print "Return Loss", s.GetReturnLoss()
    print "Insertion Loss",s.GetInsertionLoss()
    print "s11", ComplexToPhasor(s.GetS11())
    print "s12", ComplexToPhasor(s.GetS12())
    print "s21", ComplexToPhasor(s.GetS21())
    print "s22", ComplexToPhasor(s.GetS22())
p4Chk()