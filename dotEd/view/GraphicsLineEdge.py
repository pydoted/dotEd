# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsLineItem

from view.GraphicsAbstractEdge import GraphicsAbstractEdge


class GraphicsLineEdge(GraphicsAbstractEdge, QGraphicsLineItem):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsLineEdge, self).__init__()