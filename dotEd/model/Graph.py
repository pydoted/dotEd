# -*- coding: utf-8 -*-

class Graph:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.nodes = []
        self.edges = []
        self.subgraph = []
        self.directed = False

    def addNode(self, node):
        '''
        addNode (to complete)
        '''
        self.nodes.append(node)
    
    def removeNode(self, node):
        '''
        removeNode (to complete)
        '''
        self.nodes.remove(node)
    
    def addEdgde(self, edge):
        '''
        addEdgde (to complete)
        '''
        self.edges.append(edge)
    
    def removeEdgde(self, edge):
        '''
        removeEdgde (to complete)
        '''
        self.edges.remove(edge)

    @property
    def directed(self):
        '''
        directed (to complete)
        '''
        return self.directed
    
    @directed.setter
    def directed(self, directed):
        '''
        directed (to complete)
        '''
        self.directed = directed
    