import sys
from widgets.Ligne import Ligne
from widgets.pdfGestion import PdfGestion
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
        
        self.firstline = self.first_line.note_container
        self.secondeLine = self.second_line.note_container
        self.thirdLine = self.third_line.note_container
        self.fourthLine = self.fourth_line.note_container
        self.setStyleSheet("""
            QWidget {
                background-color: #CCC9DC;
                color: #0C1821;
                font-size: 16px;
            }

            #validateName {
                background-color: #CCC9DC;
                border: none;
                height: 50px;
                width: 50px;
                border-radius: 25px;
            }
            #validateName:hover {
                background-color: #777;
            }
            #choiceName {
                background-color: #CCC9DC;
                border: none;
                padding: 5px;
                margin: 5px;
                font-size: 20px;
                border-radius: 7px;
            }
            #download_PDF {
                background-color: #CCC9DC;
                border: none;
                width: 50px;
                height: 50px;
                border-radius: 25px;
                font-size: 20px;
            }
            #download_PDF:hover {
                background-color: #777;
            }
            #note_changer {
                background-color: #CCC9DC;
                border: none;
                padding: 5px;
                margin: 5px;
                font-size: 20px;
                border-radius: 7px;
            }
            #submit_button {
                background-color: #CCC9DC;
                border: none;
                padding: 5px;
                margin: 5px;
                font-size: 20px;
                border-radius: 7px;
            }
            
            QListWidget {
                background-color: #CCC9DC;
                border: none;
                padding: 5px;
                margin: 5px;
                border-radius: 7px;
            }

        """)
        
        
        self.layoutMain = QtWidgets.QVBoxLayout()    
        self.layoutLine = QtWidgets.QVBoxLayout()
        self.layoutChoiceName = QtWidgets.QHBoxLayout()
        
        self.download_PDF = QtWidgets.QPushButton("💾")
        self.download_PDF.setObjectName("download_PDF")
        
        self.choiceName = QtWidgets.QLineEdit()
        self.choiceName.setPlaceholderText("Enter the name of the song")
        self.choiceName.setAlignment(QtCore.Qt.AlignCenter)
        self.choiceName.setObjectName("choiceName")
        
        self.validateName = QtWidgets.QPushButton("✅")
        self.validateName.setObjectName("validateName")
    

        
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
            
        self.layoutChoiceName.addWidget(self.choiceName)
        self.layoutChoiceName.addWidget(self.validateName)
        self.layoutChoiceName.addWidget(self.download_PDF)
        self.layoutLine.addWidget(self.first_line_display)
        self.layoutLine.addWidget(self.second_line_display)
        self.layoutLine.addWidget(self.third_line_display)
        self.layoutLine.addWidget(self.fourth_line_display)
        
        
        self.layoutMain.addLayout(self.layoutChoiceName)
        self.layoutMain.addLayout(self.layoutLine)
        
        
        self.setLayout(self.layoutMain)
        
        self.first_line_display.itemClicked.connect(lambda: self.setCurrentIndex(1))
        self.second_line_display.itemClicked.connect(lambda: self.setCurrentIndex(2))
        self.third_line_display.itemClicked.connect(lambda: self.setCurrentIndex(3))
        self.fourth_line_display.itemClicked.connect(lambda: self.setCurrentIndex(4))
        self.validateName.clicked.connect(self.validateNameSong)
        self.download_PDF.clicked.connect(self.downloadPDF)
        
        
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
        self.note_changer.setObjectName("note_changer")
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.setObjectName("submit_button")
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
        
    def downloadPDF(self):
        firstline = self.first_line.note_container
        secondeLine = self.second_line.note_container
        thirdLine = self.third_line.note_container
        fourthLine = self.fourth_line.note_container
        
        filename = self.choiceName.text() + ".pdf"
        PdfGestion(firstline,secondeLine, thirdLine, fourthLine, filename)
        print("PDF downloaded")
        
    def validateNameSong(self):
        
        print("Song name is", self.choiceName.text())
        self.pdf = PdfGestion(self.firstline, self.secondeLine, self.thirdLine, self.fourthLine, "notes.pdf")
        self.pdf.set_filename(self.choiceName.text()) 
        self.choiceName.setEnabled(False)
        self.validateName.deleteLater()
        
    
        