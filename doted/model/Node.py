# -*- coding: utf-8 -*-


class Node:
    '''Model of a node.
    
    
    Argument(s):
    label (str): Label (default "") 
    id (int): ID
    
    Attribute(s):
    id (int): ID
    label (str): Label
    '''


    def __init__(self, idNode):
        self.id = idNode
        self.label = "n" + str(self.id)
        #self.shape enum ?
        #self.color enum ?
        #self.neighbours = [] subgraph ?
