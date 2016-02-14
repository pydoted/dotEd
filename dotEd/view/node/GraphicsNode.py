# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF
from view.node.GraphicsTextNode import GraphicsTextNode


class GraphicsNode:
    '''
    classdocs
    '''


    def __init__(self, nodeId, *args, **kargs):
        '''
        Constructor
        '''
        self.nodeId = nodeId;
        self.graphicsTextNode = GraphicsTextNode(*args, **kargs);
        self.graphicsTextNode.boundingRect().marginsAdded(QMarginsF(10, 10, 10, 10))
    
    def centerTextInShape(self):
        pass
