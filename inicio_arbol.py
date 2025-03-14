import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from bd import bd
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(MainWindow,self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))

        uic.loadUi(os.path.join(ui_path, "arbol.ui"), self)
        self.btn_buscar = self.findChild(QtWidgets.QPushButton, 'btn_buscar')
        self.btn_buscar.setText("holaaaaa")
        
        self.tree_apuntes = self.findChild(QtWidgets.QTreeWidget, 'tree_cuentas')
        self.apuntes = bd.ejecuta()

        bd.refresca(self.tree_apuntes,self.apuntes)
        

        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    app.exec()