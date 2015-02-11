'''
Created on Feb 10, 2015

@author: ryan
'''
from python.math.number.complex.Util import PhasorToComplex, ComplexToPhasor
from python.ee.rf.network.elements.S2Port import S2Port

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
if __name__ == '__main__':
    LectureNotes.pg19()