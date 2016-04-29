# -*- coding: utf-8 -*-

from PyQt5.Qt import QEvent, Qt, QRectF, QTransform
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from enumeration.EdgeArgs import EdgeArgs
from enumeration.NodeArgs import NodeArgs
from enumeration.NodeDotAttrs import NodeDotAttrs
from view.edge.GraphicsEdge import GraphicsEdge
from view.edge.GraphicsLineEdge import GraphicsLineEdge
from view.node.GraphicsEllipseNode import GraphicsEllipseNode
from view.node.GraphicsNode import GraphicsNode
from view.widget.View import View


class GraphicsGraphView(View, QGraphicsView):
    '''The GraphicsGraphView defines a graphical representation of a Graph.
    
    
    Attribute(s):
    nodes (Dictionary[GraphicNode]): All nodes (views)
    edges (Dictionary[GraphicEdge]): All edges (views)
    scene (QGraphicsScene): Scene to show items (nodes and edges)
    '''
    

    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QGraphicsView.__init__(self)

        self.nodes = {}
        self.edges = {}
        
        # Init scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.resetSceneRect()
        self.scene.installEventFilter(self)
        
        self.show()

    def addNode(self, dictArgsNode):
        '''Add a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Get the text of the node
        text = self.getText(
                    dictArgsNode[NodeArgs.dotAttrs], dictArgsNode[NodeArgs.id])
        
        # Create the node
        self.nodes[dictArgsNode[NodeArgs.id]] = GraphicsEllipseNode(
                                              dictArgsNode[NodeArgs.id], text)
               
        # Set the position
        self.nodes[dictArgsNode[NodeArgs.id]].setPos(dictArgsNode[NodeArgs.x],
                              dictArgsNode[NodeArgs.y]) 
          
        # Add the node to the scene
        self.scene.addItem(self.nodes[dictArgsNode[NodeArgs.id]])
               
        # Reset scene rect
        if len(self.scene.items()) > 2:
            self.scene.setSceneRect(self.scene.itemsBoundingRect());
        
    def editNode(self, dictArgsNode):
        '''Edit a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Get the text of the node
        text = self.getText(
                    dictArgsNode[NodeArgs.dotAttrs], dictArgsNode[NodeArgs.id])
        
        # Update the text
        self.nodes[dictArgsNode[NodeArgs.id]].graphicsTextNode.setPlainText(
                                                text)
        
        # Update position
        self.nodes[dictArgsNode[NodeArgs.id]].setX(dictArgsNode[NodeArgs.x])
        self.nodes[dictArgsNode[NodeArgs.id]].setY(dictArgsNode[NodeArgs.y])
        self.updateEdgesOfNode(self.nodes[dictArgsNode[NodeArgs.id]])

    def removeNode(self, dictArgsNode):
        '''Remove a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Remove the node from the scene
        self.scene.removeItem(self.nodes[dictArgsNode[NodeArgs.id]])
        self.nodes.pop(dictArgsNode[NodeArgs.id])
        
        # Reset scene rect
        if len(self.scene.items()) == 0:
            self.resetSceneRect()

    def addEdge(self, dictArgsEdge):
        '''Add an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        
        # Init source and dest nodes
        source = self.nodes[dictArgsEdge[EdgeArgs.sourceId]]
        dest = self.nodes[dictArgsEdge[EdgeArgs.destId]]
        
        # Create the edge
        self.edges[dictArgsEdge[EdgeArgs.id]] = GraphicsLineEdge(source, dest,
                                                    dictArgsEdge[EdgeArgs.id])
        
        # Add edge to the scene
        self.scene.addItem(self.edges[dictArgsEdge[EdgeArgs.id]])
        
    def editEdge(self, dictArgsEdge):
        '''Edit an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass
    
    def removeEdge(self, dictArgsEdge):
        '''Remove an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        # Remove the edge from the scene
        self.scene.removeItem(self.edges[dictArgsEdge[EdgeArgs.id]])
        self.edges.pop(dictArgsEdge[EdgeArgs.id])

    def updateEdgesOfNode(self, graphicsNode):
        '''Update each coordinates of each edges of the current node.
        
        Argument(s):
        graphicsNode (GraphicsNode): Current graphics node
        '''
        for edge in self.edges.values():
            # Check if the edge contains the current node
            if edge.source == graphicsNode or edge.dest == graphicsNode:
                edge.update()   

    def getText(self, dotAttrs, id):
        '''Return the label if it is defined and not void, else the id.'''
        if NodeDotAttrs.label.value in dotAttrs:
            return dotAttrs[NodeDotAttrs.label.value]
        
        return id

    def resetSceneRect(self):
        '''Reset the scene rect with the viewport.'''
        self.scene.setSceneRect(QRectF(self.viewport().rect()));

    def eventFilter(self, source, event):
        '''Handle events for the scene.'''
        if source == self.scene:
            # Left double click (mouse button)
            if (event.type() == QEvent.GraphicsSceneMouseDoubleClick and
                event.buttons() == Qt.LeftButton):
                
                # Create a node if there is not an item where we double click
                if not source.itemAt(event.scenePos(), QTransform()):
                    pos = event.scenePos()
                    self.controller.onCreateNode(pos.x(), pos.y())
                    
                    return True
            
            # Key press
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Delete:
                    # Only one item might be selected at this state
                    item = source.selectedItems()
                    
                    # If a item is selected
                    if item:
                        # Remove node
                        if isinstance(item[0], GraphicsNode):
                            self.controller.onRemoveNode(item[0].id)
                            
                        # Remove edge
                        elif isinstance(item[0], GraphicsEdge):
                            self.controller.onRemoveEdge(item[0].id)
                            
            if (event.type() == QEvent.GraphicsSceneMousePress and
                event.buttons() == Qt.LeftButton):
                # Disable multiple selection
                if (event.modifiers() == Qt.ControlModifier):
                    for it in source.selectedItems():
                        it.setSelected(False)
                else:
                    item = source.itemAt(event.scenePos(), QTransform())
                    if item:
                        for it in source.selectedItems():
                            it.setSelected(False)
                        item.setSelected(True)
                                     
        return False
