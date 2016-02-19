# -*- coding: utf-8 -*-

from observer.Observer import Observer


class Controller(Observer):
    '''Base class for controllers.
    
    
    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller
    
    Attribute(s):
    view (View): View of the controller
    ignore_notify (boolean): To ignore boomerang effect after an update of model
                             make by self.
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Observer.__init__(self, model)
        
        self.ignore = False
        self.view = view
        self.view.setController(self)
    
    def update(self):
        '''Update the view.'''
        pass
        
