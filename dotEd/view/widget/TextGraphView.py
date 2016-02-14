# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit
from view.widget.View import View


class TextGraphView(View, QTextEdit):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        View.__init__(self)
        QTextEdit.__init__(self)
        self.setPlainText("graph {\n\n}")
        
        self.nodes = {}
        self.edges = {}

    def update(self):
        nodeId = "ID"
        if nodeId not in self.nodes:
            self.nodes[nodeId] = "A"
            self.setPlainText(self.nodes[nodeId])
        
        #for all node in nodes....,
