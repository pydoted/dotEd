# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit

from pydot_ng import graph_from_dot_data

from enumeration.EdgeArgs import EdgeArgs
from enumeration.NodeArgs import NodeArgs
from enumeration.NodeDotAttrs import NodeDotAttrs
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
        self.oldPydotGraph = graph_from_dot_data(self.toPlainText())

    def addNode(self, dictArgsNode):
        '''Add a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes[dictArgsNode[NodeArgs.id]] = (dictArgsNode[NodeArgs.dotAttrs]
                                                 [NodeDotAttrs.label.value])
        self.updateStrNodes()

    def editNode(self, dictArgsNode):
        '''Edit a node.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes[dictArgsNode[NodeArgs.id]] = (dictArgsNode[NodeArgs.dotAttrs]
                                                 [NodeDotAttrs.label.value])
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
                self.strNodes += (" [label=" + labelNode.replace('\n', '') +
                                  "]")
            
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
    
    def focusOutEvent(self, event):
        '''Handle focus out event.
        
        Attribute(s):
        event (QFocusEvent): Focus event
        '''
        # Create pydot graph    
        self.pydotGraph = graph_from_dot_data(self.toPlainText())
        
        # If the pydot graph is valid
        if self.pydotGraph:
            pydotNodes = self.pydotGraph.get_nodes()
            pydotEdges = self.pydotGraph.get_edges()
 
            # -- Remove nodes --
            # We get all the ID of the nodes from the pydot graph
            pydotNodesId = []
            for pydotNode in pydotNodes:
                pydotNodesId.append(pydotNode.get_name())
            
            # If our current nodes are not in the new pydot graph,
            # we must remove them
            for nodeId in list(self.nodes.keys()):
                if not nodeId in pydotNodesId:
                    self.controller.onRemoveNode(nodeId)
 
            # -- Add nodes --
            for pydotNode in pydotNodes:
                self.controller.onCreateNode(pydotNode.get_name(),
                                             pydotNode.get_attributes(),
                                             0, 0)
            
            # -- Edit nodes -- (a real diff should be done there)
            for pydotNode in pydotNodes:
                self.controller.onEditNode(pydotNode.get_name(),
                                           pydotNode.get_attributes())
            
            # -- Remove edges --
            for edge in list(self.edges.values()):
                needToRemoveEdge = True
                # If there are pydot edges in the pydot graph
                if pydotEdges:
                    # We must remove the edge if we don't find it in the
                    # pydot graph
                    for pydotEdge in pydotEdges:
                        if ((edge[0] == pydotEdge.get_source() and
                             edge[1] == pydotEdge.get_destination()) or
                            (edge[1] == pydotEdge.get_source() and
                             edge[0] == pydotEdge.get_destination())):
                            needToRemoveEdge = False
                            break
                    
                    if needToRemoveEdge:
                        self.controller.onRemoveEdge(edge[0], edge[1])
                else:
                    self.controller.onRemoveEdge(edge[0], edge[1])
                
            # -- Add edges --
            for pydotEdge in pydotEdges:
                self.controller.onCreateEdge(pydotEdge.get_source(),
                                             pydotEdge.get_destination())
                
            QTextEdit.focusOutEvent(self, event)
        
        # Pydot graph invalid = block other views ?
        else:
            print("Syntax error.")
