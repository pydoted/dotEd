# -*- coding: utf-8 -*-

from controller.Controller import Controller


class MainWindowController(Controller):
    '''The MainWindowController class defines the controller to manage
       a Doted (app)/MainWindow (view).
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller    
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)

    def update(self, dictArgsNode, dictArgsEdge, updateModeView):
        '''Update the view.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView) : Update mode
        ''' 
        pass
