# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QColorDialog

from major_1.minor_0.enumeration.NodeArgs import NodeArgs
from major_1.minor_0.view.node.GraphicsNode import GraphicsNode as \
    GraphicsNodeV1_0
from major_1.minor_1.enumeration.NodeDotAttrs import NodeDotAttrs
from major_1.minor_1.utils.NodeDotColorUtils import NodeDotColorUtils


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
