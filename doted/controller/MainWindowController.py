# -*- coding: utf-8 -*-

from pydot_ng import *
from pydot_ng._dotparser import add_elements, push_default_stmt

class MainWindowController():
    '''The MainWindowController class defines the controller to manage
       a Doted (app)/MainWindow (view).
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller    
    '''


    def __init__(self, model, view):
        self.view = view
        self.view.setController(self)
        self.model = model


    def onImportFile(self):
        '''Import a file which contains a graph and build or rebuild''' 
        #Load graph from file with pydot_ng    
        graph = graph_from_dot_file("doted/test.dot")
        nodes = graph.get_nodes();
        for n in nodes:
            print(n.to_string())
        push_default_stmt("a -- b -- c;", a, b)
        #nods = g.get_nodes();
        #for m in nods:
        #    print(m.to_string())
        
        
    
    def onSaveFile(self):
        '''Save in a file the text description of the graph.''' 
        pass
        