# -*- coding: utf-8 -*-

class Observator:
    '''
    classdocs
    '''
    
    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.model.addObservator(self)
    
    def updateView(self):
        '''
        updateView (to complete)
        '''
        pass
