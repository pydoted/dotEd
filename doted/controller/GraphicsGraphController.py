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
            
    def onCreateNode(self, x, y):
        '''Callback function when creating a node.
        
        Argument(s):
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        self.model.addNode(None, {}, x, y)
    
    def onEditNode(self, idNode, dicDotAttrs):
        '''Callback function when editing a label a node.
        
        Argument(s):
        idNode (str): ID of the node to edit
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        self.model.editNode(idNode, dicDotAttrs)
    
    def onRemoveNode(self, idNode):
        '''Callback function when removinf a node.
        
        Argument(s):
        idNode (str): ID of the node to remove
        '''
        self.model.removeNode(idNode)
    
    def onCreateEdge(self, idSourceNode, idDestNode):
        '''Callback function when creating an edge.
        
        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        self.model.addEdge(idSourceNode, idDestNode)

    def onRemoveEdge(self, idEdge):
        '''Callback function when removing an edge.
        
        Argument(s):
        idEdge (str): ID of the edge to remove
        '''
        self.model.removeEdge(idEdge)
