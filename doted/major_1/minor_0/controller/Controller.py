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

from major_1.minor_0.enumeration.UpdateModeView import UpdateModeView
from major_1.minor_0.observer.Observer import Observer


class Controller(Observer):
    '''The Controller class defines a base class for controllers.
    
    
    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller
    
    Attribute(s):
    model (Graph): Model of the Graph in dotEd application
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Observer.__init__(self, model)
        
        self.model = model
        self.view = view
        self.view.setController(self)
    
    def update(self, dictArgsNode, dictArgsEdge, updateModeView):
        '''Update the view.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView) : Update mode
        '''
        # Update node
        if dictArgsNode:
            if updateModeView == UpdateModeView.add:
                self.view.addNode(dictArgsNode)
            elif updateModeView == UpdateModeView.edit:
                self.view.editNode(dictArgsNode)
            elif updateModeView == UpdateModeView.remove:
                self.view.removeNode(dictArgsNode)
        
        # Update edge
        else:
            if updateModeView == UpdateModeView.add:
                self.view.addEdge(dictArgsEdge)
            elif updateModeView == UpdateModeView.edit:
                self.view.editEdge(dictArgsEdge)
            elif updateModeView == UpdateModeView.remove:
                self.view.removeEdge(dictArgsEdge)
