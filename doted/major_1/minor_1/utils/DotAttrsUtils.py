# -*- coding: utf-8 -*-

from major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils as \
    DotAttrsUtilsV1
from major_1.minor_1.enumeration.NodeDotAttrs import NodeDotAttrs
from major_1.minor_1.utils.NodeDotColorUtils import NodeDotColorUtils


class DotAttrsUtils(DotAttrsUtilsV1):
    '''The DotAttrsUtils class defines a set of functions for dot attributes.
    '''
    
    
    def __init__(self):
        # Parent constructor(s)
        DotAttrsUtilsV1.__init__(self)

    def checkNodeAttrsForm(self, dictNodeAttrs):
        '''Return None if an attribute of a node is not valid, else an error
        message.
        
        Argument(s):
        dictNodeAttrs (str): Dot attributes values of the nodes
        '''
        message = DotAttrsUtilsV1.checkNodeAttrsForm(self, dictNodeAttrs)
        # If message is not None, then there is an invalid attribute
        if message:
            return message
        
        # Check color attribute
        if (NodeDotAttrs.color.value in dictNodeAttrs and
            not NodeDotColorUtils.isColorValid(dictNodeAttrs
                                               [NodeDotAttrs.color.value])):
            return DotAttrsUtilsV1.formatErrorMessage(self,
                                                    NodeDotAttrs.color.value,
                                    dictNodeAttrs[NodeDotAttrs.color.value])
        
        # All attributes are valid
        return None

    def checkEdgeAttrsForm(self, dictEdgeAttrs):
        '''Return None if an attribute of an edge is not valid, else an error
        message.
        
        Argument(s):
        dictEdgeAttrs (str): Dot attributes values of the edges
        '''
        message = DotAttrsUtilsV1.checkEdgeAttrsForm(self, dictEdgeAttrs)
        # If message is not None, then there is an invalid attribute
        if message:
            return message
        
        # All attributes are valid
        return None
    