'''
Created on Feb 1, 2015

@author: ryan
'''
import numpy as np

from python.ee.rf.network.elements.S2Port import S2Port
from python.ee.rf.network.elements.SElement import SElementTypes

class TRL(S2Port):
    
    def __init__(self, node1, node2, impedance, alpha, beta, length, z0=50.0, 
                 zs=50.0, zl =50.0):   
        super(TRL,self).__init__(node1=node1,node2=node2,z0=z0,zs=zs,zl=zl)
        self.impedance = impedance
        self.beta = beta
        self.length = length
        self.type = SElementTypes.TRL
    
    def GetA(self):
        return np.cos(self.beta * self.length)

    def GetB(self):
        return 1j * self.impedance * np.sin(self.beta * self.length)
    
    def GetC(self):
        return 1j * 1.0/self.impedance * np.sin(self.beta * self.length)
    
    def GetD(self):
        return self.GetA()