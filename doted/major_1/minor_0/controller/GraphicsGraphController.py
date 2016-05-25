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

from major_1.minor_0.controller.Controller import Controller


class GraphicsGraphController(Controller):
    '''The GraphicsGraphController class defines a controller to manage a
    Graph (model)/GraphicsGraphView (view).


    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller
    textGraphController (TextGraphController): Ref to the TextGraphController

    Attribute(s):
    textGraphController (TextGraphController): Ref to the TextGraphController
    '''

    def __init__(self, model, view, textGraphController):
        # Parent constructor(s)
        Controller.__init__(self, model, view)

        self.textGraphController = textGraphController

    def onCreateNode(self, x, y):
        '''Callback function when creating a node.

        Argument(s):
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        self.model.addNode(None, {}, x, y)

    def onEditNode(self, idNode, dicDotAttrs):
        '''Callback function when editing a label a node.

        Argument(s):
        idNode (str): ID of the node to edit
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        self.model.editNode(idNode, dicDotAttrs)

    def onRemoveNode(self, idNode):
        '''Callback function when removing a node.

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

    def onRemoveEdge(self, idEdge):
        '''Callback function when removing an edge.

        Argument(s):
        idEdge (str): ID of the edge to remove
        '''
        self.model.removeEdge(idEdge)

    def onSelectItem(self, id):
        '''Inform the controller of textual view that an item (node/edge) has
        been selected for that the controller of textual view highlight this
        item in the text.

        Argument(s):
        id (str): ID of the node
        '''
        self.textGraphController.highlightItem(id)
