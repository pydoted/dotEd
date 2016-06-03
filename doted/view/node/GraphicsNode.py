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

from PyQt5.Qt import QMarginsF
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QColorDialog, QMenu, QGraphicsItem


from doted.enumeration.NodeArgs import NodeArgs
from doted.enumeration.NodeDotAttrs import NodeDotAttrs
from doted.utils.NodeDotColorUtils import NodeDotColorUtils
from doted.view.node.GraphicsTextNode import GraphicsTextNode
from doted.view.edge.GraphicsSemiEdge import GraphicsSemiEdge
from doted.utils.NodeDotLabelUtils import NodeDotLabelUtils
from doted.utils.NodeDotPosUtils import NodeDotPosUtils

class GraphicsNodeV1_0(object):
    '''The GraphicsNode class defines a base class for a graphics node.

    Argument(s):
    id (str): ID of the node
    graphicsGraphView (GraphicsGraphView): View

    Attribute(s):
    id (str): ID of the node
    graphicsGraphView (GraphicsGraphView): View
    graphicsTextNode (GraphicsTextNode): Text (label) of the node
    semiEdge (GraphicsSemiEdge): Line between a graphics node and cursor mouse
    contextMenu (QMenu): Context menu to edit attributes
    '''

    def __init__(self, id, graphicsGraphView):
        self.id = id
        self.graphicsGraphView = graphicsGraphView

        # Init graphics text node
        self.graphicsTextNode = GraphicsTextNode()
        (self.graphicsTextNode.boundingRect().
         marginsAdded(QMarginsF(10, 10, 10, 10)))

        self.semiEdge = None

        self.contextMenu = QMenu()

        # Edit label
        editLabelAction = self.contextMenu.addAction("Edit label")
        editLabelAction.triggered.connect(self.onEditLabel)

    def edit(self, dictArgsNode):
        '''Edit all attributes of the node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        self.editLabel(dictArgsNode)
        self.editPos(dictArgsNode)

    def editLabel(self, dictArgsNode):
        '''Edit the label.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        # Get ID as default label
        label = self.id

        # Take value label if it exists
        if (NodeDotAttrs.label.value in dictArgsNode[NodeArgs.dotAttrs] and
                dictArgsNode[NodeArgs.dotAttrs][NodeDotAttrs.label.value]):
            label = NodeDotLabelUtils.getLabel(
                (dictArgsNode[NodeArgs.dotAttrs]
                 [NodeDotAttrs.label.value]))

        # Update the text if needed
        if label != self.graphicsTextNode.toPlainText():
            self.graphicsTextNode.setPlainText(label)

    def onEditLabel(self):
        '''Callback function when editing the label.'''
        self.graphicsTextNode.editLabel()

    def editPos(self, dictArgsNode):
        '''Edit the position.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        posChanged = False
        # Update x
        if self.x() != dictArgsNode[NodeArgs.x]:
            posChanged = True
            self.setX(dictArgsNode[NodeArgs.x])

        # Update y
        if self.y() != dictArgsNode[NodeArgs.y]:
            posChanged = True
            self.setY(dictArgsNode[NodeArgs.y])

        if posChanged:
            self.graphicsGraphView.updateEdgesOfNode(self)

            # Center scene on the node if needed
            if self.graphicsGraphView.enlargeSceneRect(self):
                self.graphicsGraphView.centerOn(self)

    def onEditPos(self):
        '''Callback function when editing the pos.'''
        self.graphicsGraphView.controller.onEditNode(self.id, {
            NodeDotAttrs.pos.value:
            NodeDotPosUtils.formatPos(
                self.x(),
                self.y())
        })

    def centerTextInShape(self):
        '''Center the text in the shape.'''
        pass

    def getFocus(self, id):
        '''Indicate when node get the focus to highlight him in textual view.

        Argument(s):
        id (str): ID of the node
        '''
        self.graphicsGraphView.controller.onSelectItem(id)

    def mouseMoveEvent(self, event):
        '''Handle mouse move event.

        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        # Only move the node if CTRL button pressed
        if event.modifiers() == Qt.ControlModifier:
            QGraphicsItem.mouseMoveEvent(self, event)

        # Update coordinates of the line
        elif self.semiEdge is not None:
            self.semiEdge.update(event.scenePos())

    def mousePressEvent(self, event):
        '''Handle mouse press event.

        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsItem.mousePressEvent(self, event)

        # Create the semi-edge and get the focus
        if event.buttons() == Qt.LeftButton:
            self.getFocus(self.id)
            self.semiEdge = GraphicsSemiEdge(event.scenePos(), self)
            self.scene().addItem(self.semiEdge)
        elif event.buttons() == Qt.RightButton:
            self.contextMenu.popup(event.screenPos())

    def mouseReleaseEvent(self, event):
        '''Handle mouse release event.

        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        QGraphicsItem.mouseReleaseEvent(self, event)

        # Construct edge if a semi edge is built
        if self.semiEdge is not None:
            # Remove the semi edge
            self.scene().removeItem(self.semiEdge)
            self.semiEdge = None

            # Filter item on the mouse and only get GraphicsNode
            items = [item for item in self.scene().items(event.scenePos())
                     if isinstance(item, GraphicsNode) and item != self]
            if items:
                # Create edge
                self.graphicsGraphView.controller.onCreateEdge(self.id,
                                                               items[0].id)

    def mouseDoubleClickEvent(self, event):
        '''Handle mouse double click event.

        Argument(s):
        event (QGraphicsSceneMouseEvent): Graphics scene mouse event
        '''
        # Double click on the text of the node to edit text
        self.graphicsTextNode.editLabel()


class GraphicsNode(GraphicsNodeV1_0):
    '''The GraphicsNode class defines a base class for a graphics node.

    Argument(s):
    id (str): ID of the node
    graphicsGraphView (GraphicsGraphView): View
    '''

    def __init__(self, id, graphicsGraphView):
        # Parent(s) constructor(s)
        GraphicsNodeV1_0.__init__(self, id, graphicsGraphView)

        # Edit color
        editColorAction = self.contextMenu.addAction("Edit color")
        editColorAction.triggered.connect(self.onEditColor)

    def edit(self, dictArgsNode):
        '''Edit all attributes of the node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        GraphicsNodeV1_0.edit(self, dictArgsNode)
        self.editColor(dictArgsNode)

    def editColor(self, dictArgsNode):
        '''Edit the color.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        color = None

        # Check if color is defined
        if (NodeDotAttrs.color.value in dictArgsNode[NodeArgs.dotAttrs] and
                dictArgsNode[NodeArgs.dotAttrs][NodeDotAttrs.color.value]):
            color = NodeDotColorUtils.getColor(
                dictArgsNode[NodeArgs.dotAttrs][NodeDotAttrs.color.value])
        # If not define, reset color to black
        else:
            color = QColor(Qt.black)

        # Only update if no changement
        if color and color != self.pen().color():
            self.setPen(QPen(color))

    def onEditColor(self):
        '''Callback function when editing the color.'''
        # Open ColorPicker
        colorHex = QColorDialog.getColor()

        # If "OK" button pressed
        if colorHex.isValid():
            # Set the new color
            self.setPen(QPen(colorHex))

            # Create dictionnary and send update
            dicDotAttrs = {
                NodeDotAttrs.color.value:
                NodeDotColorUtils.formatColor(colorHex.name())
            }
            self.graphicsGraphView.controller.onEditNode(self.id, dicDotAttrs)
