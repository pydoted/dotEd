# -*- coding: utf-8 -*-


class Edge:
    '''
    Model of an edge.
    
    
    Argument(s):
    source (Node): Source node
    dest (Node): Destionation node
    
    Attribute(s):
    id (int): ID
    source (Node): Source node
    dest (Node): Destionation node
    '''


    def __init__(self, source, dest, id):
        self.id = id
        self.source = source
        self.dest = dest
        #self.color enum ?
