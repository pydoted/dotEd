# -*- coding: utf-8 -*-


class Observator(object):
    '''Represent an observator. 
    
    
    Argument(s):
    model (Subject): Subject
    
    Attribute(s):
    model (Subject): Subject
    '''
    
    
    def __init__(self, model):
        self.model = model
        self.model.addObservator(self)
    
    def updateView(self):
        '''Update the view.'''
        pass
