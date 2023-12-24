import sys
import PyQt5.QtWidgets

from src.view.mainActivity import MainActivity

if __name__ == "__main__":
    application = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MainActivity()

    application.exec_()