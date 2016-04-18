# -*- coding: utf-8 -*-

from controller.Controller import Controller


class TextGraphController(Controller):
    '''The TextGraphController class defines a controller to manage
       a Graph (model)/TextGraphView (view).
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)
