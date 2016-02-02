# -*- coding: utf-8 -*-

from model.Node import Node
from model.Edge import Edge

class Factory:
    '''
    classdocs
    '''
    
    @staticmethod
    def newNode(label=""):
        return Node(label)
    
    @staticmethod
    def newEdge(source, dest):
        return Edge(source, dest)
    