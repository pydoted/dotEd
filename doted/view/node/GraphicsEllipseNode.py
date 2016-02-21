# -*- coding: utf-8 -*-

from PyQt5.Qt import QMarginsF, Qt
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QApplication

from view.edge.GraphicsSemiEdge import GraphicsSemiEdge
from view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''The GraphicsEllipseNode defines a graphics node as an ellipse containing
       a text.
    
    
    Argument(s):
    id (int): Id of the node
    label (str): Label of the node
    
    Attribute(s):
    semiEdge (GraphicsSemiEdge): Line between graphics node and mouse
    '''


    def __init__(self, id, label):
        # Parent constructor(s)
        GraphicsNode.__init__(self, id, label)
        QGraphicsEllipseItem.__init__(self)
        
        self.graphicsTextNode.setParentItem(self)
        self.setFlags(QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemIsSelectable)
        
        self.centerTextInShape()
        self.semiEdge = None

    def centerTextInShape(self):
        '''Center the text in the ellipse.'''
        self.setRect(self.graphicsTextNode.boundingRect().
                          marginsAdded(QMarginsF(10, 10, 10, 10)))
        
    def mouseMoveEvent(self, event):
        '''Event handler when moving the graphics node.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Event
        '''
        modifiers = QApplication.keyboardModifiers()
        # Move the node
        if modifiers == Qt.ControlModifier:
            return QGraphicsEllipseItem.mouseMoveEvent(self, event)
        
        # Update coordinates of the line
        if self.semiEdge is not None:
            self.semiEdge.update(event.scenePos())
    
    def mousePressEvent(self, event):
        '''Event handler when clicking on the graphics node.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Event
        '''
        QGraphicsEllipseItem.mousePressEvent(self, event)
        modifiers = QApplication.keyboardModifiers()
        
        # Deselect all items then select itself
        if modifiers == Qt.ControlModifier:
            for item in self.scene().selectedItems():
                item.setSelected(False)
            self.setSelected(True)
            return

        # Create the semi-edge
        if event.buttons() == Qt.LeftButton:
            self.semiEdge = GraphicsSemiEdge(event.scenePos(), self)
            self.scene().addItem(self.semiEdge)
        
    def mouseReleaseEvent(self, event):
        '''Event handler when releasing the mouse button.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Event
        '''
        QGraphicsEllipseItem.mouseReleaseEvent(self, event)
        
        # Need to check else it is possible to create an edge with right click
        if self.semiEdge is not None:
            # Remove the semi-edge
            self.scene().removeItem(self.semiEdge)
            self.semiEdge = None
         
            # Filter item on the mouse and only get GraphicsNode
            items = [item for item in self.scene().items(event.scenePos())
                     if isinstance(item, GraphicsNode) and item != self]
            if items:
                # Get the controller of the view, no need to check index
                controller = self.scene().views()[0].controller
                controller.onCreateEdge(self.id, items[0].id)
