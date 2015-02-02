'''
Created on Jan 31, 2015

@author: ryan
'''
import numpy as np

def ComplexToPhasor(complx):
    return np.abs(complx), np.rad2deg(np.angle(complx))

def PhasorToComplex(mag,angle):
    return mag * np.exp(1j*np.deg2rad(angle))

if __name__ == '__main__':
    mag = 2.0
    angle = 45.0
    complx = PhasorToComplex(mag, angle)
    phasor = ComplexToPhasor(complx)
    print complx
    print phasor