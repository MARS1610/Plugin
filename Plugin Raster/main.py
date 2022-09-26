import os 
import sys

'''librerias de QyQt5'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''librerias de Qgis'''
from qgis.core import *
from qgis.gui import *
from qgis.utils import * 

from .raster import interfaz

class mainMenu:
    def __init__(self, iface):
        self.iface= iface
    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster") # titulo del menu
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.IMenu)
        self.IMenuBar= self.iface.addToolBar("Raster")

        self.ejemploRaster = QAction(QIcon(""), "Raster", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)
        
    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers= QgsProject.instance().mapLayers().values()#
        for layer in layers:
            if layer.type()== QgsMapLayer.VectorLayer and layer.geometryType()==QgsWkbTypes.PolygonGeometry:
                vLayer = layer
            if layer.type() == QgsRasterLayer.RasterLayer:
                rLayer= layer
                self.dialogo.ui.cmbbx1.addItem(rLayer.name())
                epsg=rLayer.crs()
                self.dialogo.ui.Lbl1.setText(str(epsg.authid()))
                ext= rLayer.extent()
                self.dialogo.ui.lblExt.setText(str(ext.toString()))
                xmin = ext.xMinimum()
                self.dialogo.ui.lblxmn.setText(str(xmin))
                ymin = ext.yMinimum()
                self.dialogo.ui.lblymn.setText(str(ymin))
                xmax = ext.xMaximum()
                self.dialogo.ui.lblxmx.setText(str(xmax))
                ymax = ext.yMaximum()
                self.dialogo.ui.lblymx.setText(str(ymax))
                ancho= rLayer.width()
                self.dialogo.ui.lblAncho.setText(str(ancho))
                largo = rLayer.height()
                self.dialogo.ui.lblAlto.setText(str(largo))
                
                self.dialogo.ui.lblTpix.setText(str("Extension De La Capa:"+ext+"\ny Min:"+ymin+"\ny Max:"+ymax+"\nx min"+xmin+"\n X Max"
                +xmax+"\nAncho"+ancho+"\nlargo"+largo))



def unload(self):
    self.IMenu.deleteLater()
    #QgsApplication.processingRegistry().removeProvider(self.provider)