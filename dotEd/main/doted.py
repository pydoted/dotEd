# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from view.MainWindow import MainWindow 
from controller.ControllerMainWindow import ControllerMainWindow
from model.Graph import Graph
from factory.Factory import Factory
from view.GraphicsGraph import GraphicsGraph
from view.TextGraph import TextGraph
from view.PropertiesView import PropertiesView



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Initialisation
    model = Graph()
    nodeA = Factory.newNode("A")
    nodeB = Factory.newNode("B")
    model.addNode(nodeA)
    model.addNode(nodeB)

    mainWindow = MainWindow()
    controllerMain = ControllerMainWindow(model, mainWindow)
    
    graphicsGraph = GraphicsGraph()
    textGraph = TextGraph()
    propertiesView = PropertiesView()
    
    mainWindow.addWidget(propertiesView)
    mainWindow.addWidget(graphicsGraph)
    mainWindow.addWidget(textGraph)    
    
    sys.exit(app.exec_())
