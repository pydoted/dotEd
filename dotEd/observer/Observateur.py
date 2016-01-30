# -*- coding: utf-8 -*-

class Observateur:
    '''
    classdocs
    '''
    
    def __init__(self, sujet):
        '''
        Constructor
        '''
        self.sujet = sujet
        sujet.addObservateur(self)
    
    def actualise(self):
        '''
        actualise (to complete)
        '''
        pass