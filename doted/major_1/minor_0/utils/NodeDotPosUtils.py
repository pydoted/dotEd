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

import re

from doted.major_1.minor_0.enumeration.NodeArgs import NodeArgs


class NodeDotPosUtils(object):
    '''The NodeDotPosUtils class defines a set of functions for the dot pos
    node attribute.'''

    @staticmethod
    def formatPos(x, y):
        '''Format the dot pos attribute with x and y coordinates.

        Argument(s)
        x (float): x coordinate
        y (float): y coordinate
        '''
        return (
                '"' +
                str("{0:.2f}".format(x)) +
                ',' +
                str("{0:.2f}".format(y)) +
                '"'
        )

    @staticmethod
    def getPos(posAttr):
        '''Get x and y coordinates from a dot pos attribute.

        Argument(s):
        posAttr (str): Dot pos attribute
        '''
        from doted.major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils

        result = re.findall(DotAttrsUtils.realNumberPattern, posAttr)

        # posAttr if valid if we have two numbers
        if (len(result) < 2):
            return None

        return {
            NodeArgs.x: float(result[0]),
            NodeArgs.y: float(result[1])
        }

    @staticmethod
    def isPosValid(posAttr):
        '''Return True if the dot pos attribute is valid.'''
        from doted.major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils

        return re.search('^"\s*' + DotAttrsUtils.realNumberPattern +
                         "\s*,\s*" + DotAttrsUtils.realNumberPattern +
                         '\s*"$', posAttr)
