# -*- coding: utf-8 -*-
from controller.ControllerMainWindow import ControllerMainWindow
from model.Graph import Graph
from factory.Factory import Factory
from view.MainWindow import MainWindow 
from view.GraphicsGraph import GraphicsGraph
from view.TextGraph import TextGraph
from view.PropertiesView import PropertiesView

class Doted:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Initialisation
        model = Graph()
        nodeA = Factory.newNode("A")
        nodeB = Factory.newNode("B")
        model.addNode(nodeA)
        model.addNode(nodeB)
    
        self.mainWindow = MainWindow()
        controllerMain = ControllerMainWindow(model, self.mainWindow)
        
        graphicsGraph = GraphicsGraph()
        textGraph = TextGraph()
        propertiesView = PropertiesView()
        
        self.mainWindow.addWidget(propertiesView)
        self.mainWindow.addWidget(graphicsGraph)
        self.mainWindow.addWidget(textGraph)

    def run(self):
        self.mainWindow.show()
