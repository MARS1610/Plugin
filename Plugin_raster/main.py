import imp
import os
import sys 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from.raster import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface  

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Raster")

        self.ejemploRaster = QAction(QIcon(""),"Datos", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
            