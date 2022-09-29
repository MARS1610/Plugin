import imp
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

from .interfaz import Ui_MainWindow 



class interfaz (QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.Btn4.clicked.connect(self.cerrar)
        self.ui.Btn1.clicked.connect(self.abrirRaster)
        self.ui.cmbbx1.currentIndexChanged.connect(self.selectRaster)
    
    def cerrar (self):
        self.close()

   
    def nombreCmb(self): 
        self.dialogo = interfaz()
       
        layers= QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type()== 0:
                nomVLayer = layer.name()
                self.dialogo.ui.Lbl1.setText(nomVLayer)

            if layer.type() == 1:
                nomRLayer = layer.name()
                self.dialogo.ui.Lbl1.setText(nomRLayer)


    def abrirRaster(self):
        self.dialogo = interfaz()
  

        lypath, _ = QFileDialog.getOpenFileName(self, "Agrega un archivo raster (MDE)", "C:\\", "Raster (*.tif *.GRID)")
        lyInfo = QFileInfo(lypath)
        rlayer = QgsRasterLayer(lypath, lyInfo.fileName())
        if not rlayer.isValid():
            return
        
        QgsProject.instance().addMapLayer(rlayer)
        self.ui.cmbbx1.addItem(rlayer.name())
        epsg=rlayer.crs()
        self.dialogo.ui.Lbl1.setText(str(epsg.authid()))
        
    
    
    def selectRaster(self):
        self.dialogo = interfaz()
        Layertex = self.ui.cmbbx1.currentText()
        layers = QgsProject.instance().mapLayers().values()
        if self.ui.cmbbx1.currentIndex() >= 0:
            for layer in layers:
                if layer.name() == layer:
                    ext= layer.extent()
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
                    pixelSizex= rLayer.rasterUnitsPerPixelX()
                    self.dialogo.ui.lblTpix.setText(str(pixelSizex))
        
        else:
            self.ui.Lbl1.setText(Layertex)
            self.ui.Lbl1.setText(Layertex)

            


            

