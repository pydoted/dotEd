# -*- coding: utf-8 -*-

from enumeration.UpdateModeView import UpdateModeView
from model.Edge import Edge
from model.Node import Node
from observer.Subject import Subject


class Graph(Subject):
    '''The Graph class defines a graph (model).
    
    
    Argument(s):
    directed (boolean): Graph directed or not (default False)
    
    Attribute(s):
    nodes (Dictionary[Node]): All nodes
    edges (Dictionary[Edge]): All edges
    nbNodes (Dictionary[Edge]): Number of nodes
    nbEdges (Dictionary[Edge]): Number of edges
    directed (boolean): Graph directed or not
    '''


    def __init__(self, directed=False):
        # Parent constructor(s)
        Subject.__init__(self)
        
        self.nodes = {}
        self.edges = {}
        self.nbNodes = 0
        self.nbEdges = 0
        self.directed = directed

    def addNode(self, x, y):
        '''Add a Node to the graph and notify this.
        
        Argument(s):
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        self.nbNodes += 1
        node = Node(self.nbNodes, x , y)
        self.nodes[node.id] = node
        self.notify(node.getArgs(), None, UpdateModeView.add)
    
    def removeNode(self, idNode):
        '''Remove a Node from the graph.
        
        Argument(s):
        idNode (int): ID of the node to remove
        '''
        node = self.nodes.pop(idNode)
        self.notify(node.getArgs(), None, UpdateModeView.remove)

        # Get the id of the egdes to remove
        idEdgesToRemove = []
        for edge in self.edges.values():
            if (node == edge.source or node == edge.dest):
                idEdgesToRemove.append(edge.id)
        
        # Remove associated edges
        for idEdge in idEdgesToRemove:
            self.removeEdge(idEdge)

    def editLabelNode(self, idNode, labelNode):
        '''Edit a label node of the graph.
        
        Argument(s):
        idNode (int): ID of the node to edit
        labelNode (str): New label node
        '''
        
        node = self.nodes[idNode]
        node.label = labelNode
        self.notify(node.getArgs(), None, UpdateModeView.edit)
        
    def addEdge(self, idSourceNode, idDestNode):
        '''Add an Edge to the graph and notify this.
        
        Argument(s):
        idSourceNode (int): ID of the source node
        idDestNode (int): ID of the destination node
        '''
        # Only add the edge if the two nodes are not neighboring
        if not self.nodes[idSourceNode].isNeighboringTo(idDestNode):
            self.nbEdges += 1
            edge = Edge(self.nodes[idSourceNode], self.nodes[idDestNode],
                        self.nbEdges)
            self.edges[edge.id] = edge
            self.notify(None, edge.getArgs(), UpdateModeView.add)
    
    def removeEdge(self, idEdge):
        '''Remove an Edge from the graph.
        
        Argument(s):
        idEdge (int): ID of the edge to remove
        '''
        edge = self.edges.pop(idEdge)
        
        # Source and dest nodes are not neighboring anymore
        edge.source.removeNeighbour(edge.dest)
        edge.dest.removeNeighbour(edge.source)
        
        self.notify(None, edge.getArgs(), UpdateModeView.remove)
       
    def notify(self, dictArgsNode, dictArgsEdge, updateModeView):
        '''Notify all observers of the creation of a Node or an Edge.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView): Update mode
        '''
        for obs in self.observers:
            obs.update(dictArgsNode, dictArgsEdge, updateModeView) 
