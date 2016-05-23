# -*- coding: utf-8 -*-

from major_1.minor_0.utils.DotAttrsUtils import DotAttrsUtils as \
    DotAttrsUtilsV1_0
from major_1.minor_1.enumeration.NodeDotAttrs import NodeDotAttrs
from major_1.minor_1.utils.NodeDotColorUtils import NodeDotColorUtils


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
            return DotAttrsUtilsV1_0.formatErrorMessage(self,
                                                    NodeDotAttrs.color.value,
                                    dictNodeAttrs[NodeDotAttrs.color.value])
        
        # All attributes are valid
        return None
