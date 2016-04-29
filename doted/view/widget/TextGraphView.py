# -*- coding: utf-8 -*-

import re

from pydot_ng import graph_from_dot_data

from PyQt5.Qt import QMessageBox
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5.QtWidgets import QTextEdit

from enumeration.EdgeArgs import EdgeArgs
from enumeration.NodeArgs import NodeArgs
from utils.EdgeUtils import EdgeUtils
from utils.DotAttrsUtils import DotAttrsUtils
from view.widget.View import View


class TextGraphView(View, QTextEdit):
    '''The TextGraphView class defines a text (dot file) representation of a
    Graph.

    Attribute(s):
    nodes (Dictionary[Dictionary[]): Dict of Dict of attributes of nodes
    edges (Dictionary[Dictionary[]): Dict of Dict of attributes of edges
    order (List[]): List of nodes and edges IDs in order in which they should
                    be written
    graphName (str): Name of the graph
    acceptUpdate (bool): To avoid update during import
    '''


    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTextEdit.__init__(self)

        self.acceptUpdate = True
        self.nodes = {}
        self.edges = {}
        self.order = []
        self.graphName = "my_graph"

        self.strDot()
        
    def getText(self):
        '''Return the text of the view'''
        return self.toPlainText()

    def addNode(self, dictArgsNode):
        '''Add a node created in graphic view.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        if self.acceptUpdate:
            self.order.insert(0, dictArgsNode[NodeArgs.id])
            self.nodes[dictArgsNode[NodeArgs.id]] = \
                                                dictArgsNode[NodeArgs.dotAttrs]
            self.strDot()

    def editNode(self, dictArgsNode):
        '''Edit a node changed in graphic view.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        if self.acceptUpdate:
            self.nodes[dictArgsNode[NodeArgs.id]] = \
                                                dictArgsNode[NodeArgs.dotAttrs]
            self.strDot()

    def removeNode(self, dictArgsNode):
        '''Remove a node deleted in graphic view.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        if self.acceptUpdate:
            self.order.remove(dictArgsNode[NodeArgs.id])
            self.nodes.pop(dictArgsNode[NodeArgs.id])
            self.strDot()

    def addEdge(self, dictArgsEdge):
        '''Add an edge created in graphic view.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        if self.acceptUpdate:
            self.order.insert(0, dictArgsEdge[EdgeArgs.id])
            self.edges[dictArgsEdge[EdgeArgs.id]] = {
                           EdgeArgs.sourceId: dictArgsEdge[EdgeArgs.sourceId],
                           EdgeArgs.destId: dictArgsEdge[EdgeArgs.destId]
                        }
            self.strDot(dictArgsEdge[EdgeArgs.sourceId])

    def removeEdge(self, dictArgsEdge):
        '''Remove an edge deleted in graphic view.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        if self.acceptUpdate:
            self.order.remove(dictArgsEdge[EdgeArgs.id])
            self.edges.pop(dictArgsEdge[EdgeArgs.id])
            self.strDot()

    def strNode(self, id):
        '''Build the dot string representation of a node.

        Argument(s):
        id (str): ID of the node that we want to write
        '''
        # Write id of the node
        strNode = "    " + id

        # If node has attributes we write their
        argsN = self.nodes[id]
        nbAttrs = 0
        if len(argsN) > 0:
            strNode += " ["
             
        for attr in argsN:
            nbAttrs += 1
            attrVal = argsN[attr]
            if nbAttrs > 1:
                strNode += ", " + attr + "=" + attrVal.replace("\n", "")
            else:
                strNode += attr + "=" + attrVal.replace("\n", "")
            
        if len(argsN) > 0:
            strNode += " ]"
             
        # Write end statement
        strNode += ";\n"
        
        return strNode

    def strEdge(self, id):
        '''Build the dot string representation of an edge.

        Argument(s):
        id (str): ID of the edge that we want to write
        '''
        e = self.edges[id]
        strEdge = ""
        strEdge += "    " + e[EdgeArgs.sourceId] + "--" + e[EdgeArgs.destId]
        strEdge += ";\n"
        
        return strEdge

    def strDot(self, itemIdToHighlight=None):
        '''Return the dot string representation of the graph.

        Argument(s):
        itemIdToHighlight (str): ID of the Item that we want to highlight
                           (default None)
        '''
        self.setCurrentCharFormat(QTextCharFormat())
        self.setPlainText("")
        self.textCursor().insertText("graph " + self.graphName + " {\n")

        for id in self.order:
            if id == '\n':
                self.textCursor().insertText('\n')
            elif id in self.nodes:
                if id == itemIdToHighlight:
                    fmt = self.textCursor().charFormat()
                    format = QTextCharFormat()
                    format.setBackground(QBrush(QColor(190, 180, 0, 110)))
                    self.textCursor().insertText(self.strNode(id), format)
                    self.setCurrentCharFormat(fmt)
                else:
                    self.textCursor().insertText(self.strNode(id))
            else:
                if id == itemIdToHighlight:
                    fmt = self.textCursor().charFormat()
                    format = QTextCharFormat()
                    format.setBackground(QBrush(QColor(190, 180, 0, 110)))
                    self.textCursor().insertText(self.strEdge(id), format)
                    self.setCurrentCharFormat(fmt)
                else:
                    self.textCursor().insertText(self.strEdge(id))

        self.textCursor().insertText("}")

    def highlightItem(self, id):
        '''Inform the view that it must highlight an Item.

        Argument(s):
        id (str): ID of the node we want to highlight
        '''
        self.strDot(id)
        
    def checkItemsAttributes(self, items):
        '''Return true if attributes of all items are in valid form.
        
        Argument(s):
        item (List[]): List of pydot items
        '''
        for item in items:
            if not DotAttrsUtils.checkAttrsForm(item.get_attributes()):
                return False
        return True
    
    def rebuildTextModel(self, text, pydotGraph):
        '''rebuild self.nodes self.edges and self.order from text.
        
        Argument(s):
        text (str): Textual representation of the graph
        pydotGraph (PydotGraph): pydotGraph from text
        '''
        # Get name of the graph
        self.graphName = pydotGraph.get_name()
        
        text = [e+'{' for e in text.split('{') if e != ""]
        text.pop(0)
        text = ''.join(text)
        text = [e+'}' for e in text.split('}') if e != ""]
        text.pop(len(text)-1)
        stats = re.split(';', ''.join(text))
        
        # Use pydot to get all statements of the graph (in order)
        for s in stats:
            # Parse current statement
            pydotG = graph_from_dot_data("graph {" + s + "}")

            # Ignore subgraph
            if re.match("\s*(subgraph)*\s*.*\{", s):
                s = re.split('{', s)[1]
                pydotG = graph_from_dot_data("graph {" + s + "}")
            elif re.match("\s*\}.*", s):
                s = re.split('}', s)[1]
                pydotG = graph_from_dot_data("graph {" + s + "}")       
            
            # Get current statement type and attributes
            for node in pydotG.get_nodes():
                if node.get_name() not in self.order:
                    self.order.append(node.get_name())
                    self.nodes[node.get_name()] = node.get_attributes()
            
            for edge in pydotG.get_edges():
                
                idEdge = EdgeUtils.createEdgeId(edge.get_source(),
                                                edge.get_destination())
                if idEdge not in self.order:
                    self.order.append(idEdge)
                    self.edges[idEdge] = {
                                   EdgeArgs.sourceId: edge.get_source(),
                                   EdgeArgs.destId: edge.get_destination()
                                }
                    
                    # Add node source if it doesn't exist
                    nodesInGraph = [node.get_name()
                                        for node in pydotGraph.get_nodes()]
                    if (not(edge.get_source() in nodesInGraph) and 
                        not(edge.get_source() in self.order)):
                        self.order.append(edge.get_source())
                        self.nodes[edge.get_source()] = {}
                        
                    # Add node dest if it doesn't exist
                    if (not(edge.get_destination() in nodesInGraph) and 
                        not(edge.get_destination() in self.order)):
                        self.order.append(edge.get_destination())
                        self.nodes[edge.get_destination()] = {}
                        
    def importGraph(self, text):
        '''Init text after an import.

        Argument(s):
        text (str): Textual representation of the graph
        '''
        self.acceptUpdate = False
        
        pydotGraph = graph_from_dot_data(text)
        
        # Check that attributes are in valid form
        if (self.checkItemsAttributes(pydotGraph.get_nodes()) and
                            self.checkItemsAttributes(pydotGraph.get_edges())):
            self.rebuildTextModel(text, pydotGraph)
        
            # Send every elements to the model to build him
            for id, args in self.nodes.items():
                self.controller.onCreateNode(id, args)
            for id, args in self.edges.items():
                self.controller.onCreateEdge(args[EdgeArgs.sourceId],
                                             args[EdgeArgs.destId])
        # Some attributes are in invalid form
        else :
            QMessageBox.warning(self, "Syntax error",
                            "Some attributes in invalid form")

        self.strDot()
        self.acceptUpdate = True

    def focusOutEvent(self, event):
        '''Handle focus out event.

        Argument(s):
        event (QFocusEvent): Focus event
        '''
        self.acceptUpdate = False
        
        # Create pydot graph from text
        pydotGraph = graph_from_dot_data(self.toPlainText())

        # If the pydot graph is valid we can rewrite the text and check changes
        if pydotGraph:
            # Check that attributes are in valid form
            if (self.checkItemsAttributes(pydotGraph.get_nodes()) and
                            self.checkItemsAttributes(pydotGraph.get_edges())):
            
                oldNodes = self.nodes
                oldEdges = self.edges
                self.nodes = {}
                self.edges = {}
                self.order = []
                self.rebuildTextModel(self.toPlainText(), pydotGraph)        
                    
                # Compare old and new text and send changes to the model
                # Add nodes added
                added = self.nodes.keys() - oldNodes.keys()
                for idNode in added:
                    self.controller.onCreateNode(idNode, self.nodes[idNode], 0, 0)
                    
                # Edit nodes changed
                intersect = set(self.nodes.keys()).intersection(
                                                            set(oldNodes.keys()))  
                for idNode in intersect:  
                    if self.nodes[idNode] != oldNodes[idNode]:
                        self.controller.onEditNode(idNode, self.nodes[idNode])  
    
                # Remove nodes deleted
                removed = oldNodes.keys() - self.nodes.keys() 
                for idNode in removed:
                    self.controller.onRemoveNode(idNode)  
                     
                    # Delete edges which contain the node
                    edgeToRemove = []
                    for edge in self.edges:
                        if (idNode == self.edges[edge][EdgeArgs.sourceId] or 
                            idNode == self.edges[edge][EdgeArgs.destId]):
                            self.order.remove(edge)
                            edgeToRemove.append(edge)
                    for edge in edgeToRemove:
                        self.edges.pop(edge)
                    
                # Remove edges deleted
                removed = oldEdges.keys() - self.edges.keys() 
                for idEdge in removed:
                    self.controller.onRemoveEdge(
                                              oldEdges[idEdge][EdgeArgs.sourceId],
                                              oldEdges[idEdge][EdgeArgs.destId])
                    
                # Add edges added
                added = self.edges.keys() - oldEdges.keys()
                for idEdge in added:
                    nodeSource = self.edges[idEdge][EdgeArgs.sourceId]
                    nodeDest = self.edges[idEdge][EdgeArgs.destId]
                    self.controller.onCreateEdge(nodeSource, nodeDest)
                    if nodeSource not in self.nodes:
                        self.order.insert(0, nodeSource)
                        self.nodes[nodeSource] = {}
                    if nodeDest not in self.nodes:
                        self.order.insert(0, nodeDest)
                        self.nodes[nodeDest] = {}
            
                self.strDot()
                QTextEdit.focusOutEvent(self, event)
            
            # Some attributes are in invalid form
            else :
                QMessageBox.warning(self, "Syntax error",
                                "Some attributes in invalid form")
                self.setFocus()
                
        # Pydot graph invalid: show an error window
        else:
            QMessageBox.warning(self, "Syntax error",
                                "The dot structure is invalid.")
            self.setFocus()

        self.acceptUpdate = True
