# -*- coding: utf-8 -*-

from PyQt5.Qt import QLineF
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem

from view.edge.GraphicsEdge import GraphicsEdge


class GraphicsLineEdge(GraphicsEdge, QGraphicsLineItem):
    '''The GraphicsLineEdge defines a graphics edge as a simple line.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    '''


    def __init__(self, source, dest):
        # Parent constructor(s)
        GraphicsEdge.__init__(self, source, dest)
        QGraphicsLineItem.__init__(self)
        
        # Get the two shapes of each node
        sourceShape = self.source.mapToScene(self.source.shape())
        destShape = self.dest.mapToScene(self.dest.shape())
        
        # Compute the closest points between the two shapes
        pSource = self.closestPointTo(destShape.boundingRect().center(),
                                      sourceShape)
        pDest = self.closestPointTo(sourceShape.boundingRect().center(),
                                    destShape)
        
        self.setLine(QLineF(pSource, pDest))
        self.setFlag(QGraphicsItem.ItemIsSelectable)
