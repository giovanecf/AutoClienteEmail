# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adicionar.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.DataBase.DataBase import DataBase
from src.model.Cliente import Cliente


class Ui_Adicionar(object):

    def cadastrarCliente(self, Ui_MainWindow):
        msg = QMessageBox()
        msg.setWindowTitle("Inserir Cliente")
        msg.setStandardButtons(QMessageBox.Ok)

        if (self.editNome.text() == ""):
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ô LERDÂO! Tá sem NOME!")
            msg.exec_()
        else:
            nome = self.editNome.text()
            if (self.editEmail.text() == ""):
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Me diz uma coisa... Como que vai mandar os bangui sem o e-mail ?")
                msg.exec_()
            else:
                email = self.editEmail.text()
                cliente = Cliente(None, nome, email)
                db = DataBase()
                db.CadastrarCliente(cliente)

                msg.setIcon(QMessageBox.Information)
                msg.setText("Criente salvo com sucessagem garantida!")
                msg.exec_()

                self.editNome.clear()
                self.editEmail.clear()

                self.UI.listarClientes()

    def alterarCliente(self, Ui_MainWindow):
        msg = QMessageBox()
        msg.setWindowTitle("Alterar Cliente")
        msg.setStandardButtons(QMessageBox.Ok)

        if (self.editNome.text() == ""):
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tá cheirado, lek ? Falta o Nome !")
            msg.exec_()
        else:
            nome = self.editNome.text()
            if (self.editEmail.text() == ""):
                msg.setIcon(QMessageBox.Warning)
                msg.setText("BuRrO ! Tá faltando o E-mail !")
                msg.exec_()
            else:
                email = self.editEmail.text()
                cliente = Cliente(self.clienteEnviado.id, nome, email)
                db = DataBase()
                db.EditarCliente(cliente)

                msg.setIcon(QMessageBox.Information)
                msg.setText("Alteramô "+cliente.nome+"ZÃO ! (Sem o zão) Os HOMI num acha mais... rs'")
                msg.exec_()

                self.dialog.done(1)

                self.UI.listarClientes()

    def fecharTela(self):
        self.dialog.done(1)

    def setup(self, Dialog, Cliente, UI):
        self.UI = UI
        self.clienteEnviado = Cliente
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
        icon.addPixmap(QtGui.QPixmap("../Imagens/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # Não seleciona algum botão
        self.setDefaultButton(self.btnOk)
        self.setDefaultButton(self.btnCancelar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Nome"))
        self.label_2.setText(_translate("Dialog", "E-Mail"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.btnCancelar.clicked.connect(self.fecharTela)

        icon1 = QtGui.QIcon()

        if (self.clienteEnviado == None):
            Dialog.setWindowTitle(_translate("Dialog", "Cadastro"))
            icon1.addPixmap(QtGui.QPixmap("../Imagens/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnOk.setText(_translate("Dialog", "OK !"))
            self.btnOk.clicked.connect(self.cadastrarCliente)
            self.editEmail.returnPressed.connect(self.btnOk.click)
        else:
            Dialog.setWindowTitle(_translate("Dialog", "Edição"))
            icon1.addPixmap(QtGui.QPixmap("../Imagens/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnOk.setText(_translate("Dialog", "Alterar"))
            self.btnOk.clicked.connect(self.alterarCliente)
            self.editEmail.returnPressed.connect(self.btnOk.click)
            self.editNome.setText(self.clienteEnviado.nome)
            self.editEmail.setText(self.clienteEnviado.email)

        self.btnOk.setIcon(icon1)
        self.dialog = Dialog


    def setDefaultButton(self, Button):
        Button.setDefault(False)
        Button.setAutoDefault(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Adicionar()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())