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

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QVBoxLayout, \
    QPushButton, QMessageBox
import pkg_resources


class MainWindow(QMainWindow):
    '''The MainWindow class defines the main view of the application.


    Attribute(s):
    controller (MainWindowController): Controller for the view
    mainWidget (QWidget): Central widget containing all other widgets
    splitter (QSplitter): Frame that will contains widgets
    '''

    def __init__(self):
        # Parent constructor(s)
        QMainWindow.__init__(self)

        self.controller = None

        # Main widget
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("dotEd")

        # Menu
        self.createMenu()

        # Status bar just for a test
        self.statusBar().showMessage("Double click to create a node")

        # Layout/Splitter which will contain all widgets
        self.splitter = QSplitter(Qt.Horizontal)
        layout = QVBoxLayout(self.mainWidget)
        layout.addWidget(self.splitter)

        # Clear graph button
        clearGraphButton = QPushButton("Clear graph")
        clearGraphButton.clicked.connect(self.onClearGraph)
        layout.addWidget(clearGraphButton)

    def createMenu(self):
        '''Create the menu bar.'''
        menuFile = self.menuBar().addMenu("File")

        importAction = menuFile.addAction("Import")
        importAction.triggered.connect(self.onImportFile)

        saveAction = menuFile.addAction("Save")
        saveAction.triggered.connect(self.onSaveFile)

        questionMarkMenu = self.menuBar().addMenu("?")

        helpAction = questionMarkMenu.addAction("Help")
        helpAction.triggered.connect(self.onHelpAction)

        aboutAction = questionMarkMenu.addAction("About")
        aboutAction.triggered.connect(self.onAboutAction)

    def onClearGraph(self):
        '''Callback function when clicking on Clear graph button.'''
        self.controller.onClearGraph()

    def onImportFile(self):
        '''Callback function when clicking on Import.'''
        self.controller.onImportFile()

    def onSaveFile(self):
        '''Callback function when clicking on Save.'''
        self.controller.onSaveFile()

    def onHelpAction(self):
        '''Callback function when clicking on Help.'''
        graphicsViewCommands = (
            "--Graphics view--\n"
            "Create a node : Mouse double click\n"
            "Move a node : ALT + mouse move\n"
            "Create an edge : Mouse click (maintain) on a node and realease"
            " on another node\n"
            "Mutliple selection : CTRL + mouse click or use rubber band"
            " selection\n"
            "Zoom in/out : CTRL + wheel\n"
            "Remove a node/edge : Press DEL key"
        )

        textualViewCommands = (
            "--Textual view--\n"
            "Zoom in/out : CTRL + wheel\n"
            "Update : Click outside the view"
        )

        QMessageBox.information(self, "Help", graphicsViewCommands + "\n\n" +
                                textualViewCommands)

    def onAboutAction(self):
        '''Callback function when clicking on About.'''
        QMessageBox.information(self, "About", "dotEd - A graphic editor for"
                                " DOT graphs\n\n"
                                "GNU General Public License")

    def addWidgetToSplitter(self, widget):
        '''Add a widget to the splitter.

        Argument(s):
        widget (QWidget): Widget to add to the splitter
        '''
        self.splitter.addWidget(widget)
