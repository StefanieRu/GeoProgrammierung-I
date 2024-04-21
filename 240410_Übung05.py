#Aufgabe 1:
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
import urllib.parse 

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.erstellen()
        self.setWindowTitle("MainWindow")
        self.createConnects()


##Layout
    def erstellen(self):
        layout = QFormLayout()
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.Geburtstag = QDateEdit()
        self.Geburtstag.setDisplayFormat("dd/mm/yyyy")
        self.Adresse = QLineEdit()
        self.Postleitzahl = QLineEdit()
        self.Ort = QLineEdit()
        self.Land = QComboBox()
        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"]) 
        self.karte = QPushButton("Auf Karte anzeigen")        
        self.laden = QPushButton("Laden")
        self.save = QPushButton("Save")


        layout.addRow("Vorname:",self.vorname)
        layout.addRow("Name", self.name)
        layout.addRow("Geburtstag:", self.Geburtstag)
        layout.addRow("Adresse:", self.Adresse)
        layout.addRow("Postleitzahl:", self.Postleitzahl)
        layout.addRow("Ort:", self.Ort)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.karte)
        layout.addRow(self.laden)
        layout.addRow(self.save)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)     


##Menübar
        menubar = self.menuBar()
        
        filemenu = menubar.addMenu("File")
        self.savemenu = QAction("Save", self)
        self.quitmenu = QAction("Quit", self)
        filemenu.addAction(self.savemenu)
        filemenu.addAction(self.quitmenu)

        viewmenu = menubar.addMenu("View")
        self.kartemenu = QAction("Karte", self)
        viewmenu.addAction(self.kartemenu)
        self.ladenmenu = QAction("Laden", self)
        viewmenu.addAction(self.ladenmenu)


## Anziege
        self.show()




#Buttons definieren, File erstellen
    def createConnects(self):
        self.save.clicked.connect(self.defsave)
        self.savemenu.triggered.connect(self.defsave)
        self.quitmenu.triggered.connect(self.defquit)
        self.laden.clicked.connect(self.defladen)
        self.karte.clicked.connect(self.defkarte)
        self.ladenmenu.triggered.connect(self.defladen)
        self.kartemenu.triggered.connect(self.defkarte)
      


    def defsave(self):
        vorname = self.vorname.text()
        name = self.name.text()
        Geburtstag = self.Geburtstag.text()
        Adresse = self.Adresse.text()
        Postleitzahl = self.Postleitzahl.text()
        Ort = self.Ort.text()
        Land = self.Land.currentText()

        ausgabe = f"{vorname},{name},{Geburtstag},{Adresse},{Postleitzahl},{Ort},{Land}"
        filename, typ = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text-File (*.txt*)")
        datei = open(filename, "w")
        datei.write(ausgabe)
        datei.close()

    def defquit(self):
        self.close()
    
    def defladen(self):
        filename, typ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Textfile (*.txt)")
        
        datei2 = open(filename, "r")
        ausgabe2 = datei2.read().split(",")
        self.vorname.setText(ausgabe2[0])
        self.name.setText(ausgabe2[1])

        dformat=QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
        self.Geburtstag.setDate(ausgabe2[2], dformat)
        
        self.Adresse.setText(ausgabe2[3])
        self.Postleitzahl.setText(ausgabe2[4])
        self.Ort.setText(ausgabe2[5])
        self.Land.setText(ausgabe2[6])

    def defkarte(self):
        objekt = f"{self.Adresse.text()}+{self.Postleitzahl.text()}+{self.Ort.text()}+{self.Land.currentText()}"
        query = urllib.parse.quote(objekt)
        link = f"http://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))
    

app = QApplication([])
w = Fenster()
w.raise_() 
app.exec()