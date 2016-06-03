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

from doted.enumeration.NodeDotAttrs import NodeDotAttrs
from doted.utils.NodeDotColorUtils import NodeDotColorUtils
from doted.utils.NodeDotPosUtils import NodeDotPosUtils


class DotAttrsUtilsV1_0(object):
    '''The DotAttrsUtils class defines a set of functions for dot attributes.
    '''

    def formatErrorMessage(self, dotAttr, attrValue):
        '''Format a message error for a specific dot attribute.

        Argument(s):
        dotAttr (NodeDotAttrs): Dot attribute name
        attrValue(str): Dot attribute value
        '''
        return "Invalid " + dotAttr + " attribute " + attrValue

    def checkNodeAttrsForm(self, dictNodeAttrs):
        '''Return None if an attribute of a node is not valid, else an error
        message.

        Argument(s):
        dictNodeAttrs (str): Dot attributes values of the nodes
        '''
        for attr in dictNodeAttrs.keys():
            # Case of pos attribute
            if (attr == NodeDotAttrs.pos.value and
                    not NodeDotPosUtils.isPosValid(dictNodeAttrs[attr])):
                return self.formatErrorMessage(NodeDotAttrs.pos.value,
                                               dictNodeAttrs[attr])

        # All attributes are valid
        return None

    def checkEdgeAttrsForm(self, dictEdgeAttrs):
        '''Return None if an attribute of an edge is not valid, else an error
        message.

        Argument(s):
        dictEdgeAttrs (str): Dot attributes values of the edges
        '''
        # All attributes are valid
        return None


class DotAttrsUtils(DotAttrsUtilsV1_0):
    '''The DotAttrsUtils class defines a set of functions for dot attributes.
    '''

    def __init__(self):
        # Parent constructor(s)
        DotAttrsUtilsV1_0.__init__(self)

    def checkNodeAttrsForm(self, dictNodeAttrs):
        '''Return None if an attribute of a node is not valid, else an error
        message.

        Argument(s):
        dictNodeAttrs (str): Dot attributes values of the nodes
        '''
        message = DotAttrsUtilsV1_0.checkNodeAttrsForm(self, dictNodeAttrs)
        # If message is not None, then there is an invalid attribute
        if message:
            return message

        # Check color attribute
        if (NodeDotAttrs.color.value in dictNodeAttrs and
            not NodeDotColorUtils.isColorValid(dictNodeAttrs
                                               [NodeDotAttrs.color.value])):
            return DotAttrsUtilsV1_0.formatErrorMessage(
                self,
                NodeDotAttrs.color.value,
                dictNodeAttrs[NodeDotAttrs.color.value]
            )

        # All attributes are valid
        return None
