# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter

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
        layout = QHBoxLayout(self.mainWidget)
        layout.addWidget(self.splitter)
    
    def createMenu(self):
        '''Create the menu bar.'''
        self.menuBar().addAction("File")
        self.menuBar().addAction("Help")
        
    def addWidget(self, widget):
        '''Add a widget to the layout.
        
        Argument(s):
        widget (QWidget): Widget to add to the splitter
        '''
        self.splitter.addWidget(widget)
