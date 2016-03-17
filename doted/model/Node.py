# -*- coding: utf-8 -*-

from enumeration.NodeArgs import NodeArgs


class Node(object):
    '''The Node class defines a node (model).
    
    
    Argument(s):
    label (str): Label 
    id (int): Id
    x (float): x coordinate (default 0.0)
    y (float): y coordinate (default 0.0)
    
    Attribute(s):
    id (int): Id
    label (str): Label
    x (float): x coordinate
    y (float): y coordinate
    neighbours (Dictionary[Edge]): Neighbouring nodes
    '''


    def __init__(self, id, x=0.0, y=0.0):
        self.id = id
        self.label = "n" + str(self.id)
        self.x = x
        self.y = y
        self.neighbours = {}
        #self.shape enum ?
        #self.color enum ?
        
    def addNeighbour(self, node):
        '''Add a neighbour.
        
        Argument(s):
        node (Node): Neighbour
        '''
        self.neighbours[node.id] = node
        
    def removeNeighbour(self, node):
        '''Remove a neighbour.
        
        Argument(s):
        node (Node): Neighbour
        '''
        self.neighbours.pop(node.id)

    def isNeighboringTo(self, id):
        '''Check if the node is neighboring with another.
        
        Argument(s):
        id (int): Node id
        '''
        return id in self.neighbours
    
    def getArgs(self):
        '''Return a dictionary of the arguments of the node.'''
        return {
                NodeArgs.id: self.id,
                NodeArgs.label: self.label,
                NodeArgs.x: self.x,
                NodeArgs.y: self.y
            }
