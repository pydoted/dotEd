# -*- coding: utf-8 -*-

from PyQt5.Qt import QFile, QIODevice, QByteArray, QFileDialog
from PyQt5.QtWidgets import QMessageBox

from pydot_ng import graph_from_dot_file


class MainWindowController(object):
    '''The MainWindowController class defines the controller to manage
       a Doted (app)/MainWindow (view).
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller
    textGraphController (TextGraphController): Ref to the TextGraphController
    
    Attribute(s):
    model (Model): Model of the controller
    view (View): View of the controller
    textGraphController (TextGraphController): Ref to the TextGraphController
    dotFilter (str): Filter to only show dot files
    '''


    def __init__(self, model, view, textGraphController):
        self.view = view
        self.view.controller = self
        self.model = model
        
        self.textGraphController = textGraphController
        self.dotFilter = "Dot files (*.dot)"

    def onImportFile(self):
        '''Import a file which contains a graph and build or rebuild.''' 
        #Load graph from file with pydot_ng    
        result = QFileDialog.getOpenFileName(None, "Import", None,
                                             self.dotFilter)
        
        # Check if Open button has been pressed
        if len(result[0]) > 0:
            # Load dot file into a pydot graph
            pydotGraph = graph_from_dot_file(result[0])
            
            # Clear graph (ask to save before importing here in a future extension)
            self.onClearGraph()
            
            # Default position of the node
            x = [1]
            x[0] = 0
            y = [1]
            y[0] = 0
            deltaX = 100
            
            # Create nodes from pydot nodes
            for node in pydotGraph.get_nodes():
                self.model.addPydotNode(node, x, y, deltaX)
                
            # Create edges from pydot edges
            for edge in pydotGraph.get_edges():
                self.model.addPydotEdge(edge, x, y, deltaX)
    
    def onSaveFile(self):
        '''Save in a file the text description of the graph.'''        
        # Export dialog
        result = QFileDialog.getSaveFileName(None, "Export", None,
                                             self.dotFilter)
        
        # Check if Save button has been pressed
        if len(result[0]) > 0:
            filePath = result[0]
            
            # Create file
            dotFile = QFile(filePath)
            
            if (not dotFile.open(QIODevice.WriteOnly | QIODevice.Text)):
                QMessageBox.warning(None, "Export", "Export failed.")
            else:
                # Write the text from the TextGraphView into the file
                dotFile.write(QByteArray(self.textGraphController.view
                                             .strDot().encode("utf_8")))
            
            dotFile.close()

    def onClearGraph(self):
        '''Clear the graph.'''
        self.model.clear()
