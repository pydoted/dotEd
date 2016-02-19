# -*- coding: utf-8 -*-

from observer.Observer import Observer


class Controller(Observer):
    '''Base class for controllers.
    
    
    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller
    
    Attribute(s):
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Observer.__init__(self, model)
        
        self.view = view
        self.view.setController(self)
    
    def updateView(self):
        '''Update the view.'''
        self.view.update()
