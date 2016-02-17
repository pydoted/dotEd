# -*- coding: utf-8 -*-

from doted.controller.Controller import Controller


class MainWindowController(Controller):
    '''Controller to manage a MainWindow.
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller    
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)
    
    def onCreateNode(self):
        '''Callback function when creating a node.'''
        self.model.addNode("A")
        self.model.notify()
