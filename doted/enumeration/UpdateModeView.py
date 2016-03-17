from enum import Enum


class UpdateModeView(Enum):
    '''The UpdateModeView enum defines the mode when there is an update in a View.'''
    add = 0
    edit = 1
    remove = 2
