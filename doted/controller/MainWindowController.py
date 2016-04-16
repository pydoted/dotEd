# -*- coding: utf-8 -*-

from PyQt5.Qt import QFile, QIODevice, QByteArray, QFileDialog
from PyQt5.QtWidgets import QMessageBox


class MainWindowController():
    '''The MainWindowController class defines the controller to manage
       a Doted (app)/MainWindow (view).
    
    
    Argument(s):
    model (Model): Model of the controller
    view (View): View of the controller
    textGraphController (TextGraphController): Ref to the TextGraphController
    
    Attribute(s):
    textGraphController (TextGraphController): Ref to the TextGraphController
    dotFilter (str): Filter to only show dot files
    '''


    def __init__(self, model, view, textGraphController):
        self.view = view
        self.view.setController(self)
        self.model = model
        
        self.textGraphController = textGraphController
        self.dotFilter = "Dot files (*.dot)"

    def onImportFile(self):
        '''Import a file which contains a graph and build or rebuild''' 
        #Load graph from file with pydot_ng    
        result = QFileDialog.getOpenFileName(None, "Import", None,
                                             self.dotFilter)
        
        # Check if Open button has been pressed
        if len(result[0]) > 0:
            self.model.importDotFile(result[0])
    
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
