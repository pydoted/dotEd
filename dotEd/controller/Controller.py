# -*- coding: utf-8 -*-

from observer.Observator import Observator


class Controller(Observator):
    '''
    classdocs
    '''

    def __init__(self, model, view):
        '''
        Constructor
        '''
        Observator.__init__(self, model)
        self.view = view
        view.setController(self)
    
    def updateView(self):
        '''
        updateView (to complete)
        '''
        self.view.update()
