# -*- coding: utf-8 -*-

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTreeView

from view.widget.View import View


class PropertiesView(View, QTreeView):
    '''The PropertiesView class defines a view for the properties of a Node.'''


    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTreeView.__init__(self)
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Properties", "Values"])
        self.setModel(model)
