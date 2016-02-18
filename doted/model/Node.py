# -*- coding: utf-8 -*-


class Node:
    '''Model of a node.
    
    
    Argument(s):
    label (str): Label (default "") 
    
    Attribute(s):
    id (int): ID
    label (str): Label
    '''


    def __init__(self, id):
        self.id = id
        self.label = "n"+str(id)
        #self.shape enum ?
        #self.color enum ?
        #self.neighbours = [] subgraph ?
