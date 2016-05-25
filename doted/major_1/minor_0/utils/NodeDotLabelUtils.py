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

from major_1.minor_0.utils.StringUtils import StringUtils


class NodeDotLabelUtils(object):
    '''The NodeDotLabelUtils class defines a set of functions for the dot label
    node attribute.'''

    @staticmethod
    def formatLabel(label):
        '''Format the dot label attribute.

        Argument(s)
        label (str): Label
        '''
        # Must add quotes if there are spaces or EOL
        if ' ' in label or '\n' in label:
            return '"' + label.replace('\n', '\\n') + '"'

        return label

    @staticmethod
    def getLabel(labelAttr):
        '''Get the label from a dot label attribute.

        Argument(s):
        labelAttr (str): Dot label attribute
        '''
        # If it starts with a quote, then the label is between quotes : we
        # don't take these quotes
        if StringUtils.isStrBetweenDoubleQuotes(labelAttr):
            return labelAttr[1:-1].replace('\\n', '\n')

        return labelAttr
