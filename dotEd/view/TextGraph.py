# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTextEdit

from view.View import View


class TextGraph(View, QTextEdit):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        View.__init__(self)
        QTextEdit.__init__(self)
