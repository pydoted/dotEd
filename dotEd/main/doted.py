# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from view.MainWindow import MainWindow 
from controller.ControllerMainWindow import ControllerMainWindow
from model.Graph import Graph


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Initialisation
    modele = Graph()
    mainWindow = MainWindow()
    controllerMain = ControllerMainWindow(modele, mainWindow)
    
    mainWindow.showMaximized()
    
    sys.exit(app.exec_())
