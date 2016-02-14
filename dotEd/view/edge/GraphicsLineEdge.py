# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsLineItem
from view.edge.GraphicsEdge import GraphicsEdge


class GraphicsLineEdge(GraphicsEdge, QGraphicsLineItem):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsLineEdge, self).__init__()
