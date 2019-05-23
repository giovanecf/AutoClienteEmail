# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adicionar.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 227)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editNome = QtWidgets.QLineEdit(Dialog)
        self.editNome.setObjectName("editNome")
        self.verticalLayout.addWidget(self.editNome)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editEmail = QtWidgets.QLineEdit(Dialog)
        self.editEmail.setObjectName("editEmail")
        self.verticalLayout.addWidget(self.editEmail)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(200, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/Projeto Python-20190517T034935Z-001/Projeto Python/Imagens/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/Projeto Python-20190517T034935Z-001/Projeto Python/Imagens/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nome"))
        self.label_2.setText(_translate("Dialog", "E-Mail"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.btnOk.setText(_translate("Dialog", "OK !"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
