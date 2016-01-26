# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    
    sys.exit(app.exec_())
