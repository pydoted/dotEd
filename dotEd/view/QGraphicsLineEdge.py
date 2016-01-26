# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsLineItem


class GraphicsLineEdge(GraphicsAbstractEllipse, QGraphicsLineItem):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsLineEdge, self).__init__()