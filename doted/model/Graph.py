# -*- coding: utf-8 -*-

from observer.Subject import Subject
from model.Node import *
from model.Edge import *

class Graph(Subject):
    '''Model of a graph.
    
    
    Argument(s):
    directed (boolean): Graph directed or not (default False)
    
    Attribute(s):
    nodes (Dictionary[Node]): All nodes
    edges (Dictionary[Edge]): All edges
    nbNodes (Dictionary[Edge]): number of nodes
    nbEdges (Dictionary[Edge]): number of edges
    directed (boolean): Graph directed or not
    '''

    def __init__(self, directed=False):
        # Parent constructor(s)
        Subject.__init__(self)
        
        self.nodes = {}
        self.edges = {}
        self.nbNodes = 0
        self.nbEdges = 0
        self.directed = directed

    def addNode(self):
        '''Add a Node to the graph.'''
        self.nbNodes += 1
        node = Node(self.nbNodes)
        self.nodes[node.id] = node
        self.notify();
    
        
    def removeNode(self, idNode):
        '''Remove a Node from the graph.
        
        Argument(s):
        idNode (int): ID of the node to remove
        '''
        self.nodes.pop(idNode)
    
    def addEdgde(self, idSourceNode, idDestNode):
        '''Add an Edge to the graph.
        
        Argument(s):
        idSourceNode (int): ID of the source node
        idDestNode (int): ID of the destination node
        '''
        self.nbEdges += 1
        edge = Edge(self.nodes[idSourceNode],
                                    self.nodes[idDestNode], self.nbEdges)
        self.edges[edge.id] = edge
        self.notify();
    
    def removeEdgde(self, idEdge):
        '''Remove an Edge from the graph.
        
        Argument(s):
        idEdge (int): ID of the edge to remove
        '''
        self.edges.pop(idEdge)
