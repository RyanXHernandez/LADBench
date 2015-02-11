'''
Created on Jan 21, 2015

@author: ryan
'''

from python.ee.rf.network.elements.Element import Element

class SElementTypes:
    """
    This class is a container for the types of elements that can are defined in 
    this API.
    """
    CUSTOM  = -1
    LUMPED_SHUNT = 0
    LUMPED_SERIES = 1
    TRL = 2
    T_NETWORK = 3
    Y_NETWORK = 4
    TRANSFORMER = 5
    

class SElement(Element):
    
    def __init__(self, node1, node2, z0 = 50.0):
        """
        Constructor
        
        Parameters:
        -----------
        node1 : int
            The first node that this element is connected to.
            
        node2 : int
            The second node that this element is connected to.
        
        """
        super(SElement, self).__init__(node1, node2)
        self.z0 = z0
    
    @staticmethod
    def CalcGamma(z, z0):
        return (z-z0)/(z+z0)

if __name__ == '__main__':
    print "hello world!"

    