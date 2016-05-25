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

import binascii
import re

from PyQt5.QtCore import Qt
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
    pathColorNamesHexa = "ressources/colors.txt"    

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
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return QColor(NodeDotColorUtils.dictColorNamesHexa[colorAttr])
            
            # Transparent color
            if NodeDotColorUtils.isTransparentColor(colorAttr):
                return QColor(Qt.transparent)
            
            # HSV to QColor
            if NodeDotColorUtils.isHSVColor(colorAttr):
                hsv = re.findall(DotAttrsUtils.realNumberPattern,
                                colorAttr)
                return QColor.fromHsvF(float(hsv[0]), float(hsv[1]),
                                       float(hsv[2]))
        
        # In this case, we can only have a color name
        else:
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return QColor(NodeDotColorUtils.dictColorNamesHexa[colorAttr])
            
            # Transparent color
            if NodeDotColorUtils.isTransparentColor(colorAttr):
                return QColor(Qt.transparent)
        
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
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return True
            
            # Transparent color
            if NodeDotColorUtils.isTransparentColor(colorAttr):
                return True
            
            # HSV Color
            if NodeDotColorUtils.isHSVColor(colorAttr):
                return True
        
        # In this case, we can only have a color name
        else:
            if NodeDotColorUtils.colorNameExists(colorAttr):
                return True
            
            # Transparent color
            if NodeDotColorUtils.isTransparentColor(colorAttr):
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

    @staticmethod
    def isTransparentColor(color):
        return color == "transparent"
