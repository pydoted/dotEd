# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit

from enumeration.NodeArgs import NodeArgs
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

    def addNode(self, dictArgsNode):
        '''Add a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes[dictArgsNode[NodeArgs.id]] = dictArgsNode[NodeArgs.label]
        self.updateStrNodes()

    def editNode(self, dictArgsNode):
        '''Edit a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes[dictArgsNode[NodeArgs.id]] = dictArgsNode[NodeArgs.label]
        self.updateStrNodes()

    def removeNode(self, dictArgsNode):
        '''Remove a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes.pop(dictArgsNode[NodeArgs.id])
        self.updateStrNodes()

    def addEdge(self, dictArgsEdge):
        '''Add an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        
        self.edges[dictArgsEdge[EdgeArgs.id]] = (
                            dictArgsEdge[EdgeArgs.sourceId],
                            dictArgsEdge[EdgeArgs.destId])
        self.updateStrEdges()
    
    def editEdge(self, dictArgsEdge):
        '''Edit an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        self.updateStrEdges()
    
    def removeEdge(self, dictArgsEdge):
        '''Remove an edge.
        
        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        self.edges.pop(dictArgsEdge[EdgeArgs.id])
        self.updateStrEdges()
    
    def updateStrNodes(self):
        '''Update the dot string representation of the nodes.'''
        # Generate string nodes
        self.strNodes = ""
        for idNode, labelNode in self.nodes.items():
            self.strNodes += "    " + str(idNode)
            if labelNode:
                self.strNodes += (" [label=\"" + labelNode.replace('\n', '') +
                                  "\"]")
            
            self.strNodes += ";\n"
        
        self.setPlainText(self.strDot())
    
    def updateStrEdges(self):
        '''Update the dot string representation of the edges.'''
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
