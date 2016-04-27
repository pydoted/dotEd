# -*- coding: utf-8 -*-

from enumeration.NodeArgs import NodeArgs
from enumeration.NodeDotAttrs import NodeDotAttrs


class Node(object):
    '''The Node class defines a node (model).
    
    
    Argument(s):
    id (str): Id
    x (float): x coordinate (default 0.0)
    y (float): y coordinate (default 0.0)
    dicDotAttrs (Dictionary[]): Dot attributes (default {})
    
    Attribute(s):
    id (str): ID
    x (float): x coordinate
    y (float): y coordinate
    dotAttrs (Dictionary[]): Dot attributes
    neighbours (Dictionary[Edge]): Neighbouring nodes
    '''

    def __init__(self, id, dicDotAttrs={}, x=0.0, y=0.0):
        self.id = id
        self.x = x
        self.y = y
        
        self.neighbours = {}
        self.dotAttrs = {}
    
        self.edit(dicDotAttrs)
        
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

    def edit(self, dicDotAttrs):
        '''Edit dot attributes of the node.
        
        Argument(s):
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        for attr, val in dicDotAttrs.items():
                self.dotAttrs[attr] = val
    
    def isNeighboringTo(self, id):
        '''Check if the node is neighboring with another.
        
        Argument(s):
        id (str): Node id
        '''
        return id in self.neighbours
    
    def getArgs(self):
        '''Return a dictionary of the arguments of the node.'''
        return {
                NodeArgs.id: self.id,
                NodeArgs.dotAttrs: self.dotAttrs,
                NodeArgs.x: self.x,
                NodeArgs.y: self.y
            }
