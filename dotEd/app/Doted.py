# -*- coding: utf-8 -*-

from controller.GraphicsGraphController import GraphicsGraphController
from controller.MainWindowController import MainWindowController
from controller.TextGraphController import TextGraphController
from model.Graph import Graph
from view.widget.GraphicsGraphView import GraphicsGraphView
from view.widget.MainWindow import MainWindow
from view.widget.TextGraphView import TextGraphView


class Doted:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Model
        graphModel = Graph()
        
        # Views
        graphicsGraphView = GraphicsGraphView()
        textGraphView = TextGraphView()

        # Controllers
        GraphicsGraphController(graphModel, graphicsGraphView)
        TextGraphController(graphModel, textGraphView)

        # Main window
        self.mainWindow = MainWindow()
        MainWindowController(graphModel, self.mainWindow)
        
        # Adding views to main window
        self.mainWindow.addWidget(graphicsGraphView)
        self.mainWindow.addWidget(textGraphView)

    def run(self):
        self.mainWindow.show()
