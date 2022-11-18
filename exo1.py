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

        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__ok = QPushButton("Ok")
        self.__nom = QLabel("")
        self.__quit = QPushButton("Quitter")

        grid.addWidget(self.__lab, 0, 0)  # composant, ligne, colonne
        grid.addWidget(self.__text, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ok, 2, 0)  # composant, ligne, colonne
        grid.addWidget(self.__nom, 3, 0)  # composant, ligne, colonne
        grid.addWidget(self.__quit, 4, 0)  # composant, ligne, colonne

        self.__ok.clicked.connect(self._actionOk)
        self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        self.__nom.setText(f"Bonjour {self.__text.text()}")

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()