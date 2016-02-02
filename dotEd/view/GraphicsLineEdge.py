# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsLineItem

from view.GraphicsSuperEdge import GraphicsSuperEdge


class GraphicsLineEdge(GraphicsSuperEdge, QGraphicsLineItem):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsLineEdge, self).__init__()