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


class View(object):
    '''The View class defines a base class for views.


    Attribute(s):
    controller (Controller): Controller of the view
    '''

    def __init__(self):
        self.controller = None
        self.model = None

    def setController(self, controller):
        '''Set a controller.

        Argument(s):
        controller (Controller): Controller of the view
        '''
        self.controller = controller

    def setModel(self, model):
        '''Set a model.

        Argument(s):
        model (Model): Model of the view
        '''
        self.model = model

        
    def addNode(self, dictArgsNode):
        '''Add a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def editNode(self, dictArgsNode):
        '''Edit a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def removeNode(self, dictArgsNode):
        '''Remove a node.

        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        '''
        pass

    def addEdge(self, dictArgsEdge):
        '''Add an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass

    def editEdge(self, dictArgsEdge):
        '''Edit an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass

    def removeEdge(self, dictArgsEdge):
        '''Remove an edge.

        Argument(s):
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        '''
        pass
