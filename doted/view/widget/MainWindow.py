# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QVBoxLayout, \
                            QPushButton


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
        self.menuBar().addAction("Help")
        
        importAction = menuFile.addAction("Import")
        importAction.triggered.connect(self.onImportFile)

        saveAction = menuFile.addAction("Save")
        saveAction.triggered.connect(self.onSaveFile)

    def onClearGraph(self):
        '''Callback function when clicking on Clear graph button.'''
        self.controller.onClearGraph()
    
    def onImportFile(self):
        '''Callback function when clicking on Import.'''
        self.controller.onImportFile()

    def onSaveFile(self):
        '''Callback function when clicking on Save.'''
        self.controller.onSaveFile()
        
    def addWidgetToSplitter(self, widget):
        '''Add a widget to the splitter.
        
        Argument(s):
        widget (QWidget): Widget to add to the splitter
        '''
        self.splitter.addWidget(widget)
