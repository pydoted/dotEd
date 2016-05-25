# -*- coding: utf-8 -*-

# Copyright (c) 2016 Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem
# This file is part of dotEd.
# 
# dotEd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# dotEd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with dotEd.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTreeView

from major_1.minor_0.view.widget.View import View


class PropertiesView(View, QTreeView):
    '''The PropertiesView class defines a view for the properties of a Node.'''


    def __init__(self):
        # Parent constructor(s)
        View.__init__(self)
        QTreeView.__init__(self)
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Properties", "Values"])
        self.setModel(model)
