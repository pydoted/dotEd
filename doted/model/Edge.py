# -*- coding: utf-8 -*-


class Edge:
    '''
    The Edge class defines an edge (model).
    
    
    Argument(s):
    source (Node): Source node
    dest (Node): Destionation node
    id (int): Id 
    
    Attribute(s):
    id (int): ID
    source (Node): Source node
    dest (Node): Destionation node
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
                "id": self.id,
                "source": self.source,
                "dest": self.dest
            }
