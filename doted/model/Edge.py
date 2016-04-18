# -*- coding: utf-8 -*-

from enumeration.EdgeArgs import EdgeArgs


class Edge(object):
    '''
    The Edge class defines an edge (model).
    
    
    Argument(s):
    source (Node): Source node
    dest (Node): Destination node
    id (int): ID
    
    Attribute(s):
    id (int): ID
    source (Node): Source node
    dest (Node): Destination node
    '''


    def __init__(self, source, dest, id):
        self.id = id
        self.source = source
        self.dest = dest
        source.addNeighbour(dest)
        dest.addNeighbour(source)
        #self.color enum ?

    def getArgs(self):
        '''Return a dictionary of the arguments of the edge.'''
        return {
                EdgeArgs.id: self.id,
                EdgeArgs.sourceId: self.source.id,
                EdgeArgs.destId: self.dest.id
            }
