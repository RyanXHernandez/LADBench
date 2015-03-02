'''
Created on Feb 10, 2015

@author: ryan
'''
from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.S2Port import S2Port
from python.ee.rf.network.elements.lumped.Amplifier import Amplifier
import numpy as np

def Example1():
    s11 = PhasorToComplex(.38, -158.0)
    s12 = PhasorToComplex(.11, 54.0)
    s21 = PhasorToComplex(3.5, 80.0)
    s22 = PhasorToComplex(.4, -43.0)
    z0 = 50.0
    zs = 25.0
    zl = 40.0
    
    a = Amplifier(1, 2, s11, s12, s21, s22, z0, zs, zl)
    gammaS = a.CalcGamma(zs, z0)
    gammaL = a.CalcGamma(zl,z0)
    gammaIn = a.GetS11Prime()
    gammaOut = a.GetS22Prime()
    G = a.GetPowerGain(gammaL, gammaIn)
    G_T = a.GetTransducerPowerGain(gammaS, gammaL, gammaIn)
    G_A = a.GetAvailablePowerGain(gammaS, gammaOut)
    print "Gamma S = ", gammaS
    print "Gamma L = ", gammaL
    
    print "Gamma in = ", ComplexToPhasor(gammaIn)
    print "Gamma out = ", ComplexToPhasor(gammaOut)
    
    print "Power Gain", G
    print "Available Power Gain", G_A
    print "Transducer Power Gain", G_T

def Example2():
    print "Example 2"
    print "#################################################################"
    s11 = PhasorToComplex(.869, -159.0)
    s12 = PhasorToComplex(.031, -9.0)
    s21 = PhasorToComplex(4.250, 61.0)
    s22 = PhasorToComplex(.507, -117.0)
    s = S2Port(1, 2, s11, s12, s21, s22)
    
    print "K", s.CalcK()
    print "Delta", ComplexToPhasor(s.CalcDelta())
    print "Is stable?", s.IsStable()
    print "Cl", ComplexToPhasor(s.CalcCl())
    print "Rl", ComplexToPhasor(s.CalcRl())
    print "Cs", ComplexToPhasor(s.CalcCs())
    print "Rs", ComplexToPhasor(s.CalcRs())

def Example3():
    print "Example 3"
    print "#################################################################"
    
    s11_3GHz = PhasorToComplex(.80, -89.0)
    s12_3GHz = PhasorToComplex(.03, 56.0)
    s21_3GHz = PhasorToComplex(2.86, 99.0)
    s22_3GHz = PhasorToComplex(.76, -41.0)
    a3 = Amplifier(node1=1, node2=2, s11=s11_3GHz, s12=s12_3GHz, s21=s21_3GHz, 
              s22=s22_3GHz)
    
    s11_4GHz = PhasorToComplex(.72, -116.0)
    s12_4GHz = PhasorToComplex(.03, 57.0)
    s21_4GHz = PhasorToComplex(2.6, 76.0)
    s22_4GHz = PhasorToComplex(.73, -54.0)
    a4 = Amplifier(node1=1, node2=2, s11=s11_4GHz, s12=s12_4GHz, s21=s21_4GHz, 
              s22=s22_4GHz)
    
    s11_5GHz = PhasorToComplex(.66, -142.0)
    s12_5GHz = PhasorToComplex(.03, 62.0)
    s21_5GHz = PhasorToComplex(2.39, 54.0)
    s22_5GHz = PhasorToComplex(.72, -68.0)
    a5 = Amplifier(node1=1, node2=2, s11=s11_5GHz, s12=s12_5GHz, s21=s21_5GHz, 
              s22=s22_5GHz)
    
    print "f(GHz)\t K \t delta \t Unconditionally Stable?"
    print "%.1f \t %.2f \t %.3f \t %r"%(3.0,a3.CalcK(),np.abs(a3.CalcDelta()), a3.IsStable())
    print "%.1f \t %.2f \t %.3f \t %r"%(4.0,a4.CalcK(),np.abs(a4.CalcDelta()), a4.IsStable())
    print "%.1f \t %.2f \t %.3f \t %r"%(5.0,a5.CalcK(),np.abs(a5.CalcDelta()), a5.IsStable())
    
    print "Matched Gamma S = ", ComplexToPhasor(a4.GetGammaSMaxGain())
    print "Matched Gamma L = ", ComplexToPhasor(a4.GetGammaLMaxGain())
    
    print "Gs = ", a4.GetGainSMatched()
    print "G0 = ", a4.GetGain0()
    print "Gl = ", a4.GetGainLMatched()
    print "G_T = ", a4.GetGainTMatched()
    
def Problem9():
    s11_8GHz = PhasorToComplex(.52, 179.0)
    s12_8GHz = PhasorToComplex(.14, -1.0)
    s21_8GHz = PhasorToComplex(2.0, 20.0)
    s22_8GHz = PhasorToComplex(.42, -129.0)
    a = Amplifier(node1=1, node2=2, s11=s11_8GHz, s12=s12_8GHz, s21=s21_8GHz, 
              s22=s22_8GHz)
    
    print "f(GHz)\t K \t delta \t Unconditionally Stable?"
    print "%.1f \t %.2f \t %.3f \t %r"%(8.0,a.CalcK(),np.abs(a.CalcDelta()), a.IsStable())
    
    print "Matched Gamma S = ", ComplexToPhasor(a.GetGammaSMaxGain())
    print "Matched Gamma L = ", ComplexToPhasor(a.GetGammaLMaxGain())
    
    print "Gs = ", a.GetGainSMatched(), 'dB'
    print "G0 = ", a.GetGain0(), 'dB'
    print "Gl = ", a.GetGainLMatched(),'dB'
    print "G_T = ", a.GetGainTMatched(),'dB'

def Problem11():
    s11_6GHz = PhasorToComplex(.61, -170.0)
    s12_6GHz = 0.0
    s21_6GHz = PhasorToComplex(2.24, 32.0)
    s22_6GHz = PhasorToComplex(.72, -83.0)
    a = Amplifier(node1=1, node2=2, s11=s11_6GHz, s12=s12_6GHz, s21=s21_6GHz, 
              s22=s22_6GHz)
    
    print "f(GHz)\t K \t delta \t Unconditionally Stable?"
    print "%.1f \t %.2f \t %.3f \t %r"%(8.0,a.CalcK(),np.abs(a.CalcDelta()), a.IsStable())
    
    print "Matched Gamma S = ", ComplexToPhasor(a.GetGammaSMaxGain())
    print "Matched Gamma L = ", ComplexToPhasor(a.GetGammaLMaxGain())
    
    print "Gs = ", a.GetGainSMatched(), 'dB'
    print "G0 = ", a.GetGain0(), 'dB'
    print "Gl = ", a.GetGainLMatched(),'dB'
    print "G_T = ", a.GetGainTMatched(),'dB'
    
    
if __name__ == '__main__':
    Example1()
    #Example2()
    #Example3()
    #Problem9()
    #Problem11()