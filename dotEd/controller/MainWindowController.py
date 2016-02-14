# -*- coding: utf-8 -*-

from controller.Controller import Controller
from model.Node import Node


class MainWindowController(Controller):
    '''
    classdocs
    '''


    def __init__(self, model, view):
        '''
        Constructor
        '''
        Controller.__init__(self, model, view)
    
    def onCreateNode(self):
        node = Node()
        self.model.addNode(node)
        self.model.notify()
