# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem

from view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''Represent a Node as an ellipse containing a text.
    
    
    Argument(s):
    id (int): Id of the node
    label (str): Label of the node
    '''


    def __init__(self, id, label):
        # Parent constructor(s)
        GraphicsNode.__init__(self, id, label)
        QGraphicsEllipseItem.__init__(self)
        
        self.graphicsTextNode.setParentItem(self)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.centerTextInShape()

    def centerTextInShape(self):
        '''Center the text in the ellipse.'''
        self.setRect(self.graphicsTextNode.boundingRect().
                          marginsAdded(QMarginsF(10, 10, 10, 10)))
