# -*- coding: utf-8 -*-

from observer.Observer import Observer


class Controller(Observer):
    '''The Controller class defines a base class for controllers.
    
    
    Argument(s):
    model (Subject): Model of the controller
    view (View): View of the controller
    
    Attribute(s):
    view (View): View of the controller
    '''


    def __init__(self, model, view):
        # Parent constructor(s)
        Observer.__init__(self, model)
        
        self.view = view
        self.view.setController(self)
    
    def update(self, dictArgsNode, dictArgsEdge, updateModeView):
        '''Update the view.
        
        Argument(s):
        dictArgsNode (Dictionary[]): Dictionary of arguments of the node
        dictArgsEdge (Dictionary[]): Dictionary of arguments of the edge
        updateModeView (UpdateModeView) : Update mode
        ''' 
        if dictArgsNode: 
            self.view.updateNode(dictArgsNode, updateModeView)
        else:
            self.view.updateEdge(dictArgsEdge, updateModeView)
