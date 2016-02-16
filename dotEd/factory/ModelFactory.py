# -*- coding: utf-8 -*-

from model.Node import Node
from model.Edge import Edge


class ModelFactory(object):
    '''Factory to create models.'''
    
    
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
