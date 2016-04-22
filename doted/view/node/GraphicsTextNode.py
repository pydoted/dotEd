# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsTextItem

from enumeration.NodeDotAttrs import NodeDotAttrs


class GraphicsTextNode(QGraphicsTextItem):
    '''The GraphicsTextNode class defines the text of a GraphicsNode.


    Argument(s):
    label (str): Label of the node
    '''


    def __init__(self, label):
        # Parent constructor(s)
        QGraphicsTextItem.__init__(self, label)

    def keyPressEvent(self, event):
        '''Handle key pressed event.

        Argument(s):
        event (QKeyEvent): Key event
        '''
        QGraphicsTextItem.keyPressEvent(self, event)
        self.parentItem().updateShapeAndEdges()
  
    def mouseDoubleClickEvent(self, event):
        '''Handle mouse double click event.

        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsTextItem.mouseDoubleClickEvent(self, event)
        
        # Enable edit text
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        
        # Go to edit mode text
        self.setFocus()        

    def focusOutEvent(self, event):
        '''Handle focus out event.

        Argument(s):
        event (QFocusEvent ): Focus event
        '''
        QGraphicsTextItem.focusOutEvent(self, event)
        
        # Update text in other views
        node = self.parentItem()
        dicDotAttrs = {}
        dicDotAttrs[NodeDotAttrs.label.value] = self.toPlainText()
        node.getGraphicsView().controller.onEditNode(node.id, dicDotAttrs)
        
        # Disable edit text
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        
    def contextMenuEvent(self, event):
        '''Handle context menu event.
        
        Argument(s):
        event (QGraphicsSceneContextMenuEvent): Graphics scene context menu 
                                                event
        '''
        # Disable context menu (right click)
        pass

    def setPlainText(self, text):
        '''Sets the item's text to text.
        
        Argument(s):
        text (str): Text to set
        '''
        QGraphicsTextItem.setPlainText(self, text)
        self.parentItem().updateShapeAndEdges()
