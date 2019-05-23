# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox, QDesktopWidget

from src.DataBase.DataBase import DataBase
from src.model.Cliente import Cliente
from src.util.ClienteEmail import ClienteEmail
from src.view.Adicionar import Ui_Adicionar
from src.view.Carregar import Ui_Carregar


class Ui_MainWindow(object):

    def listarClientes(self):
        db = DataBase()
        lista = db.ObterClientes()

        while (self.tableClientes.rowCount() > 0):
            self.tableClientes.removeRow(0)

        row = 0
        for query in lista:
            self.tableClientes.insertRow(row)
            cod = QTableWidgetItem(str(query[0]))
            nome = QTableWidgetItem(str(query[1]))
            email = QTableWidgetItem(str(query[2]))

            self.tableClientes.setItem(row, 0, cod)
            self.tableClientes.setItem(row, 1, nome)
            self.tableClientes.setItem(row, 2, email)

            row = row + 1

    def pesquisarClientes(self):
        db = DataBase()
        texto = self.editPesquisar.text()

        lista = db.PesquisarClientes(texto)

        while (self.tableClientes.rowCount() > 0):
            self.tableClientes.removeRow(0)

        row = 0
        for query in lista:
            self.tableClientes.insertRow(row)
            cod = QTableWidgetItem(str(query[0]))
            nome = QTableWidgetItem(str(query[1]))
            email = QTableWidgetItem(str(query[2]))

            self.tableClientes.setItem(row, 0, cod)
            self.tableClientes.setItem(row, 1, nome)
            self.tableClientes.setItem(row, 2, email)

            row = row + 1


    def telaCadastrar(self):
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Adicionar()
        self.ui.setup(self.window, None, self)
        self.window.show()

    def alterar(self):
        linha = self.tableClientes.currentIndex().row();
        cliente = Cliente( self.tableClientes.item(linha, 0).text(),
                           self.tableClientes.item(linha, 1).text(),
                           self.tableClientes.item(linha, 2).text() )

        print("Alterar "+cliente.nome)

        self.window = QtWidgets.QDialog()
        self.ui = Ui_Adicionar()
        #self.ui.EnviarCliente()
        self.ui.setup(self.window, cliente, self)
        self.window.show()

    def excluirCliente(self):
        linha = self.tableClientes.currentIndex().row();
        if(linha < 0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Excluir Cliente")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Vai deletar o nada? Seleciona alguém, pô! Sou adivinho?")
            msg.exec_()

            return
        else:
            cliente = Cliente(self.tableClientes.item(linha, 0).text(),
                              self.tableClientes.item(linha, 1).text(),
                              self.tableClientes.item(linha, 2).text())

            # reply = QMessageBox::question(this, "Test", "Quit?",
            #                             QMessageBox::Yes | QMessageBox::No);

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Excluir Cliente")
            msg.setText("Vai passar "+cliente.nome+" ? (Já tava na hora mesmo...)")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resp = msg.exec_()

            if (resp == QMessageBox.Yes):
                db = DataBase()
                db.DeletarCliente(cliente)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Excluir Cliente")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setText("Boa escolha! "+cliente.nome+" é um merda, mermão!")
                msg.exec_()
                self.listarClientes()


    def enviarEmail(self):

        self.window = QtWidgets.QDialog()
        self.ui = Ui_Carregar()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/autoClienteEmailIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editPesquisar = QtWidgets.QLineEdit(self.centralwidget)
        self.editPesquisar.setObjectName("editPesquisar")
        self.horizontalLayout_2.addWidget(self.editPesquisar)
        self.btnPesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesquisar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon1)
        self.btnPesquisar.setObjectName("btnPesquisar")
        self.horizontalLayout_2.addWidget(self.btnPesquisar)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnIniciar = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Imagens/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIniciar.setIcon(icon2)
        self.btnIniciar.setObjectName("btnIniciar")
        self.verticalLayout.addWidget(self.btnIniciar)
        self.btnParar = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Imagens/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnParar.setIcon(icon3)
        self.btnParar.setObjectName("btnParar")
        self.verticalLayout.addWidget(self.btnParar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableClientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tableClientes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableClientes.setObjectName("tableClientes")
        self.tableClientes.setColumnCount(3)
        self.tableClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableClientes.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableClientes)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Imagens/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon4)
        self.btnExcluir.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.btnExcluir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Imagens/atualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAtualizar.setIcon(icon5)
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.horizontalLayout_4.addWidget(self.btnAtualizar, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.tableClientes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableClientes.setSelectionMode(QAbstractItemView.SingleSelection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoClienteEmail"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btnParar.setText(_translate("MainWindow", "Parar"))
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))
        self.btnAtualizar.setText(_translate("MainWindow", "Atualizar"))

        self.btnAtualizar.clicked.connect(self.listarClientes)
        self.btnPesquisar.clicked.connect(self.pesquisarClientes)
        self.btnAdd.clicked.connect(self.telaCadastrar)
        self.editPesquisar.returnPressed.connect(self.btnPesquisar.click)
        self.tableClientes.doubleClicked.connect(self.alterar)
        self.btnExcluir.clicked.connect(self.excluirCliente)
        self.listarClientes()
        self.btnIniciar.clicked.connect(self.enviarEmail)

    def location_on_the_screen(self, MainWindows):
        ag = QDesktopWidget().availableGeometry()

        widget = MainWindows.geometry()

        x = (ag.width()-widget.width())/2
        y = (ag.height()-widget.height())/2

        MainWindows.move(x, y)

