'''
Created on Jan 21, 2015

@author: ryan
'''

# EE Imports
from python.ee.rf.network.Element import Element

# Other
import numpy as np

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
    """
    This class denotes an s-parameters element. It must have GetA(), GetB(),
    GetC() and GetD() implemented or an exception will be raised. ABCD 
    corresponds to the ABCD matrix of a given two port element.
    """ 
    import abc
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, node1, node2, z0 = 50.0, zs = 0.0, zl = 0.0):
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
        self.SetZs(zs)
        self.SetZl(zl)
        self.s11 = None
        self.s12 = None
        self.s21 = None
        self.s22 = None
        
    def SetZs(self, zs):
        self.zs = zs
        self.SetGammaS(SElement.CalcGamma(self.zs, self.z0))
    
    def SetZl(self, zl):
        self.zl = zl
        self.SetGammaL(self.CalcGamma(zl, self.z0))
    
    def GetInputVSWR(self):
        return (1.0+np.abs(self.GetS11()))/(1.0 - np.abs(self.GetS11()))
    
    def GetOutputVSWR(self):
        return (1.0+np.abs(self.GetS22()))/(1.0 - np.abs(self.GetS22()))
    
    @staticmethod
    def CalcGamma(z, z0):
        return float(z-z0)/float(z+z0)
    
    def SetGammaS(self, gammaS):
        self.gammaS = gammaS
    
    def SetGammaL(self, gammaL):
        self.gammaL = gammaL
        
    def GetS11Prime(self):
        s11, s12, s21, s22 = self.GetSTuple()
        rl = self.gammaL
        return s11 + s12*s21*rl / (1.0-rl*s22)
    
    def GetS22Prime(self):
        s11, s12, s21, s22 = self.GetSTuple()
        rs = self.gammaS
        return s22 + s12*s21*rs/(1.0-rs*s11)
    
    def GetS21Prime(self):
        s11, s12, s21, s22 = self.GetSTuple()
        rl = self.gammaL
        rs = self.gammaS
        numerator = s21*np.sqrt(1.0-np.abs(rs)**2) * np.sqrt(1.0-np.abs(rl)**2)
        denominator = (1.0-s11*rs)*(1.0-s22*rl)-s21*s12*rl*rs
        return numerator/denominator
    
    def GetS12Prime(self):
        s11, s12, s21, s22 = self.GetSTuple()
        rl = self.gammaL
        rs = self.gammaS
        numerator = s12*np.sqrt(1.0-np.abs(rs)**2) * np.sqrt(1.0-np.abs(rl)**2)
        denominator = (1.0-s11*rs)*(1.0-s22*rl)-s21*s12*rl*rs
        return numerator/denominator
    
    def GetInsertionLossPrime(self):
        return 20 * np.log10(np.abs(self.GetS21Prime()))
    
    def GetReturnLossPrime(self):
        return 20 * np.log10(np.abs(self.GetS11Prime()))
    
    def SetS11(self, s11):
        self.s11 = s11
    
    def SetS22(self, s22):
        self.s22 = s22
    
    def SetS12(self, s12):
        self.s12 = s12
    
    def SetS21(self, s21):
        self.s21 = s21
    
    def __CalcS11__(self):
        A, B, C, D = self.GetABCDTuple()
        numerator = A + B/self.z0 - C*self.z0 - D
        denominator = A + B/self.z0 + C*self.z0 + D
        return numerator/denominator
    
    def __CalcS21__(self):
        A, B, C, D = self.GetABCDTuple()
        numerator = 2.0
        denominator = A + B/self.z0 + C * self.z0 + D
        return numerator/denominator
    
    def __CalcS12__(self):
        A, B, C, D = self.GetABCDTuple()
        numerator = 2.0* (A *D - B*C)
        denominator = A + B/self.z0 + C*self.z0 + D
        return numerator / denominator
    
    def __CalcS22__(self):
        A, B, C, D = self.GetABCDTuple()
        numerator = -A + B/self.z0 - C*self.z0 + D
        denominator = A + B/self.z0 + C * self.z0 + D
        return numerator/denominator
    
    def GetS11(self):
        if self.s11 is None:
            self.s11 = self.__CalcS11__()
        return self.s11
    
    def GetS12(self): 
        if self.s12 is None:
            self.s12 = self.__CalcS12__()
        return self.s12
    
    def GetS21(self):
        if self.s21 is None:
            self.s21 = self.__CalcS21__()
        return self.s21
    
    def GetS22(self):
        if self.s22 is None:
            self.s22 = self.__CalcS22__()
        return self.s22
    
    def GetSTuple(self):
        return self.GetS11(), self.GetS12(), self.GetS21(), self.GetS22()
    
    def GetSMatrix(self):
        s11 = self.GetS11()
        s12 = self.GetS12()
        s21 = self.GetS21()
        s22 = self.GetS22()
        row1 = [s11, s12]
        row2 = [s21, s22]
        matrix = [row1,row2]
        return np.matrix(matrix)
    
    def GetSPrimeMatrix(self):
        s11 = self.GetS11Prime()
        s12 = self.GetS12Prime()
        s21 = self.GetS21Prime()
        s22 = self.GetS22Prime()
        row1 = [s11, s12]
        row2 = [s21, s22]
        matrix = [row1,row2]
        return np.matrix(matrix)
    
    def GetReturnLoss(self):
        return 20 * np.log10(np.abs(self.GetS11()))
    
    def GetInsertionLoss(self):
        return 20 * np.log10(np.abs(self.GetS21()))
    
    @abc.abstractmethod
    def GetA(self):
        """
        Returns the A parameter of its associated ABCD matrix.
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        A : complex float
            The A parameter of its associated ABCD matrix.
        """
        return
    
    @abc.abstractmethod
    def GetB(self):
        """
        Returns the B parameter of its associated ABCD matrix.
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        B : complex float
            The A parameter of its associated ABCD matrix.
        """
        return
    
    @abc.abstractmethod
    def GetC(self):
        """
        Returns the C parameter of its associated ABCD matrix.
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        A : complex float
            The C parameter of its associated ABCD matrix.
        """
        return
    
    @abc.abstractmethod
    def GetD(self):
        """
        Returns the D parameter of its associated ABCD matrix.
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        D : complex float
            The C parameter of its associated ABCD matrix.
        """
        return
        
    def GetABCDTuple(self):
        return self.GetA(), self.GetB(), self.GetC(), self.GetD()
    
    def GetABCDMatrix(self):
        """
        Returns its associated ABCD matrix.
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        ABCD : 4x4 numpy matrix
            The associated ABCD matrix.
        """
        a = self.GetA()
        b = self.GetB()
        c = self.GetC()
        d = self.GetD()
        row1 = [a,b]
        row2 = [c,d]
        matrix = [row1,row2]
        return np.matrix(matrix)
    
class SLumpedElement(SElement):
    
    import abc
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, node1, node2, impedance, z0 = 50):
        super(SElement, self).__init__(node1, node2)
        self.impedance = impedance
        self.z0 = z0
        
    @abc.abstractmethod
    def GetA(self):
        return
    
    @abc.abstractmethod
    def GetB(self):
        return
    
    @abc.abstractmethod
    def GetC(self):
        return
    
    @abc.abstractmethod
    def GetD(self):
        return
        

class Series(SLumpedElement):
    
    def __init__(self, node1, node2, impedance, z0 = 50.0, zs=50.0, zl =50.0):
        super(Series, self).__init__(node1,node2,impedance,z0,zs,zl)
        self.type = SElementTypes.LUMPED_SERIES

    def GetA(self):
        return 1.0
    
    def GetB(self): 
        return self.impedance
    
    def GetC(self):
        return 0
    
    def GetD(self):
        return 1.0
    
class Shunt(SLumpedElement):
    
    def __init__(self, node1, node2, impedance, z0 = 50.0, zs=50.0, zl =50.0):
        super(Shunt, self).__init__(node1,node2,impedance, z0,zs,zl)
        self.type = SElementTypes.LUMPED_SERIES

    def GetA(self):
        return 1.0
    
    def GetB(self): 
        return 0.0
    
    def GetC(self):
        return 1.0/self.impedance
    
    def GetD(self):
        return 1.0
    
class TRL(SElement):
    
    def __init__(self, node1, node2, impedance, alpha, beta, length, z0=50.0, 
                 zs=50.0, zl =50.0):   
        super(TRL,self).__init__(node1,node2,z0,zs,zl)
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

class Transformer(SElement):
    
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
    
class TNetwork(SElement):  
    
    def __init__(self, node1, node2, z1, z2, z3, z0 = 50.0, zs = 50.0, zl =50.0):  
        super(TNetwork, self).__init__(node1, node2, z0,zs,zl)
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

class PINetwork(SElement):

    def __init__(self, node1, node2, z1, z2, z3, z0 =50.0, zs = 50.0, zl =50.0):
        super(PINetwork, self).__init__(node1, node2, z0, zs, zl)
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
    
class SMatrix(SElement):
    
    def __init__(self, node1, node2, s11, s12, s21, s22, z0 = 50.0, zs = 0.0,
                  zl = 0.0):
        super(SMatrix, self).__init__(node1,node2,z0,zs,zl)
        self.SetS11(s11)
        self.SetS12(s12)
        self.SetS21(s21)
        self.SetS22(s22)
    
    def GetA(self):
        pass
    
    def GetB(self):
        pass
    
    def GetC(self):
        pass
    
    def GetD(self):
        pass
    
if __name__ == '__main__':
    print "hello world!"

    