import sys
from widgets.Ligne import Ligne
try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    print("PySide6 is not installed")
    sys.exit(1)



class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.note_changer = None
        self.first_line = Ligne()
        self.second_line = Ligne()
        self.third_line = Ligne()
        self.fourth_line = Ligne()
        self.currentIndex= None
        
        self.layoutMain = QtWidgets.QVBoxLayout()      
        
        self.first_line_display = QtWidgets.QListWidget()
        self.first_line_display.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.first_line_display.setFixedHeight(50)
        self.second_line_display = QtWidgets.QListWidget()
        self.second_line_display.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.second_line_display.setFixedHeight(50)
        self.third_line_display = QtWidgets.QListWidget()
        self.third_line_display.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.third_line_display.setFixedHeight(50)
        self.fourth_line_display = QtWidgets.QListWidget()
        self.fourth_line_display.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.fourth_line_display.setFixedHeight(50)
        
        for item in self.first_line.note_container:
            self.first_line_display.addItem(str(item))
        for item in self.second_line.note_container:
            self.second_line_display.addItem(str(item))
        for item in self.third_line.note_container:
            self.third_line_display.addItem(str(item))
        for item in self.fourth_line.note_container:
            self.fourth_line_display.addItem(str(item))

        self.layoutMain.addWidget(self.first_line_display)
        self.layoutMain.addWidget(self.second_line_display)
        self.layoutMain.addWidget(self.third_line_display)
        self.layoutMain.addWidget(self.fourth_line_display)
        self.setLayout(self.layoutMain)
        
        self.first_line_display.itemClicked.connect(lambda: self.setCurrentIndex(1))
        self.second_line_display.itemClicked.connect(lambda: self.setCurrentIndex(2))
        self.third_line_display.itemClicked.connect(lambda: self.setCurrentIndex(3))
        self.fourth_line_display.itemClicked.connect(lambda: self.setCurrentIndex(4))
        
        
        
    @QtCore.Slot()
        
    def setCurrentIndex(self, lineNumber : int):
        match lineNumber:
            case 1:
                self.currentIndex = self.first_line_display.currentRow()
            case 2:
                self.currentIndex = self.second_line_display.currentRow()
            case 3:
                self.currentIndex = self.third_line_display.currentRow()
            case 4:
                self.currentIndex = self.fourth_line_display.currentRow()
            case _:
                self.currentIndex = self.first_line_display.currentRow()
        
        if (self.note_changer != None):
            self.resetSubmitWidget()
        self.note_changer = QtWidgets.QLineEdit()
        self.note_changer.setPlaceholderText("Enter a note from 0 to 24 °o°")
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.layoutMain.addWidget(self.note_changer)
        self.layoutMain.addWidget(self.submit_button)
        self.submit_button.clicked.connect(lambda: self.addNote(lineNumber))
    
    def resetSubmitWidget(self):
        self.note_changer.deleteLater()
        self.note_changer = None
        self.submit_button.deleteLater()
        self.submit_button = None

    def addNote(self, lineNumber : int):
        line = self.first_line
        line_display = self.first_line_display
        match lineNumber:
            case 2:
                line = self.second_line
                line_display = self.second_line_display
            case 3:
                line = self.third_line
                line_display = self.third_line_display
            case 4:
                line = self.fourth_line
                line_display = self.fourth_line_display
        line.addNote(int(self.note_changer.text()), self.currentIndex)
        line_display.clear()
        line_display.addItems(line.note_container)
        self.layoutMain.removeWidget(self.note_changer)
        self.layoutMain.removeWidget(self.submit_button)
        self.resetSubmitWidget()
        
        
        
    
        