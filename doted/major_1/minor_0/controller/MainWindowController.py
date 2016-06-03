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

from PyQt5.Qt import QFile, QIODevice, QByteArray, QFileDialog
from PyQt5.QtWidgets import QMessageBox


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

    dotFilter = "Dot files (*.dot)"

    def __init__(self, model, view, textGraphController):
        self.view = view
        self.view.controller = self
        self.model = model

        self.textGraphController = textGraphController

    def onImportFile(self):
        '''Import a file which contains a graph and build or rebuild the model
        with this graph.'''
        # Load graph from file with pydot_ng
        result = QFileDialog.getOpenFileName(None, "Import", None,
                                             MainWindowController.dotFilter)

        # Check if Open button has been pressed
        if len(result[0]) > 0:
            # Load dot file into a pydot graph
            # pydotGraph = graph_from_dot_file(result[0])

            # Clear graph (ask to save before importing here in a future
            # extension)
            self.onClearGraph()

    # Nodes and edges are send to the model in importGraph() in TextGraphView
    # If importGraph() is clean or change you could remove comments of theses
    # lines to build the model
#             # Create nodes from pydot nodes
#             for node in pydotGraph.get_nodes():
#                 self.model.addNode(node.get_name(), node.get_attributes())
#
#             # Create edges from pydot edges
#             for edge in pydotGraph.get_edges():
#                 self.model.addEdge(edge.get_source(), edge.get_destination())

            # Send graph's textual representation to the textual controller
            with open(result[0], "r") as file:
                self.textGraphController.importGraph(file.read())

    def onSaveFile(self):
        '''Save in a file the text description of the graph.'''
        # Export dialog
        result = QFileDialog.getSaveFileName(None, "Export", None,
                                             MainWindowController.dotFilter)

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
                                             .getText().encode("utf_8")))
            dotFile.close()

    def onClearGraph(self):
        '''Clear the graph.'''
        self.model.clear()
