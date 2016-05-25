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

from major_1.minor_0.enumeration.EdgeArgs import EdgeArgs


class Edge(object):
    '''
    The Edge class defines an edge (model).


    Argument(s):
    source (Node): Source node
    dest (Node): Destination node
    id (str): ID

    Attribute(s):
    id (str): ID
    source (Node): Source node
    dest (Node): Destination node
    '''

    def __init__(self, source, dest, id):
        self.id = id
        self.source = source
        self.dest = dest
        source.addNeighbour(dest)
        dest.addNeighbour(source)
        # self.color enum ?

    def getArgs(self):
        '''Return a dictionary of the arguments of the edge.'''
        return {
            EdgeArgs.id: self.id,
            EdgeArgs.sourceId: self.source.id,
            EdgeArgs.destId: self.dest.id
        }
