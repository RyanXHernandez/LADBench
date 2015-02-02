'''
Created on Feb 1, 2015

@author: ryan
'''
from python.ee.rf.network.elements.S2Port import S2Port

class Transformer(S2Port):
    
    def __init__(self, node1, node2, turns, z0=50.0, zs=50.0, zl =50.0):
        super(Transformer,self).__init__(node1, node2, z0,zs,zl)
        self.turns = turns
        
    def GetA(self):
        return self.turns
    
    def GetB(self):
        return 0
    
    def GetC(self):
        return 0
    
    def GetD(self):
        return 1.0 / self.turns