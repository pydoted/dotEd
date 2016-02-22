# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsLineItem

from view.edge.GraphicsEdge import GraphicsEdge


class GraphicsSemiEdge(GraphicsEdge, QGraphicsLineItem):
    '''The GraphicsSemiEdge class defines a line between a GraphicsNode and a QPoint. 
    
    
    Argument(s):
    source (QPoint): Mouse position
    dest (GraphicsNode): Node view
    '''


    def __init__(self, source, dest):
        # Parent constructor(s)
        GraphicsEdge.__init__(self, source, dest)
        QGraphicsLineItem.__init__(self)
    
    def update(self, source):
        '''Update the coordinates of the line.
        
        Argument(s):
        source (QPointF): Source point
        '''
        destShape = self.dest.mapToScene(self.dest.shape())
        p = self.closestPointTo(source, destShape)
        
        self.setLine(source.x(), source.y(), p.x(), p.y())
