# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit

from view.widget.View import View


class TextGraphView(View, QTextEdit):
    '''Text (dot file) representation of a Graph.
    
    
    Attribute(s):
    nodes (Dictionary[GraphicNode]): All nodes (views)
    edges (Dictionary[GraphicEdge]): All edges (views)
    '''


    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTextEdit.__init__(self)
                
        self.nodes = {}
        self.edges = {}

    def update(self):
        '''Update the text.'''
        nodeId = "ID"
        if nodeId not in self.nodes:
            self.nodes[nodeId] = "A"
            self.setPlainText(self.nodes[nodeId])
        
        #for all node in nodes....,
