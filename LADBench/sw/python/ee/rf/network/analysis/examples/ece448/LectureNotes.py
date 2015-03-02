'''
Created on Feb 10, 2015

@author: ryan
'''
from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.S2Port import S2Port
from python.ee.rf.network.elements.lumped.Amplifier import Amplifier

class LectureNotes(object):
    @staticmethod
    def pg19():
        s11 = PhasorToComplex(.277, -59.0)
        s12 = PhasorToComplex(.078, 93.0)
        s21 = PhasorToComplex(1.92, 64.0)
        s22 = PhasorToComplex(.848, -31.0)
        s = S2Port(1, 2, s11, s12, s21, s22)
        
        print "K", s.CalcK()
        print "Delta", ComplexToPhasor(s.CalcDelta())
        print "Is stable?", s.IsStable()
    
    @staticmethod
    def pg27():
        s11 = PhasorToComplex(.614, -167.4)
        s12 = PhasorToComplex(.046, 65.0)
        s21 = PhasorToComplex(2.187, 32.4)
        s22 = PhasorToComplex(.716, -83.0)
        
        a = Amplifier(1, 2, s11, s12, s21, s22)
        print "Is stable?", a.IsStable()
        print "Max Amplifier Gain: %.2fdB"%a.GetGainTMatched()
        print "Gamma S Matched", ComplexToPhasor(a.GetGammaSMaxGain())
        print "Gamma L Matched", ComplexToPhasor(a.GetGammaLMaxGain())
    
    @staticmethod
    def pg29():
        s11 = PhasorToComplex(.614, -167.4)
        s12 = PhasorToComplex(.046, 65.0)
        s21 = PhasorToComplex(2.187, 32.4)
        s22 = PhasorToComplex(.716, -83.0)
        
        a = Amplifier(1, 2, s11, s12, s21, s22)
        print "Is stable?", a.IsStable()
        print "Max Amplifier Gain: %.2fdB"%a.GetGainTMatched()
        print "Gamma S Matched", ComplexToPhasor(a.GetGammaSMaxGain())
        print "Gamma L Matched", ComplexToPhasor(a.GetGammaLMaxGain())
                
if __name__ == '__main__':
    LectureNotes.pg29()