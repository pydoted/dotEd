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
        self.model.addNode(x, y)
    
    def onEditLabelNode(self, idNode, labelNode):
        '''Callback function when editing a label a node.
        
        Argument(s):
        idNode (int): ID of the node to edit
        labelNode (str): New label of the node
        '''
        self.model.editLabelNode(idNode, labelNode)
    
    def onRemoveNode(self, idNode):
        '''Callback function when removinf a node.
        
        Argument(s):
        idNode (int): ID of the node to remove
        '''
        self.model.removeNode(idNode)
    
    def onCreateEdge(self, idSourceNode, idDestNode):
        '''Callback function when creating an edge.
        
        Argument(s):
        idSourceNode (int): ID of the source node
        idDestNode (int): ID of the destination node
        '''
        self.model.addEdge(idSourceNode, idDestNode)

    def onRemoveEdge(self, idEdge):
        '''Callback function when removing an edge.
        
        Argument(s):
        idEdge (int): ID of the edge to remove
        '''
        self.model.removeEdge(idEdge)
