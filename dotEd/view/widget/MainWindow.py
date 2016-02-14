# -*- coding: utf-8 -*-

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QToolBar, QHBoxLayout, QAction
from view.widget.View import View


class MainWindow(View, QMainWindow):
    '''
    classdocs
    '''

    def __init__(self, *args, **kargs):
        '''
        Constructor
        '''
        # Parent constructors
        View.__init__(self)
        QMainWindow.__init__(self, *args, **kargs)
        
        # Main widget
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("dotEd")
        
        # Menu + ToolBar
        self.createMenu()
        self.createToolBar()
        
        # Status bar just for a test
        self.statusBar().showMessage("Status bar")
        
        # Layout which will contain all views
        self.layout = QHBoxLayout()
        self.mainWidget.setLayout(self.layout)
    
    def createMenu(self):
        self.menuBar().addAction("File")
        self.menuBar().addAction("Help")
    
    def createToolBar(self):
        toolBar = QToolBar()
        createNodeAction = QAction("Node", self)
        # Just a test
        createNodeAction.triggered.connect(self.onCreateNode)
        toolBar.addAction(createNodeAction)
        
        toolBar.addAction("Edge")
        toolBar.setFloatable(False)
        self.addToolBar(Qt.TopToolBarArea, toolBar)

    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def onCreateNode(self):
        self.controller.onCreateNode()
