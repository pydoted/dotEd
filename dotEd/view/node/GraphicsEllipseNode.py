# -*- coding: utf-8 -*-

from PyQt5.QtCore import QMarginsF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem
from view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''
    classdocs
    '''


    def __init__(self, nodeId, nodeLabel, *args, **kargs):
        '''
        Constructor
        '''
        GraphicsNode.__init__(self, nodeId, nodeLabel)
        QGraphicsEllipseItem.__init__(self, *args, **kargs)
        self.graphicsTextNode.setParentItem(self)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.centerTextInShape()

    def centerTextInShape(self):
        self.setRect(self.graphicsTextNode.boundingRect().marginsAdded(QMarginsF(10, 10, 10, 10)))
