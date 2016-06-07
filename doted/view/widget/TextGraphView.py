# -*- coding: utf-8 -*-

# Copyright (c) 2016 Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem
# This file is part of dotEd.
#
# dotEd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dotEd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dotEd.  If not, see <http://www.gnu.org/licenses/>.

import re

from pydot_ng import graph_from_dot_data

from PyQt5.Qt import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit

from doted.enumeration.EdgeArgs import EdgeArgs
from doted.enumeration.NodeArgs import NodeArgs
from doted.utils.DotAttrsUtils import DotAttrsUtils
from doted.utils.EdgeUtils import EdgeUtils
from doted.view.widget.View import View


class TextGraphView(View, QTextEdit):
    '''The TextGraphView class defines a text (dot file) representation of a
    Graph.

    Attribute(s):
    nodes (Dictionary[Dictionary[]): Dict of Dict of attributes of nodes
    edges (Dictionary[Dictionary[]): Dict of Dict of attributes of edges
    graphName (str): Name of the graph
    acceptUpdate (bool): To avoid update during import
    checker (DotAttrsUtils): To check attributes of nodes and edges
    '''

    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTextEdit.__init__(self)

        self.nodes = dict()
        self.edges = dict()
        
        self.acceptUpdate = True

        self.textCursor().insertText("graph " + self.graphName + " {\n}")
        self.checker = DotAttrsUtils()

    def wheelEvent(self, event):
        '''Handle wheel event.

        Argument(s):
        event (QWheelEvent): Wheel event
        '''
        # Only zoom/dezoom if CTRL is pressed
        if event.modifiers() == Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                self.zoomIn()
            else:
                self.zoomOut()
        # Move scrollbar
        else:
            QTextEdit.wheelEvent(self, event)

    def getText(self):
        '''Return the text of the view'''
        return self.toPlainText()

    def addNode(self, node):
        '''Add a node created in graphic view.

        Argument(s):
        node (pygraphviz.Node)
        '''
        if self.acceptUpdate:
            # Write new node at the top just after graph's {
            strNode = self.strNode(node)
            self.nodes[node]=(len(text.pop(0) + "{\n"), len(strNode))
            
            text = [e for e in self.toPlainText().split('{', 2) if e != ""]
            self.setPlainText(text.pop(0) + "{\n" +
                              strNode +
                              ''.join(text) + "\n")

    def editNode(self, node):
        '''Edit a node changed in graphic view.

        Argument(s):
        node (pygraphviz.Node)
        '''
        if self.acceptUpdate:
            attrs = node.attr.keys()
            comma = ""
            # If node already have others attributes: mark comma to write
            if len(attrs) > 1:
                comma = ", "

            for attr in attrs:
                # Find node position in text
                infoPos = self.findPosItem(node)
                cursor = self.textCursor()
                cursor.setPosition(infoPos[0], QTextCursor.MoveAnchor)
                cursor.setPosition(infoPos[1], QTextCursor.KeepAnchor)
                decNode = cursor.selectedText()

                # Find start position of attribute value
                m = re.search("[ ,\[]" + attr + "\s*=\s*", decNode)
                if m:
                    indAttr = m.end()

                # If attribute already exist: replace value
                if m:
                    cursor.setPosition(infoPos[0] + indAttr,
                                       QTextCursor.MoveAnchor)

                    # Find end position of attribute value and delete her
                    # attrs = self.nodes[dictArgsNode[NodeArgs.id]]
                    cursor.setPosition(cursor.position() + len(attrs[attr]),
                                       QTextCursor.KeepAnchor)
                    cursor.removeSelectedText()

                    # Write new attribute's value
                    cursor.insertText(node.attr[attr])

                # If attribute not already exist: write all the attr
                # decalration
                else:
                    ind = decNode.find("[")
                    # If node already have parentheses
                    if ind != -1:
                        cursor.setPosition(infoPos[0] + ind + 1,
                                           QTextCursor.MoveAnchor)
                        cursor.insertText(
                            attr +
                            "=" +
                            node.attr[attr] +
                            comma
                        )
                    else:
                        cursor.setPosition(infoPos[1] - 1,
                                           QTextCursor.MoveAnchor)
                        cursor.insertText(
                            " [" +
                            attr +
                            "=" +
                            node.attr[attr] +
                            "]"
                        )

    def removeNode(self, node):
        '''Remove a node deleted in graphic view.

        Argument(s):
        node (pygraphviz.Node)
        '''
        if self.acceptUpdate:
            # Find node position in text
            infoPos = self.findPosItem(node)
            cursor = self.textCursor()
            cursor.setPosition(infoPos[0], QTextCursor.MoveAnchor)
            cursor.setPosition(infoPos[1], QTextCursor.KeepAnchor)
            cursor.removeSelectedText()

    def addEdge(self, sourceNode, destNode):
        '''Add an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        # If is an update from graphics view
        if self.acceptUpdate:
            # Write new edge at the top just after graph's {
            text = [e for e in self.toPlainText().split('{', 2) if e != ""]
            self.setPlainText(text.pop(0) + "{\n" +
                              self.strEdge(sourceNode, destNode) +
                              ''.join(text) + "\n")

        # If is an update from textual view
        else:
            # Add node source and dest if they don't exist
            self.acceptUpdate = True
            if not self.model.nodeExists(sourceNode):
                self.controller.addNode(sourceNode)
            if not self.model.nodeExists(destNode):
                self.controller.addNode(destNode)
            self.acceptUpdate = False

    def removeEdge(self, sourceNode, destNode):
        '''Remove an edge deleted in graphic view.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        if self.acceptUpdate:
            # Find node position in text
            infoPos = self.findPosItem(self.strEdge(sourceNode, destNode))
            cursor = self.textCursor()
            cursor.setPosition(infoPos[0], QTextCursor.MoveAnchor)
            cursor.setPosition(infoPos[1], QTextCursor.KeepAnchor)
            cursor.removeSelectedText()

    def strNode(self, node):
        '''Build the dot string representation of a node.

        Argument(s):
        id (str): ID of the node that we want to write
        '''
        # Write id of the node
        strNode = "    " + node

        # If node has attributes we write their
        argsN = node.attr.keys()
        nbAttrs = 0
        if len(argsN) > 0:
            strNode += " ["

        for attr in argsN:
            nbAttrs += 1
            attrVal = node.attr[attr]
            if nbAttrs > 1:
                strNode += ", " + attr + "=" + attrVal.replace("\n", "")
            else:
                strNode += attr + "=" + attrVal.replace("\n", "")

        if len(argsN) > 0:
            strNode += " ]"

        # Write end statement
        strNode += ";"

        return strNode

    def strEdge(self, sourceNode, destNode):
        '''Build the dot string representation of an edge.

        Argument(s):
        id (str): ID of the edge that we want to write
        '''
        strEdge = ""
        strEdge += "    " + sourceNode + "--" + destNode
        strEdge += ";"

        return strEdge

    def findPosItem(self, id):
        '''return index of start and end of the item's declaration

        Argument(s):
        id (str): ID of the item we want to find
        '''

        # index = 0

        # text = self.toPlainText()
        # text = [e + '{' for e in text.split('{') if e != ""]
        # index += len(text[0]) + 1
        # text.pop(0)
        # text = ''.join(text)
        # text = [e + '}' for e in text.split('}') if e != ""]
        # text.pop(len(text) - 1)
        # stats = re.split(';', ''.join(text))

        # # Use pydot to get all statements of the graph (in order)
        # for s in stats:
        #     # Parse current statement
        #     pydotG = graph_from_dot_data("graph {" + s + "}")
        #     if pydotG:
        #         # Ignore subgraph
        #         s2 = s
        #         while (re.match("\s*(subgraph)*\s*.*\{", s2) or
        #                re.match("\s*\}.*", s2)):
        #             if re.match("\s*(subgraph)*\s*.*\{", s2):
        #                 s2 = re.split('{', s2, 1)[1]
        #                 pydotG = graph_from_dot_data("graph {" + s2 + "}")
        #             elif re.match("\s*\}.*", s2):
        #                 s2 = re.split('}', s2, 1)[1]
        #                 pydotG = graph_from_dot_data("graph {" + s2 + "}")

        #         for node in pydotG.get_nodes():
        #             if node.get_name() == id:
        #                 return([index, index + len(s)])

        #         for edge in pydotG.get_edges():
        #             if EdgeUtils.createEdgeId(edge.get_source(),
        #                                       edge.get_destination()) == id:
        #                 return([index, index + len(s)])

        #         index += len(s) + 1

    def highlightItem(self, id):
        '''Inform the view that it must highlight an Item.

        Argument(s):
        id (str): ID of the node we want to highlight
        '''
        cursor = self.textCursor()
        fmt = self.textCursor().charFormat()

        # Set BackgroundColor of all text in white
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        fmt.setBackground(QBrush(QColor(0, 0, 0, 0)))
        cursor.mergeCharFormat(fmt)

        # Highlight item
        infoPos = self.findPosItem(id)
        cursor.setPosition(infoPos[0], QTextCursor.MoveAnchor)
        cursor.setPosition(infoPos[1], QTextCursor.KeepAnchor)
        # If subgraph in statement
        if re.match("\s*(subgraph)*\s*.*\{", cursor.selectedText()):
            indItem = cursor.selectedText().find(id)
            cursor.setPosition(infoPos[0] + indItem, QTextCursor.MoveAnchor)
            cursor.setPosition(infoPos[1], QTextCursor.KeepAnchor)
        format = QTextCharFormat()
        format.setBackground(QBrush(QColor(190, 180, 0, 80)))
        cursor.mergeCharFormat(format)
        self.setCurrentCharFormat(fmt)

    def checkItemsAttributes(self, nodes, edges):
        '''Return None if attributes of all items are in valid form, else an
        error message.

        Argument(s):
        nodes (List[pydot_ng.Node]): List of pydot nodes
        edges (List[pydot_ng.Edge]): List of pydot edges
        '''
        for node in nodes:
            message = self.checker.checkNodeAttrsForm(node.get_attributes())
            if message:
                return "Node " + node.to_string() + "\n" + message

        for edge in edges:
            message = self.checker.checkEdgeAttrsForm(edge.get_attributes())
            if message:
                return "Edge " + edge.to_string() + "\n" + message

        return None

    def rebuildTextModel(self, text, pydotG):
        '''rebuild self.nodes and self.edges from text.

        Argument(s):
        text (str): Textual representation of the graph
        pydotG (PydotGraph): pydotG from text
        '''
        # Get name of the graph
        self.graphName = pydotG.get_name()

        graphs = []
        graphs.append(pydotG)
        # Get all item in graph or subgraph
        while len(graphs) > 0:
            G = graphs[0]

            for node in G.get_nodes():
                if node.get_name() not in self.nodes:
                    self.nodes[node.get_name()] = node.get_attributes()

            for edge in G.get_edges():
                idEdge = EdgeUtils.createEdgeId(edge.get_source(),
                                                edge.get_destination())
                if idEdge not in self.edges:
                    self.edges[idEdge] = {
                        EdgeArgs.sourceId: edge.get_source(),
                        EdgeArgs.destId: edge.get_destination()
                    }

            for subG in G.get_subgraphs():
                graphs.append(subG)

            graphs.pop(0)

    def importGraph(self, text):
        '''Init text after an import.

        Argument(s):
        text (str): Textual representation of the graph
        '''
        self.acceptUpdate = False
        self.setPlainText(text)

        pydotGraph = graph_from_dot_data(text)

        # Check that attributes are in valid form
        message = self.checkItemsAttributes(pydotGraph.get_nodes(),
                                            pydotGraph.get_edges())
        if not message:
            self.rebuildTextModel(text, pydotGraph)

            # Send every elements to the model to build him
            for id, args in self.nodes.items():
                self.controller.onCreateNode(id, args)
            for id, args in self.edges.items():
                self.controller.onCreateEdge(args[EdgeArgs.sourceId],
                                             args[EdgeArgs.destId])

        # Some attributes are in invalid form
        else:
            QMessageBox.warning(self, "Syntax error", message)

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
            # If attributes are in valid form
            message = self.checkItemsAttributes(pydotGraph.get_nodes(),
                                                pydotGraph.get_edges())
            if not message:
                oldNodes = self.nodes
                oldEdges = self.edges
                self.nodes = {}
                self.edges = {}
                self.rebuildTextModel(self.toPlainText(), pydotGraph)

                # Compare old and new text and send changes to the model
                # Add nodes added
                added = self.nodes.keys() - oldNodes.keys()
                for idNode in added:
                    self.controller.onCreateNode(idNode, self.nodes[idNode])

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
                            edgeToRemove.append(edge)
                    self.acceptUpdate = True
                    for edge in edgeToRemove:
                        self.removeEdge({
                            EdgeArgs.id: edge,
                            EdgeArgs.sourceId:
                            self.edges[edge][EdgeArgs.sourceId],
                            EdgeArgs.destId:
                            self.edges[edge][EdgeArgs.destId]
                        })
                    self.acceptUpdate = False

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

                QTextEdit.focusOutEvent(self, event)

            # Some attributes are in invalid form: show an error window
            else:
                QMessageBox.warning(self, "Syntax error", message)
                self.setFocus()

        # Pydot graph invalid: show an error window
        else:
            QMessageBox.warning(self, "Syntax error",
                                "The dot structure is invalid.")
            self.setFocus()

        self.acceptUpdate = True
