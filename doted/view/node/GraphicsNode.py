# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF

from doted.view.node.GraphicsTextNode import GraphicsTextNode


class GraphicsNode(object):
    '''Base class view of a Node.
    
    Argument(s):
    nodeId (int): ID of the node
    nodeLabel (str): Label of the node
    
    Attribute(s):
    nodeId (int): ID of the node
    graphicsTextNode (GraphicsTextNode): Text (label) of the node
    '''


    def __init__(self, nodeId, nodeLabel):
        self.nodeId = nodeId;
        self.graphicsTextNode = GraphicsTextNode(nodeLabel);
        (self.graphicsTextNode.boundingRect().
                               marginsAdded(QMarginsF(10, 10, 10, 10)))
    
    def centerTextInShape(self):
        '''Center the text in the shape.'''
        pass
