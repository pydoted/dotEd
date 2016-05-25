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

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsItem


class GraphicsEdge(object):
    '''The GraphicsEdge class defines the base class of a graphics edge.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    graphicsGraphView (GraphicsGraphView): View
    
    Attribute(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    graphicsGraphView (GraphicsGraphView): View
    '''


    def __init__(self, source, dest, id, graphicsGraphView):
        self.source = source
        self.dest = dest
        self.id = id
        self.graphicsGraphView = graphicsGraphView
    
    def edit(self, dictArgsEdge):
        '''Edit the edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass
    
    def getFocus(self, id):
        '''Indicate when edge get the focus to highlight her in textual view
        
        Argument(s):
        id (str): ID of the node
        '''
        controller = self.graphicsGraphView.controller
        controller.onSelectItem(id)
        
    def mousePressEvent(self, event):
        '''Handle mouse press event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsItem.mousePressEvent(self, event)

        # Get the focus
        if event.buttons() == Qt.LeftButton:
            self.getFocus(self.id)
