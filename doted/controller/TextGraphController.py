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

from pydot_ng import NODE_ATTRIBUTES

from doted.utils.NodeDotPosUtils import NodeDotPosUtils
from doted.controller.Controller import Controller
from doted.enumeration.NodeArgs import NodeArgs
from doted.enumeration.NodeDotAttrs import NodeDotAttrs


class TextGraphController(Controller):
    '''The TextGraphController class defines a controller to manage
    a Graph (model)/TextGraphView (view).


    Argument(s):
    model (Graph): Model of the controller
    view (View): View of the controller
    '''

    def __init__(self, model, view):
        # Parent constructor(s)
        Controller.__init__(self, model, view)

    def importGraph(self, text):
        '''Send textual representation of the graph to the view after an import.

        Argument(s):
        text (str): Textual representation of the graph
        '''
        self.view.importGraph(text)

    def onCreateNode(self, idNode, dicDotAttrs):
        '''Callback function when creating a node.

        Argument(s):
        idNode (str): ID of the node
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        self.checkAndCleanAttrs(dicDotAttrs)

        if NodeDotAttrs.pos.value in dicDotAttrs:
            if dicDotAttrs[NodeDotAttrs.pos.value]:
                # Get position
                coords = NodeDotPosUtils.getPos(
                    dicDotAttrs[NodeDotAttrs.pos.value])
                self.model.addNode(idNode, dicDotAttrs, coords[NodeArgs.x],
                                   coords[NodeArgs.y])
            else:
                self.model.addNode(idNode, dicDotAttrs)

    def onEditNode(self, idNode, dicDotAttrs):
        '''Callback function when editing a label a node.

        Argument(s):
        idNode (str): ID of the node to edit
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        self.checkAndCleanAttrs(dicDotAttrs)

        self.model.editNode(idNode, dicDotAttrs)

    def onRemoveNode(self, idNode):
        '''Callback function when removinf a node.

        Argument(s):
        idNode (str): ID of the node to remove
        '''
        self.model.removeNode(idNode)

    def onCreateEdge(self, idSourceNode, idDestNode):
        '''Callback function when creating an edge.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        self.model.addEdge(idSourceNode, idDestNode)

    def onRemoveEdge(self, idSourceNode, idDestNode):
        '''Callback function when removing an edge.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (intstr): ID of the destination node
        '''
        self.model.removeEdgeByIdNodes(idSourceNode, idDestNode)

    def checkAndCleanAttrs(self, dicDotAttrs):
        '''Delete unknown attributes and set known empty attributes as None

        Argument(s):
        dicDotAttrs (Dictionary[]): Dot attributes of the Item
        '''
        # Set all attrs in NodeDotAttrs as None
        for attr in NodeDotAttrs:
            if attr.value not in dicDotAttrs:
                dicDotAttrs[attr.value] = None

        # Delete all attrs which are not node's attrs according to pydot
        attrToRemove = []
        for attr in dicDotAttrs:
            if attr not in NODE_ATTRIBUTES:
                attrToRemove.append(attr)
        for attr in attrToRemove:
            dicDotAttrs.pop(attr)

    def highlightItem(self, id):
        '''Inform the view that it must highlight an Item.

        Argument(s):
        id (str): ID of the node
        '''
        self.view.highlightItem(id)
