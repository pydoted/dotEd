# -*- coding: utf-8 -*-

from controller.Controller import Controller


class GraphicsGraphController(Controller):
    '''Controller to manage a Graph/GraphicsGraphView.
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)

    def onCreateNode(self):
        '''Callback function when creating a node.'''
        self.ignore = True;
        self.model.addNode()
    
    def onCreateEdge(self):
        '''Callback function when creating an edge.'''
        self.ignore = True;
        self.model.addEdgde()