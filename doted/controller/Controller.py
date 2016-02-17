# -*- coding: utf-8 -*-

from doted.observer.Observator import Observator


class Controller(Observator):
    '''Base class for controllers.
    
    
    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller
    
    Attribute(s):
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Observator.__init__(self, model)
        
        self.view = view
        self.view.setController(self)
    
    def updateView(self):
        '''Update the view.'''
        self.view.update()
