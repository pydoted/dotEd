# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF

from view.node.GraphicsTextNode import GraphicsTextNode


class GraphicsNode(object):
    '''Base class view of a Node.
    
    Argument(s):
    id (int): Id of the node
    label (str): Label of the node
    
    Attribute(s):
    id (int): Id of the node
    graphicsTextNode (GraphicsTextNode): Text (label) of the node
    '''


    def __init__(self, id, label):
        self.id = id;
        self.graphicsTextNode = GraphicsTextNode(label);
        (self.graphicsTextNode.boundingRect().
                               marginsAdded(QMarginsF(10, 10, 10, 10)))
    
    def centerTextInShape(self):
        '''Center the text in the shape.'''
        pass
