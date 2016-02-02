# -*- coding: utf-8 -*-

class Node:
    '''
    classdocs
    '''


    def __init__(self, label=""):
        '''
        Constructor
        '''
        self.id = ""
        self.label = label
        #self.shape enum ?
        #self.color enum ?
        self.neighbours = []
