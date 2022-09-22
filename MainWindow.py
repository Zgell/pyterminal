from PyQt5.QtWidgets import QMainWindow

from interface.ui import Ui_MainWindow

from utils.qkonsol import QKonsol


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.terminal = QKonsol(self.consoleWidget)
