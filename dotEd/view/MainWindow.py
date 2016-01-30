# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QWidget, QSizePolicy, QLabel, QFrame,\
    QVBoxLayout
    
from view.View import View


class MainWindow(View, QMainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        View.__init__(self)
        QMainWindow.__init__(self)
        widget = QWidget()
        #setCentralWigdet(widget)
        
        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.infoLabel = QLabel("Info label")
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        #self.infoLabel.setAlignment(Qt.AlignCenter)
        
        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        #layout.setMargin(5)
        layout.addWidget(topFiller)
        layout.addWidget(self.infoLabel)
        layout.addWidget(bottomFiller)
        widget.setLayout(layout)
        
        self.__createActions()
        self.__createMenu()
        
        self.statusBar().showMessage("msg")
        
        self.setWindowTitle("Status bar")
        self.setMinimumSize(160, 160)
        self.resize(480, 320)
        
    def __createActions(self):
        pass
    
    def __createMenu(self):
        pass
        