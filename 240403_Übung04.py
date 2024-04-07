## Aufgabe 1: GUI
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")

##Layout
        layout = QFormLayout()
        vornameLine = QLineEdit()
        nameLine = QLineEdit()
        Geburtstag = QSpinBox(minimum=1/1/1900, maximum=1/1/2100, value=1/1/2000)
        AdresseLine = QLineEdit()
        PostLeitzahlLine = QLineEdit()
        OrtLine = QLineEdit()
        Land = QComboBox()
        Land.addItems(["Schweiz", "Deutschland", "Österreich"]) 
        button1 = QPushButton("Save")


        layout.addRow("Vorname:",vornameLine)
        layout.addRow("Name", nameLine)
        layout.addRow("Geburtstag:", Geburtstag)
        layout.addRow("Adresse:", AdresseLine)
        layout.addRow("PostLeitzahl:", PostLeitzahlLine)
        layout.addRow("Ort:", OrtLine)
        layout.addRow("Land:", Land)
        layout.addRow(button1)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)     


##Menübar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        quit = QAction("Quit", self)


        filemenu.addAction(save)
        filemenu.addAction(quit)


## Anziege
        self.show()



app = QApplication([])
w = Fenster()
app.exec()

#Buttons definieren, File erstellen
def createConnects(self):
      self.button.clicked.connect(self.save)

def save(self):
        vorname = self.vornameLine.text()
        name = self.nameLine.text()
        Geburtstag = self.Geburtstag.text()
        Adresse = self.AdresseLine.text()
        PostLeitzahl = self.PostLeitzahlLine.text()
        Ort = self.OrtLine.text()
        Land = self.Land.currentText()

        ausgabe = f"{vorname},{name},{Geburtstag},{Adresse},{PostLeitzahl},{Ort},{Land}"
        print(ausgabe)## Verknüpfung mit File (file.write)??
