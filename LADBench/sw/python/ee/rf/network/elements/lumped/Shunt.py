'''
Created on Feb 1, 2015

@author: ryan
'''
from python.ee.rf.network.elements.S2Port import S2Port
from python.ee.rf.network.elements.SElement import SElementTypes

class Shunt(S2Port):
    
    def __init__(self, node1, node2, impedance, z0 = 50.0, zs=50.0, zl =50.0):
        super(Shunt, self).__init__(node1=node1,node2=node2,impedance=impedance,
                                    z0=z0,zs=zs,zl=zl)
        self.type = SElementTypes.LUMPED_SERIES

    def GetA(self):
        return 1.0
    
    def GetB(self): 
        return 0.0
    
    def GetC(self):
        return 1.0/self.impedance
    
    def GetD(self):
        return 1.0