# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem

from view.edge.EdgeUtils import EdgeUtils
from view.edge.GraphicsEdge import GraphicsEdge


class GraphicsLineEdge(GraphicsEdge, QGraphicsLineItem):
    '''The GraphicsLineEdge defines a graphics edge as a simple line.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    '''


    def __init__(self, source, dest, id):
        # Parent constructor(s)
        GraphicsEdge.__init__(self, source, dest, id)
        QGraphicsLineItem.__init__(self)
        
        self.setFlag(QGraphicsItem.ItemIsSelectable)        
        self.update()

    def update(self):
        '''Update the coordinates of the line.'''
        # Get the two shapes of each node
        sourceShape = self.source.mapToScene(self.source.shape())
        destShape = self.dest.mapToScene(self.dest.shape())
        
        # Compute the closest points between the two shapes
        pSource = EdgeUtils.closestPointTo(destShape.boundingRect().center(),
                                           sourceShape)
        pDest = EdgeUtils.closestPointTo(sourceShape.boundingRect().center(),
                                         destShape)
        
        # Draw a line between source and dest
        self.setLine(pSource.x(), pSource.y(), pDest.x(), pDest.y())
