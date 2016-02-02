# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsEllipseItem
from view.GraphicsSuperNode import GraphicsSuperNode


class GraphicsEllipseNode(GraphicsSuperNode, QGraphicsEllipseItem):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsEllipseNode, self).__init__()
    
    def paint(self):
        QGraphicsEllipseItem.paint(self)