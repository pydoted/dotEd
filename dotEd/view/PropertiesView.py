# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel

from view.View import View


class PropertiesView(View, QTreeView):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Parent constructors
        View.__init__(self)
        QTreeView.__init__(self)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Properties", "Values"])
        self.setModel(model)