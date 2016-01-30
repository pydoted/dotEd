# -*- coding: utf-8 -*-

from observer import Sujet

class Graph(Sujet):
    '''
    classdocs
    '''


    def __init__(self, directed = False):
        '''
        Constructor
        '''
        self.nodes = {}
        self.edges = {}
        self.directed = directed

    def addNode(self, node):
        '''
        addNode (to complete)
        '''
        self.nodes[node.id] = node
    
    def removeNode(self, idNode):
        '''
        removeNode (to complete)
        '''
        self.nodes.pop(idNode)
    
    def addEdgde(self, edge):
        '''
        addEdgde (to complete)
        '''
        self.edges[edge.id] = edge
    
    def removeEdgde(self, idEdge):
        '''
        removeEdgde (to complete)
        '''
        self.edges.pop(idEdge)
