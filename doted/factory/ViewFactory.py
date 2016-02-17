# -*- coding: utf-8 -*-: Victor

from doted.view.edge.GraphicsLineEdge import GraphicsLineEdge
from doted.view.node.GraphicsEllipseNode import GraphicsEllipseNode
from doted.view.widget.GraphicsGraphView import GraphicsGraphView
from doted.view.widget.MainWindow import MainWindow
from doted.view.widget.PropertiesView import PropertiesView
from doted.view.widget.TextGraphView import TextGraphView


class ViewFactory(object):
    '''Factory to create views.'''


    @staticmethod
    def newGraphicsLineEdge():
        '''Create and return a GraphicsLineEdge.'''
        return GraphicsLineEdge()
    
    @staticmethod
    def newGraphicsEllipseNode(nodeId, nodeLabel, x, y, width, height):
        '''Create and return a GraphicsEllipseNode.
        
        Argument(s):
        nodeId (int): ID of the node
        nodeLabel (str): Label of the node
        x (float): x coordinate for the rectangle of the ellipse
        y (float): y coordinate for the rectangle of the ellipse
        width (float): width for the rectangle of the ellipse
        height (float): height for the rectangle of the ellipse
        '''
        return GraphicsEllipseNode(nodeId, nodeLabel, x, y, width, height)
    
    @staticmethod
    def newGraphicsGraphView():
        '''Create and return a GraphicsGraphView.'''
        return GraphicsGraphView()
    
    @staticmethod
    def newMainWindow():
        '''Create and return a MainWindow.'''
        return MainWindow()
    
    @staticmethod
    def newPropertiesView():
        '''Create and return a PropertiesView.'''
        return PropertiesView()
    
    @staticmethod
    def newTextGraphView():
        '''Create and return a TextGraphView.'''
        return TextGraphView()
    