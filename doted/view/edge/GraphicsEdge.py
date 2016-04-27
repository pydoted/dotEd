# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsItem


class GraphicsEdge(object):
    '''The GraphicsEdge class defines the base class of a graphics edge.
    
    
    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    
    Attribute(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    '''


    def __init__(self, source, dest, id):
        self.source = source
        self.dest = dest
        self.id = id
        
    def getGraphicsView(self):
        '''Return the graphics view.'''
        return self.scene().views()[0]
        
    def getFocus(self, id):
        '''Indicate when edge get the focus to highlight her in textual view
        
        Argument(s):
        id (str): ID of the node
        '''
        controller = self.getGraphicsView().controller
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
