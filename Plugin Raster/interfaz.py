from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 811, 421))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmbbx1 = QtWidgets.QComboBox(self.groupBox)
        self.cmbbx1.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.cmbbx1.setObjectName("cmbbx1")
        self.Btn1 = QtWidgets.QPushButton(self.groupBox)
        self.Btn1.setGeometry(QtCore.QRect(180, 50, 31, 23))
        self.Btn1.setObjectName("Btn1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 201, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Lbl1 = QtWidgets.QLabel(self.groupBox)
        self.Lbl1.setGeometry(QtCore.QRect(20, 120, 200, 13))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Lbl1.setFont(font)
        self.Lbl1.setObjectName("Lbl1")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 151, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 170, 791, 241))
        self.textEdit.setObjectName("textEdit")
        self.lblExt = QtWidgets.QLabel(self.groupBox)
        self.lblExt.setGeometry(QtCore.QRect(130, 180, 900, 13))
        self.lblExt.setObjectName("lblExt")
        self.lblxmn = QtWidgets.QLabel(self.groupBox)
        self.lblxmn.setGeometry(QtCore.QRect(150, 280, 500, 13))
        self.lblxmn.setObjectName("lblxmn")
        self.lblymn = QtWidgets.QLabel(self.groupBox)
        self.lblymn.setGeometry(QtCore.QRect(150, 330, 500, 13))
        self.lblymn.setObjectName("lblymn")
        self.lblxmx = QtWidgets.QLabel(self.groupBox)
        self.lblxmx.setGeometry(QtCore.QRect(590, 280, 500, 13))
        self.lblxmx.setObjectName("lblxmx")
        self.lblymx = QtWidgets.QLabel(self.groupBox)
        self.lblymx.setGeometry(QtCore.QRect(590, 330, 500, 13))
        self.lblymx.setObjectName("lblymx")
        self.lblTpix = QtWidgets.QLabel(self.groupBox)
        self.lblTpix.setGeometry(QtCore.QRect(150, 240, 500, 13))
        self.lblTpix.setObjectName("lblTpix")
        self.lblAncho = QtWidgets.QLabel(self.groupBox)
        self.lblAncho.setGeometry(QtCore.QRect(150, 380, 500, 13))
        self.lblAncho.setObjectName("lblAncho")
        self.lblAlto = QtWidgets.QLabel(self.groupBox)
        self.lblAlto.setGeometry(QtCore.QRect(590, 380, 500, 13))
        self.lblAlto.setObjectName("lblAlto")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 500, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(456, 280, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(460, 330, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 380, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(460, 380, 91, 16))
        self.label_11.setObjectName("label_11")
        self.Btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.Btn2.setObjectName("Btn2")
        self.Btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3.setGeometry(QtCore.QRect(400, 450, 75, 23))
        self.Btn3.setObjectName("Btn3")
        self.Btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn4.setGeometry(QtCore.QRect(740, 450, 75, 23))
        self.Btn4.setObjectName("Btn4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M??dulo r??ster"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos de entrada"))
        self.label.setText(_translate("MainWindow", "Selecciona el archivo"))
        self.Btn1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Sistema de referencia geoespacial"))
        self.Lbl1.setText(_translate("MainWindow", "SCRG"))
        self.label_3.setText(_translate("MainWindow", "Datos de informaci??n"))
        self.lblExt.setText(_translate("MainWindow", "Extent"))
        self.lblxmn.setText(_translate("MainWindow", "Xmin"))
        self.lblymn.setText(_translate("MainWindow", "ymin"))
        self.lblxmx.setText(_translate("MainWindow", "xmax"))
        self.lblymx.setText(_translate("MainWindow", "ymax"))
        self.lblTpix.setText(_translate("MainWindow", "tpixel"))
        self.lblAncho.setText(_translate("MainWindow", "Ancho"))
        self.lblAlto.setText(_translate("MainWindow", "Alto"))
        self.label_4.setText(_translate("MainWindow", "extenciones"))
        self.label_5.setText(_translate("MainWindow", "unidades de pixel"))
        self.label_6.setText(_translate("MainWindow", "coordenadas min X"))
        self.label_7.setText(_translate("MainWindow", "coordenadas min Y"))
        self.label_8.setText(_translate("MainWindow", "coordenadas max X"))
        self.label_9.setText(_translate("MainWindow", "coordenadas max Y"))
        self.label_10.setText(_translate("MainWindow", "Pixeles ancho"))
        self.label_11.setText(_translate("MainWindow", "Pixeles Largo"))
        self.Btn2.setText(_translate("MainWindow", "Ayuda"))
        self.Btn3.setText(_translate("MainWindow", "Ejecutar"))
        self.Btn4.setText(_translate("MainWindow", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
