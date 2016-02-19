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
        
    def update(self, dictArgsNode, dictArgsEdge):
        '''Update the view.
        
        Argument(s):
        dictArgsNode (dict): dictionary of arguments of the node
        dictArgsEdge (dict): dictionary of arguments of the edge
        ''' 
        if self.ignore:
            self.ignore = False
        else:
            if dictArgsNode: 
                self.view.updateNode(dictArgsNode)
            else:
                self.view.updateNode(dictArgsEdge)
            
    def onCreateNode(self):
        '''Callback function when creating a node.'''
        self.ignore = True;
        self.model.addNode()
       
    
    def onCreateEdge(self):
        '''Callback function when creating an edge.'''
        self.ignore = True;
        self.model.addEdgde()