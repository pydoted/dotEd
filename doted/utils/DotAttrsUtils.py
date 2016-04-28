# -*- coding: utf-8 -*-

import re

from enumeration.NodeArgs import NodeArgs


class DotAttrsUtils(object):
    '''The DotAttrsUtils class defines a set of functions for dot attributes.'''


    @staticmethod
    def formatPos(x, y):
        '''Format the dot pos attribute with x and y coordinates.
        
        Argument(s)
        x (float): x coordinate
        y (float): y coordinate
        '''
        return "\"" + str(x) + "," + str(y) + "!\""

    @staticmethod
    def extractPos(posAttr):
        '''Extract x and y coordinates from a dot pos attribute.
        
        Argument(s):
        posAttr (str): Dot pos attribute 
        '''
        # The regex means: extract all -/+ floating numbers from the string
        result = re.findall("-?\d+\.?\d*", posAttr)
        
        return {
            NodeArgs.x: float(result[0]),
            NodeArgs.y: float(result[1])
        }
