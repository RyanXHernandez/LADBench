'''
Created on Jan 22, 2015

@author: ryan
'''

class Network(object):
    '''
    classdocs
    '''


    def __init__(self, elements = None):
        '''
        Constructor
        '''
        if elements is None:
            self.elements = []
        self.elements = elements
            

    def addElement(self, element):
        self.elements +=  element