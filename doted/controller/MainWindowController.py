# -*- coding: utf-8 -*-

from controller.Controller import Controller


class MainWindowController(Controller):
    '''Controller to manage a MainWindow.
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller    
    '''

    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)
