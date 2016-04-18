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
        self.resetNbNodes()
        self.resetNbEdges()
        self.directed = directed
    
    def clear(self):
        '''Clear the graph.'''
        # Remove all nodes (will also remove all edges)
        for idNode in list(self.nodes.keys()):
            self.removeNode(idNode)
    
    def addPydotNode(self, pydotNode, x, y, deltaX):
        '''Add a pydot node in the graph.
        
        Argument(s):
        pydotNode (pydot_ng.Node) : Pydot node
        x (List[float]): x coordinate of the node
        y (List[float]): y coordinate of the node
        deltaX (float): Delta increment for x coordinate
        '''
        if not self.nodeExists(pydotNode.get_name()):
            node = Node(pydotNode.get_name(), x[0] , y[0])
            x[0] += deltaX
            label = pydotNode.get_label()
            if label:
                # Transform "label" to label 
                node.label = label[1:len(label) - 1]
            
            self.nodes[node.id] = node
            self.notify(node.getArgs(), None, UpdateModeView.add)

    def addPydotEdge(self, pydotEdge, x, y, deltaX):
        '''Add a pydot edge in the graph.
        
        Argument(s):
        pydotEdge (pydot_ng.Edge) : Pydot edge
        x (List[float]): x coordinate of the node
        y (List[float]): y coordinate of the node
        deltaX (float): Delta increment for x coordinate
        '''
        # Create source node if it doesn't exist
        idSourceNode = pydotEdge.get_source()
        if not self.nodeExists(idSourceNode):
            node = Node(idSourceNode, x[0], y[0])
            x[0] += deltaX
            self.nodes[node.id] = node
            self.notify(node.getArgs(), None, UpdateModeView.add)

        # Create dest node if it doesn't exist
        idDestNode = pydotEdge.get_destination()
        if not self.nodeExists(idDestNode):
            node = Node(idDestNode, x[0], y[0])
            x[0] += deltaX
            self.nodes[node.id] = node
            self.notify(node.getArgs(), None, UpdateModeView.add)
        
        self.addEdge(idSourceNode, idDestNode)

    def addNode(self, x, y):
        '''Add a Node to the graph and notify this.
        
        Argument(s):
        x (float): x coordinate of the node
        y (float): y coordinate of the node
        '''
        # Increment id while the id already exists
        self.nbNodes += 1
        while str(self.nbNodes) in self.nodes:
            self.nbNodes += 1
        
        node = Node(str(self.nbNodes), x , y)
        self.nodes[node.id] = node
        self.notify(node.getArgs(), None, UpdateModeView.add)
    
    def nodeExists(self, idNode):
        '''Check if a node exists.
        
        Argument(s):
        idNode (int): ID of the node to check
        '''
        return idNode in self.nodes
    
    def removeNode(self, idNode):
        '''Remove a Node from the graph.
        
        Argument(s):
        idNode (int): ID of the node to remove
        '''
        node = self.nodes.pop(idNode)
        self.notify(node.getArgs(), None, UpdateModeView.remove)

        # Removes associated edges
        for edge in list(self.edges.values()):
            if node == edge.source or node == edge.dest:
                self.removeEdge(edge.id)
        
        if not self.nodes:
            self.resetNbNodes()

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
        
        if not self.edges:
            self.resetNbEdges()
        
        self.notify(None, edge.getArgs(), UpdateModeView.remove)
    
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
