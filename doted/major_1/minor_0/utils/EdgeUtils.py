# -*- coding: utf-8 -*-


class EdgeUtils(object):
    '''The EdgeUtils class defines a set of functions for edges.'''

    @staticmethod
    def createEdgeId(idSourceNode, idDestNode):
        '''Create an ID for an edge.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        return idSourceNode + "-" + idDestNode

    @staticmethod
    def closestPointTo(point, path):
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
                while not path.contains(mid):
                    point = mid
                    mid = (point + target) / 2.0

                while path.contains(mid):
                    mid = (point + mid) / 2.0

            return mid
