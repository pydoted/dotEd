# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsTextItem


class GraphicsTextNode(QGraphicsTextItem):
    '''
    classdocs
    '''


    def __init__(self, nodeLabel):
        '''
        Constructor
        '''
        QGraphicsTextItem.__init__(self, nodeLabel)
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
    
    def keyPressEvent(self, event):
        QGraphicsTextItem.keyPressEvent(self, event)
        self.parentItem().centerTextInShape()
