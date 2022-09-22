from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import QMainWindow

from interface.ui import Ui_MainWindow

from utils.qkonsol import QKonsol


class AppWindow(QMainWindow, Ui_MainWindow):
    
    killTerminal = Signal()  # Used to force running process to halt
    

    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.terminal = QKonsol(self.consoleWidget)
        self.killTerminal.connect(self.terminal.terminateApp)


    def closeEvent(self, event):
        # Forces process to exit to allow main window to close
        self.killTerminal.emit()
