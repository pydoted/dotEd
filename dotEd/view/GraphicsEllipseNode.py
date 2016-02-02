# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsEllipseItem
from view.GraphicsAbstractNode import GraphicsAbstractNode


class GraphicsEllipseNode(GraphicsAbstractNode, QGraphicsEllipseItem):
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