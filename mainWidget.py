import sys
from musique.Ligne import Ligne
try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    print("PySide6 is not installed")
    sys.exit(1)



class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        
        self.first_line = Ligne()
        self.currentIndex= None
        
        self.layoutMain = QtWidgets.QVBoxLayout()
        
        
        self.first_line_display = QtWidgets.QListWidget()
        self.first_line_display.setFlow(QtWidgets.QListWidget.LeftToRight)
        self.first_line_display.setFixedHeight(50)
        
        for item in self.first_line.note_container:
            self.first_line_display.addItem(str(item))

        self.layoutMain.addWidget(self.first_line_display)
        self.setLayout(self.layoutMain)
        
        self.first_line_display.itemClicked.connect(self.setCurrentIndex)
        
        
        
    @QtCore.Slot()
        
    def setCurrentIndex(self):
        self.note_changer = QtWidgets.QLineEdit()
        self.note_changer.setPlaceholderText("Enter a note from 0 to 24 °o°")
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.layoutMain.addWidget(self.note_changer)
        self.layoutMain.addWidget(self.submit_button)
        print(self.first_line_display.currentRow())
        self.currentIndex = self.first_line_display.currentRow()
        self.submit_button.clicked.connect(self.addNote)
    
    def addNote(self):
        self.first_line.addNote(int(self.note_changer.text()), self.currentIndex)
        self.first_line_display.clear()
        self.first_line_display.addItems(self.first_line.note_container)
        self.layoutMain.removeWidget(self.note_changer)
        self.layoutMain.removeWidget(self.submit_button)
        self.note_changer.deleteLater()
        self.note_changer = None
        self.submit_button.deleteLater()
        self.submit_button = None
        
        
        
    
        