# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from doted.view.node.GraphicsEllipseNode import GraphicsEllipseNode
from doted.view.widget.View import View


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
        self.show()

    def update(self):
        '''Update the scene.'''
        nodeId = "ID"
        if nodeId not in self.nodes:
            self.nodes[nodeId] = GraphicsEllipseNode(nodeId, "A", 0.0, 0.0, 100, 100)
            self.scene.addItem(self.nodes[nodeId])
