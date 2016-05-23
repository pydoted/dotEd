# -*- coding: utf-8 -*-

import re

from major_1.minor_0.enumeration.NodeArgs import NodeArgs


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
        return '"' + str(x) + ',' + str(y) + '"'

    @staticmethod
    def getPos(posAttr):
        '''Get x and y coordinates from a dot pos attribute.
        
        Argument(s):
        posAttr (str): Dot pos attribute 
        '''
        from major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils

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
        from major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils

        return re.search('^"\s*' + DotAttrsUtils.realNumberPattern +
                        "\s*,\s*" + DotAttrsUtils.realNumberPattern +
                        '\s*"$', posAttr)
