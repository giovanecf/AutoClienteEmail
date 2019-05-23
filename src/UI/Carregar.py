# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carregando.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import threading
from queue import Queue
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def __init__(self):
        self.processo()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 101)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.btnCarregar = QtWidgets.QPushButton(Dialog)
        self.btnCarregar.setObjectName("btnCarregar")
        self.verticalLayout.addWidget(self.btnCarregar)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enviado 13 de 174 "))
        self.btnCarregar.setText(_translate("Dialog", "Carregar"))
        self.btnCarregar.clicked.connect(self.carregar)

        self.dialog = Dialog

    def carregar(self):
        for i in range(1000001):
            print(i)
            self.label.setText("Enviado "+format(i)+" de 174")
            p = i/10000
            self.progressBar.setValue(p)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
