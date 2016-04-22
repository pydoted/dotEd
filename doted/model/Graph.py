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
    x (float): x coordinate for auto pos x node
    y (float): y coordinate for auto pos y node
    deltaX (float): delta x to compute new auto pos x of a node
    '''
    
    
    deltaX = 100

    def __init__(self, directed=False):
        # Parent constructor(s)
        Subject.__init__(self)
        
        self.nodes = {}
        self.edges = {}
        self.resetNbNodes()
        self.resetNbEdges()
        self.directed = directed
        
        self.x = 0
        self.y = 0
    
    def clear(self):
        '''Clear the graph.'''
        # Remove all nodes (will also remove all edges)
        for idNode in list(self.nodes.keys()):
            self.removeNode(idNode)
    
    def nodeExists(self, idNode):
        '''Check if a node exists.
        
        Argument(s):
        idNode (str): ID of the node to check
        '''
        return idNode in self.nodes
    
    def edgeExists(self, idSourceNode, idDestNode):
        '''Check if an edge exist.
        
        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        # The two nodes must exist and be neighbored
        return (self.nodeExists(idSourceNode) and
                self.nodeExists(idDestNode) and
                self.nodes[idSourceNode].isNeighboringTo(idDestNode))
    
    def addNode(self, id, dicDotAttrs={}, x=None, y=None):
        '''Add a Node to the graph and notify this.
        
        Argument(s):
        id (str): id of the node
        dicDotAttrs (Dictionary[]): Dot attributes of the node (default {})
        x (float): x coordinate of the node (default None)
        y (float): y coordinate of the node (default None)
        '''
        # Generate an ID if it is not defined
        if not id:
            self.nbNodes += 1
            # Increment id while the id already exists
            while str(self.nbNodes) in self.nodes:
                self.nbNodes += 1
            id = str(self.nbNodes)
        
        # Only create the node if it doesn't exist
        if not self.nodeExists(id):            
            node = Node(id, dicDotAttrs, x if x else self.x, 
                        y if y else self.y)
            if not x:
                self.x += Graph.deltaX

            self.nodes[node.id] = node
            self.notify(node.getArgs(), None, UpdateModeView.add)
    
    def editNode(self, idNode, dicDotAttrs):
        '''Edit a label node of the graph.
        
        Argument(s):
        idNode (int): ID of the node to edit
        dicDotAttrs (Dictionary[]): Dot attributes of the node
        '''
        if self.nodeExists(idNode):
            node = self.nodes[idNode]            
            node.edit(dicDotAttrs)
            self.notify(node.getArgs(), None, UpdateModeView.edit)
    
    def removeNode(self, idNode):
        '''Remove a Node from the graph.
        
        Argument(s):
        idNode (str): ID of the node to remove
        '''
        node = self.nodes.pop(idNode)
        self.notify(node.getArgs(), None, UpdateModeView.remove)

        # Removes associated edges
        for edge in list(self.edges.values()):
            if node == edge.source or node == edge.dest:
                self.removeEdge(edge.id)
        
        if not self.nodes:
            self.resetNbNodes()
        
    def addEdge(self, idSourceNode, idDestNode):
        '''Add an Edge to the graph and notify this.
        
        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        # Add the two nodes
        self.addNode(idSourceNode)
        self.addNode(idDestNode)
        
        # Only create the edge if it doesn't exist
        if not self.edgeExists(idSourceNode, idDestNode):
            self.nbEdges += 1
            edge = Edge(self.nodes[idSourceNode], self.nodes[idDestNode],
                        self.nbEdges)
            self.edges[edge.id] = edge
            self.notify(None, edge.getArgs(), UpdateModeView.add)
    
    def removeEdge(self, idEdge):
        '''Remove an Edge from the graph.
        
        Argument(s):
        idEdge (str): ID of the edge to remove
        '''
        # Check if it exists
        if idEdge in self.edges:
            # Remove it
            edge = self.edges.pop(idEdge)
            
            # Source and dest nodes are not neighboring anymore
            edge.source.removeNeighbour(edge.dest)
            edge.dest.removeNeighbour(edge.source)
            
            if not self.edges:
                self.resetNbEdges()
            
            self.notify(None, edge.getArgs(), UpdateModeView.remove)
    
    def removeEdgeByIdNodes(self, idSourceNode, idDestNode):
        '''Remove an Edge from the graph with the two nodes ID.
        
        Argument(s):
        idSourceNode (str): ID of the source node
        idDestNode (str): ID of the destination node
        '''
        if self.edgeExists(idSourceNode, idDestNode):
            for key, value in list(self.edges.items()):
                if ((value.source.id == idSourceNode and
                     value.dest.id == idDestNode) or
                    (value.source.id == idDestNode and
                     value.dest.id == idSourceNode)):
                    self.removeEdge(key)
                    break

    def resetNbNodes(self):
        '''Reset number of nodes.'''
        self.nbNodes = 0
    
    def resetNbEdges(self):
        '''Reset number of edges.'''
        self.nbEdges = 0
    
    def notify(self, dictArgsNode, dictArgsEdge, updateModeView):
        '''Notify all observers of the creation of a Node or an Edge.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView): Update mode
        '''
        for obs in self.observers:
            obs.update(dictArgsNode, dictArgsEdge, updateModeView) 
