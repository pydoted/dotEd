# -*- coding: utf-8 -*-

from PyQt5.Qt import QMarginsF, Qt
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem

from view.edge.GraphicsSemiEdge import GraphicsSemiEdge
from view.node.GraphicsNode import GraphicsNode


class GraphicsEllipseNode(GraphicsNode, QGraphicsEllipseItem):
    '''The GraphicsEllipseNode class defines a graphics node as an ellipse 
       containing a text.
    
    
    Argument(s):
    id (str): ID of the node
    label (str): Label of the node
    '''


    def __init__(self, id, label):
        # Parent constructor(s)
        GraphicsNode.__init__(self, id, label)
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
        self.getGraphicsView().updateEdgesOfNode(self)

    def centerTextInShape(self):
        '''Center the text in the ellipse.'''
        self.setRect(self.graphicsTextNode.boundingRect().
                          marginsAdded(QMarginsF(10, 10, 10, 10)))
        
    def mouseMoveEvent(self, event):
        '''Handle mouse move event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''        
        # Move the node
        if event.modifiers() == Qt.ControlModifier:
            QGraphicsEllipseItem.mouseMoveEvent(self, event)
            
            # Update coordinates of each edge of the current node
            self.getGraphicsView().updateEdgesOfNode(self)
        
        # Update coordinates of the line
        if self.semiEdge is not None:
            self.semiEdge.update(event.scenePos())
    
    def mousePressEvent(self, event):
        '''Handle mouse press event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsEllipseItem.mousePressEvent(self, event)

        # Create the semi-edge
        if event.buttons() == Qt.LeftButton:
            self.semiEdge = GraphicsSemiEdge(event.scenePos(), self)
            self.scene().addItem(self.semiEdge)
        
    def mouseReleaseEvent(self, event):
        '''Handle mouse release event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsEllipseItem.mouseReleaseEvent(self, event)
        
        # Construct edge if a semi edge is built
        if self.semiEdge is not None:
            # Remove the semi edge
            self.scene().removeItem(self.semiEdge)
            self.semiEdge = None
         
            # Filter item on the mouse and only get GraphicsNode
            items = [item for item in self.scene().items(event.scenePos())
                     if isinstance(item, GraphicsNode) and item != self]
            if items:
                # Create edge
                self.getGraphicsView().controller.onCreateEdge(self.id,
                                                               items[0].id)
                
    def mouseDoubleClickEvent(self, event):
        '''Handle mouse double click event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        # Double click on the text of the node to edit text
        self.graphicsTextNode.mouseDoubleClickEvent(event)
