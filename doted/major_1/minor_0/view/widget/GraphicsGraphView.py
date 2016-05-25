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

from PyQt5.Qt import QEvent, Qt, QRectF, QTransform
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from major_1.minor_0.enumeration.EdgeArgs import EdgeArgs
from major_1.minor_0.enumeration.NodeArgs import NodeArgs
from major_1.minor_0.view.edge.GraphicsEdge import GraphicsEdge
from major_1.minor_0.view.edge.GraphicsLineEdge import GraphicsLineEdge
from major_1.minor_0.view.node.GraphicsEllipseNode import GraphicsEllipseNode
from major_1.minor_0.view.node.GraphicsNode import GraphicsNode
from major_1.minor_0.view.widget.View import View


class GraphicsGraphView(View, QGraphicsView):
    '''The GraphicsGraphView defines a graphical representation of a Graph.


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

        # Enable Antiliasing
        self.setRenderHint(QPainter.Antialiasing)

        # Rectangular selection
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRubberBandSelectionMode(Qt.IntersectsItemShape)

        # Init scene
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.resetSceneRect()
        self.scene.installEventFilter(self)

        self.show()

    def addNode(self, dictArgsNode):
        '''Add a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Create the node
        self.nodes[dictArgsNode[NodeArgs.id]] = GraphicsEllipseNode(
            dictArgsNode[NodeArgs.id],
            self)
        # Edit it
        self.editNode(dictArgsNode)

        # Add it to the scene
        self.scene.addItem(self.nodes[dictArgsNode[NodeArgs.id]])

    def editNode(self, dictArgsNode):
        '''Edit a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.nodes[dictArgsNode[NodeArgs.id]].edit(dictArgsNode)

    def removeNode(self, dictArgsNode):
        '''Remove a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Remove the node from the scene
        self.scene.removeItem(self.nodes[dictArgsNode[NodeArgs.id]])
        self.nodes.pop(dictArgsNode[NodeArgs.id])

        # Reset scene rect
        if not self.scene.items():
            self.resetSceneRect()

    def addEdge(self, dictArgsEdge):
        '''Add an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        # Init source and dest nodes
        source = self.nodes[dictArgsEdge[EdgeArgs.sourceId]]
        dest = self.nodes[dictArgsEdge[EdgeArgs.destId]]

        # Create the edge
        self.edges[dictArgsEdge[EdgeArgs.id]] = GraphicsLineEdge(source, dest,
                                                                 dictArgsEdge[
                                                                     EdgeArgs.id],
                                                                 self)
        # Edit it
        self.editEdge(dictArgsEdge)

        # Add edge to the scene
        self.scene.addItem(self.edges[dictArgsEdge[EdgeArgs.id]])

    def editEdge(self, dictArgsEdge):
        '''Edit an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        self.edges[dictArgsEdge[EdgeArgs.id]].edit(dictArgsEdge)

    def removeEdge(self, dictArgsEdge):
        '''Remove an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        # Remove the edge from the scene
        self.scene.removeItem(self.edges[dictArgsEdge[EdgeArgs.id]])
        self.edges.pop(dictArgsEdge[EdgeArgs.id])

    def updateEdgesOfNode(self, graphicsNode):
        '''Update each coordinates of each edges of the current node.

        Argument(s):
        graphicsNode (GraphicsNode): Current graphics node
        '''
        for edge in self.edges.values():
            # Check if the edge contains the current node
            if edge.source == graphicsNode or edge.dest == graphicsNode:
                edge.update()

    def resetSceneRect(self):
        '''Reset the scene rect with the viewport.'''
        self.scene.setSceneRect(QRectF(self.viewport().rect()))

    def eventFilter(self, source, event):
        '''Handle events for the scene.'''
        if source == self.scene:
            if (event.type() == QEvent.GraphicsSceneMouseMove and
                    event.modifiers() == Qt.ControlModifier):
                # Get nodes/edges
                items = source.selectedItems()

                # Filter to only get nodes
                nodes = [item for item in items if
                         isinstance(item, GraphicsNode)]

                # Update all edges for each selected nodes
                for node in nodes:
                    self.updateEdgesOfNode(node)

            # Left double click (mouse button)
            if (event.type() == QEvent.GraphicsSceneMouseDoubleClick and
                    event.buttons() == Qt.LeftButton):

                # Create a node if there is not an item where we double click
                if not source.itemAt(event.scenePos(), QTransform()):
                    pos = event.scenePos()
                    self.controller.onCreateNode(pos.x(), pos.y())

                    return True

            # Key press
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Delete:
                    # Get selected items (nodes/edges)
                    items = source.selectedItems()

                    for item in items:
                        # Remove node
                        if (isinstance(item, GraphicsNode) and not
                                item.graphicsTextNode.hasFocus()):
                            self.controller.onRemoveNode(item.id)

                        # Remove edge
                        elif isinstance(item, GraphicsEdge):
                            self.controller.onRemoveEdge(item.id)

        return False

    def updateSceneRect(self, graphicsNode):
        '''Expand the scene rect if a node is outside the current scene rect.

        Argument(s):
        graphicsNode (GraphicsNode): Current graphics node
        '''
        sceneRectUpdated = False
        rect = self.sceneRect()
        factor = 2

        # Left border
        if graphicsNode.x() + graphicsNode.boundingRect().left() < rect.left():
            sceneRectUpdated = True
            rect.setLeft(graphicsNode.x() +
                         graphicsNode.boundingRect().left() * factor)
        # Right boder
        elif (graphicsNode.x() + graphicsNode.boundingRect().right() >
              rect.right()):
            sceneRectUpdated = True
            rect.setRight(graphicsNode.x() +
                          graphicsNode.boundingRect().right() * factor)

        # Top border
        if graphicsNode.y() + graphicsNode.boundingRect().top() < rect.top():
            sceneRectUpdated = True
            rect.setTop(graphicsNode.y() +
                        graphicsNode.boundingRect().top() * factor)
        # Bottom border
        elif (graphicsNode.y() + graphicsNode.boundingRect().bottom() >
              rect.bottom()):
            sceneRectUpdated = True
            rect.setBottom(graphicsNode.y() +
                           graphicsNode.boundingRect().bottom() * factor)

        # Node not in the current scene rect: we need to update it
        if sceneRectUpdated:
            self.scene.setSceneRect(rect)

        return sceneRectUpdated
