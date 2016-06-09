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

class Controller(object):
    '''The Controller class defines a base class for controllers.


    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller

    Attribute(s):
    model (Graph): Model of the Graph in dotEd application
    view (View): View of the controller
    '''

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setController(self)

