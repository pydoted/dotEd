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

from doted.enumeration.UpdateModeView import UpdateModeView
from doted.observer.Subject import Subject
from doted.utils.EdgeUtils import EdgeUtils
from pygraphviz import *


class Graph(Subject):
    '''The Graph class defines a graph (model).

    Argument(s):
    directed (boolean): Graph directed or not (default False)

    Attribute(s):
    graph (AGraph): the pygraphviz representation of a graph
    freshId (int): the next fresh id for a node
    '''

    def __init__(self, name="", directed=False):
        # Parent constructor(s)
        Subject.__init__(self)

        self.freshId = 0
        self.graph = AGraph(directed=directed)
        self.name = name

    def clear(self):
        '''Clear the graph.'''
        self.freshId = 0
        self.graph.clear()

    def nodeExists(self, idNode):
        '''Check if a node exists.

        Argument(s):
        idNode (str): ID of the node to check
        '''
        return idNode in self.graph.nodes()

    def edgeExists(self, idSourceNode, idDestNode):
        '''Check if an edge exist.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        return self.graph.has_edge(idSourceNode, idDestNode)

    def addNode(self, id, **attr):
        '''Add a Node to the graph and notify this.

        Argument(s):
        id (str): id of the node
        attr (dict): Dot attributes of the node (empty by default)

        '''        
        # Generate an ID if it is not defined
        if not id:
            id = str(self.freshId)
            self.freshId += 1
        
        if not self.nodeExists(id):
            self.graph.add_node(id, **attr)
            self.notify(self.graph.get_node(id), None, UpdateModeView.add)
        else:
            self.graph.add_node(id, **attr)
            self.notify(self.graph.get_node(id), None, UpdateModeView.edit)
        
    def editNode(self, idNode, **attr):
        '''Edit attributes of a node of the graph.

        Argument(s):
        idNode (str): ID of the node to edit
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        if self.nodeExists(idNode):
            self.graph.add_node(idNode, **attr)
            self.notify(idNode, None, UpdateModeView.edit)
        else:
            raise KeyError("Node %s not in graph." % idNode)
        

    def removeNode(self, idNode):
        '''Remove a Node from the graph.

        Argument(s):
        idNode (str): ID of the node to remove
        '''
        self.graph.delete_node(idNode)
        self.notify(idNode, None, UpdateModeView.remove)


        
    def addEdge(self, idSourceNode, idDestNode, **attr):
        '''Add an Edge to the graph and notify this.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        attr (dict): attributes of the edge
        '''
        # Add the two nodes
        self.addNode(idSourceNode)
        self.addNode(idDestNode)
        
        if not self.edgeExists(idSourceNode, idDestNode):
            self.graph.add_edge(idSourceNode, idDestNode, **attr)
            self.notify(None, self.graph.get_edge(idSourceNode, idDestNode), UpdateModeView.add)
        else:
            self.graph.add_edge(idSourceNode, idDestNode, **attr)
            self.notify(None, self.graph.get_edge(idSourceNode, idDestNode), UpdateModeView.edit)

    def editEdge(self, idSourceNode, idDestNode, **attr):
        '''Edit an Edge of the graph and notify this.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        attr (dict): attributes of the edge
        '''
        if not self.graph.has_edge(idSourceNode, idDestNode):
            raise KeyError("Edge %s - %s nit in graph." % (idSourceNode, idDestNode))

        self.graph.add_edge(idSourceNode, idDestNode, **attr)
        self.notify(None, self.graph.get_edge(idSourceNode, idDestNode), UpdateModeView.edit)

    def removeEdge(self, idSourceNode, idDestNode):
        '''Remove an Edge from the graph.

        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        self.graph.remove_edge(idSourceNode, idDestNode)
        self.notify(None, edge.getArgs(), UpdateModeView.remove)

    def notify(self, node, edge, updateModeView):
        '''Notify all observers of the creation of a Node or an Edge.

        Argument(s):
        node (pygraphviz.Node)
        edge (pygraphviz.Edge)
        updateModeView (UpdateModeView): Update mode
        '''
        for obs in self.observers:
            obs.update(node, edge, updateModeView)

    def getName(self):
        '''Return the name of the graph'''
        return self.name
                        
    def setName(self, name):
        '''Set the name of the graph

        Argument(s):
        name (string)
        '''
        self.name = name
        
    def nodes(self):
        return self.graph.nodes()

    def edges(self):
        return self.graph.edges()
