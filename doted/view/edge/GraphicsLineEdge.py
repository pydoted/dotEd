# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsLineItem

from view.edge.GraphicsEdge import GraphicsEdge


class GraphicsLineEdge(GraphicsEdge, QGraphicsLineItem):
    '''Represent an Edge as a simple line.'''


    def __init__(self):
        # Parent constructor(s)
        GraphicsLineEdge.__init__(self)
