'''
The main file to run.
'''
from PyQt5.QtWidgets import QApplication
import sys

#from Interface.ui_MainWindow import Ui_MainWindow
from MainWindow import AppWindow


if __name__ == '__main__':
    '''
    Execute the program.
    '''
    app = QApplication(sys.argv)
    mainWindow = AppWindow()
    mainWindow.show()
    sys.exit(app.exec_())