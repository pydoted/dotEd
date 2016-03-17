# -*- coding: utf-8 -*-

from PyQt5.Qt import QEvent, Qt, QRectF, QTransform
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from enumeration.EdgeArgs import EdgeArgs
from enumeration.NodeArgs import NodeArgs
from enumeration.UpdateModeView import UpdateModeView
from view.edge.GraphicsLineEdge import GraphicsLineEdge
from view.node.GraphicsEllipseNode import GraphicsEllipseNode
from view.widget.View import View
from view.node.GraphicsNode import GraphicsNode
from view.edge.GraphicsEdge import GraphicsEdge


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
        self.scene.setSceneRect(QRectF(self.viewport().rect()));
        self.scene.installEventFilter(self)
        
        self.show()

    def updateNode(self, dictArgsNode, updateModeView):
        '''Update a node (on the scene).
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        updateModeView (UpdateModeView) : Update mode
        '''
        id = dictArgsNode[NodeArgs.id]
       
        # Add node
        if updateModeView == UpdateModeView.add:
            self.nodes[id] = GraphicsEllipseNode(id,
                                                 dictArgsNode[NodeArgs.label])
            self.nodes[id].setX(dictArgsNode[NodeArgs.x])
            self.nodes[id].setY(dictArgsNode[NodeArgs.y])  
        
            self.scene.addItem(self.nodes[id])
        
        # Edit node
        elif updateModeView == UpdateModeView.edit:
            self.nodes[id].graphicsTextNode.setPlainText(
                                            dictArgsNode[NodeArgs.label])
        
        # Remove node
        elif updateModeView == UpdateModeView.remove:
            self.scene.removeItem(self.nodes[id])
            self.nodes.pop(id)
            
    def updateEdge(self, dictArgsEdge, updateModeView):
        '''Update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView) : Update mode
        '''
        id = dictArgsEdge[EdgeArgs.id]
        
        # Add edge
        if updateModeView == UpdateModeView.add:
            # Init source and dest nodes
            source = self.nodes[dictArgsEdge[EdgeArgs.sourceId]]
            dest = self.nodes[dictArgsEdge[EdgeArgs.destId]]
            
            self.edges[id] = GraphicsLineEdge(source, dest, id)
            self.scene.addItem(self.edges[id])
        
        # Edit edge
        elif updateModeView == UpdateModeView.edit:
            pass
        
        # Remove edge
        elif updateModeView == UpdateModeView.remove:
            self.scene.removeItem(self.edges[id])
            self.edges.pop(id)

    def updateEdgesOfNode(self, graphicsNode):
        '''Update each coordinates of each edges of the current node.
        
        Argument(s):
        graphicsNode (GraphicsNode): Current graphics node
        '''
        for edge in self.edges.values():
            # Check if the edge contains the current node
            if edge.source == graphicsNode or edge.dest == graphicsNode:
                edge.update()   

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
