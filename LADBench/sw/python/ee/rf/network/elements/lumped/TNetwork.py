'''
Created on Feb 1, 2015

@author: ryan
'''
from python.ee.rf.network.elements.S2Port import S2Port

class TNetwork(S2Port):  
    
    def __init__(self, node1, node2, z1, z2, z3, z0 = 50.0, zs = 50.0, zl =50.0):  
        super(TNetwork, self).__init__(node1=node1, node2=node2, z0=z0,zs=zs,zl=zl)
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        
    def GetA(self):
        return 1 + self.z1/ self.z3
    
    def GetB(self):
        return self.z1 + self.z2 + self.z1 * self.z2 / self.z3
    
    def GetC(self):
        return 1.0/self.z3
    
    def GetD(self):
        return 1.0 + self.z2 / self.z3