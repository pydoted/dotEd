# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QPushButton

from controller.GraphicsGraphController import GraphicsGraphController
from controller.MainWindowController import MainWindowController
from controller.TextGraphController import TextGraphController
from model.Graph import Graph
from view.widget.GraphicsGraphView import GraphicsGraphView
from view.widget.MainWindow import MainWindow
from view.widget.TextGraphView import TextGraphView


class Doted(object):
    '''The Doted class provides a main application.
    
    
    Attribute(s):
    mainWindow (MainWindow) -- Application view
    '''


    def __init__(self):
        # Model
        graphModel = Graph()
        
        # Views
        graphicsGraphView = GraphicsGraphView()
        textGraphView = TextGraphView()

        # Controllers
        GraphicsGraphController(graphModel, graphicsGraphView)
        textGraphController = TextGraphController(graphModel, textGraphView)

        # Main window
        self.mainWindow = MainWindow()
        MainWindowController(graphModel, self.mainWindow, textGraphController)
        
        # Clear graph button
        clearGraphButton = QPushButton("Clear graph")
        clearGraphButton.clicked.connect(graphModel.clear)
        
        # Adding views to main window
        self.mainWindow.addWidgetToLayout(clearGraphButton)
        self.mainWindow.addWidgetToSplitter(graphicsGraphView)
        self.mainWindow.addWidgetToSplitter(textGraphView)
        
        # Activate actions in menu of the main window
        self.mainWindow.initMenuAction()

    def run(self):
        '''Run the application.'''
        self.mainWindow.show()
