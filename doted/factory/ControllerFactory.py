# -*- coding: utf-8 -*-

from controller.GraphicsGraphController import GraphicsGraphController
from controller.MainWindowController import MainWindowController
from controller.TextGraphController import TextGraphController


class ControllerFactory(object):
    '''The ControllerFactory class allows to create controllers.'''
    
    
    @staticmethod
    def newGraphicsGraphController(model, view):
        '''Create and return a GraphicsGraphController.
        
        Argument(s):
        model (Model): Model of the controller
        view (View): View of the controller
        '''
        return GraphicsGraphController(model, view)
    
    @staticmethod
    def newMainWindowController(model, view):
        '''Create and return a MainWindowController.
        
        Argument(s):
        model (Model): Model of the controller
        view (View): View of the controller
        '''
        return MainWindowController(model, view)

    @staticmethod
    def newTextGraphController(model, view):
        '''Create and return a TextGraphController.
        
        Argument(s):
        model (Model): Model of the controller
        view (View): View of the controller
        '''
        return TextGraphController(model, view)
        