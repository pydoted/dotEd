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

from PyQt5.QtWidgets import QGraphicsLineItem

from major_1.minor_0.utils.EdgeUtils import EdgeUtils


class GraphicsSemiEdge(QGraphicsLineItem):
    '''The GraphicsSemiEdge class defines a line between a GraphicsNode and a
    QPoint.


    Argument(s):
    source (QPoint): Mouse position
    dest (GraphicsNode): Node view
    '''

    def __init__(self, source, dest):
        # Parent constructor(s)
        QGraphicsLineItem.__init__(self)

        self.source = source
        self.dest = dest

    def update(self, source):
        '''Update the coordinates of the line.

        Argument(s):
        source (QPointF): Source point
        '''
        destShape = self.dest.mapToScene(self.dest.shape())
        p = EdgeUtils.closestPointTo(source, destShape)

        self.setLine(source.x(), source.y(), p.x(), p.y())
