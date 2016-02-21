# -*- coding: utf-8 -*-

from PyQt5.Qt import QEvent, Qt, QRectF
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from view.edge.GraphicsLineEdge import GraphicsLineEdge
from view.node.GraphicsEllipseNode import GraphicsEllipseNode
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
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setSceneRect(QRectF(self.viewport().rect()));
        self.scene.installEventFilter(self)
        
        self.show()

    def updateNode(self, dictArgsNode):
        '''Create or update a node (on the scene).
        
        Argument(s):
        dictArgsNode (Dictionary[]): dictionary of arguments of the node
        '''
        id = dictArgsNode["id"]
        
        self.nodes[id] = GraphicsEllipseNode(id, dictArgsNode["label"])
        self.nodes[id].setX(dictArgsNode["x"])
        self.nodes[id].setY(dictArgsNode["y"])
        
        self.scene.addItem(self.nodes[id])
            
    def updateEdge(self, dictArgsEdge):
        '''Create or update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): dictionary of arguments of the edge
        '''
        id = dictArgsEdge["id"]
        source = self.nodes[dictArgsEdge["source"].id]
        dest = self.nodes[dictArgsEdge["dest"].id]
        
        self.edges[id] = GraphicsLineEdge(source, dest)
        
        self.scene.addItem(self.edges[id])

    def eventFilter(self, source, event):
        '''Handle events for the scene.'''
        if source == self.scene:
            # Create a node
            if (event.type() == QEvent.GraphicsSceneMouseDoubleClick and
                event.buttons() == Qt.LeftButton):
                pos = event.scenePos()
                self.controller.onCreateNode(pos.x(), pos.y())
                
                return True
            
        return False
