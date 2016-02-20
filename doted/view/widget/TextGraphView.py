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

    def updateNode(self, dictArgsNode):
        '''Create or update a node (in the text).
        
        
        Argument(s):
        dictArgsNode (Dictionary[]): dictionary of arguments of the node
        '''
        nodeId = dictArgsNode["id"]
        self.nodes[nodeId] = dictArgsNode["label"]
        
        # The way of displaying will change
        stringNodes = ""
        for id, label in self.nodes.items():
            stringNodes += str(id) + " [label=\"" + label + "\"] ;\n"
        self.setPlainText(stringNodes)

    def updateEdge(self, dictArgsEdge):
        '''Create or update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): dictionary of arguments of the edge
        '''
        pass
