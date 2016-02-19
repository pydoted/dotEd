# -*- coding: utf-8 -*-

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
        self.show()

    def updateNode(self, dictArgsNode):
        '''Create or update a node (on the scene).
        
        
        Argument(s):
        dictArgsNode (dict): dictionary of arguments of the node
        '''
        nodeId = dictArgsNode["id"]
        if nodeId not in self.nodes:
            self.nodes[nodeId] = GraphicsEllipseNode(nodeId,
                                                         dictArgsNode["label"])
            self.scene.addItem(self.nodes[nodeId])
            
    def updateEdge(self, dictArgsEdge):
        '''Create or update an edge (on the scene).
        
        
        Argument(s):
        dictArgsEdge (dict): dictionary of arguments of the edge
        '''
        pass