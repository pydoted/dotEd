# -*- coding: utf-8 -*-


class StringUtils(object):
    '''The StringUtils class defines a set of functions for strings.'''

    @staticmethod
    def isStrBetweenDoubleQuotes(text):
        '''Return True if the text is between double quotes, else False.

        Argument(s):
        text (str): Text to test
        '''
        return text.startswith('"') and text.endswith('"')
