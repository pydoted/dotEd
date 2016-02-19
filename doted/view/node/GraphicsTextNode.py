# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsTextItem


class GraphicsTextNode(QGraphicsTextItem):
    '''Represent the text view of a Node.
    
    
    Argument(s):
    label (str): Label of the node
    '''


    def __init__(self, label):
        # Parent constructor(s)
        QGraphicsTextItem.__init__(self, label)
        
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
    
    def keyPressEvent(self, event):
        '''Center the text in the shape each time the text is modified.
        
        Argument(s):
        event (QKeyEvent): Key event
        '''
        QGraphicsTextItem.keyPressEvent(self, event)
        self.parentItem().centerTextInShape()
