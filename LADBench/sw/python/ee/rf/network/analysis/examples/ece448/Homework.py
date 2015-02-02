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
    def Problem1Partc():
        s  = Series(node1=1, node2=2, impedance=1j*3e-9*7.5e9*2*np.pi)
        trl = TRL(node1=1, node2=2, impedance=20.0, alpha=0, beta=2*np.pi*7.5e9/3e8, length=1e-2)
        print s.GetABCDMatrix() *trl.GetABCDMatrix()
        print s.GetABCDMatrix()
    
    @staticmethod
    def Problem2():
        # Problem 2 hwk 2
        tNetwork = TNetwork(node1=1, node2=2, z1=8.56, z2 = 8.56 , z3 = 141.8)
        print tNetwork.GetABCDMatrix()
        print(tNetwork.GetSMatrix())
        print tNetwork.GetInsertionLoss()
        print tNetwork.GetInputVSWR()
    
    @staticmethod
    def Problem3():
        tNetwork = TNetwork(node1=1, node2=2, z1=8.56, z2 = 8.56 , z3 = 141.8, zl=100.0)
        print tNetwork.GetSPrimeMatrix()
        print tNetwork.GetInsertionLossPrime()
        print tNetwork.GetReturnLossPrime()
    
    @staticmethod
    def Problem4():
        s11 = PhasorToComplex(.78, -42.0)
        s12 = PhasorToComplex(.71, -138.0)
        s21 = s12
        s22 = PhasorToComplex(.23, 26.0)
        s = S2Port(node1=1, node2=2, z0=50.0, zs=50.0, zl=2.5, s11= s11, s12=s12,s21=s21,s22=s22)
        row1 =  [ComplexToPhasor(s.GetS11Prime()), ComplexToPhasor(s.GetS12Prime())]
        row2 = [ComplexToPhasor(s.GetS21Prime()), ComplexToPhasor(s.GetS22Prime())]
        sPMatrix = np.array([row1,row2])
        print sPMatrix
        print s.GetInsertionLossPrime()
        print s.GetReturnLossPrime()
    
    @staticmethod
    def Problem5():
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
        print s.GetSPrimeMatrix()
        print s.GetInsertionLossPrime()
        print s.GetReturnLossPrime()
    

class Homework3:
    
    @staticmethod
    def Problem1():
        w = 2 * np.pi * 10e9
        L = 1e-9
        impedance = 1j * w * L
        sh = Shunt(node1=1, node2=2, impedance = impedance, z0 = 100.0)
        print sh.GetABCDMatrix()
        print sh.GetSMatrix()
        print sh.GetInsertionLoss()
        print sh.GetReturnLoss()


    
if __name__ == '__main__':
    Homework2.Problem5()