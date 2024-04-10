#Aufgabe 1:
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow")

##Layout
        layout = QFormLayout()
        vornameLine = QLineEdit()
        nameLine = QLineEdit()
        Geburtstag = QDateEdit()
        AdresseLine = QLineEdit()
        PostleitzahlLine = QLineEdit()
        OrtLine = QLineEdit()
        Land = QComboBox()
        Land.addItems(["Schweiz", "Deutschland", "Österreich"]) 
        button1 = QPushButton("Auf Karte anzeigen")        
        button2 = QPushButton("Laden")
        button3 = QPushButton("Save")


        layout.addRow("Vorname:",vornameLine)
        layout.addRow("Name", nameLine)
        layout.addRow("Geburtstag:", Geburtstag)
        layout.addRow("Adresse:", AdresseLine)
        layout.addRow("Postleitzahl:", PostleitzahlLine)
        layout.addRow("Ort:", OrtLine)
        layout.addRow("Land:", Land)
        layout.addRow(button1)
        layout.addRow(button2)
        layout.addRow(button3)

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

        viewmenu = menubar.addMenu("View")
        karte = QAction("Karte", self)
        viewmenu.addAction(karte)


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
        Postleitzahl = self.PostleitzahlLine.text()
        Ort = self.OrtLine.text()
        Land = self.Land.currentText()

        ausgabe = f"{vorname},{name},{Geburtstag},{Adresse},{Postleitzahl},{Ort},{Land}"
        print(ausgabe)## Verknüpfung mit File (file.write)??
