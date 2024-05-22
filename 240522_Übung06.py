from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5.uic import *
import urllib.parse 

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Designer/showmap.ui", self)

        self.OkButton.clicked.connect(self.map)


    def map(self):
        latitude = self.latitude.text()
        longitude = self.longitude.text()
        link = f"https://www.google.ch/maps/place/{latitude},{longitude}"
        QDesktopServices.openUrl(QUrl(link))

app = QApplication([])

window = Fenster()
window.show()
app.exec()