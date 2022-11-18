import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__lab1 = QLabel("Température")
        self.__nombre = QLineEdit("")
        self.__lab2 = QLabel("°C")
        self.__convert = QPushButton("Convertir")
        self.__list = QComboBox()
        self.__list.addItems(['°C -> K', 'K -> °C'])
        self.__lab3 = QLabel("Conversion")
        self.__lab4 = QLabel("")
        self.__lab5 = QLabel("K")
        self.__espace = QLabel("")
        self.__aide = QPushButton("?")


        grid.addWidget(self.__lab1, 0, 0)
        grid.addWidget(self.__nombre, 0, 1)
        grid.addWidget(self.__lab2, 0, 2)
        grid.addWidget(self.__convert, 1, 1)
        grid.addWidget(self.__list, 1, 2)
        grid.addWidget(self.__lab3, 2, 0)
        grid.addWidget(self.__lab4, 2, 1)
        grid.addWidget(self.__lab5, 2, 2)
        grid.addWidget(self.__espace, 3, 0)
        grid.addWidget(self.__aide, 4, 2)

        self.setWindowTitle("Conversion de Température")
        self.__aide.clicked.connect(self.info)


    def info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.setText("")
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()