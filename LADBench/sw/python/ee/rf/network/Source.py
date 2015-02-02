'''
Created on Jan 22, 2015

@author: ryan
'''
from python.ee.rf.network.elements.Element import Element

import numpy as np


class Source(Element):
    '''
    classdocs
    '''


    def __init__(self, node1, node2, amplitude, f, phase):
        '''
        Constructor
        '''
        super(Source, self).__init__(node1,node2)
        self.amplitude = amplitude
        self.f =  f
        self.w = 2*np.pi
        self.phase = phase

class SinusoidalSource(Source):
    
    def __init___(self, node1, node2, amplitude, f, phase):
        super(SinusoidalSource, self).__init__(node1, node2, amplitude, f, phase)
        self.t = 0
        
    def out(self, t, numSamples):
        output = []
        for ti in np.arange(self.t, t,numSamples):
            output = self.amplitude * np.sin(self.w*ti +  self.phase)
        self.t += t
        return output 

class DCSource(Source):
    
    def __init__(self, node1, node2, amplitude):
        super(DCSource, self).__init__(node1,node2,amplitude,f=0.0,phase=0.0)
        