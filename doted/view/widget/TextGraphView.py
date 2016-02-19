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
        dictArgsNode (dict): dictionary of arguments of the node
        '''
        nodeId = dictArgsNode["id"]
        if self.nodes[nodeId] is None:
            self.nodes[nodeId] = dictArgsNode["label"]
            self.setPlainText(self.nodes[nodeId])
        
        #for all node in nodes....,
