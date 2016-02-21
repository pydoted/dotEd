# -*- coding: utf-8 -*-

from model.Edge import Edge
from model.Node import Node


class ModelFactory(object):
    '''The ModelFactory class allows to create models.'''
    
    
    @staticmethod
    def newGraph(directed=False):
        '''Create and return a Graph.
        
        Argument(s):
        directed (boolean): Graph directed or not (default False)
        '''
        # Import done here to prevent circular import
        from model.Graph import Graph
        return Graph(directed)
    
    @staticmethod
    def newNode(label=""):
        '''Create and return a Node.
        
        Argument(s):
        label (str): Label of the node (default "")
        '''
        return Node(label)
    
    @staticmethod
    def newEdge(source, dest):
        '''Create and return an Edge.
        
        Argument(s):
        source (Node): Source node of the edge
        dest (Node): Destionation node of the edge
        '''
        return Edge(source, dest)
