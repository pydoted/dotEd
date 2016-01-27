# -*- coding: utf-8 -*-
from abc import ABCMeta
from PyQt5.QtWidgets import QGraphicsView




class AbstractView(QGraphicsView):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta


    def __init__(self, source, dest):
        '''
        Constructor
        '''
        QGraphicsView.__init__()