# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from view.View import View


class GraphicsGraph(View, QGraphicsView):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        View.__init__(self)
        QGraphicsView.__init__(self)

        self.nodes = []
        self.edges = []
        
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
