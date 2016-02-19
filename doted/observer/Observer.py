# -*- coding: utf-8 -*-


class Observer(object):
    '''Represent an observer. 
    
    
    Argument(s):
    model (Subject): Subject
    
    Attribute(s):
    model (Subject): Subject
    '''
    
    
    def __init__(self, model):
        self.model = model
        self.model.addObserver(self)
    
    def update(self):
        '''Update the observer.'''
        pass
