# -*- coding: utf-8 -*-
from observer.Observateur import Observateur

class Controller(Observateur):
    '''
    classdocs
    '''

    def __init__(self, model, view):
        '''
        Constructor
        '''
        Observateur.__init__(self, model)
        self.view = view
        view.setController(self)
    
    def actualise(self):
        '''
        actualise (to complete)
        '''
        pass
