'''
Created on Jan 22, 2015

@author: ryan
'''
import numpy as np

from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.lumped.Series import Series
from python.ee.rf.network.elements.distributed.TRL import TRL
from python.ee.rf.network.elements.lumped.TNetwork import TNetwork
from python.ee.rf.network.elements.lumped.Shunt import Shunt
from python.ee.rf.network.elements.S2Port import S2Port

class Homework1:
    
    pass

class Homework2:
    
    @staticmethod
    def Problem1():
        print "Problem 1 Part a"
        print "#################################################################"
        s  = Series(node1=1, node2=2, impedance=1j*3e-9*7.5e9*2*np.pi)
        print s.GetSMatrix()
        print "Return loss", s.GetReturnLoss()
        print "Insertion Loss", s.GetInsertionLoss()
        print "Problem 1 Part b"
        print "#################################################################"
        trl = TRL(node1=1, node2=2, impedance=20.0, alpha=0, beta=2*np.pi*7.5e9/3e8, length=1e-2)
        print trl.GetSMatrix()
        print "Return loss", trl.GetReturnLoss()
        print "Insertion Loss", trl.GetInsertionLoss()
        print "Problem 1 Part c"
        print "#################################################################"
        cascade =  s * trl
        print "s11",ComplexToPhasor(cascade.GetS11())
        print "s12",ComplexToPhasor(cascade.GetS12())
        print "s21",ComplexToPhasor(cascade.GetS21())
        print "s22",ComplexToPhasor(cascade.GetS22())
        print cascade.GetInsertionLoss()
        print cascade.GetReturnLoss()

        
    @staticmethod
    def Problem2():
        # Problem 2 hwk 2
        print "Problem 2"
        print "#################################################################"
        tNetwork = TNetwork(node1=1, node2=2, z1=8.56, z2 = 8.56 , z3 = 141.8)
        #print tNetwork.GetABCDMatrix()
        print(tNetwork.GetSMatrix())
        print "Insertion Loss",tNetwork.GetInsertionLoss()
        print "VSWR", tNetwork.GetInputVSWR()
    
    @staticmethod
    def Problem3():
        print "Problem 3"
        print "#################################################################"
        tNetwork = TNetwork(node1=1, node2=2, z1=8.56, z2 = 8.56 , z3 = 141.8, zl=100.0)
        print tNetwork.GetSPrimeMatrix()
        print "Insertion Loss",tNetwork.GetInsertionLossPrime()
        print "Return loss", tNetwork.GetReturnLossPrime()
    
    @staticmethod
    def Problem4():
        print "Problem 4"
        print "#################################################################"
        s11 = PhasorToComplex(.78, -42.0)
        s12 = PhasorToComplex(.71, -138.0)
        s21 = s12
        s22 = PhasorToComplex(.23, 26.0)
        s = S2Port(node1=1, node2=2, z0=50.0, zs=50.0, zl=2.5, s11= s11, s12=s12,s21=s21,s22=s22)
        row1 =  [ComplexToPhasor(s.GetS11Prime()), ComplexToPhasor(s.GetS12Prime())]
        row2 = [ComplexToPhasor(s.GetS21Prime()), ComplexToPhasor(s.GetS22Prime())]
        sPMatrix = np.array([row1,row2])
        print sPMatrix
        print "Insertion Loss",s.GetInsertionLossPrime()
        print "Return loss", s.GetReturnLossPrime()
        print "Input VSWR", s.GetInputVSWR()
    
    @staticmethod
    def Problem5():
        print "Problem 5"
        print "#################################################################"
        z0 = 50.0
        zs = z0
        zl = zs
        gammaS = PhasorToComplex(.73, 120.0)
        gammaL = PhasorToComplex(.695, 117.0)
        s11 = PhasorToComplex(.78, -126.0)
        s12 = PhasorToComplex(.07, 12.0)
        s21 = PhasorToComplex(2.33, 56.0)
        s22 = PhasorToComplex(.62, -94.0)
        s = S2Port(node1=1, node2=2, z0=50.0, zs=zs, zl=zl, s11= s11, s12=s12,s21=s21,s22=s22)
        s.SetGammaL(gammaL)
        s.SetGammaS(gammaS)
        #row1 =  [ComplexToPhasor(s.GetS11Prime()), ComplexToPhasor(s.GetS12Prime())]
        #row2 = [ComplexToPhasor(s.GetS21Prime()), ComplexToPhasor(s.GetS22Prime())]
        #sPMatrix = np.array([row1,row2])
        #print sPMatrix
        
        print "s11",ComplexToPhasor(s.GetS11Prime())
        print "s12",ComplexToPhasor(s.GetS12Prime())
        print "s21",ComplexToPhasor(s.GetS21Prime())
        print "s22",ComplexToPhasor(s.GetS22Prime())        
        print "Insertion Loss",s.GetInsertionLossPrime()
        print "Return loss",s.GetReturnLossPrime()
        print "Input VSWR", s.GetInputVSWR()

class Homework3:
    
    @staticmethod
    def Problem1():
        print "Problem 1"
        print "#################################################################"
        w = 2 * np.pi * 10e9
        L = 1e-9
        impedance = 1j * w * L
        sh = Shunt(node1=1, node2=2, impedance = impedance, z0 = 100.0)
        print "s11", ComplexToPhasor(sh.GetS11())
        print "s12", ComplexToPhasor(sh.GetS12())
        print "s21", ComplexToPhasor(sh.GetS21())
        print "s22", ComplexToPhasor(sh.GetS22())
        print "Insertion Loss",sh.GetInsertionLoss()
        print "Return loss",sh.GetReturnLoss()

class Homework4:
    
    @staticmethod
    def Problem1():
        print "Problem 1"
        print "#################################################################"
        s11 = PhasorToComplex(.88, -115.0)
        s12 = PhasorToComplex(.029, 31.0)
        s21 = PhasorToComplex(9.4, 110.0)
        s22 = PhasorToComplex(.328, -67.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()

    
    @staticmethod
    def Problem2():
        print "Problem 2"
        print "#################################################################"
        s11 = PhasorToComplex(.96, 180.0)
        s12 = PhasorToComplex(.007, -16.0)
        s21 = PhasorToComplex(3.67, 68.0)
        s22 = PhasorToComplex(.72, -174.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Frequency: .5 GHz"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()
        
        s11 = PhasorToComplex(.95, 172.0)
        s12 = PhasorToComplex(.008, -35.0)
        s21 = PhasorToComplex(2.03, 44.0)
        s22 = PhasorToComplex(.78, -172.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Frequency: 1 GHz"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()
        
        s11 = PhasorToComplex(.78, 153.0)
        s12 = PhasorToComplex(.014, -83.0)
        s21 = PhasorToComplex(2.09, -17.0)
        s22 = PhasorToComplex(.91, -174.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Frequency: 2 GHz"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()
        
        s11 = PhasorToComplex(.88, -51.0)
        s12 = PhasorToComplex(.008, 79.0)
        s21 = PhasorToComplex(.84, 88.0)
        s22 = PhasorToComplex(.88, 171.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Frequency: 4 GHz"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()
    
    @staticmethod
    def Problem3():
        print "Problem 2"
        print "#################################################################"
        s11 = PhasorToComplex(.34, -170.0)
        s12 = PhasorToComplex(.06, 70.0)
        s21 = PhasorToComplex(4.3, 80.0)
        s22 = PhasorToComplex(.45, -25.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Device A"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Mu", s.CalcMu()
        print "Is stable?", s.IsStable()
        
        s11 = PhasorToComplex(.75, -60.0)
        s12 = PhasorToComplex(.2, 70.0)
        s21 = PhasorToComplex(5.0, 90.0)
        s22 = PhasorToComplex(.51, -60.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Device B"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Mu", s.CalcMu()
        print "Is stable?", s.IsStable()
        
        s11 = PhasorToComplex(.65, -140.0)
        s12 = PhasorToComplex(.04, 60.0)
        s21 = PhasorToComplex(2.4, 50.0)
        s22 = PhasorToComplex(.7, -65.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        print "Device C"
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Mu", s.CalcMu()
        print "Is stable?", s.IsStable()
    
if __name__ == '__main__':
    Homework4.Problem1()
    Homework4.Problem2()
    Homework4.Problem3()