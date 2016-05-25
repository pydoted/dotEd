# -*- coding: utf-8 -*-

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
