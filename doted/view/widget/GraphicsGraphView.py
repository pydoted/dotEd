# -*- coding: utf-8 -*-

from PyQt5.Qt import QEvent, Qt, QRectF
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from view.node.GraphicsEllipseNode import GraphicsEllipseNode
from view.widget.View import View


class GraphicsGraphView(View, QGraphicsView):
    '''Graphical representation of a Graph.
    
    
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
        nodeId = dictArgsNode["id"]
        self.nodes[nodeId] = GraphicsEllipseNode(nodeId,
                                                     dictArgsNode["label"])
        self.nodes[nodeId].setX(dictArgsNode["x"])
        self.nodes[nodeId].setY(dictArgsNode["y"])
        self.scene.addItem(self.nodes[nodeId])
            
    def updateEdge(self, dictArgsEdge):
        '''Create or update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): dictionary of arguments of the edge
        '''
        pass
    
    def onCreateNode(self, x, y):
        '''Callback funtion when creating a node.'''
        self.controller.onCreateNode(x, y)
        
    def onCreateEdge(self):
        '''Callback funtion when creating an edge.'''
        self.controller.onCreateEdge()

    def eventFilter(self, source, event):
        '''Handle events for the scene.'''
        # When left-doubleclicking on the scene, it creates a node 
        if (source == self.scene and
            event.type() == QEvent.GraphicsSceneMouseDoubleClick and
            event.button() == Qt.LeftButton):
            pos = event.scenePos()
            self.onCreateNode(pos.x(), pos.y())
            
            return True
        
        return False
