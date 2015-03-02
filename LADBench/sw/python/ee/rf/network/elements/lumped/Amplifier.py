'''
Created on Feb 21, 2015

@author: ryan
'''
from python.ee.rf.network.elements.S2Port import S2Port
import numpy as np
import warnings

class Amplifier(S2Port):
    '''
    classdocs
    '''
    
    def __init__(self, node1, node2, s11=None, s12=None, s21=None, s22=None, 
                 z0 = 50.0, zs = 50.0, zl = 50.0):
        
        super(Amplifier, self).__init__(node1,node2,s11,s12,s21,s22,z0,zs,zl)
    
    def GetMaxStableGain(self):
        return np.abs(self.GetS21())/np.abs(self.GetS11())
    
    def GetMaxTransducerPowerGain(self):
        K = self.CalcK()
        return self.GetMaxStableGain() * (K- np.sqrt(K**2-1))
        
    def GetGammaSMaxGain(self):
        delta = self.CalcDelta()
        s11 = self.GetS11Prime()
        s22 = self.GetS22Prime()
        B1 = 1+ np.abs(s11)**2 - np.abs(s22)**2 - np.abs(delta)**2
        C1 = s11 - delta * np.conjugate(s22)
        
        in_sqrt = B1**2 - 4 * np.abs(C1)**2
        if in_sqrt < 0:
            #TODO Figure out the problem this can cause. The problem is said
            # to occur when value inside the square root of this equation is 
            # less than zero. This is related in Pozar 4th Edition on pg. 572.
            warnings.warn("Possible problem with solution.")
        numerator1 = B1 + np.sqrt(in_sqrt)
        numerator2 = B1 - np.sqrt(in_sqrt)
        denominator = 2.0*C1
        solution1 = numerator1/denominator
        solution2 = numerator2/denominator
        if np.abs(solution1) < np.abs(solution2):
            return solution1
        return solution2    
    def GetGammaLMaxGain(self):
        delta = self.CalcDelta()
        s11 = self.GetS11Prime()
        s22 = self.GetS22Prime()
        B2 = 1+ np.abs(s22)**2 - np.abs(s11)**2 - np.abs(delta)**2
        C2 = s22 - delta * np.conjugate(s11)
        
        in_sqrt = B2**2 - 4 * np.abs(C2)**2
        if in_sqrt < 0:
            #TODO Figure out the problem this can cause. The problem is said
            # to occur when value inside the square root of this equation is 
            # less than zero. This is related in Pozar 4th Edition on pg. 572.
            warnings.warn("Possible problem with solution.")
        numerator1 = B2 + np.sqrt(in_sqrt)
        numerator2 = B2 - np.sqrt(in_sqrt)
        denominator = 2.0*C2
        solution1 = numerator1/denominator
        solution2 = numerator2/denominator
        if np.abs(solution1) < np.abs(solution2):
            return solution1
        return solution2
    
    def GetGainS(self, gammaS, gammaIn):
        # Units of dB
        numerator = 1.0 - np.abs(gammaS)**2
        denominator = np.abs(1.0-gammaIn*gammaS)**2
        return 10.0* np.log10(numerator/denominator)
    
    def GetGainL(self, gammaL):
        # Units of dB
        numerator = 1.0 - np.abs(gammaL)**2
        denominator = np.abs(1.0-self.GetS22Prime()*gammaL)**2
        return 10.0 * np.log10(numerator/denominator)
    
    def GetGain0(self):
        # Units of dB
        return 10.0 * np.log10(np.abs(self.GetS21Prime())**2)
    
    def GetGainT(self, gammaS, gammaL, gammaIn):
        # Units of dB
        return 10.0*np.log10(self.GetGain0()*self.GetGainL(gammaL) \
            * self.GetGainS(gammaS, gammaIn))
    
    def GetGainSMatched(self):
        # Units of dB
        gammaS = self.GetGammaSMaxGain()
        return self.GetGainS(gammaS, np.conjugate(gammaS))
    
    def GetGainLMatched(self):
        # Units of dB
        gammaL = self.GetGammaLMaxGain()
        return self.GetGainL(gammaL)

    
    def GetGainTMatched(self):
        # Units of dB
        return self.GetGain0() + self.GetGainLMatched() \
            + self.GetGainSMatched()
    
    def GetAvailablePowerGain(self, gammaS, gammaOut):
        # TODO Refactor
        numerator = np.abs(self.GetS21Prime())**2 * (1.0-np.abs(gammaS)**2) 
        denominator = np.abs(1.0-self.GetS11Prime()*gammaS)**2 \
                        * (1.0-np.abs(gammaOut)**2)
        return numerator/denominator
    
    def GetPowerGain(self, gammaL, gammaIn):
        numerator = np.abs(self.GetS21Prime())**2 *(1.0-np.abs(gammaL)**2)
        denominator = (1-np.abs(gammaIn)**2) \
                        * np.abs(1.0-self.GetS22Prime()*gammaL)**2
        return numerator / denominator
    
    def GetTransducerPowerGain(self,gammaS, gammaL,gammaIn):
        numerator = np.abs(self.GetS21Prime())**2 * (1.0-np.abs(gammaS)**2) \
                        *(1.0-np.abs(gammaL)**2)
        denominator = np.abs(1.0-gammaS*gammaIn)**2 \
                        * np.abs(1-self.GetS22Prime() * gammaL)**2
        return numerator/denominator