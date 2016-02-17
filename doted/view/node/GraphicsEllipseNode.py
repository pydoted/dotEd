# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem

from doted.view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''Represent a Node as an ellipse containing a text.
    
    
    Argument(s):
    nodeId (int): ID of the node
    nodeLabel (str): Label of the node
    x (float): x coordinate for the rectangle of the ellipse
    y (float): y coordinate for the rectangle of the ellipse
    width (float): width for the rectangle of the ellipse
    height (float): height for the rectangle of the ellipse
    '''


    def __init__(self, nodeId, nodeLabel, x, y, width, height):
        # Parent constructor(s)
        GraphicsNode.__init__(self, nodeId, nodeLabel)
        QGraphicsEllipseItem.__init__(self, x, y, width, height)
        
        self.graphicsTextNode.setParentItem(self)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.centerTextInShape()

    def centerTextInShape(self):
        '''Center the text in the ellipse.'''
        self.setRect(self.graphicsTextNode.boundingRect().
                          marginsAdded(QMarginsF(10, 10, 10, 10)))
