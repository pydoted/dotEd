# -*- coding: utf-8 -*-

from PyQt5.Qt import QMarginsF, Qt
from PyQt5.QtWidgets import QGraphicsItem

from utils.DotAttrsUtils import DotAttrsUtils
from enumeration.NodeDotAttrs import NodeDotAttrs
from view.edge.GraphicsSemiEdge import GraphicsSemiEdge
from view.node.GraphicsTextNode import GraphicsTextNode


class GraphicsNode(object):
    '''The GraphicsNode class defines a base class for a graphics node.
    
    Argument(s):
    id (str): ID of the node
    label (str): Label of the node
    
    Attribute(s):
    id (str): ID of the node
    graphicsTextNode (GraphicsTextNode): Text (label) of the node
    semiEdge (GraphicsSemiEdge): Line between a graphics node and cursor mouse
    sceneRectHasBeenUpdated (bool): Flag to check if the scene rect has been
                                    updated
    isMoving (bool): Flag to check if a node is moving
    lastX (float): Last x coordinate of the node 
    lastY (float): Last y coordinate of the node
    '''


    def __init__(self, id, label):
        self.id = id;
        
        # Init graphics text node
        self.graphicsTextNode = GraphicsTextNode(label);
        (self.graphicsTextNode.boundingRect().
                               marginsAdded(QMarginsF(10, 10, 10, 10)))
        
        self.semiEdge = None
        self.sceneRectHasBeenUpdated = False
        
        self.isMoving = False        
        self.lastX = None
        self.lastY = None
    
    def centerTextInShape(self):
        '''Center the text in the shape.'''
        pass

    def getGraphicsView(self):
        '''Return the graphics view.'''
        return self.scene().views()[0]
    
    def getGraphicsViewController(self):
        '''Return the controller of the graphics view.'''
        return self.getGraphicsView().controller
    
    def getFocus(self, id):
        '''Indicate when node get the focus to highlight him in textual view.
        
        Argument(s):
        id (str): ID of the node
        '''
        self.getGraphicsViewController().onSelectItem(id)
        
    def mouseMoveEvent(self, event):
        '''Handle mouse move event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''        
        # Move the node
        if event.modifiers() == Qt.ControlModifier:
            QGraphicsItem.mouseMoveEvent(self, event)
            
            # Update coordinates of each edge of the current node
            self.getGraphicsView().updateEdgesOfNode(self)
            self.getFocus(self.id)
            
            self.isMoving = True
            self.lastX = event.scenePos().x()
            self.lastY = event.scenePos().y()
            
            # Update scene rect if needed
            if self.getGraphicsView().updateSceneRect(self):
                self.sceneRectHasBeenUpdated = True
                    
        # Update coordinates of the line
        if self.semiEdge is not None:
            self.semiEdge.update(event.scenePos())
    
    def mousePressEvent(self, event):
        '''Handle mouse press event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsItem.mousePressEvent(self, event)
        
        # Create the semi-edge and get the focus
        if event.buttons() == Qt.LeftButton:
            self.getFocus(self.id)
            self.semiEdge = GraphicsSemiEdge(event.scenePos(), self)
            self.scene().addItem(self.semiEdge)
        
    def mouseReleaseEvent(self, event):
        '''Handle mouse release event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsItem.mouseReleaseEvent(self, event)
        
        # Notify other view(s) to update position of the node
        if self.isMoving:
            self.isMoving = False
            dicDotAttrs = {}
            dicDotAttrs[NodeDotAttrs.pos.value] = (DotAttrsUtils.formatPos(
                                        self.lastX,
                                        self.lastY))
            self.getGraphicsViewController().onEditNode(self.id, dicDotAttrs)
            self.getFocus(self.id)
        
        # Center scene on the node if needed
        if self.sceneRectHasBeenUpdated:
            self.getGraphicsView().centerOn(self)
            self.sceneRectHasBeenUpdated = False
        
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
                self.getGraphicsViewController().onCreateEdge(self.id,
                                                              items[0].id)
                
    def mouseDoubleClickEvent(self, event):
        '''Handle mouse double click event.
        
        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        # Double click on the text of the node to edit text
        self.graphicsTextNode.mouseDoubleClickEvent(event)
