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

    def addNode(self, dictArgsNode):
        '''Add a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def editNode(self, dictArgsNode):
        '''Edit a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def removeNode(self, dictArgsNode):
        '''Remove a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def addEdge(self, dictArgsEdge):
        '''Add an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass

    def editEdge(self, dictArgsEdge):
        '''Edit an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass

    def removeEdge(self, dictArgsEdge):
        '''Remove an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass
