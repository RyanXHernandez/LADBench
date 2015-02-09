'''
Created on Feb 1, 2015

@author: ryan
'''
from python.ee.rf.network.elements.SElement import SElementTypes
from python.ee.rf.network.elements.S2Port import S2Port

class Series(S2Port):
    
    def __init__(self, node1, node2, impedance, z0 = 50.0, zs=50.0, zl =50.0):
        super(Series, self).__init__(node1,node2,z0=z0,zs=zs,zl=zl)
        self.type = SElementTypes.LUMPED_SERIES
        self.impedance = impedance

    def GetA(self):
        return 1.0
    
    def GetB(self): 
        return self.impedance
    
    def GetC(self):
        return 0
    
    def GetD(self):
        return 1.0