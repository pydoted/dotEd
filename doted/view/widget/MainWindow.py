# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QVBoxLayout

from view.widget.View import View


class MainWindow(View, QMainWindow):
    '''The MainWindow class defines the main view of the application.
    
    
    Attribute(s):
    mainWidget (QWidget): Central widget containing all other widgets
    splitter (QSplitter): Frame that will contains widgets
    '''

    def __init__(self):
        # Parent constructors
        View.__init__(self)
        QMainWindow.__init__(self)
        
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
        self.layout = QVBoxLayout(self.mainWidget)
        self.layout.addWidget(self.splitter)

    def createMenu(self):
        '''Create the menu bar.'''
        menuFile = self.menuBar().addMenu("File")
        self.menuBar().addAction("Help")
        
        self.importAction = menuFile.addAction("Import")
        self.saveAction = menuFile.addAction("Save")
        
    def initMenuAction(self):
        '''Connect signals of QActions with their slots.'''
        self.importAction.triggered.connect(self.controller.onImportFile)
        self.saveAction.triggered.connect(self.controller.onSaveFile)
        
    def addWidgetToSplitter(self, widget):
        '''Add a widget to the splitter.
        
        Argument(s):
        widget (QWidget): Widget to add to the splitter
        '''
        self.splitter.addWidget(widget)
        
    def addWidgetToLayout(self, widget):
        '''Add a widget to the layout.
        
        Argument(s):
        widget (QWidget): Widget to add to the splitter
        '''
        self.layout.addWidget(widget)
