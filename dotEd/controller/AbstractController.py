# -*- coding: utf-8 -*-
from abc import ABCMeta


class AbstractController:
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta


    def __init__(self, model, view):
        '''
        Constructor
        '''
        self.model = model
        self.view = view
