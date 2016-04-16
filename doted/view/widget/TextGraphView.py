# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit

from enumeration.NodeArgs import NodeArgs
from enumeration.UpdateModeView import UpdateModeView
from enumeration.EdgeArgs import EdgeArgs
from view.widget.View import View


class TextGraphView(View, QTextEdit):
    '''The TextGraphView class defines a text (dot file) representation of a
       Graph.
    
    
    Attribute(s):
    nodes (Dictionary[GraphicNode]): All nodes (views)
    edges (Dictionary[GraphicEdge]): All edges (views)
    strNodes (str): Text for nodes
    textEdges (str): Text for edges
    graphName (str): Name of the graph
    '''


    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTextEdit.__init__(self)
                
        self.nodes = {}
        self.edges = {}
        
        self.strNodes = ""
        self.strEdges = ""
        self.graphName = "my_graph"
        
        self.setPlainText(self.strDot())

    def updateNode(self, dictArgsNode, updateModeView):
        '''Create or update a node (in the text).
        
        
        Argument(s):
        dictArgsNode (Dictionary[]): dictionary of arguments of the node
        updateModeView (UpdateModeView) : Update mode
        '''
        nodeId = dictArgsNode[NodeArgs.id]
        
        # Add node
        if updateModeView == UpdateModeView.add:
            self.nodes[id] = dictArgsNode[NodeArgs.label]
        
        # Edit node
        elif updateModeView == UpdateModeView.edit:
            self.nodes[id] = dictArgsNode[NodeArgs.label]
        
        # Remove node
        elif updateModeView == UpdateModeView.remove:
            self.nodes.pop(id)
        
        # Generate string nodes
        self.strNodes = ""
        for idNode, labelNode in self.nodes.items():
            self.strNodes += "    " + str(idNode)
            if labelNode:
                self.strNodes += (" [label=\"" + labelNode.replace('\n', '') +
                                  "\"]")
            
            self.strNodes += ";\n"
            
        
        self.setPlainText(self.strDot())

    def updateEdge(self, dictArgsEdge, updateModeView):
        '''Create or update an edge (on the scene).
        
        Argument(s):
        dictArgsEdge (Dictionary[]): dictionary of arguments of the edge
        updateModeView (UpdateModeView) : Update mode
        '''
        id = dictArgsEdge[EdgeArgs.id]
        
        # Add edge
        if updateModeView == UpdateModeView.add:
            self.edges[id] = (dictArgsEdge[EdgeArgs.sourceId],
                              dictArgsEdge[EdgeArgs.destId])
        
        # Edit edge
        elif updateModeView == UpdateModeView.edit:
            pass
        
        # Remove edge
        elif updateModeView == UpdateModeView.remove:
            self.edges.pop(id)
        
        # Generate string edges
        self.strEdges = ""
        for tupleIdNodes in self.edges.values():
            self.strEdges += ("    " + str(tupleIdNodes[0]) + "--" +
                              str(tupleIdNodes[1]) + ";\n")
        
        self.setPlainText(self.strDot())
    
    def strDot(self):
        '''Return the dot string representation of the graph.'''
        return ("graph " + self.graphName + " {\n" +
                self.strNodes + self.strEdges +
                "}")
