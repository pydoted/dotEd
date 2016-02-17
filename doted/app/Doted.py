# -*- coding: utf-8 -*-

from doted.model.Graph import Graph
from doted.factory.ControllerFactory import ControllerFactory
from doted.factory.ViewFactory import ViewFactory


class Doted(object):
    '''Represent the main application.
    
    
    Attribute(s):
    mainWindow (MainWindow) -- Application view
    '''


    def __init__(self):
        # Model
        graphModel = Graph()
        
        # Views
        graphicsGraphView = ViewFactory.newGraphicsGraphView()
        textGraphView = ViewFactory.newTextGraphView()

        # Controllers
        ControllerFactory.newGraphicsGraphController(graphModel,
                                                     graphicsGraphView)
        ControllerFactory.newTextGraphController(graphModel, textGraphView)

        # Main window
        self.mainWindow = ViewFactory.newMainWindow()
        ControllerFactory.newMainWindowController(graphModel, self.mainWindow)
        
        # Adding views to main window
        self.mainWindow.addWidget(graphicsGraphView)
        self.mainWindow.addWidget(textGraphView)

    def run(self):
        '''Run the application.'''
        self.mainWindow.showMaximized()
