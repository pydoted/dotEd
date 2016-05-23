# -*- coding: utf-8 -*-

import binascii
import re

from PyQt5.QtGui import QColor

from major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils
from major_1.minor_0.utils.StringUtils import StringUtils


class NodeDotColorUtils(object):
    '''The NodeDotColorUtils class defines a set of functions for the dot color
    node attribute.
    
    Attribute(s):
    dictColorNamesHexa (Dict[str]): Link between name and hexa colors
    pathColorNamesHexa (str): Path containing the name/hexa colors
    '''
    
    
    dictColorNamesHexa = {}
    pathColorNamesHexa = "../ressources/colors.txt"    

    @staticmethod
    def formatColor(color):
        '''Format the dot color attribute.
        
        Argument(s)
        color (str): color
        '''
        return '"' + str(color) + '"'

    @staticmethod
    def getColor(colorAttr):
        '''Return the QColor of a dot color attribute.
        
        Argument(s):
        colorAttr (str): Color attribute
        '''
        if StringUtils.isStrBetweenDoubleQuotes(colorAttr):
            # Remove double quotes
            colorAttr = colorAttr[1:-1].strip()
            
            # Hexa to QColor
            if NodeDotColorUtils.isHexaColor(colorAttr):
                return QColor(colorAttr)
            
            # Color name to QColor
            elif NodeDotColorUtils.colorNameExists(colorAttr):
                return QColor(NodeDotColorUtils.dictColorNamesHexa[colorAttr])
            
            # HSV to QColor
            elif NodeDotColorUtils.isHSVColor(colorAttr):
                hsv = re.findall(DotAttrsUtils.realNumberPattern,
                                colorAttr)
                return QColor.fromHsvF(float(hsv[0]), float(hsv[1]),
                                       float(hsv[2]))
        
        # In this case, we can only have a color name
        else:
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return QColor(NodeDotColorUtils.dictColorNamesHexa[colorAttr])
        
        # Normaly whe should never reach this case
        return None
    
    @staticmethod
    def createDictColorNamesHexa():
        '''Load the link between name and hexa colors into a dictionnary.'''
        with open(NodeDotColorUtils.pathColorNamesHexa) as f:
            for line in f:
                (key, val) = line.split()
                NodeDotColorUtils.dictColorNamesHexa[key] = val
    
    @staticmethod
    def isColorValid(colorAttr):
        '''Return True if the dot color attribute is valid, else False.
        
        Argument(s):
        colorAttr (str): Color attribute
        '''
        if StringUtils.isStrBetweenDoubleQuotes(colorAttr):
            # Remove double quotes
            colorAttr = colorAttr[1:-1].strip()
        
            # Hexa color
            if NodeDotColorUtils.isHexaColor(colorAttr):
                return True
            # Color name
            elif NodeDotColorUtils.colorNameExists(colorAttr):
                return True
            # HSV Color
            elif NodeDotColorUtils.isHSVColor(colorAttr):
                return True
        # In this case, we can only have a color name
        else:
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return True
        
        return False
    
    @staticmethod
    def isHexaColor(color):
        '''Return True if the color is a hexa color, else False.
        
        Argument(s):
        color (str): Color
        '''
        # Hexa color must start with a "#"
        if not color.startswith('#') or len(color) == 1:
            return False
        
        try:
            binascii.unhexlify(color[1:])
        except Exception:
            return False
        else:
            return True

    @staticmethod
    def colorNameExists(color):
        '''Return True if the color name exists, else False.
        
        Argument(s):
        color (str): Color
        '''
        # Load the dictionnary if needed
        if not NodeDotColorUtils.dictColorNamesHexa:
            NodeDotColorUtils.createDictColorNamesHexa()
        
        return color in NodeDotColorUtils.dictColorNamesHexa
    
    @staticmethod
    def isHSVColor(color):
        '''Return True if the color is a HSV color, else False.
        
        Argument(s):
        color (str): Color
        '''
        return re.search(DotAttrsUtils.realNumberPattern + "\s*,?\s*" +
                         DotAttrsUtils.realNumberPattern + "\s*,?\s*" +
                         DotAttrsUtils.realNumberPattern, color.strip())
