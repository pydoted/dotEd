# -*- coding: utf-8 -*-


class GraphicsEdge(object):
    '''The GraphicsEdge class defines the base class of a graphics edge.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    
    Attribute(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    '''


    def __init__(self, source, dest, id):
        self.source = source
        self.dest = dest
        self.id = id
