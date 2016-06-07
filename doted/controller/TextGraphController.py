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

    def onCreateNode(self, idNode, attr):
        '''Callback function when creating a node.

        Argument(s):
        idNode (str): ID of the node
        attr (dict): attributes
        '''
        self.checkAndCleanAttrs(attr)
        self.model.addNode(idNode, **attr)

    def onEditNode(self, idNode, attr):
        '''Callback function when editing a label a node.

        Argument(s):
        idNode (str): ID of the node to edit
        attr (dict): attributes
        '''
        self.checkAndCleanAttrs(attr)
        self.model.editNode(idNode, attr)

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
        self.model.removeEdge(idSourceNode, idDestNode)

    def checkAndCleanAttrs(self, attr):
        '''Delete unknown attributes and set known empty attributes as None

        Argument(s):
        attr (dict): attributes
        '''
        pass

    def highlightItem(self, id):
        '''Inform the view that it must highlight an Item.

        Argument(s):
        id (str): ID of the node
        '''
        self.view.highlightItem(id)


    def createGraphFromText(self, text):
        raise TODO
