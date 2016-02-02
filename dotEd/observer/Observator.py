# -*- coding: utf-8 -*-

class Observator:
    '''
    classdocs
    '''
    
    def __init__(self, subject):
        '''
        Constructor
        '''
        self.sujet = subject
        self.subject.addObservator(self)
    
    def update(self):
        '''
        update (to complete)
        '''
        pass