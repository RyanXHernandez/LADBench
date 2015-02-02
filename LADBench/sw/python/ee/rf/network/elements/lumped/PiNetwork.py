'''
Created on Feb 1, 2015

@author: ryan
'''
from python.ee.rf.network.elements.S2Port import S2Port

class PiNetwork(S2Port):

    def __init__(self, node1, node2, z1, z2, z3, z0 =50.0, zs = 50.0, zl =50.0):
        super(PiNetwork, self).__init__(node1, node2, z0, zs, zl)
        self.y1 = 1.0/self.z1
        self.y2 = 1.0/self.z2
        self.y3 - 1.0/self.z3
    
    def GetA(self):
        return 1.0 + self.y2/self.y3
    
    def GetB(self):
        return 1.0 / self.y3
    
    def GetC(self):
        return self.y1 + self.y2 + self.y1 * self.y2 / self.y3
    
    def GetD(self):
        return 1.0 + self.y1 / self.y3