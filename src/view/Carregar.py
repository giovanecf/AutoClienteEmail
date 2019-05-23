# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carregando.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import threading
from queue import Queue

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.DataBase.DataBase import DataBase
from src.util.ClienteEmail import ClienteEmail


class Ui_Carregar(object):

    def exampleJob(self, worker):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Rapidez")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText(" Acabei aqui! Cobrei geral :-)")

        for i in range(500001):
            print(i)
            p = i / 5000
            self.progressBar.setValue(p)
            #self.label.setText("Enviando "+str(i)+" de 500001")

        with self.print_lock:
            print(threading.current_thread().name, worker)
            msg.exec_()
            self.dialog.done(1)

    def threader(self):
        while True:
            worker = self.q.get()
            self.exampleJob(worker)
            self.q.task_done()

    def processo(self):
        self.print_lock = threading.Lock()
        self.q = Queue()

        t = threading.Thread(target=self.threader)
        t.daemon = True
        t.start()

        self.q.put(0)

    def __init__(self):
        self.processo()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 68)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enviando..."))
        self.label.setText(_translate("Dialog", "Obtendo dados do BD..."))

        self.dialog = Dialog


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Carregar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
