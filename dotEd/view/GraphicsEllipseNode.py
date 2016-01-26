# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGraphicsEllipseNode


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