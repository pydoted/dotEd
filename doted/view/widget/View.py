# -*- coding: utf-8 -*-


class View(object):
    '''The View class defines a base class for views.
    
    
    Attribute(s):
    controller (Controller): Controller of the view
    '''


    def __init__(self):
        self.controller = None

    def setController(self, controller):
        '''Set a controller.
        
        Argument(s):
        controller (Controller): Controller of the view
        '''
        self.controller = controller

    def update(self):
        '''Update the view.'''
        pass
