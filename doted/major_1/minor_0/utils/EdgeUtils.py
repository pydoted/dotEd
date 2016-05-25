# -*- coding: utf-8 -*-

# Copyright (c) 2016 Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem
# This file is part of dotEd.
#
# dotEd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dotEd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dotEd.  If not, see <http://www.gnu.org/licenses/>.


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
