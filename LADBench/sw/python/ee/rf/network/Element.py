'''
Created on Jan 22, 2015

@author: ryan
'''

class Element(object):
    
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

class LumpedElement(Element):

    def __init__(self, node1, node2, impedance):
        super(LumpedElement, self).__init__(node1, node2)
        self.impedance = impedance
