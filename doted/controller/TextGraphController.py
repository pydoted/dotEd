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

    def onCreateNode(self, idNode, dicDotAttrs, x, y):
        '''Callback function when creating a node.
        
        Argument(s):
        idNode (str): ID of the node
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        self.model.addNode(idNode, dicDotAttrs, x, y)
    
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
        
    def onRemoveEdge(self, idSourceNode, idDestNode):
        '''Callback function when removing an edge.
        
        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (intstr): ID of the destination node
        '''
        self.model.removeEdgeByIdNodes(idSourceNode, idDestNode)
