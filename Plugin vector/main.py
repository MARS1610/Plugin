#importación de librerias python
import os
import sys 

#importación de librerias para el diseño de interfaz 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from osgeo import gdal, osr

from .vector import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Vector")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Vector")
        
        self.ejemplo = QAction(QIcon("D:\sistemas op\QGIS 322\apps\qgis-ltr\python\plugins\Plugin vector/vector.png"), "Vector", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemplo)
        self.ejemplo.setObjectName("Nombre vector")
        self.ejemplo.setWhatsThis("Configuracion de plugin vector")
        self.ejemplo.setStatusTip("Estatus del plugin vector")

        self.ejemplo.triggered.connect(self.startInterfaz)


    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == 0:
                self.dialogo.ui.cmb1.addItem(layer.name())
        
    def unload(self):
            self.IMenu.deleteLater()
            #QgsApplication.processingGuiRegistry().removeProvider(self.provider)
