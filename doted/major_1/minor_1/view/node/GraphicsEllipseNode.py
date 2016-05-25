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

from PyQt5.Qt import QMarginsF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem

from doted.major_1.minor_1.view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''The GraphicsEllipseNode class defines a graphics node as an ellipse
    containing a text.


    Argument(s):
    id (str): ID of the node
    graphicsGraphView (GraphicsGraphView): View
    '''

    def __init__(self, id, graphicsGraphView):
        # Parent constructor(s)
        GraphicsNode.__init__(self, id, graphicsGraphView)
        QGraphicsEllipseItem.__init__(self)

        # Init text node
        self.graphicsTextNode.setParentItem(self)
        self.setFlags(QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemIsSelectable)
        self.centerTextInShape()

    def updateShapeAndEdges(self):
        '''Center the text in the shape and update coordinates of each edge of
           the current node'''
        self.centerTextInShape()
        self.graphicsGraphView.updateEdgesOfNode(self)

    def centerTextInShape(self):
        '''Center the text in the ellipse.'''
        self.setRect(self.graphicsTextNode.boundingRect().
                     marginsAdded(QMarginsF(10, 10, 10, 10)))
