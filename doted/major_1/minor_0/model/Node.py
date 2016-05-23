# -*- coding: utf-8 -*-

from major_1.minor_0.utils.NodeDotPosUtils import NodeDotPosUtils
from major_1.minor_0.enumeration.NodeArgs import NodeArgs
from major_1.minor_0.enumeration.NodeDotAttrs import NodeDotAttrs


class Node(object):
    '''The Node class defines a node (model).
    
    
    Argument(s):
    id (str): ID
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
        
        dictAttrs = dicDotAttrs.copy()
        dictAttrs[NodeDotAttrs.pos.value] = NodeDotPosUtils.formatPos(x, y)
        self.edit(dictAttrs)
        
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
            # Case of pos attribute: we need to update x and y
            if attr == NodeDotAttrs.pos.value:
                if val:
                    pos = NodeDotPosUtils.getPos(val)
                    if pos:
                        self.x = pos[NodeArgs.x]
                        self.y = pos[NodeArgs.y]
                    else:
                        self.x = 0.0
                        self.y = 0.0
                else:
                    self.x = 0.0
                    self.y = 0.0
                        
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
