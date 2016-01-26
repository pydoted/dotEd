# -*- coding: utf-8 -*-


class Factory:
    '''
    classdocs
    '''

    @staticmethod
    def newGraph(directed = False):
        return Graph(directed)
    
    @staticmethod
    def newNode(label = ""):
        return Node(label)
    
    @staticmethod
    def newEdge(source, dest):
        return Edge(source, dest)