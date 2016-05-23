# -*- coding: utf-8 -*-

from major_1.minor_0.utils.NodeDotPosUtils import NodeDotPosUtils
from major_1.minor_0.enumeration.NodeDotAttrs import NodeDotAttrs


class DotAttrsUtils(object):
    '''The DotAttrsUtils class defines a set of functions for dot attributes.
    
    Attribute(s):
    realNumberPattern (str): Real number pattern
    '''
    
    
    realNumberPattern = "-?\d+\.?\d*"

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
