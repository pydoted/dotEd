# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from view.widget.View import View


class MainWindow(View, QMainWindow):
    '''Main view of the application.
    
    
    Attribute(s):
    mainWidget (QWidget): Central widget containing all other widgets
    layout (QHBoxLayout): Layout of the central widget
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
        self.statusBar().showMessage("Status bar")
        
        # Layout which will contain all views
        self.layout = QHBoxLayout()
        self.mainWidget.setLayout(self.layout)
    
    def createMenu(self):
        '''Create the menu bar.'''
        self.menuBar().addAction("File")
        self.menuBar().addAction("Help")
        
    def addWidget(self, widget):
        '''Add a widget to the layout.
        
        Argument(s):
        widget (QWidget): Widget to add to the layout
        '''
        self.layout.addWidget(widget)
