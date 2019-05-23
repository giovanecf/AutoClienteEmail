import sys

from PyQt5 import QtWidgets

from src.view.Menu import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.location_on_the_screen(MainWindow)
MainWindow.show()
sys.exit(app.exec_())