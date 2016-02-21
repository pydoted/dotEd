# -*- coding: utf-8 -*-

from controller.Controller import Controller


class GraphicsGraphController(Controller):
    '''The GraphicsGraphController class defines a controller to manage a
       Graph (model)/GraphicsGraphView (view).
    
    
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
        dictArgsNode (Dictionary[]): dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): dictionary of arguments of the edge
        ''' 
        if dictArgsNode: 
            self.view.updateNode(dictArgsNode)
        else:
            self.view.updateEdge(dictArgsEdge)
            
    def onCreateNode(self, x, y):
        '''Callback function when creating a node.
        
        Argument(s):
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        self.model.addNode(x, y)
    
    def onCreateEdge(self, idSourceNode, idDestNode):
        '''Callback function when creating an edge.
        
        Argument(s):
        idSourceNode (int): ID of the source node
        idDestNode (int): ID of the destination node
        '''
        self.model.addEdge(idSourceNode, idDestNode)
