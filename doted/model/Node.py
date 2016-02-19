# -*- coding: utf-8 -*-


class Node:
    '''Model of a node.
    
    
    Argument(s):
    label (str): Label 
    id (int): Id
    
    Attribute(s):
    id (int): Id
    label (str): Label
    '''


    def __init__(self, id):
        self.id = id
        self.label = "n" + str(self.id)
        #self.shape enum ?
        #self.color enum ?
        #self.neighbours = [] subgraph ?

    def getArgs(self):
        '''return a dictionary of the arguments of the node.'''
        return {"id":self.id, "label":self.label}