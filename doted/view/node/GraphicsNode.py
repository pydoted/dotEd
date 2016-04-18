# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF

from view.node.GraphicsTextNode import GraphicsTextNode


class GraphicsNode(object):
    '''The GraphicsNode class defines a base class for a graphics node.
    
    Argument(s):
    id (int): Id of the node
    label (str): Label of the node
    
    Attribute(s):
    id (int): ID of the node
    graphicsTextNode (GraphicsTextNode): Text (label) of the node
    semiEdge (GraphicsSemiEdge): Line between a graphics node and cursor mouse
    '''


    def __init__(self, id, label):
        self.id = id;
        
        # Init graphics text node
        self.graphicsTextNode = GraphicsTextNode(label);
        (self.graphicsTextNode.boundingRect().
                               marginsAdded(QMarginsF(10, 10, 10, 10)))
        
        self.semiEdge = None
    
    def centerTextInShape(self):
        '''Center the text in the shape.'''
        pass

    def getGraphicsView(self):
        '''Return the graphics view.'''
        return self.scene().views()[0]
