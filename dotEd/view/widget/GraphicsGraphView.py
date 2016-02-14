# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from view.node.GraphicsEllipseNode import GraphicsEllipseNode
from view.widget.View import View


class GraphicsGraphView(View, QGraphicsView):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        View.__init__(self)
        QGraphicsView.__init__(self)

        self.nodes = {}
        self.edges = {}
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.show()

    def update(self):
        nodeId = "ID"
        if nodeId not in self.nodes:
            self.nodes[nodeId] = GraphicsEllipseNode(nodeId, "A", 0.0, 0.0, 100, 100)
            self.scene.addItem(self.nodes[nodeId])
