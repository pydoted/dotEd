# -*- coding: utf-8 -*-

from major_1.minor_0.controller.GraphicsGraphController import \
    GraphicsGraphController
from major_1.minor_0.controller.MainWindowController import \
    MainWindowController
from major_1.minor_0.controller.TextGraphController import TextGraphController
from major_1.minor_0.model.Graph import Graph
from major_1.minor_0.view.widget.MainWindow import MainWindow
from major_1.minor_1.view.widget.GraphicsGraphView import GraphicsGraphView
from major_1.minor_1.view.widget.TextGraphView import TextGraphView


class Doted(object):
    '''The Doted class provides a main application.


    Attribute(s):
    model (Graph): Model representing the graph
    graphicsGraphView (GraphicsGraphView): Graphic view
    textGraphView (TextGraphView): Textual view
    graphicsGraphController (GraphicsGraphController): Graphic controller
    textGraphController (TextGraphController): Textual controller
    mainWindow (MainWindow): Application view
    mainWindowController (MainWindowController): Application controller
    '''

    def __init__(self):
        # Model
        self.graphModel = Graph()

        # Views
        self.graphicsGraphView = GraphicsGraphView()
        self.textGraphView = TextGraphView()

        # Controllers
        self.textGraphController = TextGraphController(
            self.graphModel,
            self.textGraphView)
        self. graphicsGraphController = GraphicsGraphController(
            self.graphModel,
            self.graphicsGraphView,
            self.textGraphController)

        # Main application
        self.mainWindow = MainWindow()
        self.mainWindowController = MainWindowController(
            self.graphModel,
            self.mainWindow,
            self.textGraphController)

        # Adding views to main window
        self.mainWindow.addWidgetToSplitter(self.graphicsGraphView)
        self.mainWindow.addWidgetToSplitter(self.textGraphView)

    def run(self):
        '''Run the application.'''
        self.mainWindow.show()
