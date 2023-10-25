from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from MainWindow import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
