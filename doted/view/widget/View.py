# -*- coding: utf-8 -*-


class View(object):
    '''The View class defines a base class for views.
    
    
    Attribute(s):
    controller (Controller): Controller of the view
    '''


    def __init__(self):
        self.controller = None

    def setController(self, controller):
        '''Set a controller.
        
        Argument(s):
        controller (Controller): Controller of the view
        '''
        self.controller = controller

    def updateNode(self, dictArgsNode, updateMode):
        '''Update a node (on the scene).
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        updateMode (UpdateMode) : Update mode
        '''
        pass
            
            
    def updateEdge(self, dictArgsEdge, updateMode):
        '''Update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateMode (UpdateMode) : Update mode
        '''
        pass
