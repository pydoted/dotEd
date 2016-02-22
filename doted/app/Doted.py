# -*- coding: utf-8 -*-

from factory.ControllerFactory import ControllerFactory
from factory.ViewFactory import ViewFactory
from factory.ModelFactory import ModelFactory


class Doted(object):
    '''The Doted class provides a main application.
    
    
    Attribute(s):
    mainWindow (MainWindow) -- Application view
    '''


    def __init__(self):
        # Model
        graphModel = ModelFactory.newGraph()
        
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
