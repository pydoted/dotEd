# -*- coding: utf-8 -*-

from model import Node
from model import Edge

class Factory:
    '''
    classdocs
    '''
    
    @staticmethod
    def newNode(label = ""):
        return Node(label)
    
    @staticmethod
    def newEdge(source, dest):
        return Edge(source, dest)
    