import sys
from PySide6 import QtWidgets, QtCore
from widgets.window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet("QWidget  { background-color: #238C86; }")
    QtCore.QCoreApplication.setApplicationName("Tabs Generator")
    widget= Window()
    widget.show()
    widget.resize(800, 600)

    sys.exit(app.exec())