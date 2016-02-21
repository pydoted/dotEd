# -*- coding: utf-8 -*-


class GraphicsEdge(object):
    '''The GraphicsEdge class defines the base class of a graphics edge.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    
    Attribute(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    '''


    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        
    def closestPointTo(self, point, path):
        '''Return the closest point between a point and a path.
        
        Argument(s):
        point (QPointF): Point
        path (QPainterPath): Painter path
        '''
        target = path.boundingRect().center()
        mid = (point + target) / 2.0
        
        if path.contains(mid):
            return mid
        else:
            while (mid - point).manhattanLength() > 1:
                while not path.contains(mid) :
                    point = mid
                    mid = (point + target) / 2.0
    
                while path.contains(mid) :
                    mid = (point + mid) / 2.0
                    
            return mid
