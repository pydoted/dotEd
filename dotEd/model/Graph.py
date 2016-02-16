# -*- coding: utf-8 -*-

from factory.ModelFactory import ModelFactory
from observer.Subject import Subject


class Graph(Subject):
    '''Model of a graph.
    
    
    Argument(s):
    directed (boolean): Graph directed or not (default False)
    
    Attribute(s):
    nodes (Dictionary[Node]): All nodes
    edges (Dictionary[Edge]): All edges
    directed (boolean): Graph directed or not
    '''

    def __init__(self, directed=False):
        # Parent constructor(s)
        Subject.__init__(self)
        
        self.nodes = {}
        self.edges = {}
        self.directed = directed

    def addNode(self, label):
        '''Add a Node to the graph.
        
        Argument(s):
        label (str): Label of the node
        '''
        node = ModelFactory.newNode(label)
        self.nodes[node.id] = node
    
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
        edge = ModelFactory.newEdge(self.nodes[idSourceNode],
                                    self.nodes[idDestNode])
        self.edges[edge.id] = edge
    
    def removeEdgde(self, idEdge):
        '''Remove an Edge from the graph.
        
        Argument(s):
        idEdge (int): ID of the edge to remove
        '''
        self.edges.pop(idEdge)
